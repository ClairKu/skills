---
name: qieman-ui-guidelines
description: 且慢（Qieman）官方UI设计规范技能，用于创建符合且慢品牌视觉风格的HTML高保真原型和界面设计。包含完整的颜色系统、排版规范、组件样式、页面框架等UI设计指南。当需要创建且慢品牌相关的网页、报告、仪表板或任何UI界面时使用此技能。
license: Complete terms in LICENSE.txt
---

# 且慢 UI 设计规范

## 概述

此技能提供且慢（Qieman）的完整UI设计规范，用于创建高保真原型和符合品牌标准的界面设计。

**关键词**：且慢UI设计、UI规范、高保真原型、HTML原型、界面设计、品牌设计系统、设计规范、盈米基金、Qieman

**适用场景**：
- 创建家庭财务规划报告等金融类报告页面
- 设计且慢品牌相关的Web界面
- 构建响应式HTML原型
- 实现符合品牌规范的交互组件

## 页面框架规范

### 标准页面结构

页面应包含以下四个主要区域：

#### 1. 页头海报
- **布局**：左右排版，左侧文本，右侧配置插图/图表
- **背景色**：`#3180EC`（页头海报背景）
- **比例**：4:3
- **文字颜色**：反色 `#FFFFFF`
- **标题层级**：
  - 大标题：32pt（Title 1）- "xx的家庭财务规划报告"
  - 小标题：16pt（Body 2）- "报告生成时间：2024年1月15日"
- **右侧元素**：可配置柱状图、插图或其他视觉元素

#### 2. 摘要区域
- **背景色**：`#DBEBFF`（摘要卡片背景）
- **描边**：`1px solid #9CCBF8`（摘要卡片描边）
- **圆角**：中圆角 12px
- **内边距**：12px
- **用途**：展示关键信息摘要

#### 3. 内容区域
- **模块间距**：16px
- **卡片样式**：
  - 背景色：`#FFFFFF`（默认卡片）
  - 圆角：小圆角 8px
  - 内边距：12px
  - 间距：16px（模块间）

#### 4. 页尾
- **背景色**：`#3180EC`
- **文字颜色**：反色 `#FFFFFF`
- **内容**：盈米基金｜Qieman MCP
- **比例**：4:3

## 颜色系统

### 主色

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **brand** | `#1B88EE` | 品牌主色，用于按钮、链接、强调元素 |

### 文本颜色层级

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **text/neutral** | `#333333` | 标题文字、正文文字等较重要文字 |
| **text/neutral subtle** | `#606060` | 正文、少部分描述文字等较为重要的文字 |
| **text/neutral subtler** | `#999999` | Icon、描述、辅助说明文字等次要文字 |
| **text/neutral subtlest** | `#CCCCCC` | 辅助icon、辅助描述文本 |
| **text/inverse** | `#FFFFFF` | 反色文字（用于深色背景） |
| **text/primary** | `#1B88EE` | 成功、链接色 |
| **text/error** | `#FA440C` | 警告、卖出（上涨） |
| **text/warning** | `#EA9500` | 提醒、信息 |
| **text/success** | `#07AD8F` | 买入、下跌 |

### 页面背景色

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **background/page/deep** | `#F9FAFB` | 浅灰色背景适用于页面背景 |

### 卡片背景色

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **background/card/default** | `#FFFFFF` | 白色 |
| **background/card/deep** | `#F9FAFB` | 浅灰 |
| **background/card/deeper** | `#F7F7F7` | 中灰色 |
| **background/card/primary faded** | `#F0F6FF` | 高亮、成功 |
| **background/card/warning faded** | `#FFFAEF` | 提醒 |
| **background/card/error faded** | `#FEEDE9` | 出错、警示 |

### 边框颜色

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **border/neutral faded** | `#D8D8D8` | 灰色 |
| **border/primary** | `#1B88EE` | 强调 |
| **border/neutral blue** | `#9CCBF8` | 蓝色 |
| **border/neutral yellow** | `#FFDC9E` | 黄色 |
| **border/neutral red** | `#FAB6A5` | 红色 |

### 图表数据颜色

用于数据可视化的12色配色系统：

| 颜色编号 | 颜色值 | 示例用途 |
|---------|--------|---------|
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

## 排版系统

### 字号阶梯

#### 标题字号
- **Title 1**：32pt - 页面主标题
- **Title 2**：26pt - 章节标题
- **Title 3**：24pt - 小节标题
- **Title 4**：19pt - 卡片标题
- **Title 5**：18pt - 小标题

#### 正文字号
- **Body 1**：17pt - 重要正文
- **Body 2**：16pt - 标准正文
- **Body 3**：15pt - 次要正文

#### 说明文字字号
- **Caption 1**：14pt - 说明文字
- **Caption 2**：13pt - 次要说明
- **Caption 3**：12pt - 辅助说明
- **Caption 4**：11pt - 最小文字

### 字体规范

- **标题字体**：Poppins（Arial 作为备选）
- **正文字体**：Lora（Georgia 作为备选）
- **字体回退**：确保在字体不可用时自动回退到系统字体

## 间距与布局系统

### 卡片圆角

- **小圆角**：8px - 标准卡片、按钮
- **中圆角**：12px - 摘要卡片、特殊容器
- **大圆角**：24px - 大型容器、特殊设计元素

### 间距规范

- **模块间距**：16px - 模块之间的间距
- **卡片内边距**：12px - 卡片内部元素与边缘的距离

### 比例规范

- **页头/页尾比例**：4:3

