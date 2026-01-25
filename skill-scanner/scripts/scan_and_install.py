#!/usr/bin/env python3
# Skill Scanner Script (Optimized)

import os
import re
import sys
import shutil
import argparse
import subprocess
import tempfile
import json
from datetime import datetime

# --- Configuration & Setup ---

def find_project_root(start_path):
    """
    Finds the project root by looking for '.git' or 'skills' directory.
    Starts from start_path and goes up.
    """
    current_path = os.path.abspath(start_path)
    while True:
        if os.path.isdir(os.path.join(current_path, ".git")):
            return current_path
        # If we find a 'skills' folder that is not inside another 'skills' folder
        if os.path.isdir(os.path.join(current_path, "skills")):
            # Check if it's not just a subdir named skills (heuristic)
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:  # Reached filesystem root
            return os.getcwd()  # Fallback
        current_path = parent_path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = find_project_root(SCRIPT_DIR)
DEFAULT_SKILLS_DIR = os.path.join(PROJECT_ROOT, "skills")

# Configuration file name (placed in skills root)
CONFIG_FILE_NAME = ".skills-config.json"


def load_skills_config(skills_root):
    """
    Load configuration from .skills-config.json if exists.
    Otherwise, auto-detect directory structure.
    
    Returns a dict with:
    - official_sources: dict mapping repo patterns to local paths
    - third_party_dir: where to install third-party skills
    - categories: list of known category directories
    - category_keywords: dict mapping categories to keywords
    """
    config_path = os.path.join(skills_root, CONFIG_FILE_NAME)
    
    # Try to load config file
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(f"📋 Loaded config from {CONFIG_FILE_NAME}")
                return config
        except Exception as e:
            print(f"⚠️  Failed to load config: {e}, using auto-detection")
    
    # Auto-detect directory structure
    return auto_detect_structure(skills_root)


