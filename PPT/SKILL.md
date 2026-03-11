---
name: qieman-pptx
description: "基于且慢（Qieman）品牌色彩规范的 PowerPoint 演示文稿创建、编辑和分析。当需要创建符合且慢品牌视觉风格的演示文稿时使用此技能，包括：创建新演示文稿、修改现有内容、使用模板、添加图表和表格等任务。所有颜色、字体和设计元素严格遵循且慢 UI 设计规范。"
license: Complete terms in LICENSE.txt
---

# 且慢 PowerPoint 演示文稿创建、编辑和分析

## 概述

本技能提供基于且慢（Qieman）品牌色彩规范的 PowerPoint 演示文稿创建、编辑和分析能力。所有设计元素（颜色、字体、布局）严格遵循且慢 UI 设计规范，确保品牌一致性。

**关键词**：且慢PPT、Qieman演示文稿、品牌演示、金融报告、数据可视化、且慢设计规范、盈米基金

## 且慢品牌色彩规范

### 主色与品牌色

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **brand** | `#1B88EE` | 品牌主色，用于按钮、链接、强调元素 |
| **poster-bg** | `#3180EC` | 页头海报和页尾的背景色 |
| **summary-bg** | `#DBEBFF` | 摘要区域的背景色 |
| **summary-border** | `#9CCBF8` | 摘要卡片的边框颜色 |

### 文本颜色层级

| 层级 | 颜色值 | 用途 |
|------|--------|------|
| **text/neutral** | `#333333` | 标题文字、正文文字等较重要文字 |
| **text/neutral subtle** | `#606060` | 正文、少部分描述文字等较为重要的文字 |
| **text/neutral subtler** | `#999999` | Icon、描述、辅助说明文字等次要文字 |
| **text/neutral subtlest** | `#CCCCCC` | 辅助icon、辅助描述文本 |
| **text/inverse** | `#FFFFFF` | 反色文字（用于深色背景） |

### 功能色

| 功能 | 颜色值 | 用途 |
|------|--------|------|
| **text/primary** | `#1B88EE` | 成功、链接色 |
| **text/error** | `#FA440C` | 警告、卖出（上涨） |
| **text/warning** | `#EA9500` | 提醒、信息 |
| **text/success** | `#07AD8F` | 买入、下跌 |

### 页面背景色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **background/page/deep** | `#F9FAFB` | 浅灰色背景适用于页面背景 |

### 卡片背景色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **background/card/default** | `#FFFFFF` | 白色卡片背景 |
| **background/card/deep** | `#F9FAFB` | 浅灰卡片背景 |
| **background/card/deeper** | `#F7F7F7` | 中灰色卡片背景 |
| **background/card/primary faded** | `#F0F6FF` | 高亮、成功卡片背景 |
| **background/card/warning faded** | `#FFFAEF` | 提醒卡片背景 |
| **background/card/error faded** | `#FEEDE9` | 出错、警示卡片背景 |

### 边框颜色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **border/neutral faded** | `#D8D8D8` | 灰色边框（默认） |
| **border/primary** | `#1B88EE` | 强调边框 |
| **border/neutral blue** | `#9CCBF8` | 蓝色边框 |
| **border/neutral yellow** | `#FFDC9E` | 黄色边框 |
| **border/neutral red** | `#FAB6A5` | 红色边框 |

### 图表数据颜色

用于数据可视化的12色配色系统，按顺序使用：

| 编号 | 颜色值 | 用途 |
|------|--------|------|
| **chart01** | `#69B1F4` | 柱状图、折线图主色 |
| **chart02** | `#F88D72` | 对比数据、次要系列 |
| **chart03** | `#FBCA74` | 警告数据、特殊标记 |
| **chart04** | `#7DD4C4` | 成功数据、正向指标 |
| **chart05** | `#68E0F3` | 辅助数据系列 |
| **chart06** | `#ADAFE8` | 辅助数据系列 |
| **chart07** | `#3A7BB8` | 深色数据系列 |
| **chart08** | `#FAB6A5` | 错误数据、负向指标 |
| **chart09** | `#EDC273` | 中性数据系列 |
| **chart10** | `#9CCBF8` | 浅色数据系列 |
| **chart11** | `#C8CAEF` | 浅色数据系列 |
| **chart12** | `#6B9CCA` | 中等深度数据系列 |

