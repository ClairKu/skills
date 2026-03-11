# 且慢 UI 组件 CSS 参考

## 卡片组件

### 基础卡片

```css
.card {
  background: var(--bg-card-default, #FFFFFF);
  border-radius: var(--radius-small, 8px);
  padding: var(--spacing-card-padding, 12px);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

### 高亮卡片

```css
.card-primary {
  background: var(--bg-card-primary-faded, #F0F6FF);
  border: 1px solid var(--border-neutral-blue, #9CCBF8);
  border-radius: var(--radius-medium, 12px);
  padding: var(--spacing-card-padding, 12px);
}
```

### 警告卡片

```css
.card-warning {
  background: var(--bg-card-warning-faded, #FFFAEF);
  border: 1px solid var(--border-neutral-yellow, #FFDC9E);
  border-radius: var(--radius-medium, 12px);
  padding: var(--spacing-card-padding, 12px);
}
```

### 错误卡片

```css
.card-error {
  background: var(--bg-card-error-faded, #FEEDE9);
  border: 1px solid var(--border-neutral-red, #FAB6A5);
  border-radius: var(--radius-medium, 12px);
  padding: var(--spacing-card-padding, 12px);
}
```

## 摘要卡片

```css
.summary-card {
  background: var(--color-summary-bg, #DBEBFF);
  border: 1px solid var(--color-summary-border, #9CCBF8);
  border-radius: var(--radius-medium, 12px);
  padding: var(--spacing-card-padding, 12px);
}
```

## 按钮组件

### 主要按钮

```css
.btn-primary {
  background: var(--color-brand-primary, #1B88EE);
  color: var(--text-inverse, #FFFFFF);
  border: none;
  border-radius: var(--radius-small, 8px);
  padding: 12px 24px;
  font-family: var(--font-family-body);
  font-size: 16pt;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-primary:hover {
  background: #1580E0;
}

.btn-primary:active {
  background: #0F78D4;
}

.btn-primary:disabled {
  background: var(--text-neutral-subtlest, #CCCCCC);
  cursor: not-allowed;
}
```

### 文字按钮

```css
.btn-text {
  background: transparent;
  color: var(--color-brand-primary, #1B88EE);
  border: none;
  padding: 8px 16px;
  font-family: var(--font-family-body);
  font-size: 16pt;
  cursor: pointer;
}

.btn-text:hover {
  color: #1580E0;
  text-decoration: underline;
}

.btn-text:disabled {
  color: var(--text-neutral-subtlest, #CCCCCC);
  cursor: not-allowed;
}
```

## 页头海报

```css
.poster-header {
  background: var(--color-poster-bg, #3180EC);
  color: var(--text-inverse, #FFFFFF);
  display: flex;
  align-items: center;
  aspect-ratio: 4 / 3;
  padding: 32px;
}

.poster-header h1 {
  font-family: var(--font-family-heading);
  font-size: var(--font-title-1, 32pt);
  margin: 0;
}

.poster-header .subtitle {
  font-family: var(--font-family-body);
  font-size: var(--font-body-2, 16pt);
  opacity: 0.9;
}
```

## 页尾

```css
.page-footer {
  background: var(--color-poster-bg, #3180EC);
  color: var(--text-inverse, #FFFFFF);
  text-align: center;
  padding: 24px;
  font-family: var(--font-family-body);
  font-size: var(--font-body-2, 16pt);
}
```

## 链接

```css
a {
  color: var(--color-brand-primary, #1B88EE);
  text-decoration: none;
  transition: color 0.2s;
}

a:hover {
  color: #1580E0;
  text-decoration: underline;
}
```

## 图标尺寸

```css
.icon-sm { font-size: 16px; }
.icon-md { font-size: 20px; }
.icon-lg { font-size: 24px; }
.icon-xl { font-size: 32px; }
```
