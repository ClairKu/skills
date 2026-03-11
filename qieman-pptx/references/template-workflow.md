# 模板工作流详细参考

## 模板清单格式

在 `template-inventory.md` 中记录：

```markdown
# 模板清单分析
**总幻灯片数：[数量]**
**重要：幻灯片从 0 开始索引（第一张 = 0，最后一张 = count-1）**

## [类别名称]
- 幻灯片 0：[布局代码] - 描述/用途
- 幻灯片 1：[布局代码] - 描述/用途
[... 每张幻灯片单独列出 ...]
```

## 模板映射示例

```python
template_mapping = [
    0,   # 幻灯片 0（标题/封面）
    34,  # 幻灯片 34（B1：标题和正文）
    34,  # 再次使用幻灯片 34
    50,  # 幻灯片 50（E1：引用）
    54,  # 幻灯片 54（F2：结束 + 文本）
]
```

**布局匹配原则**：
- 单列：统一叙述或单一主题
- 两列：恰好 2 个不同项目
- 三列：恰好 3 个不同项目
- 图像+文本：有实际图像时才使用
- 引用布局：仅用于带归属的人员引用
- 永远不要使用占位符多于内容数量的布局

## inventory.py 输出的 JSON 结构

```json
{
  "slide-0": {
    "shape-0": {
      "placeholder_type": "TITLE",
      "left": 1.5,
      "top": 2.0,
      "width": 7.5,
      "height": 1.2,
      "paragraphs": [
        {
          "text": "段落文本",
          "bullet": true,
          "level": 0,
          "alignment": "CENTER",
          "space_before": 10.0,
          "space_after": 6.0,
          "line_spacing": 22.4,
          "font_name": "Arial",
          "font_size": 14.0,
          "bold": true,
          "italic": false,
          "underline": false,
          "color": "FF0000"
        }
      ]
    }
  }
}
```

**关键特性**：
- 幻灯片命名为 "slide-0"、"slide-1"
- 形状按视觉位置排序为 "shape-0"、"shape-1"
- 占位符类型：TITLE, CENTER_TITLE, SUBTITLE, BODY, OBJECT, 或 null
- SLIDE_NUMBER 占位符自动排除
- 当 `bullet: true` 时 `level` 始终包含
- 仅非默认属性包含在输出中

## 替换文本 JSON 格式

### 段落格式示例

```json
{
  "slide-0": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "演示文稿标题",
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
          "text": "项目符号内容（无需手动添加符号）",
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
          "text": "常规段落文本"
        }
      ]
    }
  }
}
```

### 关键规则

1. **未列出的形状自动清除**：替换 JSON 中没有 `"paragraphs"` 的形状将自动清除文本
2. **不要手动添加项目符号符号**：当 `bullet: true` 时，符号自动添加
3. **保留原始格式属性**：包含清单中的段落属性
4. **验证形状存在性**：replace.py 会验证所有引用的形状
5. **重叠形状**：优先选择 `default_font_size` 更大或 `placeholder_type` 更合适的形状

### 验证错误示例

```
错误：替换 JSON 中的无效形状：
  - 在 'slide-0' 上未找到形状 'shape-99'。可用形状：shape-0, shape-1, shape-4
  - 清单中未找到幻灯片 'slide-999'

错误：替换文本使这些形状的溢出更严重：
  - slide-0/shape-2：溢出恶化 1.25"（之前 0.00"，现在 1.25"）
```

## 常见格式模式

| 幻灯片元素 | 格式要求 |
|-----------|---------|
| 标题幻灯片 | 粗体，有时居中 |
| 章节标题 | 粗体 |
| 项目符号 | `"bullet": true, "level": 0` |
| 正文 | 通常无特殊属性 |
| 引用 | 特殊对齐或字体 |
