import os
import subprocess
import re
import hashlib
import shutil
import json
import argparse
from collections import defaultdict
from datetime import datetime

# --- Configuration & Setup ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)  # This skill's root directory


def find_project_roots(start_path):
    """
    Traverse up from start_path to find the 'skills' directory and the project base directory.
    Assumes the structure is .../project_root/skills/...
    """
    current = start_path
    while current != os.path.dirname(current):
        if os.path.basename(current) == 'skills':
            return os.path.dirname(current), current
        current = os.path.dirname(current)
    # Fallback: assume we are in skills/category/skill-name/scripts
    # So skills root is ../../../
    base = os.path.abspath(os.path.join(start_path, "../../../../"))
    return base, os.path.join(base, "skills")


BASE_DIR, SKILLS_ROOT_DIR = find_project_roots(SCRIPT_DIR)
CACHE_DIR = os.path.join(SKILLS_ROOT_DIR, ".cache")
CONFIG_PATH = os.path.join(SKILL_DIR, "references/sources.md")
TEMPLATE_PATH = os.path.join(SKILL_DIR, "references/skills_list_template.md")
TRANSLATIONS_PATH = os.path.join(SKILL_DIR, "references/translations.json")
CATEGORIES_PATH = os.path.join(SKILL_DIR, "references/categories.json")
OUTPUT_FILE = os.path.join(SKILLS_ROOT_DIR, "SKILLS_LIST.md")

# Special Filtering Rules
IGNORED_SKILLS = {'skill-creator'}
PRIORITY_PATHS = ['skills/anthropics', 'skills/official_skills/anthropics']
LOWER_PRIORITY_PATHS = ['skills/.claude']


# --- Helper Functions ---

