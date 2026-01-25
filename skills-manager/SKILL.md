---
name: skills-manager
description: 技能管理器。扫描、更新、整理工作区所有Skill，生成清单，检测冲突。自动适配任何目录结构，与 skill-scanner 协同管理技能生命周期。
version: 2.0.0
author: Clair
---

# Skills Manager

技能管理器。扫描、更新、汇总整理当前环境中的所有 Agent Skills。
支持自动从远程仓库拉取最新技能，并生成详细的冲突分析报告。

## 核心特性

- **自动适配**：无需配置，自动检测现有目录结构
- **灵活配置**：通过 `sources.md` 配置任意远程仓库
- **冲突检测**：识别同名技能，提供解决建议
- **跨环境兼容**：在任何目录结构下都能正常工作

## 目录结构自动检测

本技能会自动扫描你的 `skills/` 目录，无需手动配置目录结构。

### 典型目录布局示例

```
skills/
├── <官方技能目录>/       # 由 skills-manager 更新的官方技能
│   ├── <provider-1>/     # 如 anthropics, openai 等
│   └── <provider-2>/
├── <用户技能目录>/       # 用户自己创建的技能
└── <第三方技能目录>/     # 由 skill-scanner 安装的第三方技能
    ├── <category-1>/     # 如 agent, dev, tools 等
    └── <category-2>/
```

具体目录名称由你的环境决定，脚本会自动识别和适配。

## 使用场景

* 想要查看当前有哪些可用的 Skills。
* 需要检查 Skills 是否有重复或冲突。
* 想要从配置的源自动更新 Skills。
* 生成 Skills 汇总清单。

## 核心功能

1. **自动更新 (Auto Update & Sparse Checkout)**：
   * 读取 `reference/sources.md` 配置清单。
   * **精准拉取**：使用 Git Sparse Checkout 仅拉取仓库中的 `skills` 相关目录，不包含杂乱的非技能文件。
   * **缓存机制**：在 `.cache` 目录维护镜像，确保更新高效且安全。
   * 自动去重：根据 `skills-manager/reference/sources.md`仓库更新顺序去重，保留先添加更新到本地的skill。
2. **全域扫描与智能过滤 (Smart Scan)**：
   * 遍历 `skills/` 目录下所有 `SKILL.md` 文件。
3. **生成报告 (Report Generation)**：
   * 输出 `skills/SKILLS_LIST.md`。
   * 依序包含：技能统计、完整技能清单、冲突详情、更新日志。

## 使用方法

### 1. 常用指令

* 用户: "我现在有哪些 skills？"
* 用户: "帮我检查一下 skills 有没有重复的"
* 用户: "帮我更新一下 skills"
* 用户: "生成 skills 清单"

### 2. 执行脚本

当用户请求更新或检查 Skills 时，请直接运行以下脚本，并根据输出的 Markdown 报告回答用户。

**仅扫描并生成报告 (推荐)**:

```bash
python3 skills/<category>/skills-manager/scripts/manage_skills.py
```

**拉取远程更新并生成报告**:

```bash
python3 skills/<category>/skills-manager/scripts/manage_skills.py --update
```

脚本执行完毕后，请读取 `skills/SKILLS_LIST.md` 为用户进行总结。

## 配置文件

配置文件位于：`skills/<category>/skills-manager/reference/sources.md` (Markdown 表格格式)

| Name             | URL                                      | Local Path                        | Remote Subfolder | Branch | Flatten |
| ---------------- | ---------------------------------------- | --------------------------------- | ---------------- | ------ | ------- |
| Anthropic Skills | https://github.com/anthropics/skills.git | skills/official_skills/anthropics | skills           | main   | Yes     |
| ...              | ...                                      | ...                               | ...              | ...    | ...     |

* **Remote Subfolder**: 指定只拉取远程仓库的哪个子目录（空格分隔）。如 `skills` 或 `.` (全部)。
* **Flatten**: 是否将 Remote Subfolder 的内容平铺到 Local Path (去除 Remote Subfolder 目录层级)。Yes/No。

## 输出格式约定

生成的清单文件位于：`skills/SKILLS_LIST.md`，采用以下格式约定以优化中文阅读体验：

### 报告结构

* **Update Status**: 自动更新的日志，显示各仓库的更新成功/失败状态。
* **Summary**: 技能总数、冲突数及过滤规则说明。
* **Conflict Analysis**: (如有) 列出同名技能的文件路径冲突，提示是否内容一致。
* **Skills List**: 核心技能表格。
* **Update History**: 本次运行的新增/删除技能记录。

### 技能表格字段约定

| 字段                         | 格式约定                                                        | 示例                                       |
| ---------------------------- | --------------------------------------------------------------- | ------------------------------------------ |
| **名称 (Name)**              | **中文名称** `<br>英文ID`                                       | **算法艺术** `<br>algorithmic-art`         |
| **描述 (Description)**       | 优先显示中文描述。`<br>`无翻译则显示原文并标记 `*(待翻译)*`     | 使用 p5.js 创建...                         |
| **来源 (Source)**            | 技能所属仓库或来源                                              | Anthropic, OpenAI, Yingmi                  |

## 与 skill-scanner 的协作

`skills-manager` 和 `skill-scanner` 是技能管理的两个核心组件，各有分工：

| 功能 | skills-manager | skill-scanner |
|------|----------------|---------------|
| **更新配置的源** | ✅ 从 sources.md 配置的源自动更新 | ❌ |
| **安装第三方技能** | ❌ | ✅ 扫描任意 GitHub 仓库并安装 |
| **生成技能清单** | ✅ 输出 SKILLS_LIST.md | ❌ |
| **检测冲突** | ✅ 识别同名技能冲突 | ✅ 安装前检查是否已存在 |
| **自动分类** | ✅ 按来源组织 | ✅ 按关键词分类 |

### 推荐工作流

1. **安装新的第三方技能**：使用 `skill-scanner`
   ```bash
   # 脚本会自动检测目录结构并安装到合适位置
   python3 <skill-scanner-path>/scripts/scan_and_install.py --url <REPO_URL>
   ```

2. **更新配置的源**：使用 `skills-manager`
   ```bash
   python3 <skills-manager-path>/scripts/manage_skills.py --update
   ```

3. **生成最新清单**：使用 `skills-manager`
   ```bash
   python3 <skills-manager-path>/scripts/manage_skills.py
   ```

两个技能都会自动检测目录结构，无需手动配置目录名称。
