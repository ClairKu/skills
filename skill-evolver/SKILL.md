---
name: skill-evolver
description: 技能自进化工厂。具备"自进化"能力的技能生成器，用于自动化生成、验证和部署新的 Agent Skills。当用户说"学会某某能力"、"创建新技能"、"生成一个技能来处理XX"时触发。
---

# 技能进化器 (Skill Evolver)

这是一个元技能（Meta-Skill），赋予 Agent 自我扩展能力。基于"生成-验证-部署"闭环机制，自动化创建高质量的 Agent Skills。

## 设计理念：进化循环

1. **感知 (Perceive)**: 识别当前能力的缺失或接收用户的新技能需求
2. **生成 (Evolve)**: 基于标准规范生成技能代码和文档
3. **验证 (Validate)**: 在沙箱环境中运行测试用例，确保技能可用性
4. **适应 (Adapt)**: 验证失败则利用错误日志进行自我修正；成功则部署技能

## 核心工具

### 1. `scaffold_skill` - 初始化脚手架

创建符合规范的技能目录结构：

```bash
python scripts/evolve_tools.py scaffold <技能名称>
```

生成结构：
```
<技能名称>/
├── SKILL.md          # 技能元数据和说明
├── scripts/          # 脚本目录
├── tests/            # 测试用例
└── references/       # 参考文档
```

### 2. `validate_skill` - 进化验证器

在隔离环境中运行技能的测试用例：

```bash
python scripts/evolve_tools.py validate <技能路径>
```

- **输入**: 技能临时路径
- **输出**: `{"success": bool, "logs": str}`
- **机制**: 如果测试失败，Agent 应读取 `logs` 并修改代码后重试

### 3. `deploy_skill` - 部署上线

将验证通过的技能部署到正式目录：

```bash
python scripts/evolve_tools.py deploy <技能路径> --category <分类>
```

## 使用流程

```python
# 1. 接收任务："学会查询股票价格"

# 2. 创建脚手架
temp_path = scaffold_skill(name="stock-checker")

# 3. 编写代码
# ... 写入 SKILL.md, scripts/query.py, tests/test_query.py ...

# 4. 验证
result = validate_skill(path=temp_path)

if result['success']:
    # 5. 部署
    deploy_skill(source_path=temp_path, category="finance")
else:
    # 6. 自我修正循环
    # 分析 result['logs']，修改代码，重试验证
```

## 技能开发规范

详细的开发规范请参考 [开发规范文档](./references/evolution_architect.md)，包括：

- 目录结构要求
- SKILL.md 规范
- 脚本编写规范
- 测试规范
- 进化策略

## 依赖

- Python 3
- `pytest` (用于运行测试验证)
