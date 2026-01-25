import os
import sys
import json
import argparse
import datetime
from pathlib import Path

# Try importing parsers, handle missing dependencies gracefully
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    import docx
except ImportError:
    docx = None

BASE_DIR = Path(__file__).resolve().parent.parent
MEMORY_DIR = BASE_DIR / "memory"
JDS_DIR = BASE_DIR / "references" / "jds"

def extract_text(file_path):
    """Extracts text from PDF or DOCX."""
    path = Path(file_path)
    if not path.exists():
        return f"错误: 文件 {file_path} 未找到。"
    
    text = ""
    if path.suffix.lower() == '.pdf':
        if not PdfReader:
            return "错误: 未安装 pypdf 库。请运行 `pip install pypdf`。"
        try:
            reader = PdfReader(str(path))
            for page in reader.pages:
                text += page.extract_text() + "\n"
        except Exception as e:
            return f"错误: 读取 PDF 失败: {str(e)}"
            
    elif path.suffix.lower() in ['.docx', '.doc']:
        if not docx:
            return "错误: 未安装 python-docx 库。请运行 `pip install python-docx`。"
        try:
            doc = docx.Document(str(path))
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            return f"错误: 读取 DOCX 失败: {str(e)}"
    
    elif path.suffix.lower() in ['.txt', '.md']:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        return "错误: 不支持的文件格式。"
        
    return text.strip()

def get_jd_content(jd_name):
    """Retrieves content of a specific JD file."""
    # Try exact match first, then partial match
    files = list(JDS_DIR.glob("*"))
    target = None
    
    for f in files:
        if f.stem.lower() == jd_name.lower():
            target = f
            break
            
    if not target:
        # Try finding file that contains the name
        for f in files:
            if jd_name.lower() in f.stem.lower():
                target = f
                break
    
    if target:
        with open(target, 'r', encoding='utf-8') as f:
            return f.read()
    return f"错误: 在 {JDS_DIR} 中未找到 JD '{jd_name}'"

def log_candidate(name, role, summary, decision, vector_tags):
    """Logs candidate analysis to history for future comparison."""
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "name": name,
        "role": role,
        "summary": summary,
        "decision": decision,
        "tags": vector_tags # e.g., ["senior", "python", "high-potential"]
    }
    
    if not MEMORY_DIR.exists():
        MEMORY_DIR.mkdir(parents=True)
        
    with open(MEMORY_DIR / "candidate_history.jsonl", "a", encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return "候选人记录已保存。"

def update_learning(feedback_text, rule_category="通用"):
    """Updates the knowledge base with new feedback rules."""
    kb_path = MEMORY_DIR / "knowledge_base.md"
    
    if not MEMORY_DIR.exists():
        MEMORY_DIR.mkdir(parents=True)
        
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entry = f"\n- [{date_str}] **学习到的规则 ({rule_category})**: {feedback_text}"
    
    with open(kb_path, "a", encoding='utf-8') as f:
        f.write(new_entry)
        
    return "知识库已更新。Agent 将在未来的分析中应用此规则。"

def get_history(role_filter=None, limit=5):
    """Retrieves recent candidate history for comparison."""
    history = []
    hist_path = MEMORY_DIR / "candidate_history.jsonl"
    
    if not hist_path.exists():
        return []

    with open(hist_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                try:
                    data = json.loads(line)
                    if role_filter and role_filter.lower() not in data.get('role', '').lower():
                        continue
                    history.append(data)
                except:
                    continue
    
    return history[-limit:]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resume Intelligence Tools")
    subparsers = parser.add_subparsers(dest="command")
    
    # Parse Command
    parse_parser = subparsers.add_parser("parse")
    parse_parser.add_argument("file_path", help="Path to resume file")
    
    # Get JD Command
    jd_parser = subparsers.add_parser("get_jd")
    jd_parser.add_argument("jd_name", help="Name of the JD file")
    
    # Log Command
    log_parser = subparsers.add_parser("log")
    log_parser.add_argument("--name", required=True)
    log_parser.add_argument("--role", required=True)
    log_parser.add_argument("--summary", required=True)
    log_parser.add_argument("--decision", required=True)
    log_parser.add_argument("--tags", default="[]")
    
    # Learn Command
    learn_parser = subparsers.add_parser("learn")
    learn_parser.add_argument("feedback", help="The feedback rule to learn")
    
    # History Command
    hist_parser = subparsers.add_parser("history")
    hist_parser.add_argument("--role", help="Filter by role")
    
    args = parser.parse_args()
    
    if args.command == "parse":
        print(extract_text(args.file_path))
    elif args.command == "get_jd":
        print(get_jd_content(args.jd_name))
    elif args.command == "log":
        print(log_candidate(args.name, args.role, args.summary, args.decision, args.tags))
    elif args.command == "learn":
        print(update_learning(args.feedback))
    elif args.command == "history":
        hist = get_history(args.role)
        print(json.dumps(hist, indent=2, ensure_ascii=False))
