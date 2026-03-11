---
name: qieman-pptx
description: 基于且慢（Qieman）品牌色彩规范的 PowerPoint 演示文稿创建、编辑和分析。当需要创建符合且慢品牌视觉风格的演示文稿时使用此技能，包括创建新演示文稿、修改现有内容、使用模板、添加图表和表格等任务。所有颜色、字体和设计元素严格遵循且慢 UI 设计规范。
---

# 且慢 PowerPoint 演示文稿创建、编辑和分析

## 概述

基于且慢（Qieman）品牌色彩规范的 PowerPoint 演示文稿全流程支持。所有设计元素严格遵循且慢 UI 设计规范，确保品牌一致性。

## 且慢品牌色彩快速参考

| 用途 | 颜色值 | 说明 |
|------|--------|------|
| **品牌主色** | `#1B88EE` | 按钮、链接、强调元素 |
| **页头/页尾背景** | `#3180EC` | 海报和页尾背景 |
| **摘要背景** | `#DBEBFF` | 摘要区域背景 |
| **摘要边框** | `#9CCBF8` | 摘要卡片边框 |
| **重要文字** | `#333333` | 标题、正文 |
| **普通文字** | `#606060` | 描述文字 |
| **次要文字** | `#999999` | 辅助说明 |
| **反色文字** | `#FFFFFF` | 深色背景上使用 |
| **成功/买入** | `#07AD8F` | 正向指标 |
| **警告** | `#EA9500` | 提醒信息 |
| **错误/卖出** | `#FA440C` | 负向指标 |

**图表配色**（按顺序使用）：`#69B1F4` `#F88D72` `#FBCA74` `#7DD4C4` `#68E0F3` `#ADAFE8` `#3A7BB8` `#FAB6A5` `#EDC273` `#9CCBF8` `#C8CAEF` `#6B9CCA`

完整颜色系统详见 [color-system.md](references/color-system.md)

### 字体规范

- **标题字体**：Poppins, Arial, sans-serif
- **正文字体**：Lora, Georgia, serif
- **等宽字体**：'Courier New', monospace

### 字号阶梯

| 类别 | 字号 |
|------|------|
| Title 1-5 | 32pt / 26pt / 24pt / 19pt / 18pt |
| Body 1-3 | 17pt / 16pt / 15pt |
| Caption 1-4 | 14pt / 13pt / 12pt / 11pt |

## 读取和分析内容

### 文本提取

```bash
python -m markitdown path-to-file.pptx
```

### 原始 XML 访问

用于处理注释、演讲者备注、幻灯片布局、动画等复杂格式。

#### 解包文件

```bash
python ooxml/scripts/unpack.py <office_file> <output_dir>
```

**注意**：unpack.py 位于 `skills/pptx/ooxml/scripts/unpack.py`，如不存在使用 `find . -name "unpack.py"` 定位。

#### 关键文件结构

- `ppt/presentation.xml` — 主演示文稿元数据
- `ppt/slides/slide{N}.xml` — 单个幻灯片内容
- `ppt/notesSlides/notesSlide{N}.xml` — 演讲者备注
- `ppt/comments/modernComment_*.xml` — 评论
- `ppt/slideLayouts/` — 布局模板
- `ppt/slideMasters/` — 主幻灯片模板
- `ppt/theme/` — 主题和样式
- `ppt/media/` — 图片和媒体

#### 字体和颜色提取

**分析已有演示文稿时**：
1. 读取 `ppt/theme/theme1.xml` 中的颜色和字体方案
2. 检查 `ppt/slides/slide1.xml` 中的实际使用
3. 用 grep 搜索 `<a:solidFill>`, `<a:srgbClr>` 等模式

## 创建新的 PowerPoint 演示文稿

使用 **html2pptx** 工作流将 HTML 幻灯片转换为 PowerPoint。

### 设计原则

1. **分析内容**：考虑主题、基调和行业特点
2. **品牌优先**：所有颜色必须从且慢颜色系统中选择
3. **视觉层次**：通过字号、粗细和颜色创建清晰层级
4. **可读性**：确保强对比度、适当大小、干净对齐
5. **一致性**：在整个演示文稿中重复模式和视觉语言

视觉设计细节选项详见 [visual-details.md](references/visual-details.md)

