---
name: qieman-ui-guidelines
description: 且慢（Qieman）官方 UI 设计规范技能，用于创建符合且慢品牌视觉风格的 HTML 高保真原型和界面设计。包含完整的颜色系统、排版规范、组件样式、页面框架等 UI 设计指南。当需要创建且慢品牌相关的网页、报告、仪表板或任何 UI 界面时使用此技能。
---

# 且慢 UI 设计规范

## 概述

且慢（Qieman）品牌的完整 UI 设计系统，用于创建高保真 HTML 原型界面。适用于财务报告、数据可视化仪表板、产品展示页面等场景。

**适用场景**：家庭财务规划报告、Web 界面设计、响应式 HTML 原型、品牌交互组件

## 颜色系统

### 主色

- **Brand Primary**: `#1B88EE` — 按钮、链接、强调元素

### 文本颜色层级

| 层级 | 颜色值 | 用途 |
|------|--------|------|
| **text/neutral** | `#333333` | 标题、重要正文 |
| **text/neutral-subtle** | `#606060` | 正文、描述文字 |
| **text/neutral-subtler** | `#999999` | 辅助说明、Icon |
| **text/neutral-subtlest** | `#CCCCCC` | 辅助描述文本 |
| **text/inverse** | `#FFFFFF` | 深色背景上的文字 |

### 功能色

| 功能 | 颜色值 | 用途 |
|------|--------|------|
| **text/primary** | `#1B88EE` | 链接色 |
| **text/error** | `#FA440C` | 警告、卖出（上涨） |
| **text/warning** | `#EA9500` | 提醒、信息 |
| **text/success** | `#07AD8F` | 买入、下跌 |

### 背景色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **page/deep** | `#F9FAFB` | 页面背景 |
| **card/default** | `#FFFFFF` | 白色卡片 |
| **card/deep** | `#F9FAFB` | 浅灰卡片 |
| **card/deeper** | `#F7F7F7` | 中灰卡片 |
| **card/primary-faded** | `#F0F6FF` | 高亮卡片 |
| **card/warning-faded** | `#FFFAEF` | 提醒卡片 |
| **card/error-faded** | `#FEEDE9` | 警示卡片 |

### 特殊用途色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **poster-bg** | `#3180EC` | 页头海报/页尾背景 |
| **summary-bg** | `#DBEBFF` | 摘要卡片背景 |
| **summary-border** | `#9CCBF8` | 摘要卡片边框 |

### 边框颜色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **border/neutral-faded** | `#D8D8D8` | 默认灰色边框 |
| **border/primary** | `#1B88EE` | 强调边框 |
| **border/neutral-blue** | `#9CCBF8` | 蓝色边框 |
| **border/neutral-yellow** | `#FFDC9E` | 黄色边框 |
| **border/neutral-red** | `#FAB6A5` | 红色边框 |

### 图表数据颜色

12 色配色系统，按顺序使用：

| 编号 | 颜色值 | 用途 |
|------|--------|------|
| **chart01** | `#69B1F4` | 柱状图、折线图主色 |
| **chart02** | `#F88D72` | 对比数据 |
| **chart03** | `#FBCA74` | 警告数据 |
| **chart04** | `#7DD4C4` | 成功数据 |
| **chart05** | `#68E0F3` | 辅助系列 |
| **chart06** | `#ADAFE8` | 辅助系列 |
| **chart07** | `#3A7BB8` | 深色系列 |
| **chart08** | `#FAB6A5` | 错误数据 |
| **chart09** | `#EDC273` | 中性系列 |
| **chart10** | `#9CCBF8` | 浅色系列 |
| **chart11** | `#C8CAEF` | 浅色系列 |
| **chart12** | `#6B9CCA` | 中深系列 |

## 排版系统

### 字体

| 用途 | 字体 |
|------|------|
| 标题 | Poppins, Arial, sans-serif |
| 正文 | Lora, Georgia, serif |
| 等宽 | 'Courier New', monospace |

### 字号阶梯

