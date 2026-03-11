# 且慢完整颜色系统

## 主色与品牌色

| 颜色名称 | 颜色值 | 用途 |
|---------|--------|------|
| **brand** | `#1B88EE` | 品牌主色，用于按钮、链接、强调元素 |
| **poster-bg** | `#3180EC` | 页头海报和页尾的背景色 |
| **summary-bg** | `#DBEBFF` | 摘要区域的背景色 |
| **summary-border** | `#9CCBF8` | 摘要卡片的边框颜色 |

## 文本颜色层级

| 层级 | 颜色值 | 用途 |
|------|--------|------|
| **text/neutral** | `#333333` | 标题文字、正文文字等较重要文字 |
| **text/neutral subtle** | `#606060` | 正文、描述文字等较为重要的文字 |
| **text/neutral subtler** | `#999999` | Icon、描述、辅助说明文字等次要文字 |
| **text/neutral subtlest** | `#CCCCCC` | 辅助icon、辅助描述文本 |
| **text/inverse** | `#FFFFFF` | 反色文字（用于深色背景） |

## 功能色

| 功能 | 颜色值 | 用途 |
|------|--------|------|
| **text/primary** | `#1B88EE` | 成功、链接色 |
| **text/error** | `#FA440C` | 警告、卖出（上涨） |
| **text/warning** | `#EA9500` | 提醒、信息 |
| **text/success** | `#07AD8F` | 买入、下跌 |

## 页面背景色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **background/page/deep** | `#F9FAFB` | 浅灰色页面背景 |

## 卡片背景色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **background/card/default** | `#FFFFFF` | 白色卡片背景 |
| **background/card/deep** | `#F9FAFB` | 浅灰卡片背景 |
| **background/card/deeper** | `#F7F7F7` | 中灰色卡片背景 |
| **background/card/primary faded** | `#F0F6FF` | 高亮、成功卡片背景 |
| **background/card/warning faded** | `#FFFAEF` | 提醒卡片背景 |
| **background/card/error faded** | `#FEEDE9` | 出错、警示卡片背景 |

## 边框颜色

| 名称 | 颜色值 | 用途 |
|------|--------|------|
| **border/neutral faded** | `#D8D8D8` | 灰色边框（默认） |
| **border/primary** | `#1B88EE` | 强调边框 |
| **border/neutral blue** | `#9CCBF8` | 蓝色边框 |
| **border/neutral yellow** | `#FFDC9E` | 黄色边框 |
| **border/neutral red** | `#FAB6A5` | 红色边框 |

## 图表数据颜色

用于数据可视化的 12 色配色系统，按顺序使用：

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

## PPT 中的颜色应用指南

### 调色板选择

| 场景 | 用色方案 |
|------|----------|
| **金融报告** | 主色系 + 功能色（成功/错误用于涨跌） |
| **数据展示** | 图表配色系统，确保色盲友好 |
| **强调内容** | `#1B88EE` 或 `#3180EC` |
| **背景选择** | `#FFFFFF`（主要内容）/ `#F9FAFB`（页面背景） |

### 替换 JSON 中的颜色值

在模板替换工作流中使用且慢颜色（不含 `#` 前缀）：

- 标题：`"color": "333333"`
- 正文：`"color": "606060"`
- 强调：`"color": "1B88EE"`
- 错误：`"color": "FA440C"`
- 成功：`"color": "07AD8F"`
