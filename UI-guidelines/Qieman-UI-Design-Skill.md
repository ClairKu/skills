---
name: qieman-ui-design
description: 根据且慢（Qieman）UI设计规范创建高保真UI设计原型，输出符合品牌规范的HTML格式界面。使用此技能当用户需要创建网页组件、页面、仪表板、数据可视化界面、财务报告、交互式原型或任何需要符合且慢品牌设计规范的高保真UI设计时。生成包含完整样式系统、交互元素、图表集成和响应式布局的生产级代码。
license: Complete terms in LICENSE.txt
---

# 且慢 UI 设计规范

## 概述

本技能提供且慢（Qieman）品牌的完整UI设计系统，用于创建高保真度的HTML原型界面。适用于财务报告、数据可视化仪表板、产品展示页面等场景。

**关键词**：UI设计、高保真原型、HTML界面、且慢设计规范、品牌界面、财务报告、数据可视化、响应式设计、组件库

## 颜色系统

### 主色

- **Brand Primary**: `#1B88EE` - 品牌主色，用于按钮、链接、强调元素

### 文本颜色层级

| 层级 | 颜色值 | 用途 |
|------|--------|------|
| **text/neutral** | `#333333` | 标题文字、正文文字等较重要文字 |
| **text/neutral-subtle** | `#606060` | 正文、少部分描述文字等较为重要的文字 |
| **text/neutral-subtler** | `#999999` | Icon、描述、辅助说明文字等次要文字 |
| **text/neutral-subtlest** | `#CCCCCC` | 辅助icon、辅助描述文本 |
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
| **background/card/primary-faded** | `#F0F6FF` | 高亮、成功卡片背景 |
| **background/card/warning-faded** | `#FFFAEF` | 提醒卡片背景 |
| **background/card/error-faded** | `#FEEDE9` | 出错、警示卡片背景 |

### 边框颜色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **border/neutral-faded** | `#D8D8D8` | 灰色边框（默认） |
| **border/primary** | `#1B88EE` | 强调边框 |
| **border/neutral-blue** | `#9CCBF8` | 蓝色边框 |
| **border/neutral-yellow** | `#FFDC9E` | 黄色边框 |
| **border/neutral-red** | `#FAB6A5` | 红色边框 |

### 图表数据颜色

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

### 特殊用途颜色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **poster-bg** | `#3180EC` | 页头海报背景色 |
| **summary-bg** | `#DBEBFF` | 摘要卡片背景色 |
| **summary-border** | `#9CCBF8` | 摘要卡片边框色 |

## 版式系统

### 字号阶梯

#### 标题字号

| 级别 | 字号 | 用途 |
|------|------|------|
| **Title 1** | `32pt` | 主标题、大标题 |
| **Title 2** | `26pt` | 二级标题 |
| **Title 3** | `24pt` | 三级标题 |
| **Title 4** | `19pt` | 四级标题 |
| **Title 5** | `18pt` | 五级标题 |

#### 正文字号

| 级别 | 字号 | 用途 |
|------|------|------|
| **Body 1** | `17pt` | 主要正文 |
| **Body 2** | `16pt` | 标准正文 |
| **Body 3** | `15pt` | 次要正文 |

#### 说明文字字号

| 级别 | 字号 | 用途 |
|------|------|------|
| **Caption 1** | `14pt` | 说明文字 |
| **Caption 2** | `13pt` | 次要说明 |
| **Caption 3** | `12pt` | 辅助说明 |
| **Caption 4** | `11pt` | 最小说明文字 |

### 字体系列

- **标题字体**: Poppins, Arial, sans-serif
- **正文字体**: Lora, Georgia, serif
- **等宽字体**: 'Courier New', monospace（用于代码、数据展示）

### 间距系统

| 类型 | 间距值 | 用途 |
|------|--------|------|
| **模块间距** | `16px` | 内容模块之间的间距 |
| **卡片内边距** | `12px` | 卡片内部内容与边框的距离 |

### 圆角体系

| 类型 | 圆角值 | 用途 |
|------|--------|------|
| **小圆角** | `8px` | 小按钮、小卡片、输入框 |
| **中圆角** | `12px` | 标准卡片、中等尺寸组件 |
| **大圆角** | `24px` | 大型卡片、特殊形状 |

## 交互元素样式

### 按钮

