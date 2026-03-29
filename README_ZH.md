# 毛主席思想AI助手

基于毛泽东思想哲学原理的智能助手Skill，帮助用户运用科学方法论解决实际问题。

## 🎯 项目简介

本项目是一个基于WorkBuddy平台的AI助手Skill，深度融合了毛泽东思想的20个核心原则，构建了完整的组织韧性评估框架和决策支持系统。

## 🌟 核心特色

### 🔬 完整的毛泽东思想体系
- **20个核心原则**：覆盖毛主席思想的完整理论体系
- **多维度应用**：组织韧性、权力结构、决策过程三大领域
- **实战导向**：军事战略、统一战线等实战原则集成

### 📊 量化评估系统
- **0-100分制**：标准化评分体系
- **多级评估**：优秀、良好、一般、需要改进
- **改进建议**：针对性改进措施

### 🛠️ 三大核心功能模块

#### 1. 组织韧性评估框架
- **统一战线的组织能力**：团结一切可以团结的力量
- **军事战略的抗压能力**：保存自己，消灭敌人的策略
- **群众基础的稳固程度**：一切为了群众，一切依靠群众

#### 2. 权力结构动态演化模型
- **权力结构分析**：4种权力类型识别和分析
- **权力演化预测**：趋势分析和场景预测
- **民主集中制应用**：权力平衡和制度建设

#### 3. 决策过程还原分析引擎
- **决策过程还原分析**：6步标准决策流程
- **决策质量评估**：5大质量维度量化评估
- **毛泽东思想原则应用评估**：5大原则应用水平分析

## 📁 项目结构

```
Claw/
├── SKILL.md              # Skill定义文件
├── scripts/              # 核心功能脚本
│   ├── organizational_resilience.py    # 组织韧性评估引擎
│   ├── power_structure.py              # 权力结构分析模块
│   ├── decision_analysis.py            # 决策过程分析引擎
│   └── integrated_mao_analysis.py      # 综合集成引擎
├── references/           # 参考文档
├── examples/            # 使用示例
├── README.md            # 英文说明文档
├── README_ZH.md         # 中文说明文档
├── requirements.txt     # Python依赖
└── LICENSE              # 开源许可证
```

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 测试功能
```bash
# 测试组织韧性评估
python scripts/organizational_resilience.py

# 测试权力结构分析
python scripts/power_structure.py

# 测试决策过程分析
python scripts/decision_analysis.py

# 测试综合集成引擎
python scripts/integrated_mao_analysis.py
```

## 📋 使用示例

### 基本使用
```python
from scripts.integrated_mao_analysis import IntegratedMaoAnalysisEngine

# 创建分析引擎
engine = IntegratedMaoAnalysisEngine()

# 组织数据示例
organization_data = {
    "组织名称": "示例组织",
    "成员数量": 50,
    "成立时间": "2020年",
    "主要业务": "软件开发",
    "面临挑战": ["市场竞争激烈", "技术更新快", "人才流失"]
}

# 进行综合分析
result = engine.comprehensive_analysis(organization_data)

# 输出结果
print(result["综合评估报告"])
print(result["综合改进方案"])
```

### 输出示例
```
综合得分: 46.83分（需要改进）

各维度表现：
- 组织韧性: 52.13分
- 权力结构: 80.0分（优秀）
- 决策过程: 6.6分（需要重点改进）

改进方案类型：基础建设型
```

## 🔧 技术架构

### 模块化设计
```
IntegratedMaoAnalysisEngine
├── OrganizationalResilienceEngine (组织韧性)
├── PowerStructureAnalyzer (权力结构)  
└── DecisionProcessAnalyzer (决策过程)
```

### 可扩展性
- 每个模块独立开发测试
- 标准接口设计，易于扩展新功能
- 支持自定义评估指标

## 📈 应用场景

### 企业组织诊断
- 评估组织抗压能力
- 分析权力结构稳定性
- 优化决策流程

### 团队建设
- 提升团队韧性
- 建立民主集中制
- 培养群众路线思维

### 个人成长
- 学习矛盾分析方法
- 掌握实践检验方法
- 培养独立自主精神

## 🤝 贡献指南

我们欢迎各种形式的贡献！请参考以下步骤：

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

感谢毛泽东同志的伟大思想，为本项目提供了坚实的理论基础和实践指导。

---

*"实事求是，群众路线，独立自主，自力更生" - 毛泽东思想活的灵魂*