---
name: ppt-parser
description: PPT 内容提取工具。从 PowerPoint 演示文稿 (.pptx) 中提取文本、表格和演讲者备注。当用户需要阅读、分析或总结 PowerPoint 文件内容时触发。
---

# PPT 内容解析器 (PowerPoint Parser)

从 PowerPoint 演示文稿中提取结构化内容，支持幻灯片标题、正文文本、表格数据和演讲者备注。

## 使用场景

- 需要阅读和理解 PPT 文件的内容
- 需要总结或分析演示文稿
- 需要从 PPT 中提取特定信息

## 提取内容

- 幻灯片标题
- 文本框和形状中的文本内容
- 表格数据
- 演讲者备注

## 使用方法

### 提取为 Markdown（推荐）

默认输出格式，最适合阅读和分析：

```bash
python scripts/extract_ppt.py <PPT文件路径>
```

### 提取为 JSON

需要结构化数据进行进一步处理时使用：

```bash
python scripts/extract_ppt.py <PPT文件路径> --format json
```

## 依赖安装

此技能需要 `python-pptx` 库：

```bash
pip install -r requirements.txt
```

## 使用示例

### 示例 1: 总结演示文稿

```bash
# 1. 提取内容
python scripts/extract_ppt.py presentation.pptx > content.md

# 2. 读取 content.md 并进行总结
```

### 示例 2: 查找特定内容

```bash
# 1. 提取内容
python scripts/extract_ppt.py report.pptx

# 2. 使用 grep 搜索关键词
grep "目标" content.md
```

## 输出格式说明

### Markdown 输出

```markdown
# Presentation Content

## Slide 1: 标题
### Content
- 内容项 1
- 内容项 2

### Notes
演讲者备注内容...

---

## Slide 2: 第二页标题
...
```

### JSON 输出

```json
[
  {
    "slide_number": 1,
    "title": "标题",
    "content": ["内容项 1", "内容项 2"],
    "notes": "演讲者备注内容"
  }
]
```