def auto_detect_structure(skills_root):
    """
    Auto-detect the directory structure by scanning existing directories.
    Returns a configuration dict.
    """
    config = {
        "official_sources": {},
        "third_party_dir": None,
        "categories": [],
        "category_keywords": get_default_category_keywords()
    }
    
    if not os.path.isdir(skills_root):
        return config
    
    # Scan top-level directories
    top_dirs = []
    category_dirs = []
    
    for item in os.listdir(skills_root):
        item_path = os.path.join(skills_root, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            top_dirs.append(item)
            
            # Check if this directory contains categorized subdirectories
            subdirs = [d for d in os.listdir(item_path) 
                      if os.path.isdir(os.path.join(item_path, d)) and not d.startswith('.')]
            
            # Heuristic: if most subdirs contain SKILL.md, it's a category container
            skill_count = 0
            for subdir in subdirs:
                if os.path.exists(os.path.join(item_path, subdir, 'SKILL.md')):
                    skill_count += 1
            
            if skill_count > 0 and skill_count >= len(subdirs) * 0.5:
                # This is likely a categorized skills directory
                category_dirs.append(item)
    
    # Detect official sources by common naming patterns
    official_patterns = ['official', 'anthropic', 'openai', 'huggingface', 'vendor']
    third_party_patterns = ['other', 'third', 'community', 'external', 'imported', 'downloaded']
    
    for dir_name in top_dirs:
        dir_lower = dir_name.lower()
        
        # Check for official directories
        if any(p in dir_lower for p in official_patterns):
            # Scan for provider subdirectories
            dir_path = os.path.join(skills_root, dir_name)
            for subdir in os.listdir(dir_path):
                subdir_path = os.path.join(dir_path, subdir)
                if os.path.isdir(subdir_path):
                    subdir_lower = subdir.lower()
                    if 'anthropic' in subdir_lower:
                        config["official_sources"]["anthropics/skills"] = f"{dir_name}/{subdir}"
                    elif 'openai' in subdir_lower:
                        config["official_sources"]["openai/codex-skills"] = f"{dir_name}/{subdir}"
                    elif 'huggingface' in subdir_lower:
                        config["official_sources"]["huggingface/skills"] = f"{dir_name}/{subdir}"
        
        # Check for third-party directory
        if any(p in dir_lower for p in third_party_patterns):
            config["third_party_dir"] = dir_name
            # Detect existing categories
            dir_path = os.path.join(skills_root, dir_name)
            for subdir in os.listdir(dir_path):
                if os.path.isdir(os.path.join(dir_path, subdir)) and not subdir.startswith('.'):
                    config["categories"].append(subdir)
    
    # If no third-party dir found, use first categorized dir or create default
    if not config["third_party_dir"]:
        if category_dirs:
            # Use the first categorized directory that's not official
            for cd in category_dirs:
                if not any(p in cd.lower() for p in official_patterns):
                    config["third_party_dir"] = cd
                    dir_path = os.path.join(skills_root, cd)
                    for subdir in os.listdir(dir_path):
                        if os.path.isdir(os.path.join(dir_path, subdir)) and not subdir.startswith('.'):
                            config["categories"].append(subdir)
                    break
        
        # Still no third-party dir? Default to 'imported'
        if not config["third_party_dir"]:
            config["third_party_dir"] = "imported"
    
    # Remove duplicates from categories
    config["categories"] = list(set(config["categories"]))
    
    print(f"🔍 Auto-detected structure:")
    print(f"   Third-party dir: {config['third_party_dir']}/")
    if config["categories"]:
        print(f"   Categories: {', '.join(sorted(config['categories']))}")
    if config["official_sources"]:
        print(f"   Official sources: {len(config['official_sources'])} configured")
    
    return config


def get_default_category_keywords():
    """Return default category-to-keywords mapping."""
    return {
        "agent-engineering": ["agent", "bot", "llm", "ai", "prompt", "context", "memory", "tool", "skill", "reasoning", "planning", "eval", "evaluation", "mcp"],
        "content-design": ["content", "design", "diagram", "chart", "video", "image", "writing", "doc", "documentation", "visual", "media", "presentation", "slide", "transcript", "subtitle", "caption", "youtube"],
        "product-management": ["product", "manager", "planning", "story", "requirement", "rfp", "project", "roadmap", "agile", "scrum", "business", "jira", "linear"],
        "research-analysis": ["research", "analysis", "data", "search", "paper", "arxiv", "brain", "obsidian", "insight", "report", "finance", "market", "stock"],
        "software-development": ["code", "software", "dev", "git", "test", "debug", "python", "js", "react", "java", "cpp", "programming", "api", "web", "backend", "frontend", "server", "deploy"],
        "productivity-tools": ["organizer", "invoice", "email", "calendar", "job", "application", "video-downloader", "download", "utility", "automation"]
    }


# Global config - loaded lazily
_CONFIG = None


def get_config(skills_root):
    """Get or load the configuration."""
    global _CONFIG
    if _CONFIG is None:
        _CONFIG = load_skills_config(skills_root)
    return _CONFIG


# --- Helper Functions ---

def is_official_source(url, config):
    """
    Check if the URL is from an official source.
    Returns the local path prefix if official, None otherwise.
    """
    if not url or not config.get("official_sources"):
        return None
    url_lower = url.lower()
    for source_pattern, local_path in config["official_sources"].items():
        if source_pattern in url_lower:
            return local_path
    return None


def classify_skill(skill_info, config):
    """
    Classifies a skill into a category based on:
    1. Existing categories in the skills directory
    2. Keywords in name/description
    
    Returns a category name or 'uncategorized'.
    """
    name = skill_info.get('name', '').lower()
    description = skill_info.get('description', '').lower()
    text = f"{name} {description}"
    
    existing_categories = config.get("categories", [])
    category_keywords = config.get("category_keywords", get_default_category_keywords())
    
    # Score against known categories (both existing and keyword-defined)
    all_categories = set(existing_categories) | set(category_keywords.keys())
    scores = {cat: 0 for cat in all_categories}
    
    for cat, keywords in category_keywords.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # Bonus for existing categories (prefer them)
    for cat in existing_categories:
        if cat in scores:
            scores[cat] += 0.5
    
    # Find max score
    if scores:
        best_cat = max(scores, key=scores.get)
        if scores[best_cat] > 0:
            return best_cat
    
    # Fallback: check if name prefix matches any existing category
    if '-' in name:
        prefix = name.split('-')[0]
        for cat in existing_categories:
            if prefix in cat or cat.startswith(prefix):
                return cat
    
    return "uncategorized"


def parse_frontmatter(file_path):
    """Parses the YAML frontmatter from a SKILL.md file using regex."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Allow for potential whitespace after ---
        match = re.match(r'^---\s*\n(.*?)\n---\s*', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            data = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    # Strip whitespace and quotes
                    val = value.strip()
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'"):
                        val = val[1:-1]
                    data[key.strip()] = val
            return data
    except Exception as e:
        print(f"Warning: Failed to parse {file_path}: {e}")
    return None


def find_skills(root_path):
    """Recursively finds all directories containing SKILL.md."""
    skills = {}
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Skip .git and other hidden dirs
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        if 'SKILL.md' in filenames:
            skill_path = os.path.join(dirpath, 'SKILL.md')
            metadata = parse_frontmatter(skill_path)
            if metadata and 'name' in metadata:
                skill_name = metadata['name']
                skills[skill_name] = {
                    'name': skill_name,
                    'path': dirpath,
                    'description': metadata.get('description', 'No description provided.')
                }
    return skills


def clone_repo(url, temp_dir):
    """Clones a git repository to a temporary directory."""
    print(f"Cloning {url}...")
    try:
        subprocess.check_call(['git', 'clone', '--depth', '1', url, temp_dir])
        return True
    except subprocess.CalledProcessError:
        print(f"Error: Failed to clone {url}")
        return False


def install_skill(skill_info, skills_root, config, source_url=None, use_categorization=True, target_dir=None):
    """
    Installs a skill to the appropriate directory based on source type and auto-detected structure.
    
    Args:
        skill_info: Dict with name, path, description
        skills_root: Root skills directory (e.g., /path/to/skills)
        config: Configuration dict from load_skills_config()
        source_url: Git URL of the source repository
        use_categorization: Whether to auto-categorize (default True)
        target_dir: Override destination directory (disables auto-categorization)
    """
    skill_name = skill_info['name']
    src_path = skill_info['path']
    third_party_dir = config.get("third_party_dir", "imported")
    
    if target_dir:
        # User specified explicit target directory
        dest_path = os.path.join(target_dir, skill_name)
        print(f"📂 Installing '{skill_name}' to specified directory")
    else:
        # Check if source is official
        official_path = is_official_source(source_url, config)
        
        if official_path:
            # Official source: install to detected official path
            dest_path = os.path.join(skills_root, official_path, skill_name)
            print(f"📂 Official source detected: installing '{skill_name}' to {official_path}/")
        elif use_categorization:
            # Third-party source: install to third_party_dir/<category>/
            category = classify_skill(skill_info, config)
            dest_path = os.path.join(skills_root, third_party_dir, category, skill_name)
            print(f"📂 Classified '{skill_name}' as '{category}' → {third_party_dir}/{category}/")
        else:
            # No categorization, use third_party_dir directly
            dest_path = os.path.join(skills_root, third_party_dir, skill_name)
            print(f"📂 Installing '{skill_name}' to {third_party_dir}/")
    
    if os.path.exists(dest_path):
        print(f"⏭️  Skipping {skill_name}: Directory already exists at {dest_path}")
        return False
    
    try:
        if not os.path.exists(os.path.dirname(dest_path)):
            os.makedirs(os.path.dirname(dest_path))
        shutil.copytree(src_path, dest_path)
        print(f"✅ Installed {skill_name} to {dest_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to install {skill_name}: {e}")
        return False


# --- Main Execution ---

def main():
    parser = argparse.ArgumentParser(description="Scan and install Anthropic-style skills.")
    parser.add_argument("--url", help="Git repository URL to scan")
    parser.add_argument("--path", help="Local directory path to scan")
    parser.add_argument("--report-only", action="store_true", help="Only show the report, do not install")
    parser.add_argument("--install", help="Skills to install: 'all' or comma-separated indices (e.g. '1,3')")
    parser.add_argument("--target-dir", help="Directory to install skills (default: auto-categorize in skills root)")
    parser.add_argument("--skills-dir", help=f"Root directory of local skills (default: {DEFAULT_SKILLS_DIR})")
    parser.add_argument("--no-auto-cat", action="store_true", help="Disable auto-categorization and use target-dir")

    args = parser.parse_args()
    
    skills_root = args.skills_dir if args.skills_dir else DEFAULT_SKILLS_DIR
    
    # Determine logic
    use_auto_cat = not args.no_auto_cat
    target_dir = args.target_dir  # None means use auto-categorization logic
    source_url = args.url  # Track source URL for official source detection

    if not args.url and not args.path:
        parser.print_help()
        sys.exit(1)

    # 0. Load configuration (auto-detect structure)
    config = load_skills_config(skills_root)
    
    # 1. Identify Local Skills
    print(f"Scanning local skills in {skills_root}...")
    local_skills = find_skills(skills_root)
    print(f"Found {len(local_skills)} local skills.")

    # 2. Prepare Source
    temp_dir = None
    source_path = args.path
    if args.url:
        temp_dir = tempfile.mkdtemp(prefix="skill_scanner_")
        if not clone_repo(args.url, temp_dir):
            shutil.rmtree(temp_dir)
            sys.exit(1)
        source_path = temp_dir

    # 3. Scan Source Skills
    print(f"Scanning source skills in {source_path}...")
    source_skills = find_skills(source_path)
    print(f"Found {len(source_skills)} source skills.")

    # 4. Compare
    new_skills = []
    existing_skills = []
    for name, info in source_skills.items():
        if name in local_skills:
            existing_skills.append(info)
        else:
            new_skills.append(info)

    # 5. Report
    print("\n" + "="*60)
    print(f"SCAN REPORT")
    print("="*60)

    if existing_skills:
        print(f"\nExisting Skills ({len(existing_skills)}):")
        for s in existing_skills:
            print(f"  - {s['name']}")

    if new_skills:
        print(f"\nNew Skills Found ({len(new_skills)}):")
        for i, s in enumerate(new_skills):
            desc = s['description']
            print(f"  [{i+1}] {s['name']}: {desc}")
    else:
        print("\nNo new skills found.")

    # 6. Install Interaction
    if not args.report_only and new_skills:
        print("\n" + "-"*60)
        selection = args.install
        if not selection:
            selection = input("Enter numbers of skills to install (comma-separated, e.g., '1,3'), 'all' for all, or 'q' to quit: ").strip().lower()
        else:
            selection = selection.strip().lower()

        to_install = []
        if selection == 'all':
            to_install = new_skills
        elif selection == 'q' or selection == '':
            print("Operation cancelled.")
        else:
            try:
                indices = [int(x.strip()) - 1 for x in selection.split(',')]
                for idx in indices:
                    if 0 <= idx < len(new_skills):
                        to_install.append(new_skills[idx])
                    else:
                        print(f"Warning: Index {idx+1} is out of range.")
            except ValueError:
                print("Invalid input.")

        if to_install:
            third_party_dir = config.get("third_party_dir", "imported")
            
            if target_dir:
                print(f"\n📦 Installing {len(to_install)} skills to {target_dir}...")
            elif use_auto_cat:
                # Check if official source
                official_path = is_official_source(source_url, config)
                if official_path:
                    print(f"\n📦 Official source detected! Installing {len(to_install)} skills to {official_path}/...")
                else:
                    print(f"\n📦 Third-party source: Installing {len(to_install)} skills to {third_party_dir}/<category>/...")
            else:
                print(f"\n📦 Installing {len(to_install)} skills to {third_party_dir}/...")
            
            count = 0
            for skill in to_install:
                if install_skill(
                    skill, 
                    skills_root,
                    config,
                    source_url=source_url,
                    use_categorization=use_auto_cat, 
                    target_dir=target_dir
                ):
                    count += 1
            print(f"\n✅ Successfully installed {count} skills.")

    # Cleanup
    if temp_dir:
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    main()