#### 主要按钮
- **背景色**: `#1B88EE`
- **文字颜色**: `#FFFFFF`
- **圆角**: `8px`
- **内边距**: `12px 24px`
- **字体**: Body 2 (16pt)
- **状态**:
  - 默认：背景 `#1B88EE`
  - 悬浮：背景 `#1580E0`（略深）
  - 激活：背景 `#0F78D4`
  - 禁用：背景 `#CCCCCC`，文字 `#FFFFFF`

#### 文字按钮
- **背景色**: 透明
- **文字颜色**: `#1B88EE`
- **字体**: Body 2 (16pt)
- **状态**:
  - 默认：文字 `#1B88EE`
  - 悬浮：文字 `#1580E0`，下划线
  - 激活：文字 `#0F78D4`
  - 禁用：文字 `#CCCCCC`

### 链接文本

- **颜色**: `#1B88EE`
- **默认状态**: 正常显示
- **悬浮状态**: 颜色加深至 `#1580E0`，添加下划线
- **访问过状态**: 保持 `#1B88EE` 或使用 `#1580E0`

## 页面框架规范

### 页头海报

- **布局**: 左右排版（Flex布局，4:3比例）
- **左侧元素**:
  - 大标题：32pt (Title 1)，反色文字 `#FFFFFF`
  - 小标题：16pt (Body 2)，反色文字 `#FFFFFF`
- **右侧元素**: 柱状插图或装饰图形
- **背景色**: `#3180EC`
- **比例**: 4:3（使用 aspect-ratio: 4/3）
- **文字颜色**: `#FFFFFF` (inverse)

### 摘要区域

- **背景色**: `#DBEBFF`
- **描边**: `1px solid #9CCBF8`
- **圆角**: `12px` (中圆角)
- **内边距**: `12px`
- **模块间距**: `16px`

### 内容区

- **模块间距**: `16px`
- **卡片样式**:
  - 背景色: `#FFFFFF`
  - 圆角: `8px` (小圆角)
  - 内边距: `12px`
  - 可选边框: `1px solid #D8D8D8`

### 页尾

- **背景色**: `#3180EC`
- **内容**: "盈米基金｜Qieman MCP" 或类似品牌信息
- **比例**: 4:3
- **文字颜色**: `#FFFFFF` (inverse)
- **字体**: Body 2 (16pt)

## 组件规范

### 卡片组件

**基础卡片**
```css
.card {
  background: #FFFFFF;
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

**高亮卡片**
```css
.card-primary {
  background: #F0F6FF;
  border: 1px solid #9CCBF8;
  border-radius: 12px;
  padding: 12px;
}
```

**警告卡片**
```css
.card-warning {
  background: #FFFAEF;
  border: 1px solid #FFDC9E;
  border-radius: 12px;
  padding: 12px;
}
```

**错误卡片**
```css
.card-error {
  background: #FEEDE9;
  border: 1px solid #FAB6A5;
  border-radius: 12px;
  padding: 12px;
}
```

### 图标系统

**使用 RemixIcon 图标库**

```html
<!-- 引入 RemixIcon -->
<link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">

<!-- 使用图标 -->
<i class="ri-home-line"></i>
<i class="ri-chart-line"></i>
<i class="ri-user-line"></i>
```

**图标尺寸规范**:
- 小图标: `16px` × `16px`
- 标准图标: `20px` × `20px`
- 大图标: `24px` × `24px`
- 超大图标: `32px` × `32px`

**图标颜色**:
- 默认: `#333333` (text/neutral)
- 次要: `#999999` (text/neutral-subtler)
- 强调: `#1B88EE` (primary)
- 反色: `#FFFFFF` (inverse)

### 数据图表

**使用 Apache ECharts**

```html
<!-- 引入 ECharts -->
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
```

**图表配色方案**:
按顺序使用 chart01-chart12 颜色值，确保色盲友好的配色组合。

**图表类型支持**:
- 柱状图（Bar Chart）
- 折线图（Line Chart）
- 饼图（Pie Chart）
- 散点图（Scatter Chart）
- 面积图（Area Chart）
- 雷达图（Radar Chart）
- 仪表盘（Gauge Chart）

