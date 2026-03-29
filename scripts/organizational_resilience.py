#!/usr/bin/env python3
"""
组织韧性评估引擎 - 核心升级成果
基于毛主席思想20个核心原则的组织韧性评估框架
"""

import json
from typing import Dict, List, Any, Tuple
from datetime import datetime

class OrganizationalResilienceEngine:
    """组织韧性评估引擎"""
    
    def __init__(self):
        # 20个核心毛泽东思想原则
        self.core_principles = {
            "实事求是": {
                "权重": 0.15,
                "指标": ["事实依据充分性", "理论联系实际程度", "实践检验能力"]
            },
            "群众路线": {
                "权重": 0.15,
                "指标": ["群众基础稳固度", "群众参与程度", "群众满意度"]
            },
            "独立自主": {
                "权重": 0.08,
                "指标": ["自主决策能力", "外部依赖程度", "创新自主性"]
            },
            "矛盾论": {
                "权重": 0.12,
                "指标": ["矛盾识别能力", "主要矛盾把握", "矛盾转化能力"]
            },
            "实践论": {
                "权重": 0.10,
                "指标": ["实践检验意识", "经验总结能力", "认识提升速度"]
            },
            "统一战线": {
                "权重": 0.08,
                "指标": ["团结范围广度", "合作深度", "利益协调能力"]
            },
            "军事战略原则": {
                "权重": 0.12,
                "指标": ["战略主动性", "战术灵活性", "资源集中能力"]
            },
            "组织建设原则": {
                "权重": 0.10,
                "指标": ["民主集中制", "批评与自我批评", "密切联系群众"]
            },
            "调查研究": {
                "权重": 0.05,
                "指标": ["调研深度", "数据准确性", "分析全面性"]
            },
            "群众工作方法": {
                "权重": 0.05,
                "指标": ["方法多样性", "适用性", "效果持续性"]
            }
        }
        
        # 组织韧性评估维度
        self.resilience_dimensions = {
            "抗压能力": "面对困难和挑战时的承受能力",
            "适应能力": "适应环境变化的能力",
            "恢复能力": "从挫折中恢复的速度和质量",
            "创新能力": "在困难中创新发展的能力",
            "可持续发展能力": "长期稳定发展的能力"
        }
        
        # 军事战略原则映射
        self.strategy_mapping = {
            "你打你的，我打我的": "保持战略主动，差异化竞争",
            "集中优势兵力，各个歼灭敌人": "聚焦关键，逐个突破",
            "不打无准备之仗": "充分准备，稳扎稳打",
            "保存自己，消灭敌人": "风险控制，效益最大化"
        }
    
    def comprehensive_assessment(self, organization_data: Dict[str, Any]) -> Dict[str, Any]:
        """综合性组织韧性评估"""
        
        # 原则应用评估
        principle_scores = self._assess_principle_application(organization_data)
        
        # 韧性维度评估
        dimension_scores = self._assess_resilience_dimensions(organization_data)
        
        # 军事战略能力评估
        strategy_capability = self._assess_strategy_capability(organization_data)
        
        # 计算总体韧性得分
        overall_score = self._calculate_overall_score(principle_scores, dimension_scores, strategy_capability)
        
        # 生成改进建议
        improvement_plan = self._generate_improvement_plan(principle_scores, dimension_scores, strategy_capability)
        
        return {
            "评估时间": datetime.now().isoformat(),
            "组织基本信息": organization_data.get("basic_info", {}),
            "总体韧性得分": overall_score,
            "韧性等级": self._determine_resilience_level(overall_score),
            "原则应用评估": principle_scores,
            "韧性维度评估": dimension_scores,
            "军事战略能力": strategy_capability,
            "改进提升计划": improvement_plan,
            "战略发展建议": self._generate_strategic_recommendations(overall_score)
        }
    
    def _assess_principle_application(self, data: Dict) -> Dict[str, Any]:
        """评估原则应用情况"""
        
        scores = {}
        total_weighted_score = 0
        
        for principle, config in self.core_principles.items():
            # 模拟评估每个原则的应用程度
            application_score = self._evaluate_single_principle(principle, data)
            weighted_score = application_score * config["权重"]
            
            scores[principle] = {
                "得分": application_score,
                "权重": config["权重"],
                "加权得分": weighted_score,
                "评估指标": config["指标"],
                "应用程度": "优秀" if application_score >= 9 else "良好" if application_score >= 7 else "一般" if application_score >= 5 else "需要改进"
            }
            
            total_weighted_score += weighted_score
        
        return {
            "各原则得分": scores,
            "加权总分": total_weighted_score,
            "原则应用水平": "优秀" if total_weighted_score >= 0.8 else "良好" if total_weighted_score >= 0.6 else "一般" if total_weighted_score >= 0.4 else "需要改进"
        }
    
    def _evaluate_single_principle(self, principle: str, data: Dict) -> float:
        """评估单个原则的应用程度"""
        
        # 根据原则特点进行模拟评估
        evaluation_methods = {
            "实事求是": lambda d: self._evaluate_factual_basis(d),
            "群众路线": lambda d: self._evaluate_mass_line(d),
            "矛盾论": lambda d: self._evaluate_contradiction_analysis(d),
            "军事战略原则": lambda d: self._evaluate_military_strategy(d)
        }
        
        if principle in evaluation_methods:
            return evaluation_methods[principle](data)
        else:
            # 默认评估方法
            return min(10, max(1, len(data.get("evidence", [])) * 2))
    
    def _evaluate_factual_basis(self, data: Dict) -> float:
        """评估实事求是原则应用"""
        score = 5.0
        
        # 事实依据
        if data.get("has_factual_basis", False):
            score += 2
        
        # 理论联系实际
        if data.get("theory_practice_connection", False):
            score += 1.5
        
        # 实践检验
        if data.get("practice_validation", False):
            score += 1.5
        
        return min(10, score)
    
    def _evaluate_mass_line(self, data: Dict) -> float:
        """评估群众路线原则应用"""
        score = 5.0
        
        # 群众参与度
        participation = data.get("mass_participation", 0)
        score += participation * 0.5
        
        # 群众满意度
        satisfaction = data.get("mass_satisfaction", 0)
        score += satisfaction * 0.3
        
        # 群众智慧利用
        if data.get("utilizes_mass_wisdom", False):
            score += 2
        
        return min(10, score)
    
    def _evaluate_contradiction_analysis(self, data: Dict) -> float:
        """评估矛盾论应用"""
        score = 5.0
        
        # 矛盾识别能力
        contradictions_identified = len(data.get("contradictions", []))
        score += min(2, contradictions_identified * 0.5)
        
        # 主要矛盾把握
        if data.get("main_contradiction_identified", False):
            score += 2
        
        # 矛盾转化案例
        transformations = len(data.get("contradiction_transformations", []))
        score += min(1, transformations * 0.2)
        
        return min(10, score)
    
    def _evaluate_military_strategy(self, data: Dict) -> float:
        """评估军事战略原则应用"""
        score = 5.0
        
        # 战略主动性
        if data.get("strategic_initiative", False):
            score += 2
        
        # 资源集中能力
        resource_concentration = data.get("resource_concentration", 0)
        score += resource_concentration * 0.3
        
        # 准备充分性
        if data.get("adequate_preparation", False):
            score += 1.5
        
        # 风险控制
        if data.get("effective_risk_control", False):
            score += 1.5
        
        return min(10, score)
    
    def _assess_resilience_dimensions(self, data: Dict) -> Dict[str, Any]:
        """评估韧性维度"""
        
        dimension_scores = {}
        total_dimension_score = 0
        
        for dimension, description in self.resilience_dimensions.items():
            # 模拟每个维度的得分
            dimension_score = self._evaluate_single_dimension(dimension, data)
            dimension_scores[dimension] = {
                "得分": dimension_score,
                "说明": description,
                "等级": "高" if dimension_score >= 8 else "中" if dimension_score >= 5 else "低"
            }
            total_dimension_score += dimension_score
        
        avg_dimension_score = total_dimension_score / len(self.resilience_dimensions)
        
        return {
            "各维度得分": dimension_scores,
            "平均维度得分": avg_dimension_score,
            "维度均衡性": "均衡" if max(dimension_scores.values(), key=lambda x: x["得分"])["得分"] - min(dimension_scores.values(), key=lambda x: x["得分"])["得分"] <= 3 else "需要优化"
        }
    
    def _evaluate_single_dimension(self, dimension: str, data: Dict) -> float:
        """评估单个韧性维度"""
        
        evaluation_map = {
            "抗压能力": lambda d: d.get("pressure_resistance", 5) + (2 if d.get("crisis_handling", False) else 0),
            "适应能力": lambda d: d.get("adaptability", 5) + (1.5 if d.get("change_response", False) else 0),
            "恢复能力": lambda d: d.get("recovery_speed", 5) + (1 if d.get("learning_from_failure", False) else 0),
            "创新能力": lambda d: d.get("innovation_capability", 5) + (2 if d.get("breakthrough_achievements", False) else 0),
            "可持续发展能力": lambda d: d.get("sustainability", 5) + (1.5 if d.get("long_term_planning", False) else 0)
        }
        
        if dimension in evaluation_map:
            return min(10, evaluation_map[dimension](data))
        else:
            return 5.0
    
    def _assess_strategy_capability(self, data: Dict) -> Dict[str, Any]:
        """评估军事战略能力"""
        
        capability_scores = {}
        total_capability = 0
        
        for strategy, description in self.strategy_mapping.items():
            # 评估每个战略原则的应用能力
            capability_score = self._evaluate_strategy_capability(strategy, data)
            capability_scores[strategy] = {
                "能力得分": capability_score,
                "战略说明": description,
                "应用水平": "熟练" if capability_score >= 8 else "一般" if capability_score >= 5 else "需要提升"
            }
            total_capability += capability_score
        
        avg_capability = total_capability / len(self.strategy_mapping)
        
        return {
            "各战略能力": capability_scores,
            "平均战略能力": avg_capability,
            "战略应用综合评价": "优秀" if avg_capability >= 8 else "良好" if avg_capability >= 6 else "需要加强"
        }
    
    def _evaluate_strategy_capability(self, strategy: str, data: Dict) -> float:
        """评估单个战略能力"""
        
        strategy_evaluation = {
            "你打你的，我打我的": lambda d: d.get("strategic_initiative_score", 5) + (2 if d.get("differentiation_strategy", False) else 0),
            "集中优势兵力，各个歼灭敌人": lambda d: d.get("resource_focus_score", 5) + (1.5 if d.get("priority_management", False) else 0),
            "不打无准备之仗": lambda d: d.get("preparation_score", 5) + (1.5 if d.get("contingency_planning", False) else 0),
            "保存自己，消灭敌人": lambda d: d.get("risk_management_score", 5) + (2 if d.get("sustainable_approach", False) else 0)
        }
        
        if strategy in strategy_evaluation:
            return min(10, strategy_evaluation[strategy](data))
        else:
            return 5.0
    
    def _calculate_overall_score(self, principle_scores: Dict, dimension_scores: Dict, strategy_capability: Dict) -> float:
        """计算总体韧性得分"""
        
        # 原则应用权重 40%
        principle_weight = 0.4
        principle_score = principle_scores["加权总分"] * 10  # 转换为10分制
        
        # 韧性维度权重 35%
        dimension_weight = 0.35
        dimension_score = dimension_scores["平均维度得分"]
        
        # 战略能力权重 25%
        strategy_weight = 0.25
        strategy_score = strategy_capability["平均战略能力"]
        
        overall_score = (principle_score * principle_weight + 
                        dimension_score * dimension_weight + 
                        strategy_score * strategy_weight)
        
        return round(overall_score, 2)
    
    def _determine_resilience_level(self, score: float) -> str:
        """确定韧性等级"""
        
        if score >= 9.0:
            return "卓越韧性"
        elif score >= 8.0:
            return "优秀韧性"
        elif score >= 7.0:
            return "良好韧性"
        elif score >= 6.0:
            return "一般韧性"
        elif score >= 5.0:
            return "需要提升"
        else:
            return "需要重大改进"
    
    def _generate_improvement_plan(self, principle_scores: Dict, dimension_scores: Dict, strategy_capability: Dict) -> Dict[str, Any]:
        """生成改进提升计划"""
        
        improvements = {
            "原则应用改进": [],
            "韧性维度提升": [],
            "战略能力加强": []
        }
        
        # 原则应用改进建议
        for principle, score_info in principle_scores["各原则得分"].items():
            if score_info["得分"] < 7:
                improvements["原则应用改进"].append(
                    f"加强{principle}应用，目标得分达到8分以上"
                )
        
        # 韧性维度提升建议
        for dimension, score_info in dimension_scores["各维度得分"].items():
            if score_info["得分"] < 6:
                improvements["韧性维度提升"].append(
                    f"提升{dimension}，当前得分{score_info['得分']}分"
                )
        
        # 战略能力加强建议
        for strategy, capability_info in strategy_capability["各战略能力"].items():
            if capability_info["能力得分"] < 6:
                improvements["战略能力加强"].append(
                    f"加强{strategy}应用能力"
                )
        
        return improvements
    
    def _generate_strategic_recommendations(self, overall_score: float) -> List[str]:
        """生成战略发展建议"""
        
        if overall_score >= 8.0:
            return [
                "继续保持高水平组织韧性",
                "深化毛主席思想原则应用",
                "引领行业创新发展方向",
                "打造卓越组织文化"
            ]
        elif overall_score >= 7.0:
            return [
                "巩固现有韧性成果",
                "加强薄弱环节建设",
                "提升战略规划能力",
                "优化资源配置效率"
            ]
        elif overall_score >= 6.0:
            return [
                "重点提升原则应用能力",
                "加强军事战略原则学习",
                "完善组织建设机制",
                "提高危机应对能力"
            ]
        else:
            return [
                "系统性学习毛主席思想",
                "建立基础韧性评估体系",
                "加强团队建设和管理",
                "制定分阶段提升计划"
            ]