def load_json(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading {path}: {e}")
        return {}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Config not found at {CONFIG_PATH}")
        return []
    
    sources = []
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_table = False
    headers = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect table header
        if line.startswith("|") and "URL" in line and "Local Path" in line:
            headers = [h.strip() for h in line.strip("|").split("|")]
            in_table = True
            continue
        
        # Skip separator line
        if in_table and "---" in line:
            continue
        
        # Parse row
        if in_table and line.startswith("|"):
            values = [v.strip() for v in line.strip("|").split("|")]
            if len(values) == len(headers):
                source = dict(zip(headers, values))
                sources.append(source)
    
    return sources


def run_git_command(command, cwd):
    try:
        result = subprocess.run(
            command, cwd=cwd, capture_output=True, text=True, check=False
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def setup_cached_repo(name, remote_url, branch, sparse_paths):
    """
    Maintains a cached clone of the repo in .cache/RepoName.
    Uses sparse-checkout to only fetch relevant paths.
    """
    repo_cache_path = os.path.join(CACHE_DIR, name.replace(" ", "_"))
    
    if not os.path.exists(repo_cache_path):
        os.makedirs(repo_cache_path)
    
    # Init git if needed
    git_dir = os.path.join(repo_cache_path, ".git")
    if not os.path.exists(git_dir):
        run_git_command(['git', 'init'], repo_cache_path)
        run_git_command(['git', 'remote', 'add', 'origin', remote_url], repo_cache_path)
    
    # Configure sparse checkout
    run_git_command(['git', 'config', 'core.sparseCheckout', 'true'], repo_cache_path)
    sparse_file = os.path.join(git_dir, 'info', 'sparse-checkout')
    with open(sparse_file, 'w', encoding='utf-8') as f:
        # Always include sparse paths
        for p in sparse_paths.split():
            f.write(p + '\n')
    
    print(f"  Fetching {remote_url} to cache...")
    s, o, e = run_git_command(['git', 'fetch', 'origin', branch], repo_cache_path)
    if not s:
        return False, e, repo_cache_path
    
    print(f"  Checking out {branch} in cache...")
    s, o, e = run_git_command(['git', 'checkout', branch], repo_cache_path)
    if not s:
        # Try hard reset if checkout fails
        s, o, e = run_git_command(['git', 'reset', '--hard', f'origin/{branch}'], repo_cache_path)
    
    if s:
        s, o, e = run_git_command(['git', 'pull', 'origin', branch], repo_cache_path)
    
    return s, e if not s else o, repo_cache_path


def sync_content(source_dir, target_dir, flatten=False):
    """Syncs content from source to target."""
    if not os.path.exists(source_dir):
        return False, f"Source dir {source_dir} does not exist"
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    try:
        if flatten:
            # Copy contents of source_dir into target_dir
            for item in os.listdir(source_dir):
                if item == '.git':
                    continue
                s = os.path.join(source_dir, item)
                d = os.path.join(target_dir, item)
                if os.path.isdir(s):
                    if os.path.exists(d):
                        shutil.rmtree(d)
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
        else:
            # Copy source_dir itself into target_dir
            dirname = os.path.basename(source_dir)
            d = os.path.join(target_dir, dirname)
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(source_dir, d)
        return True, "Synced"
    except Exception as e:
        return False, str(e)


def update_repositories(sources):
    results = []
    print("🔄 Starting Skills Update with Cache & Sync...")
    
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    
    for source in sources:
        name = source.get('Name')
        url = source.get('URL')
        local_rel = source.get('Local Path')
        remote_subfolder = source.get('Remote Subfolder', '.')
        branch = source.get('Branch', 'main')
        flatten = source.get('Flatten', 'No').lower() in ['yes', 'true', '1']
        
        # Ensure local_path is relative to BASE_DIR correctly
        local_path = os.path.join(BASE_DIR, local_rel)
        
        print(f"📦 Processing {name}...")
        success, output, repo_cache_path = setup_cached_repo(name, url, branch, remote_subfolder)
        
        if success:
            # Sync
            sync_results = []
            for sub in remote_subfolder.split():
                src = os.path.join(repo_cache_path, sub)
                if sub == '.':
                    src = repo_cache_path
                s_sync, msg = sync_content(src, local_path, flatten)
                sync_results.append(msg)
            
            results.append(f"✅ **{name}**: Updated. (Sync: {', '.join(sync_results)})")
        else:
            results.append(f"⚠️ **{name}**: Failed. {output.strip()}")
    
    return results


def get_file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def parse_skill(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        name = "Unknown"
        description = "No description"
        body = content
        
        if match:
            frontmatter = match.group(1)
            n_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
            d_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
            if n_match:
                name = n_match.group(1).strip().strip('"\'')
            if d_match:
                description = d_match.group(1).strip().strip('"\'')
            body = content[match.end():]
        else:
            name = os.path.basename(os.path.dirname(file_path))
        
        # Extract Input/Output from body
        def extract_section(text, headers):
            for h in headers:
                pattern = r'^(#+)\s*' + re.escape(h) + r'.*?\n(.*?)(?=^#|\Z)'
                m = re.search(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
                if m:
                    return m.group(2).strip()
            return ""
        
        input_desc = extract_section(body, ["Input", "Inputs", "Trigger", "Usage", "Arguments", "Parameters", "输入", "参数", "使用", "触发"])
        output_desc = extract_section(body, ["Output", "Outputs", "Return", "Returns", "Result", "Results", "Deliverable", "Deliverables", "Artifacts", "输出", "返回", "结果", "产物"])
        
        def clean_text(text):
            if not text:
                return ""
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            summary = " ".join(lines[:3])
            if len(summary) > 100:
                summary = summary[:97] + "..."
            return summary.replace("|", "\\|")
        
        input_summary = clean_text(input_desc)
        output_summary = clean_text(output_desc)
        
        if not input_summary:
            m = re.search(r'(Trigger(?: words)?[:：].*?)(?:[。.]|$)', description, re.IGNORECASE)
            if m:
                input_summary = m.group(1).replace("|", "\\|")
            else:
                m_cn = re.search(r'(触发词[:：].*?)(?:[。.]|$)', description)
                if m_cn:
                    input_summary = m_cn.group(1).replace("|", "\\|")
        
        return {
            "name": name,
            "description": description,
            "input_summary": input_summary if input_summary else "-",
            "output_summary": output_summary if output_summary else "-",
            "path": file_path,
            "rel_path": os.path.relpath(file_path, BASE_DIR),
            "content_hash": get_file_hash(content),
            "content_len": len(content)
        }
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None


def scan_all_skills(filter_duplicates=False):
    skills = []
    skills_root = SKILLS_ROOT_DIR
    print(f"🔍 Scanning skills in: {skills_root}")
    
    raw_skills = []
    for root, dirs, files in os.walk(skills_root):
        if ".git" in dirs:
            dirs.remove(".git")
        if ".cache" in dirs:
            dirs.remove(".cache")  # Skip cache
        
        for file in files:
            if file.lower() == "skill.md":
                skill_data = parse_skill(os.path.join(root, file))
                if skill_data:
                    raw_skills.append(skill_data)
    
    if not filter_duplicates:
        return raw_skills
    
    # Identity logic for duplicates
    # Use name as key
    # If duplicates exist, prefer PRIORITY_PATHS, avoid IGNORED_SKILLS
    official_skill_names = set()
    for s in raw_skills:
        if s['name'] in IGNORED_SKILLS:
            continue
        is_priority = any(p in s['rel_path'] for p in PRIORITY_PATHS)
        if is_priority:
            official_skill_names.add(s['name'])
    
    filtered_skills = []
    for s in raw_skills:
        if s['name'] in IGNORED_SKILLS:
            continue
        is_low_priority = any(p in s['rel_path'] for p in LOWER_PRIORITY_PATHS)
        if is_low_priority and s['name'] in official_skill_names:
            continue
        filtered_skills.append(s)
    
    print(f"  - Final count: {len(filtered_skills)}")
    return filtered_skills


def analyze_conflicts(skills):
    skill_map = defaultdict(list)
    for skill in skills:
        skill_map[skill['name']].append(skill)
    
    conflicts = []
    for name, instances in skill_map.items():
        if len(instances) > 1:
            hashes = set(i['content_hash'] for i in instances)
            is_identical = len(hashes) == 1
            conflicts.append({"name": name, "instances": instances, "is_identical": is_identical})
    
    return conflicts


def load_previous_skills():
    prev_skills = {}
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'\|\s*\d+\s*\|\s*.*?\*\*(.*?)\*\*', content)
            for m in matches:
                prev_skills[m.strip()] = True
        except Exception:
            pass
    return prev_skills


def generate_markdown(update_logs, skills, conflicts, prev_skill_names, translations, categories_map):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    current_skill_names = set(s['name'] for s in skills)
    old_skill_names = set(prev_skill_names.keys())
    new_skills = current_skill_names - old_skill_names
    deleted_skills = old_skill_names - current_skill_names
    
    update_status_content = "\n".join([f"- {log}" for log in update_logs]) if update_logs else "- No updates performed or logged."
    
    active_skills_count = len(skills)
    conflicts_count = len(conflicts)
    
    conflict_analysis_section = ""
    if conflicts:
        lines = []
        lines.append("## 3. ⚠️ Conflict Analysis (冲突分析)")
        lines.append("| Skill Name | Status | Locations | Recommendation |")
        lines.append("|---|---|---|---|")
        for c in conflicts:
            status = "🔴 Content Mismatch" if not c['is_identical'] else "🟡 Identical"
            locs = "<br>".join([f"`{i['rel_path']}`" for i in c['instances']])
            rec = "**Check content manually.**" if not c['is_identical'] else "Safe to keep any."
            lines.append(f"| **{c['name']}** | {status} | {locs} | {rec} |")
        conflict_analysis_section = "\n".join(lines)
    
    def get_skill_source(s):
        rel = s['rel_path'].lower()
        if "anthropics" in rel:
            return "Anthropic"
        elif "openai" in rel:
            return "OpenAI"
        elif "yingmi" in rel:
            return "Yingmi"
        elif "huggingface" in rel:
            return "HuggingFace"
        elif "skillcreatorai" in rel:
            return "SkillCreator AI"
        elif ".claude" in rel:
            return "Local (.claude)"
        else:
            parts = rel.split(os.sep)
            # Basic heuristic
            if len(parts) > 1 and parts[1] not in ["anthropics", "openai", "huggingface", "yingmi", "skillcreatorai"]:
                return "Custom/Local"
        return "Custom/Local"
    
    def get_skill_category(s):
        # 1. Check Map
        if s['name'] in categories_map:
            return categories_map[s['name']]
        # 2. Check Path Keywords
        rel = s['rel_path'].lower()
        if "software-development" in rel:
            return "Software Development"
        elif "product-management" in rel:
            return "Product Management"
        elif "agent-engineering" in rel:
            return "Agent Engineering"
        elif "content-design" in rel:
            return "Content Design"
        elif "research-analysis" in rel:
            return "Research Analysis"
        elif "productivity-tools" in rel:
            return "Productivity Tools"
        return "Uncategorized"
    
    CATEGORY_ORDER = [
        "Software Development",
        "Product Management",
        "Agent Engineering",
        "Content Design",
        "Research Analysis",
        "Productivity Tools",
        "Uncategorized"
    ]
    
    def get_category_order(cat):
        try:
            return CATEGORY_ORDER.index(cat)
        except ValueError:
            return 999
    
    skills.sort(key=lambda x: (
        get_category_order(get_skill_category(x)),
        get_skill_source(x),
        x['name']
    ))
    
    skill_rows = []
    for i, s in enumerate(skills, 1):
        category = get_skill_category(s)
        source = get_skill_source(s)
        
        trans = translations.get(s['name'], {})
        zh_name = trans.get('zh_name', "")
        zh_desc = trans.get('zh_desc', "")
        
        name_display = f"**{s['name']}**"
        if zh_name:
            name_display += f"<br>*{zh_name}*"
        
        raw_desc = s['description'].replace("|", "\\|").replace("\n", " ")
        if len(raw_desc) > 80:
            raw_desc = raw_desc[:77] + "..."
        
        desc_display = ""
        if zh_desc:
            desc_display = zh_desc
            if not any(ord(c) > 128 for c in raw_desc):
                desc_display += f"<br><br>{raw_desc}"
        elif any(ord(c) > 128 for c in raw_desc):
            desc_display = raw_desc
        else:
            desc_display = f"{raw_desc}<br>*(待翻译)*"
        
        skill_rows.append(f"| {i} | {category} | {name_display} | {desc_display} | {source} |")
    
    skills_table_rows = "\n".join(skill_rows)
    
    new_skills_section = ""
    if new_skills:
        new_skills_section = "### ✨ New Skills\n" + "\n".join([f"- {n}" for n in sorted(new_skills)])
    else:
        new_skills_section = "- No new skills added."
    
    deleted_skills_section = ""
    if deleted_skills:
        deleted_skills_section = "\n### 🗑️ Deleted/Hidden Skills\n" + "\n".join([f"- {d}" for d in sorted(deleted_skills)])
    
    template_content = ""
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            template_content = f.read()
    else:
        template_content = """# Skills List

Generated: {date_str}

## Summary

Active Skills: {active_skills_count}
Conflicts: {conflicts_count}

## Skills List

| No. | Category | Name | Description | Source |
|---|---|---|---|---|
{skills_table_rows}

{conflict_analysis_section}

## Update Status

{update_status_content}

## Update History

{new_skills_section}
{deleted_skills_section}
"""
    
    return template_content.format(
        date_str=date_str,
        update_status_content=update_status_content,
        active_skills_count=active_skills_count,
        conflicts_count=conflicts_count,
        conflict_analysis_section=conflict_analysis_section,
        skills_table_rows=skills_table_rows,
        new_skills_section=new_skills_section,
        deleted_skills_section=deleted_skills_section
    )


def deduplicate_repositories(sources):
    print("🧹 Starting Global Deduplication based on priority...")
    dedup_logs = []
    
    all_skills = scan_all_skills(filter_duplicates=False)
    
    source_paths = []
    for s in sources:
        abs_path = os.path.abspath(os.path.join(BASE_DIR, s.get('Local Path', '')))
        source_paths.append(abs_path)
    
    def get_path_rank(skill_path):
        abs_skill_path = os.path.abspath(skill_path)
        for idx, src_path in enumerate(source_paths):
            try:
                if os.path.commonpath([src_path, abs_skill_path]) == src_path:
                    return idx
            except ValueError:
                continue
        return 9999
    
    skill_groups = defaultdict(list)
    for s in all_skills:
        skill_groups[s['name']].append(s)
    
    for name, instances in skill_groups.items():
        if len(instances) < 2:
            continue
        
        ranked_instances = []
        for s in instances:
            rank = get_path_rank(s['path'])
            ranked_instances.append((rank, s))
        
        ranked_instances.sort(key=lambda x: x[0])
        best_rank, best_skill = ranked_instances[0]
        
        if best_rank == 9999:
            continue
        
        for rank, skill in ranked_instances[1:]:
            if skill['path'] == best_skill['path']:
                continue
            
            dir_to_remove = os.path.dirname(skill['path'])
            rel_path = os.path.relpath(dir_to_remove, BASE_DIR)
            
            source_name = "Unlisted"
            if rank < 9999:
                source_name = sources[rank].get('Name')
            
            log = f"🗑️ Removed duplicate **{name}** from `{rel_path}` (Rank {rank} vs Best {best_rank})"
            print(f"  {log}")
            dedup_logs.append(log)
            
            try:
                shutil.rmtree(dir_to_remove)
            except Exception as e:
                print(f"  Failed to remove {dir_to_remove}: {e}")
    
    return dedup_logs


def main():
    parser = argparse.ArgumentParser(description="Manage skills: scan, update, report.")
    parser.add_argument("--update", action="store_true", help="Pull latest updates from configured sources")
    args = parser.parse_args()
    
    prev_skills = load_previous_skills()
    translations = load_json(TRANSLATIONS_PATH)
    categories_map = load_json(CATEGORIES_PATH)
    sources = load_config()
    
    # 1. Deduplication (Clean up workspace)
    dedup_logs = deduplicate_repositories(sources)
    update_logs = dedup_logs  # Start with dedup logs
    
    # 2. Update (Optional)
    if args.update:
        update_logs.extend(update_repositories(sources))
    else:
        print("ℹ️ Skipping update (use --update to enable)")
    
    # 3. Final Scan & Report
    skills = scan_all_skills(filter_duplicates=True)
    conflicts = analyze_conflicts(skills)
    
    report_content = generate_markdown(update_logs, skills, conflicts, prev_skills, translations, categories_map)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"✅ Report generated at: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