## CSS 变量定义

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
  
  /* 图表颜色 */
  --chart-01: #69B1F4;
  --chart-02: #F88D72;
  --chart-03: #FBCA74;
  --chart-04: #7DD4C4;
  --chart-05: #68E0F3;
  --chart-06: #ADAFE8;
  --chart-07: #3A7BB8;
  --chart-08: #FAB6A5;
  --chart-09: #EDC273;
  --chart-10: #9CCBF8;
  --chart-11: #C8CAEF;
  --chart-12: #6B9CCA;
  
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
  
  /* 间距 */
  --spacing-module: 16px;
  --spacing-card-padding: 12px;
  
  /* 圆角 */
  --radius-small: 8px;
  --radius-medium: 12px;
  --radius-large: 24px;
  
  /* 字体 */
  --font-family-heading: 'Poppins', 'Arial', sans-serif;
  --font-family-body: 'Lora', 'Georgia', serif;
  --font-family-mono: 'Courier New', monospace;
}
```

## 技术实现要求

### HTML 结构

1. **使用语义化HTML5标签**
2. **响应式布局**: 使用 Flex/Grid 布局
3. **比例控制**: 使用 `aspect-ratio` CSS 属性实现 4:3 比例区块
4. **字体加载**: 使用 Google Fonts 或本地字体文件

### CSS 要求

1. **CSS变量管理**: 所有颜色、字号、间距使用CSS变量
2. **响应式设计**: 使用媒体查询适配不同屏幕尺寸
3. **现代CSS**: 使用 Flexbox/Grid 布局
4. **性能优化**: 避免不必要的重绘和回流

### JavaScript 集成

1. **ECharts 初始化**: 确保DOM加载完成后初始化图表
2. **交互处理**: 实现按钮、链接的交互状态
3. **数据绑定**: 支持动态数据更新

## 设计原则

### 视觉层级

1. **通过字号建立层级**: Title 1 (32pt) > Title 2 (26pt) > Body (16pt)
2. **通过颜色建立层级**: neutral (#333) > subtle (#606060) > subtler (#999999)
3. **通过背景色区分**: 白色卡片 > 浅灰背景 > 深灰背景

### 一致性

1. **颜色使用一致**: 同类型元素使用相同颜色
2. **间距使用一致**: 模块间距统一 16px，卡片内边距统一 12px
3. **圆角使用一致**: 根据组件尺寸选择对应圆角

### 可访问性

1. **颜色对比度**: 确保文本与背景对比度满足 WCAG AA 标准（至少 4.5:1）
2. **色盲友好**: 图表配色考虑色盲用户
3. **语义化标记**: 使用正确的HTML语义标签

## 使用示例

### 创建财务规划报告

当用户需要创建家庭财务规划报告时：

1. **页头海报区域**:
   - 背景色: `#3180EC`
   - 左侧：大标题（32pt）+ 报告生成时间（16pt）
   - 右侧：财务数据可视化图表
   - 文字颜色: `#FFFFFF`

2. **摘要区域**:
   - 背景色: `#DBEBFF`
   - 边框: `1px solid #9CCBF8`
   - 圆角: `12px`
   - 内边距: `12px`

3. **内容卡片**:
   - 背景色: `#FFFFFF`
   - 圆角: `8px`
   - 内边距: `12px`
   - 模块间距: `16px`

4. **数据图表**:
   - 使用 ECharts 实现
   - 使用 chart01-chart12 配色方案
   - 确保响应式适配

5. **页尾**:
   - 背景色: `#3180EC`
   - 文字: "盈米基金｜Qieman MCP"
   - 文字颜色: `#FFFFFF`

## 输出要求

### 交付物

1. **完整的HTML文件**: 包含所有样式和脚本的单文件
2. **响应式设计**: 适配桌面端和移动端
3. **交互功能**: 按钮、链接等交互元素正常工作
4. **数据可视化**: ECharts 图表正确渲染

### 代码质量

1. **代码注释**: 关键部分添加注释说明
2. **结构清晰**: HTML结构语义化，CSS组织有序
3. **可维护性**: 使用CSS变量，便于后续修改

## 注意事项

1. **字体加载**: 确保 Poppins 和 Lora 字体正确加载
2. **图表响应式**: ECharts 图表需要监听窗口大小变化
3. **浏览器兼容**: 确保现代浏览器正常显示
4. **性能优化**: 避免过多动画影响性能

## 快速参考

### 常用颜色

- 主色: `#1B88EE`
- 重要文字: `#333333`
- 普通文字: `#606060`
- 次要文字: `#999999`
- 反色文字: `#FFFFFF`
- 页面背景: `#F9FAFB`
- 卡片背景: `#FFFFFF`
- 摘要背景: `#DBEBFF`

### 常用字号

- 主标题: `32pt`
- 副标题: `26pt`
- 标准正文: `16pt`
- 说明文字: `14pt`

### 常用间距

- 模块间距: `16px`
- 卡片内边距: `12px`

### 常用圆角

- 小圆角: `8px`
- 中圆角: `12px`
- 大圆角: `24px`