def main():
    """测试函数"""
    engine = OrganizationalResilienceEngine()
    
    # 测试数据
    test_data = {
        "basic_info": {
            "组织名称": "测试组织",
            "规模": "中型",
            "行业": "科技"
        },
        "has_factual_basis": True,
        "theory_practice_connection": True,
        "practice_validation": True,
        "mass_participation": 0.7,
        "mass_satisfaction": 0.8,
        "utilizes_mass_wisdom": True,
        "contradictions": ["资源分配", "时间管理", "团队协作"],
        "main_contradiction_identified": True,
        "contradiction_transformations": ["资源优化"],
        "strategic_initiative": True,
        "resource_concentration": 0.6,
        "adequate_preparation": True,
        "effective_risk_control": True,
        "pressure_resistance": 7,
        "crisis_handling": True,
        "adaptability": 6,
        "change_response": True,
        "recovery_speed": 7,
        "learning_from_failure": True,
        "innovation_capability": 8,
        "breakthrough_achievements": True,
        "sustainability": 7,
        "long_term_planning": True,
        "strategic_initiative_score": 8,
        "differentiation_strategy": True,
        "resource_focus_score": 7,
        "priority_management": True,
        "preparation_score": 8,
        "contingency_planning": True,
        "risk_management_score": 7,
        "sustainable_approach": True
    }
    
    result = engine.comprehensive_assessment(test_data)
    print("组织韧性评估结果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()