### 且慢字体规范

- **标题字体**: Poppins, Arial, sans-serif
- **正文字体**: Lora, Georgia, serif
- **等宽字体**: 'Courier New', monospace（用于代码、数据展示）

### 字号阶梯

#### 标题字号
- **Title 1**: `32pt` - 主标题、大标题
- **Title 2**: `26pt` - 二级标题
- **Title 3**: `24pt` - 三级标题
- **Title 4**: `19pt` - 四级标题
- **Title 5**: `18pt` - 五级标题

#### 正文字号
- **Body 1**: `17pt` - 主要正文
- **Body 2**: `16pt` - 标准正文
- **Body 3**: `15pt` - 次要正文

#### 说明文字字号
- **Caption 1**: `14pt` - 说明文字
- **Caption 2**: `13pt` - 次要说明
- **Caption 3**: `12pt` - 辅助说明
- **Caption 4**: `11pt` - 最小说明文字

## 读取和分析内容

### 文本提取
如果只需要读取演示文稿的文本内容，可以转换为 markdown：

```bash
# 转换文档为 markdown
python -m markitdown path-to-file.pptx
```

### 原始 XML 访问
需要原始 XML 访问以处理：注释、演讲者备注、幻灯片布局、动画、设计元素和复杂格式。对于这些功能，需要解包演示文稿并读取其原始 XML 内容。

#### 解包文件
`python ooxml/scripts/unpack.py <office_file> <output_dir>`

**注意**：unpack.py 脚本位于 `skills/pptx/ooxml/scripts/unpack.py`（相对于项目根目录）。如果脚本不存在于此路径，使用 `find . -name "unpack.py"` 定位它。

#### 关键文件结构
* `ppt/presentation.xml` - 主演示文稿元数据和幻灯片引用
* `ppt/slides/slide{N}.xml` - 单个幻灯片内容（slide1.xml, slide2.xml 等）
* `ppt/notesSlides/notesSlide{N}.xml` - 每张幻灯片的演讲者备注
* `ppt/comments/modernComment_*.xml` - 特定幻灯片的评论
* `ppt/slideLayouts/` - 幻灯片布局模板
* `ppt/slideMasters/` - 主幻灯片模板
* `ppt/theme/` - 主题和样式信息
* `ppt/media/` - 图片和其他媒体文件

#### 字体和颜色提取
**当给定示例设计以模仿时**：始终首先使用以下方法分析演示文稿的字体和颜色：
1. **读取主题文件**：检查 `ppt/theme/theme1.xml` 中的颜色（`<a:clrScheme>`）和字体（`<a:fontScheme>`）
2. **采样幻灯片内容**：检查 `ppt/slides/slide1.xml` 中的实际字体使用（`<a:rPr>`）和颜色
3. **搜索模式**：使用 grep 在所有 XML 文件中查找颜色（`<a:solidFill>`, `<a:srgbClr>`）和字体引用

## 创建新的 PowerPoint 演示文稿（不使用模板）

创建新的 PowerPoint 演示文稿时，使用 **html2pptx** 工作流程将 HTML 幻灯片转换为 PowerPoint，并确保精确定位。

### 设计原则

**关键**：在创建任何演示文稿之前，分析内容并选择适当的设计元素：
1. **考虑主题**：这个演示文稿是关于什么的？它暗示了什么基调、行业或情绪？
2. **检查品牌**：如果用户提到公司/组织，考虑其品牌颜色和身份
3. **匹配调色板到内容**：选择反映主题的颜色
4. **说明你的方法**：在编写代码之前解释你的设计选择

