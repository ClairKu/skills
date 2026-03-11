# 且慢 CSS 变量定义

在项目中引入以下 CSS 变量以统一管理设计系统：

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
