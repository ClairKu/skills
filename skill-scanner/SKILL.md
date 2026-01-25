---
name: skill-scanner
description: 扫描 GitHub 仓库或本地目录，发现符合 Anthropic 标准的 Skills，与本地 Skills 库进行对比，并支持一键安装新技能。自动检测目录结构并智能分类安装，适配任何 Skills 目录布局。
version: 2.0.0
author: Clair
---

该技能用于发现、对比和安装新的 Skills。遵循 Anthropic 的 Skill 结构规范（包含 `SKILL.md` 的目录）。

## 核心特性

- **自动适配**：无需配置，自动检测现有目录结构
- **智能分类**：基于关键词将技能分配到合适的分类目录
- **可配置**：支持通过配置文件自定义行为
- **跨环境兼容**：在任何目录结构下都能正常工作

## 使用场景

当你想从外部仓库（如 `anthropics/skills` 或其他开源仓库）引入新技能时使用。

## 目录结构自动检测

脚本会自动扫描你的 `skills/` 目录，检测：

1. **官方技能目录**：包含 `official`, `anthropic`, `openai`, `huggingface` 等关键词的目录
2. **第三方技能目录**：包含 `other`, `third`, `community`, `external`, `imported` 等关键词的目录
3. **现有分类**：扫描已存在的分类子目录

如果检测不到，默认安装到 `skills/imported/` 目录。

## 核心功能

1. **扫描 (Scan)**: 给定一个 Git URL 或本地路径，递归查找所有包含 `SKILL.md` 的子目录。
2. **对比 (Compare)**: 将扫描到的技能与当前 `skills/` 目录进行对比，识别新技能和已存在的技能。
3. **智能安装 (Smart Install)**: 
   * 自动检测目录结构
   * 识别官方仓库 vs 第三方仓库
   * 基于关键词自动分类
   * 优先使用已存在的分类目录

## 使用方法

### 1. 扫描并交互式安装（推荐）

```bash
python3 path/to/skill-scanner/scripts/scan_and_install.py --url <GIT_REPO_URL>
```

工具会自动：
1. 检测现有目录结构
2. 扫描远程仓库中的技能
3. 与本地技能对比，显示新技能
4. 交互式选择要安装的技能
5. 自动分类并安装到合适位置

### 2. 自定义安装路径

```bash
# 指定目标目录（覆盖自动检测）
python3 scripts/scan_and_install.py \
  --url <GIT_REPO_URL> \
  --target-dir ./my-skills/custom-folder

# 禁用自动分类
python3 scripts/scan_and_install.py \
  --url <GIT_REPO_URL> \
  --no-auto-cat
```

### 3. 仅扫描并生成报告

```bash
python3 scripts/scan_and_install.py --url <GIT_REPO_URL> --report-only
```

## 自定义配置（可选）

在 `skills/` 目录下创建 `.skills-config.json` 文件来自定义行为：

```json
{
  "official_sources": {
    "anthropics/skills": "official/anthropics",
    "openai/codex-skills": "official/openai"
  },
  "third_party_dir": "community",
  "categories": ["ai", "dev", "tools", "docs"],
  "category_keywords": {
    "ai": ["agent", "llm", "prompt", "ai"],
    "dev": ["code", "git", "test", "api"],
    "tools": ["utility", "automation"],
    "docs": ["doc", "writing", "content"]
  }
}
```

如果不创建配置文件，脚本会自动检测并使用合理的默认值。

## 默认分类关键词

| 分类 | 关键词 |
|------|--------|
| agent-engineering | agent, llm, prompt, context, memory, tool, skill, reasoning, planning, eval, mcp |
| content-design | content, design, video, image, writing, doc, visual, media, transcript, youtube |
| product-management | product, planning, story, requirement, rfp, project, roadmap, agile, jira |
| research-analysis | research, analysis, data, search, paper, arxiv, obsidian, finance, market |
| software-development | code, dev, git, test, debug, python, react, api, web, backend, frontend, deploy |
| productivity-tools | organizer, invoice, email, calendar, job, download, utility, automation |

## 依赖

* Python 3
* Git (如果扫描远程仓库)
* Standard libraries (os, re, shutil, subprocess, tempfile, json)
