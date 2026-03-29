# 基本使用示例

## 矛盾论分析示例

### 问题：团队协作效率低下

```python
from scripts.contradiction_analysis import ContradictionAnalyzer

analyzer = ContradictionAnalyzer()
problem = "团队协作效率低下，成员之间沟通不畅，项目进度缓慢"

result = analyzer.analyze_problem(problem)
print("矛盾分析结果：")
print(json.dumps(result, ensure_ascii=False, indent=2))
```

**预期输出：**
- 识别主要矛盾：沟通不畅
- 次要矛盾：进度缓慢
- 解决建议：改善沟通机制

## 实践论学习示例

### 场景：学习新技术

```python
from scripts.practical_theory import PracticeTheoryAnalyzer

analyzer = PracticeTheoryAnalyzer()
experience = "我刚开始学习人工智能，感觉概念很抽象"
goal = "掌握AI技术并应用于实际项目"

result = analyzer.analyze_learning_process(experience, goal)
print("学习路径规划：")
print(json.dumps(result, ensure_ascii=False, indent=2))
```

**预期输出：**
- 当前阶段：感性认识
- 实践计划：深入观察 → 初步实践
- 检验标准：技能掌握程度

## 群众路线需求收集示例

### 场景：产品改进

```python
from scripts.mass_line import MassLineAnalyzer

analyzer = MassLineAnalyzer()
user_input = "用户反映产品界面不够友好，需要改进"

result = analyzer.collect_user_needs(user_input)
print("群众需求分析：")
print(json.dumps(result, ensure_ascii=False, indent=2))
```

**预期输出：**
- 需求层次：基本需求（界面友好）
- 利益相关方：用户、产品团队
- 参与方案：用户调研、民主讨论