### 布局提示

- **两列布局（首选）**：跨全宽标题 + 下方两列（40%/60% 分割）
- **全幻灯片布局**：图表/表格占据整个幻灯片以获最大影响
- **永远不要垂直堆叠**图表/表格于文本下方

### 工作流程

1. **强制 — 读取整个文件**：完整读取 [`html2pptx.md`](html2pptx.md)，不设范围限制
2. 为每张幻灯片创建 HTML 文件（16:9 为 720pt × 405pt）
   - 文本使用 `<p>`、`<h1>`-`<h6>`、`<ul>`、`<ol>`
   - 占位区域使用 `class="placeholder"`
   - 先用 Sharp 将渐变和图标栅格化为 PNG
   - 所有颜色使用且慢颜色值
3. 创建并运行 JavaScript 文件，使用 [`html2pptx.js`](scripts/html2pptx.js) 转换并保存
   - `html2pptx()` 处理每个 HTML 文件
   - PptxGenJS API 添加图表和表格
   - 图表使用 chart01-chart12 配色
4. **视觉验证**：`python scripts/thumbnail.py output.pptx workspace/thumbnails --cols 4`
   - 检查文本截断/重叠/定位/对比度/颜色规范
   - 发现问题则调整并重新生成，直到正确

## 编辑现有 PowerPoint 演示文稿

使用原始 Office Open XML (OOXML) 格式编辑。

### 工作流程

1. **强制 — 读取整个文件**：完整读取 [`ooxml.md`](ooxml.md)，不设范围限制
2. 解包：`python ooxml/scripts/unpack.py <office_file> <output_dir>`
3. 编辑 XML 文件，确保颜色符合且慢品牌规范
4. 验证：`python ooxml/scripts/validate.py <dir> --original <file>`
5. 打包：`python ooxml/scripts/pack.py <input_directory> <office_file>`

## 使用模板创建演示文稿

基于现有模板复制、重排幻灯片后替换内容。

### 工作流程

1. **提取并分析模板**：
   - `python -m markitdown template.pptx > template-content.md`
   - `python scripts/thumbnail.py template.pptx`
   - 创建 `template-inventory.md`，列出每张幻灯片的布局和用途
2. **创建大纲**：基于清单选择布局，匹配内容结构，保存 `outline.md`
3. **重排幻灯片**：`python scripts/rearrange.py template.pptx working.pptx 0,34,34,50,52`
4. **提取文本清单**：`python scripts/inventory.py working.pptx text-inventory.json`
5. **生成替换文本**：创建 `replacement-text.json`
6. **应用替换**：`python scripts/replace.py working.pptx replacement-text.json output.pptx`

模板工作流的详细 JSON 格式和替换规则详见 [template-workflow.md](references/template-workflow.md)

## 缩略图网格

```bash
python scripts/thumbnail.py template.pptx [output_prefix] [--cols 4]
```

- 默认 5 列，每网格最多 30 张幻灯片
- 幻灯片从 0 开始索引
- 网格限制：3列=12张, 4列=20张, 5列=30张, 6列=42张

## 幻灯片转图像

```bash
soffice --headless --convert-to pdf template.pptx
pdftoppm -jpeg -r 150 template.pdf slide
```

## 品牌检查清单

- [ ] 所有颜色来自且慢颜色系统
- [ ] 品牌主色 `#1B88EE` 用于主要强调
- [ ] 文本颜色遵循层级（`#333333` → `#606060` → `#999999`）
- [ ] 图表使用 chart01-chart12 配色
- [ ] 标题 Poppins/Arial，正文 Lora/Georgia
- [ ] 字号符合阶梯规范
- [ ] 背景色/边框色符合规范
- [ ] 功能色（error/warning/success）正确应用

## 依赖项

- **markitdown**：`pip install "markitdown[pptx]"`
- **pptxgenjs**：`npm install -g pptxgenjs`
- **playwright**：`npm install -g playwright`
- **react-icons**：`npm install -g react-icons react react-dom`
- **sharp**：`npm install -g sharp`
- **LibreOffice**：`sudo apt-get install libreoffice`
- **Poppler**：`sudo apt-get install poppler-utils`
- **defusedxml**：`pip install defusedxml`