**且慢品牌要求**：
- ✅ **必须使用且慢色彩规范**：所有颜色必须从上述且慢颜色系统中选择
- ✅ **品牌主色优先**：主要强调元素使用 `#1B88EE`
- ✅ **文本层级清晰**：标题使用 `#333333`，正文使用 `#606060`，辅助文字使用 `#999999`
- ✅ **图表配色**：数据图表必须使用 chart01-chart12 配色系统
- ✅ **字体规范**：标题使用 Poppins/Arial，正文使用 Lora/Georgia
- ✅ **视觉层次**：通过大小、粗细和颜色创建清晰的视觉层次
- ✅ **可读性**：确保强对比度、适当大小的文本、干净的对齐
- ✅ **一致性**：在整个演示文稿中重复模式、间距和视觉语言

#### 且慢调色板选择指南

**且慢品牌调色板**（必须使用）：
1. **主色系**：`#1B88EE`（品牌主色）+ `#3180EC`（页头背景）+ `#DBEBFF`（摘要背景）
2. **文本层级**：`#333333`（重要）→ `#606060`（普通）→ `#999999`（次要）→ `#CCCCCC`（最次要）
3. **功能色**：`#1B88EE`（主要/成功）→ `#07AD8F`（成功/买入）→ `#EA9500`（警告）→ `#FA440C`（错误/卖出）
4. **背景色**：`#FFFFFF`（卡片）→ `#F9FAFB`（页面）→ `#F7F7F7`（深灰卡片）
5. **图表色**：按顺序使用 chart01-chart12（`#69B1F4`, `#F88D72`, `#FBCA74`, `#7DD4C4`, `#68E0F3`, `#ADAFE8`, `#3A7BB8`, `#FAB6A5`, `#EDC273`, `#9CCBF8`, `#C8CAEF`, `#6B9CCA`）

**选择原则**：
- **金融报告**：使用主色系 + 功能色（成功/错误用于涨跌）
- **数据展示**：使用图表配色系统，确保色盲友好
- **强调内容**：使用 `#1B88EE` 或 `#3180EC` 作为强调色
- **背景选择**：白色卡片（`#FFFFFF`）用于主要内容，浅灰（`#F9FAFB`）用于页面背景

#### 视觉细节选项

**几何图案**：
- 对角线部分分隔符而非水平线
- 非对称列宽（30/70, 40/60, 25/75）
- 90° 或 270° 旋转的文本标题
- 圆形/六边形图像框架
- 角落的三角形强调形状
- 重叠形状以增加深度

**边框和框架处理**：
- 单侧厚单色边框（10-20pt）
- 双线边框，对比色
- 角括号而非完整框架
- L 形边框（顶部+左侧或底部+右侧）
- 标题下方的下划线强调（3-5pt 厚）

**字体处理**：
- 极端大小对比（72pt 标题 vs 11pt 正文）
- 全大写标题，宽字母间距
- 超大显示类型的编号部分
- 等宽字体（Courier New）用于数据/统计/技术内容
- 压缩字体（Arial Narrow）用于密集信息
- 轮廓文本用于强调

**图表和数据样式**：
- 单色图表，关键数据使用单一强调色
- 水平条形图而非垂直
- 点图而非条形图
- 最小网格线或无网格线
- 元素上的直接数据标签（无图例）
- 关键指标的超大数字

**布局创新**：
- 全出血图像，文本叠加
- 侧边栏列（20-30% 宽度）用于导航/上下文
- 模块化网格系统（3×3, 4×4 块）
- Z 形或 F 形内容流
- 彩色形状上的浮动文本框
- 杂志风格的多列布局

**背景处理**：
- 占据幻灯片 40-60% 的纯色块
- 渐变填充（仅垂直或对角线）
- 分割背景（两种颜色，对角线或垂直）
- 边缘到边缘的色带
- 负空间作为设计元素