## 交互元素样式

### 按钮

#### 主要按钮
- **背景色**：`#1B88EE`
- **文字颜色**：`#FFFFFF`
- **圆角**：8px
- **状态**：
  - 默认：`#1B88EE`
  - 悬浮：加深10-15%
  - 按下：加深20%

#### 文字按钮
- **文字颜色**：`#1B88EE`
- **背景**：透明
- **悬浮状态**：添加背景 `rgba(27, 136, 238, 0.1)`

#### 禁用状态
- **背景色/文字色**：`#CCCCCC`
- **光标**：`not-allowed`

### 链接文本

- **颜色**：`#1B88EE`
- **悬浮状态**：加深颜色，添加下划线
- **访问后**：保持品牌色

## 图标与图表系统

### 图标库

使用 **RemixIcon** 图标库

**CDN引入**：
```html
<link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
```

**使用示例**：
```html
<i class="ri-chart-line"></i>
```

### 数据图表

使用 **Apache ECharts** 进行数据可视化

**CDN引入**：
```html
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
```

**配色方案**：使用上述12色图表配色系统

## CSS变量定义

建议在项目中定义以下CSS变量以统一管理：

```css
:root {
  /* 主色与品牌色 */
  --color-brand-primary: #1B88EE;
  --color-poster-bg: #3180EC;
  --color-summary-bg: #DBEBFF;
  --color-summary-border: #9CCBF8;
  
  /* 文本颜色层级 */
  --text-neutral: #333333;
  --text-neutral-subtle: #606060;
  --text-neutral-subtler: #999999;
  --text-neutral-subtlest: #CCCCCC;
  --text-inverse: #FFFFFF;
  --text-primary: #1B88EE;
  --text-error: #FA440C;
  --text-warning: #EA9500;
  --text-success: #07AD8F;
  
  /* 背景颜色 */
  --bg-page-deep: #F9FAFB;
  --bg-card-default: #FFFFFF;
  --bg-card-deep: #F9FAFB;
  --bg-card-deeper: #F7F7F7;
  --bg-card-primary-faded: #F0F6FF;
  --bg-card-warning-faded: #FFFAEF;
  --bg-card-error-faded: #FEEDE9;
  
  /* 边框颜色 */
  --border-neutral-faded: #D8D8D8;
  --border-primary: #1B88EE;
  --border-neutral-blue: #9CCBF8;
  --border-neutral-yellow: #FFDC9E;
  --border-neutral-red: #FAB6A5;
  
  /* 字号 */
  --font-title-1: 32pt;
  --font-title-2: 26pt;
  --font-title-3: 24pt;
  --font-title-4: 19pt;
  --font-title-5: 18pt;
  --font-body-1: 17pt;
  --font-body-2: 16pt;
  --font-body-3: 15pt;
  --font-caption-1: 14pt;
  --font-caption-2: 13pt;
  --font-caption-3: 12pt;
  --font-caption-4: 11pt;
  
  /* 圆角 */
  --radius-small: 8px;
  --radius-medium: 12px;
  --radius-large: 24px;
  
  /* 间距 */
  --spacing-module: 16px;
  --spacing-card-padding: 12px;
}
```

## 实现指南

### 创建HTML高保真原型步骤

1. **页面框架搭建**
   - 使用Flex或Grid布局实现4:3比例的页头和页尾
   - 确保响应式适配

2. **样式系统应用**
   - 引入CSS变量定义
   - 应用颜色系统
   - 应用排版系统

3. **组件实现**
   - 按照规范实现按钮、卡片等组件
   - 引入RemixIcon图标库
   - 集成ECharts图表库

4. **视觉层次**
   - 使用字号系统建立清晰的视觉层次
   - 通过颜色深浅区分信息重要性
   - 利用间距系统创建呼吸感

### 设计重点

1. **视觉层次**：标题32pt > 正文16pt，通过字号建立清晰层次
2. **颜色层级**：重要文字 `#333333` > 描述文字 `#606060` > 辅助文字 `#999999`
3. **卡片层级**：通过背景色（`#DBEBFF`、`#F9FAFB`）创建层级区分
4. **圆角统一**：使用8/12/24px圆角体系统一UI元素
5. **色盲友好**：图表配色确保色盲用户可识别（如 `#69B1F4` + `#FBCA74` 组合）

### 响应式设计

- 确保在不同屏幕尺寸下正常显示
- 移动端适配时保持视觉一致性
- 使用相对单位（rem/em）而非固定px

## 使用示例

### 创建家庭财务规划报告页面

当需要创建家庭财务规划报告等高保真原型时：

1. **页头海报**：
   - 背景色：`#3180EC`
   - 大标题：32pt，白色文字
   - 小标题：16pt，白色文字
   - 右侧配置ECharts柱状图

2. **摘要卡片**：
   - 背景色：`#DBEBFF`
   - 边框：`1px solid #9CCBF8`
   - 圆角：12px
   - 内边距：12px

3. **内容区域**：
   - 使用白色卡片（`#FFFFFF`）
   - 圆角：8px
   - 模块间距：16px

4. **页尾**：
   - 背景色：`#3180EC`
   - 文字：白色，显示"盈米基金｜Qieman MCP"

### 颜色使用场景

- **主要操作**：使用 `#1B88EE`
- **成功状态**：使用 `#07AD8F`
- **警告信息**：使用 `#EA9500`
- **错误提示**：使用 `#FA440C`
- **重要文字**：使用 `#333333`
- **辅助文字**：使用 `#999999`
