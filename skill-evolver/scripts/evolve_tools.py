import os
import shutil
import subprocess
import sys
import json
import tempfile
from pathlib import Path

# 定义基础路径
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # 指向 skills/ 目录
GENERATED_SKILLS_DIR = BASE_DIR / "generated"

def scaffold_skill(name: str) -> str:
    """
    创建一个新的技能脚手架目录。
    返回临时目录的路径。
    """
    # 使用 tempfile 创建一个临时目录，但在系统临时目录中可能不方便查看，
    # 我们在 skill-evolver 下创建一个 workspace 目录
    workspace = Path(__file__).resolve().parent.parent / "sandbox" / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)
    
    skill_dir = workspace / name
    
    if skill_dir.exists():
        shutil.rmtree(skill_dir)
    
    skill_dir.mkdir()
    (skill_dir / "scripts").mkdir()
    (skill_dir / "tests").mkdir()
    (skill_dir / "references").mkdir()
    
    # 创建空的 SKILL.md 模板
    with open(skill_dir / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(f"---\nname: {name}\ndescription: TODO\nversion: 0.1.0\n---\n\n# {name}\n")
        
    return str(skill_dir)

def validate_skill(path: str) -> dict:
    """
    运行技能目录下的测试用例。
    """
    skill_path = Path(path)
    test_dir = skill_path / "tests"
    
    if not test_dir.exists() or not list(test_dir.glob("test_*.py")):
        return {
            "success": False,
            "logs": "No tests found in 'tests/' directory. Evolution requires validation."
        }
    
    # 安装依赖 (如果有 requirements.txt)
    req_file = skill_path / "requirements.txt"
    if req_file.exists():
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", str(req_file)],
                check=True,
                capture_output=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "logs": f"Dependency installation failed:\n{e.stderr}"
            }

    # 运行测试
    # 尝试使用 pytest，如果失败则尝试 unittest
    logs = []
    success = False
    
    # 检查 pytest 是否可用
    has_pytest = False
    try:
        subprocess.run([sys.executable, "-m", "pytest", "--version"], check=True, capture_output=True)
        has_pytest = True
    except subprocess.CalledProcessError:
        pass

    if has_pytest:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_dir)],
                capture_output=True,
                text=True
            )
            logs.append("--- Pytest Output ---")
            logs.append(result.stdout)
            logs.append(result.stderr)
            
            if result.returncode == 0:
                success = True
        except Exception as e:
            logs.append(f"Pytest execution error: {str(e)}")
    
    # 如果 pytest 不可用或失败，且我们还没成功，尝试 unittest
    if not success:
        logs.append("--- Fallback to Unittest ---")
        try:
            # 使用 unittest discover
            result = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "-s", str(test_dir), "-p", "test_*.py"],
                capture_output=True,
                text=True
            )
            logs.append(result.stdout)
            logs.append(result.stderr)
            
            if result.returncode == 0:
                success = True
        except Exception as e:
            logs.append(f"Unittest execution error: {str(e)}")
            
    return {
        "success": success,
        "logs": "\n".join(logs)
    }

def deploy_skill(source_path: str, category: str = "generated") -> str:
    """
    将验证通过的技能部署到正式目录。
    """
    src = Path(source_path)
    skill_name = src.name
    
    # 目标路径：skills/clair_skills/<category>/<skill_name> 
    # 或者 skills/<category>/<skill_name>
    # 这里默认放到 skills/generated/<category>/<skill_name> 以示区分
    
    # 为了简单，我们假设 category 是相对于 skills/ 根目录的子目录
    # 如果 category 是 "clair_skills/new_tools"，则路径为 skills/clair_skills/new_tools/skill_name
    
    # 修正：默认部署到 skills/clair_skills/imported (如果未指定) 或者用户指定的 category
    if category == "generated":
        target_base = BASE_DIR / "clair_skills" / "generated"
    else:
        target_base = BASE_DIR / category
        
    target_path = target_base / skill_name
    
    target_base.mkdir(parents=True, exist_ok=True)
    
    if target_path.exists():
        shutil.rmtree(target_path)
        
    shutil.copytree(src, target_path)
    
    # 清理临时目录
    # shutil.rmtree(src) # 可选：保留以便调试，或者由 scaffold 清理
    
    return str(target_path)

if __name__ == "__main__":
    # 简单的 CLI 接口供测试
    import argparse
    parser = argparse.ArgumentParser(description="Skill Evolver Tools")
    subparsers = parser.add_subparsers(dest="command")
    
    scaffold_parser = subparsers.add_parser("scaffold")
    scaffold_parser.add_argument("name")
    
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path")
    
    deploy_parser = subparsers.add_parser("deploy")
    deploy_parser.add_argument("path")
    deploy_parser.add_argument("--category", default="generated")
    
    args = parser.parse_args()
    
    if args.command == "scaffold":
        print(scaffold_skill(args.name))
    elif args.command == "validate":
        res = validate_skill(args.path)
        print(json.dumps(res, indent=2))
    elif args.command == "deploy":
        print(deploy_skill(args.path, args.category))