### 布局提示
**创建包含图表或表格的幻灯片时**：
- **两列布局（首选）**：使用跨全宽的标题，然后下方两列 - 一列文本/项目符号，另一列特色内容。这提供了更好的平衡，使图表/表格更易读。使用不等列宽的 flexbox（例如，40%/60% 分割）以优化每种内容类型的空间。
- **全幻灯片布局**：让特色内容（图表/表格）占据整个幻灯片以获得最大影响和可读性
- **永远不要垂直堆叠**：不要将图表/表格放在单列中的文本下方 - 这会导致可读性差和布局问题

### 工作流程
1. **强制 - 读取整个文件**：从头到尾完整读取 [`html2pptx.md`](html2pptx.md)。**读取此文件时永远不要设置任何范围限制。** 在继续创建演示文稿之前，阅读完整文件内容以了解详细语法、关键格式规则和最佳实践。
2. 为每张幻灯片创建具有适当尺寸的 HTML 文件（例如，16:9 为 720pt × 405pt）
   - 对所有文本内容使用 `<p>`、`<h1>`-`<h6>`、`<ul>`、`<ol>`
   - 对将添加图表/表格的区域使用 `class="placeholder"`（渲染为灰色背景以可见）
   - **关键**：首先使用 Sharp 将渐变和图标栅格化为 PNG 图像，然后在 HTML 中引用
   - **布局**：对于包含图表/表格/图像的幻灯片，使用全幻灯片布局或两列布局以获得更好的可读性
   - **且慢颜色应用**：在 HTML/CSS 中使用且慢颜色值，确保所有颜色符合品牌规范
3. 创建并运行使用 [`html2pptx.js`](scripts/html2pptx.js) 库的 JavaScript 文件，将 HTML 幻灯片转换为 PowerPoint 并保存演示文稿
   - 使用 `html2pptx()` 函数处理每个 HTML 文件
   - 使用 PptxGenJS API 向占位符区域添加图表和表格
   - **图表配色**：使用且慢 chart01-chart12 配色系统
   - 使用 `pptx.writeFile()` 保存演示文稿
4. **视觉验证**：生成缩略图并检查布局问题
   - 创建缩略图网格：`python scripts/thumbnail.py output.pptx workspace/thumbnails --cols 4`
   - 仔细阅读并检查缩略图图像：
     - **文本截断**：文本被标题栏、形状或幻灯片边缘截断
     - **文本重叠**：文本与其他文本或形状重叠
     - **定位问题**：内容太靠近幻灯片边界或其他元素
     - **对比度问题**：文本与背景之间的对比度不足
     - **颜色规范**：验证所有颜色符合且慢品牌规范
   - 如果发现问题，调整 HTML 边距/间距/颜色并重新生成演示文稿
   - 重复直到所有幻灯片在视觉上正确

## 编辑现有 PowerPoint 演示文稿

编辑现有 PowerPoint 演示文稿中的幻灯片时，需要使用原始 Office Open XML (OOXML) 格式。这涉及解包 .pptx 文件、编辑 XML 内容并重新打包。

### 工作流程
1. **强制 - 读取整个文件**：从头到尾完整读取 [`ooxml.md`](ooxml.md)（约 500 行）。**读取此文件时永远不要设置任何范围限制。** 在进行任何演示文稿编辑之前，阅读完整文件内容以了解 OOXML 结构和编辑工作流程的详细指导。
2. 解包演示文稿：`python ooxml/scripts/unpack.py <office_file> <output_dir>`
3. 编辑 XML 文件（主要是 `ppt/slides/slide{N}.xml` 和相关文件）
   - **应用且慢颜色**：在编辑时，确保所有颜色值符合且慢品牌规范
   - **更新主题**：如果需要，更新 `ppt/theme/theme1.xml` 以包含且慢颜色方案