| 级别 | 字号 | 用途 |
|------|------|------|
| **Title 1** | 32pt | 主标题 |
| **Title 2** | 26pt | 二级标题 |
| **Title 3** | 24pt | 三级标题 |
| **Title 4** | 19pt | 四级标题 |
| **Title 5** | 18pt | 五级标题 |
| **Body 1** | 17pt | 重要正文 |
| **Body 2** | 16pt | 标准正文 |
| **Body 3** | 15pt | 次要正文 |
| **Caption 1** | 14pt | 说明文字 |
| **Caption 2** | 13pt | 次要说明 |
| **Caption 3** | 12pt | 辅助说明 |
| **Caption 4** | 11pt | 最小文字 |

### 间距与圆角

| 类型 | 值 | 用途 |
|------|------|------|
| 模块间距 | 16px | 模块之间 |
| 卡片内边距 | 12px | 卡片内部 |
| 小圆角 | 8px | 按钮、小卡片 |
| 中圆角 | 12px | 标准卡片 |
| 大圆角 | 24px | 大型容器 |

## 页面框架规范

### 1. 页头海报

- **布局**：左右排版（Flex，4:3 比例）
- **背景色**：`#3180EC`
- **文字颜色**：`#FFFFFF`
- **左侧**：大标题 32pt + 小标题 16pt
- **右侧**：柱状图或装饰图形

### 2. 摘要区域

- **背景色**：`#DBEBFF`
- **边框**：`1px solid #9CCBF8`
- **圆角**：12px | **内边距**：12px

### 3. 内容区域

- **卡片背景**：`#FFFFFF` | **圆角**：8px
- **内边距**：12px | **模块间距**：16px

### 4. 页尾

- **背景色**：`#3180EC` | **文字**：`#FFFFFF`
- **内容**：盈米基金｜Qieman MCP

## 交互元素样式

### 主要按钮

- **背景**：`#1B88EE` | **文字**：`#FFFFFF` | **圆角**：8px
- 悬浮：`#1580E0` | 激活：`#0F78D4` | 禁用：`#CCCCCC`

### 文字按钮

- **文字**：`#1B88EE` | **背景**：透明
- 悬浮：`#1580E0` + 下划线

### 链接

- **颜色**：`#1B88EE` | 悬浮加深至 `#1580E0` + 下划线

## 图标与图表

### 图标库：RemixIcon

```html
<link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
<i class="ri-chart-line"></i>
```

图标尺寸：16px / 20px / 24px / 32px
图标颜色：`#333333`（默认）/ `#999999`（次要）/ `#1B88EE`（强调）/ `#FFFFFF`（反色）

### 数据图表：Apache ECharts

```html
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
```

使用 chart01-chart12 配色方案，确保色盲友好。

## 设计原则

1. **视觉层级**：Title 1 (32pt) > Title 2 (26pt) > Body (16pt)；颜色 `#333` > `#606060` > `#999`
2. **一致性**：同类元素相同颜色，模块间距统一 16px，卡片内边距统一 12px
3. **可访问性**：文本/背景对比度 ≥ 4.5:1（WCAG AA），图表配色色盲友好

## 实现流程

1. **页面框架**：Flex/Grid 布局实现 4:3 页头页尾
2. **样式系统**：引入 CSS 变量定义（详见 [css-variables.md](references/css-variables.md)）
3. **组件实现**：按规范实现按钮、卡片等（详见 [components.md](references/components.md)）
4. **图表集成**：ECharts 在 DOM 加载后初始化，监听窗口大小变化

## 输出要求

- 完整的单 HTML 文件（含样式和脚本）
- 响应式适配桌面端和移动端
- 交互元素正常工作
- ECharts 图表正确渲染

## 快速参考

| 用途 | 值 |
|------|------|
| 主色 | `#1B88EE` |
| 重要文字 | `#333333` |
| 普通文字 | `#606060` |
| 次要文字 | `#999999` |
| 页面背景 | `#F9FAFB` |
| 摘要背景 | `#DBEBFF` |
| 主标题 | 32pt |
| 标准正文 | 16pt |
| 模块间距 | 16px |
| 小圆角 | 8px |