4. **关键**：每次编辑后立即验证并修复任何验证错误，然后再继续：`python ooxml/scripts/validate.py <dir> --original <file>`
5. 打包最终演示文稿：`python ooxml/scripts/pack.py <input_directory> <office_file>`

## 使用模板创建新的 PowerPoint 演示文稿

需要创建遵循现有模板设计的演示文稿时，需要先复制和重新排列模板幻灯片，然后替换占位符内容。

### 工作流程
1. **提取模板文本并创建视觉缩略图网格**：
   * 提取文本：`python -m markitdown template.pptx > template-content.md`
   * 读取 `template-content.md`：读取整个文件以了解模板演示文稿的内容。**读取此文件时永远不要设置任何范围限制。**
   * 创建缩略图网格：`python scripts/thumbnail.py template.pptx`
   * 有关更多详细信息，请参阅 [创建缩略图网格](#创建缩略图网格) 部分

2. **分析模板并将清单保存到文件**：
   * **视觉分析**：查看缩略图网格以了解幻灯片布局、设计模式和视觉结构
   * 在 `template-inventory.md` 创建并保存模板清单文件，包含：
     ```markdown
     # 模板清单分析
     **总幻灯片数：[数量]**
     **重要：幻灯片从 0 开始索引（第一张幻灯片 = 0，最后一张幻灯片 = count-1）**

     ## [类别名称]
     - 幻灯片 0：[布局代码（如果可用）] - 描述/用途
     - 幻灯片 1：[布局代码] - 描述/用途
     - 幻灯片 2：[布局代码] - 描述/用途
     [... 每张幻灯片必须单独列出其索引 ...]
     ```
   * **使用缩略图网格**：参考视觉缩略图以识别：
     - 布局模式（标题幻灯片、内容布局、部分分隔符）
     - 图像占位符位置和数量
     - 幻灯片组之间的设计一致性
     - 视觉层次和结构
   * 此清单文件是下一步选择适当模板所必需的

3. **基于模板清单创建演示文稿大纲**：
   * 查看步骤 2 中的可用模板。
   * 为第一张幻灯片选择介绍或标题模板。这应该是第一个模板之一。
   * 为其他幻灯片选择安全的、基于文本的布局。
   * **关键：匹配布局结构到实际内容**：
     - 单列布局：用于统一叙述或单一主题
     - 两列布局：仅在您有恰好 2 个不同项目/概念时使用
     - 三列布局：仅在您有恰好 3 个不同项目/概念时使用
     - 图像 + 文本布局：仅在您有实际图像要插入时使用
     - 引用布局：仅用于实际的人员引用（带归属），从不用于强调
     - 永远不要使用占位符多于您有内容的布局
     - 如果您有 2 个项目，不要将它们强制放入 3 列布局
     - 如果您有 4+ 个项目，考虑分成多张幻灯片或使用列表格式
   * 在选择布局之前计算您的实际内容片段
   * 验证所选布局中的每个占位符都将填充有意义的内容
   * 选择代表每个内容部分的**最佳**布局的一个选项。
   * 保存 `outline.md`，包含内容和使用可用设计的模板映射
   * 示例模板映射：
      ```
      # 要使用的模板幻灯片（基于 0 的索引）
      # 警告：验证索引在范围内！有 73 张幻灯片的模板的索引为 0-72
      # 映射：大纲中的幻灯片编号 -> 模板幻灯片索引
      template_mapping = [
          0,   # 使用幻灯片 0（标题/封面）
          34,  # 使用幻灯片 34（B1：标题和正文）
          34,  # 再次使用幻灯片 34（第二张 B1 的副本）
          50,  # 使用幻灯片 50（E1：引用）
          54,  # 使用幻灯片 54（F2：结束 + 文本）
      ]
      ```

4. **使用 `rearrange.py` 复制、重新排序和删除幻灯片**：
   * 使用 `scripts/rearrange.py` 脚本创建具有所需顺序幻灯片的新演示文稿：
     ```bash
     python scripts/rearrange.py template.pptx working.pptx 0,34,34,50,52
     ```
   * 脚本自动处理重复幻灯片的复制、删除未使用的幻灯片和重新排序
   * 幻灯片索引从 0 开始（第一张幻灯片是 0，第二张是 1，等等）
   * 同一幻灯片索引可以出现多次以复制该幻灯片

5. **使用 `inventory.py` 脚本提取所有文本**：
   * **运行清单提取**：
     ```bash
     python scripts/inventory.py working.pptx text-inventory.json
     ```
   * **读取 text-inventory.json**：读取整个 text-inventory.json 文件以了解所有形状及其属性。**读取此文件时永远不要设置任何范围限制。**

   * 清单 JSON 结构：
      ```json
        {
          "slide-0": {
            "shape-0": {
              "placeholder_type": "TITLE",  // 或 null 对于非占位符
              "left": 1.5,                  // 位置（英寸）
              "top": 2.0,
              "width": 7.5,
              "height": 1.2,
              "paragraphs": [
                {
                  "text": "段落文本",
                  // 可选属性（仅在非默认时包含）：
                  "bullet": true,           // 明确检测到的项目符号
                  "level": 0,               // 仅在 bullet 为 true 时包含
                  "alignment": "CENTER",    // CENTER, RIGHT（不是 LEFT）
                  "space_before": 10.0,     // 段落前间距（点）
                  "space_after": 6.0,       // 段落后间距（点）
                  "line_spacing": 22.4,     // 行间距（点）
                  "font_name": "Arial",     // 来自第一次运行
                  "font_size": 14.0,        // 点
                  "bold": true,
                  "italic": false,
                  "underline": false,
                  "color": "FF0000"         // RGB 颜色
                }
              ]
            }
          }
        }
      ```

   * 关键特性：
     - **幻灯片**：命名为 "slide-0"、"slide-1" 等
     - **形状**：按视觉位置排序（从上到下，从左到右）为 "shape-0"、"shape-1" 等
     - **占位符类型**：TITLE, CENTER_TITLE, SUBTITLE, BODY, OBJECT, 或 null
     - **默认字体大小**：从布局占位符提取的 `default_font_size`（点）（如果可用）
     - **幻灯片编号已过滤**：具有 SLIDE_NUMBER 占位符类型的形状自动从清单中排除
     - **项目符号**：当 `bullet: true` 时，`level` 始终包含（即使为 0）
     - **间距**：`space_before`、`space_after` 和 `line_spacing`（点）（仅在设置时包含）
     - **颜色**：`color` 用于 RGB（例如，"FF0000"），`theme_color` 用于主题颜色（例如，"DARK_1"）
     - **属性**：仅非默认值包含在输出中

6. **生成替换文本并将数据保存到 JSON 文件**
   基于上一步的文本清单：
   - **关键**：首先验证清单中存在哪些形状 - 仅引用实际存在的形状
   - **验证**：replace.py 脚本将验证替换 JSON 中的所有形状是否存在于清单中
     - 如果您引用不存在的形状，您将收到显示可用形状的错误
     - 如果您引用不存在的幻灯片，您将收到指示幻灯片不存在的错误
     - 所有验证错误在脚本退出前一次性显示
   - **重要**：replace.py 脚本在内部使用 inventory.py 来识别所有文本形状
   - **自动清除**：除非您为它们提供 "paragraphs"，否则清单中的所有文本形状将被清除
   - 向需要内容的形状添加 "paragraphs" 字段（不是 "replacement_paragraphs"）
   - 替换 JSON 中没有 "paragraphs" 的形状将自动清除其文本
   - 为占位符文本生成适当的替换内容
   - 使用形状大小确定适当的内容长度
   - **关键**：包含原始清单中的段落属性 - 不要只提供文本
   - **重要**：当 bullet: true 时，不要在文本中包含项目符号符号（•, -, *）- 它们会自动添加
   - **基本格式规则**：
     - 标题/标题通常应具有 `"bold": true`
     - 列表项应具有 `"bullet": true, "level": 0`（当 bullet 为 true 时，level 是必需的）
     - 保留任何对齐属性（例如，居中文本的 `"alignment": "CENTER"`）
     - 当与默认值不同时包含字体属性（例如，`"font_size": 14.0`, `"font_name": "Lora"`）
     - **且慢颜色应用**：使用且慢颜色值，例如：
       - 标题：`"color": "333333"`（text/neutral）
       - 正文：`"color": "606060"`（text/neutral subtle）
       - 强调：`"color": "1B88EE"`（brand primary）
       - 错误：`"color": "FA440C"`（text/error）
       - 成功：`"color": "07AD8F"`（text/success）
     - 替换脚本期望**正确格式化的段落**，而不仅仅是文本字符串
     - **重叠形状**：优先选择具有更大 default_font_size 或更适当 placeholder_type 的形状
   - 将更新的清单与替换保存到 `replacement-text.json`
   - **警告**：不同的模板布局具有不同的形状数量 - 在创建替换之前始终检查实际清单

   显示正确格式的段落字段示例：
   ```json
   "paragraphs": [
     {
       "text": "新演示文稿标题文本",
       "alignment": "CENTER",
       "bold": true,
       "color": "333333"
     },
     {
       "text": "章节标题",
       "bold": true,
       "color": "333333"
     },
     {
       "text": "第一个项目符号点，无项目符号符号",
       "bullet": true,
       "level": 0,
       "color": "606060"
     },
     {
       "text": "红色文本",
       "color": "FA440C"
     },
     {
       "text": "主题颜色文本",
       "theme_color": "DARK_1"
     },
     {
       "text": "常规段落文本，无特殊格式"
     }
   ]
   ```

   **替换 JSON 中未列出的形状将自动清除**：
   ```json
   {
     "slide-0": {
       "shape-0": {
         "paragraphs": [...] // 此形状获得新文本
       }
       // 清单中的 shape-1 和 shape-2 将自动清除
     }
   }
   ```

   **演示文稿的常见格式模式**：
   - 标题幻灯片：粗体文本，有时居中
   - 幻灯片内的章节标题：粗体文本
   - 项目符号列表：每个项目需要 `"bullet": true, "level": 0`
   - 正文：通常不需要特殊属性
   - 引用：可能具有特殊对齐或字体属性

7. **使用 `replace.py` 脚本应用替换**
   ```bash
   python scripts/replace.py working.pptx replacement-text.json output.pptx
   ```

   脚本将：
   - 首先使用 inventory.py 中的函数提取所有文本形状的清单
   - 验证替换 JSON 中的所有形状是否存在于清单中
   - 清除清单中识别的所有形状的文本
   - 仅将新文本应用到替换 JSON 中定义了 "paragraphs" 的形状
   - 通过应用 JSON 中的段落属性来保留格式
   - 自动处理项目符号、对齐、字体属性和颜色
   - 保存更新的演示文稿

   示例验证错误：
   ```
   错误：替换 JSON 中的无效形状：
     - 在 'slide-0' 上未找到形状 'shape-99'。可用形状：shape-0, shape-1, shape-4
     - 清单中未找到幻灯片 'slide-999'
   ```

   ```
   错误：替换文本使这些形状的溢出更严重：
     - slide-0/shape-2：溢出恶化 1.25"（之前 0.00"，现在 1.25"）
   ```

## 创建缩略图网格

创建 PowerPoint 幻灯片的视觉缩略图网格以进行快速分析和参考：

```bash
python scripts/thumbnail.py template.pptx [output_prefix]
```

**特性**：
- 创建：`thumbnails.jpg`（或 `thumbnails-1.jpg`、`thumbnails-2.jpg` 等，用于大型演示文稿）
- 默认：5 列，每网格最多 30 张幻灯片（5×6）
- 自定义前缀：`python scripts/thumbnail.py template.pptx my-grid`
  - 注意：如果要在特定目录中输出，输出前缀应包含路径（例如，`workspace/my-grid`）
- 调整列：`--cols 4`（范围：3-6，影响每网格的幻灯片数）
- 网格限制：3 列 = 12 张幻灯片/网格，4 列 = 20，5 列 = 30，6 列 = 42
- 幻灯片从 0 开始索引（幻灯片 0、幻灯片 1 等）

**用例**：
- 模板分析：快速了解幻灯片布局和设计模式
- 内容审查：整个演示文稿的视觉概览
- 导航参考：通过视觉外观查找特定幻灯片
- 质量检查：验证所有幻灯片格式正确

**示例**：
```bash
# 基本用法
python scripts/thumbnail.py presentation.pptx

# 组合选项：自定义名称、列
python scripts/thumbnail.py template.pptx analysis --cols 4
```

## 将幻灯片转换为图像

要视觉分析 PowerPoint 幻灯片，使用两步过程将它们转换为图像：

1. **将 PPTX 转换为 PDF**：
   ```bash
   soffice --headless --convert-to pdf template.pptx
   ```

2. **将 PDF 页面转换为 JPEG 图像**：
   ```bash
   pdftoppm -jpeg -r 150 template.pdf slide
   ```
   这将创建 `slide-1.jpg`、`slide-2.jpg` 等文件。

选项：
- `-r 150`：设置分辨率为 150 DPI（调整质量/大小平衡）
- `-jpeg`：输出 JPEG 格式（如果首选，使用 `-png` 获取 PNG）
- `-f N`：要转换的第一页（例如，`-f 2` 从第 2 页开始）
- `-l N`：要转换的最后一页（例如，`-l 5` 在第 5 页停止）
- `slide`：输出文件的前缀

特定范围的示例：
```bash
pdftoppm -jpeg -r 150 -f 2 -l 5 template.pdf slide  # 仅转换第 2-5 页
```

## 代码风格指南
**重要**：为 PPTX 操作生成代码时：
- 编写简洁的代码
- 避免冗长的变量名和冗余操作
- 避免不必要的 print 语句

## 且慢品牌应用检查清单

在创建或编辑且慢品牌演示文稿时，确保：

- [ ] 所有颜色值来自且慢颜色系统
- [ ] 品牌主色 `#1B88EE` 用于主要强调元素
- [ ] 文本颜色遵循层级系统（`#333333` → `#606060` → `#999999`）
- [ ] 图表使用 chart01-chart12 配色系统
- [ ] 标题使用 Poppins/Arial，正文使用 Lora/Georgia
- [ ] 字号符合且慢字号阶梯
- [ ] 背景色使用且慢背景色系统
- [ ] 边框颜色符合且慢边框规范
- [ ] 功能色（error/warning/success）正确应用
- [ ] 视觉验证通过且慢品牌规范检查

## 依赖项

所需依赖项（应该已安装）：

- **markitdown**：`pip install "markitdown[pptx]"`（用于从演示文稿中提取文本）
- **pptxgenjs**：`npm install -g pptxgenjs`（用于通过 html2pptx 创建演示文稿）
- **playwright**：`npm install -g playwright`（用于 html2pptx 中的 HTML 渲染）
- **react-icons**：`npm install -g react-icons react react-dom`（用于图标）
- **sharp**：`npm install -g sharp`（用于 SVG 栅格化和图像处理）
- **LibreOffice**：`sudo apt-get install libreoffice`（用于 PDF 转换）
- **Poppler**：`sudo apt-get install poppler-utils`（用于 pdftoppm 将 PDF 转换为图像）
- **defusedxml**：`pip install defusedxml`（用于安全 XML 解析）
