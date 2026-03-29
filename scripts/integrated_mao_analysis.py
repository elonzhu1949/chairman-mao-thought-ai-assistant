#!/usr/bin/env python3
"""
毛泽东思想综合集成引擎 - 完整升级版
集成组织韧性评估、权力结构分析、决策过程分析三大功能
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime

class IntegratedMaoAnalysisEngine:
    """毛泽东思想综合集成分析引擎"""
    
    def __init__(self):
        # 导入各个模块（使用相对导入）
        import sys
        import os
        sys.path.append(os.path.dirname(__file__))
        
        from organizational_resilience import OrganizationalResilienceEngine
        from power_structure import PowerStructureAnalyzer
        from decision_analysis import DecisionProcessAnalyzer
        
        self.resilience_engine = OrganizationalResilienceEngine()
        self.power_analyzer = PowerStructureAnalyzer()
        self.decision_analyzer = DecisionProcessAnalyzer()
        
        # 综合评估指标
        self.comprehensive_indicators = {
            "组织健康度": "组织整体运行状况和适应能力",
            "领导力水平": "领导能力和决策水平",
            "群众基础": "群众支持和参与程度",
            "制度完善度": "制度建设和执行效果",
            "发展潜力": "未来发展空间和能力"
        }
    
    def comprehensive_analysis(self, organization_data: Dict[str, Any]) -> Dict[str, Any]:
        """综合组织分析"""
        
        # 组织韧性评估
        resilience_result = self.resilience_engine.comprehensive_assessment(organization_data)
        
        # 权力结构分析
        power_structure_result = self.power_analyzer.analyze_power_structure(
            organization_data.get("description", "")
        )
        
        # 决策过程分析
        decision_process_result = self.decision_analyzer.analyze_decision_process(
            organization_data.get("decision_description", ""),
            organization_data.get("context", {})
        )
        
        # 综合评估
        comprehensive_assessment = self._integrate_assessments(
            resilience_result, power_structure_result, decision_process_result
        )
        
        # 生成改进方案
        improvement_plan = self._generate_comprehensive_improvement_plan(comprehensive_assessment)
        
        return {
            "分析时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "组织基本信息": organization_data.get("basic_info", {}),
            "组织韧性评估": resilience_result,
            "权力结构分析": power_structure_result,
            "决策过程分析": decision_process_result,
            "综合评估报告": comprehensive_assessment,
            "综合改进方案": improvement_plan,
            "毛泽东思想应用总结": self._summarize_mao_application(
                resilience_result, power_structure_result, decision_process_result
            )
        }
    
    def _integrate_assessments(self, resilience: Dict, power: Dict, decision: Dict) -> Dict[str, Any]:
        """整合三个维度的评估结果"""
        
        # 计算综合得分
        resilience_score = resilience.get("总体韧性得分", 0)
        power_score = power.get("权力稳固性评估", {}).get("总体稳固性得分", 0)
        decision_score = decision.get("决策质量评估", {}).get("总体质量得分", 0)
        
        # 标准化得分（转换为0-100分）
        normalized_scores = {
            "组织韧性": (resilience_score / 30) * 100,
            "权力结构": (power_score / 30) * 100,
            "决策过程": (decision_score / 10) * 10
        }
        
        # 计算综合得分（加权平均）
        weights = {"组织韧性": 0.4, "权力结构": 0.3, "决策过程": 0.3}
        comprehensive_score = sum(normalized_scores[dim] * weights[dim] for dim in normalized_scores)
        
        # 确定综合等级
        comprehensive_level = self._determine_comprehensive_level(comprehensive_score)
        
        return {
            "各维度得分": normalized_scores,
            "综合得分": round(comprehensive_score, 2),
            "综合等级": comprehensive_level,
            "优势领域": self._identify_strength_areas(normalized_scores),
            "薄弱环节": self._identify_weak_areas(normalized_scores),
            "发展建议": self._generate_development_suggestions(normalized_scores)
        }
    
    def _generate_comprehensive_improvement_plan(self, assessment: Dict) -> Dict[str, Any]:
        """生成综合改进方案"""
        
        comprehensive_level = assessment.get("综合等级", "")
        weak_areas = assessment.get("薄弱环节", [])
        
        if comprehensive_level == "优秀":
            plan_type = "保持优化型"
            focus_areas = ["持续创新", "引领发展", "树立标杆"]
        elif comprehensive_level == "良好":
            plan_type = "提升完善型"
            focus_areas = ["补强短板", "优化结构", "提高效率"]
        else:
            plan_type = "基础建设型"
            focus_areas = ["夯实基础", "完善制度", "加强建设"]
        
        # 针对薄弱环节的具体措施
        specific_measures = []
        for area in weak_areas:
            if "组织韧性" in area:
                specific_measures.extend([
                    "加强群众基础建设",
                    "完善统一战线策略",
                    "提升矛盾转化能力"
                ])
            elif "权力结构" in area:
                specific_measures.extend([
                    "优化权力配置",
                    "完善民主集中制",
                    "加强权力监督"
                ])
            elif "决策过程" in area:
                specific_measures.extend([
                    "提高决策科学性",
                    "加强民主参与",
                    "完善决策机制"
                ])
        
        return {
            "改进方案类型": plan_type,
            "重点改进领域": focus_areas,
            "具体改进措施": list(set(specific_measures))[:10],  # 去重并限制数量
            "实施时间框架": self._determine_implementation_timeline(comprehensive_level),
            "预期效果": self._predict_improvement_effects(comprehensive_level),
            "风险控制": self._identify_improvement_risks(weak_areas)
        }
    
    def _summarize_mao_application(self, resilience: Dict, power: Dict, decision: Dict) -> Dict[str, Any]:
        """总结毛泽东思想应用"""
        
        # 提取各模块的毛泽东思想应用情况
        resilience_principles = resilience.get("原则应用情况", {})
        power_principles = power.get("毛泽东思想原则应用", {}).get("原则应用得分", {})
        decision_principles = decision.get("毛泽东思想原则应用评估", {}).get("原则应用得分", {})
        
        # 综合评估应用水平
        application_levels = {}
        
        # 分析各原则的应用情况
        all_principles = set(list(resilience_principles.keys()) + 
                           list(power_principles.keys()) + 
                           list(decision_principles.keys()))
        
        for principle in all_principles:
            scores = []
            if principle in resilience_principles:
                scores.append(resilience_principles[principle])
            if principle in power_principles:
                scores.append(power_principles[principle])
            if principle in decision_principles:
                scores.append(decision_principles[principle])
            
            if scores:
                avg_score = sum(scores) / len(scores)
                application_levels[principle] = {
                    "平均得分": round(avg_score, 2),
                    "应用水平": "优秀" if avg_score >= 8 else "良好" if avg_score >= 6 else "一般",
                    "应用模块": ["组织韧性" if principle in resilience_principles else "",
                              "权力结构" if principle in power_principles else "",
                              "决策过程" if principle in decision_principles else ""]
                }
        
        return {
            "毛泽东思想原则应用总结": application_levels,
            "总体应用水平": self._calculate_overall_application_level(application_levels),
            "成功应用案例": self._identify_successful_applications(application_levels),
            "需要加强原则": self._identify_weak_principles(application_levels),
            "应用效果评估": "毛泽东思想在组织分析中发挥了重要指导作用"
        }
    
    # 辅助方法实现
    def _determine_comprehensive_level(self, score: float) -> str:
        """确定综合等级"""
        if score >= 85:
            return "优秀"
        elif score >= 70:
            return "良好"
        elif score >= 60:
            return "一般"
        else:
            return "需要改进"
    
    def _identify_strength_areas(self, scores: Dict) -> List[str]:
        """识别优势领域"""
        strengths = []
        for area, score in scores.items():
            if score >= 80:
                strengths.append(f"{area}表现优秀")
        return strengths if strengths else ["各领域均有提升空间"]
    
    def _identify_weak_areas(self, scores: Dict) -> List[str]:
        """识别薄弱环节"""
        weaknesses = []
        for area, score in scores.items():
            if score < 60:
                weaknesses.append(f"{area}需要加强")
        return weaknesses if weaknesses else ["各领域表现均衡"]
    
    def _generate_development_suggestions(self, scores: Dict) -> List[str]:
        """生成发展建议"""
        suggestions = []
        
        for area, score in scores.items():
            if score >= 80:
                suggestions.append(f"保持{area}优势，发挥引领作用")
            elif score >= 60:
                suggestions.append(f"持续优化{area}，提升整体水平")
            else:
                suggestions.append(f"重点加强{area}建设，补齐短板")
        
        return suggestions
    
    def _determine_implementation_timeline(self, level: str) -> Dict[str, str]:
        """确定实施时间框架"""
        if level == "优秀":
            return {
                "短期": "3个月内完成优化调整",
                "中期": "6-12个月实现持续领先",
                "长期": "1-3年形成核心竞争力"
            }
        elif level == "良好":
            return {
                "短期": "6个月内完成重点改进",
                "中期": "1-2年实现全面提升",
                "长期": "2-3年达到优秀水平"
            }
        else:
            return {
                "短期": "1年内完成基础建设",
                "中期": "2-3年实现明显改善",
                "长期": "3-5年达到良好水平"
            }
    
    def _predict_improvement_effects(self, level: str) -> Dict[str, str]:
        """预测改进效果"""
        if level == "优秀":
            return {
                "组织效能": "显著提升",
                "竞争力": "持续增强",
                "发展潜力": "充分释放",
                "风险控制": "有效加强"
            }
        elif level == "良好":
            return {
                "组织效能": "稳步提升",
                "竞争力": "明显增强",
                "发展潜力": "逐步释放",
                "风险控制": "有效改善"
            }
        else:
            return {
                "组织效能": "基础改善",
                "竞争力": "逐步提升",
                "发展潜力": "开始显现",
                "风险控制": "初步建立"
            }
    
    def _identify_improvement_risks(self, weak_areas: List[str]) -> List[str]:
        """识别改进风险"""
        risks = []
        
        if "组织韧性" in str(weak_areas):
            risks.append("改进过程中可能出现组织不稳定")
        if "权力结构" in str(weak_areas):
            risks.append("权力调整可能引发内部矛盾")
        if "决策过程" in str(weak_areas):
            risks.append("决策机制改革需要时间适应")
        
        return risks if risks else ["改进风险总体可控"]
    
    def _calculate_overall_application_level(self, application_levels: Dict) -> str:
        """计算总体应用水平"""
        if not application_levels:
            return "未知"
        
        avg_scores = [app["平均得分"] for app in application_levels.values()]
        overall_avg = sum(avg_scores) / len(avg_scores)
        
        if overall_avg >= 8:
            return "优秀"
        elif overall_avg >= 6:
            return "良好"
        else:
            return "一般"
    
    def _identify_successful_applications(self, application_levels: Dict) -> List[str]:
        """识别成功应用案例"""
        successes = []
        for principle, app_info in application_levels.items():
            if app_info["平均得分"] >= 8:
                successes.append(f"{principle}原则应用效果显著")
        return successes if successes else ["各原则应用均有改进空间"]
    
    def _identify_weak_principles(self, application_levels: Dict) -> List[str]:
        """识别需要加强的原则"""
        weak_principles = []
        for principle, app_info in application_levels.items():
            if app_info["平均得分"] < 6:
                weak_principles.append(principle)
        return weak_principles if weak_principles else ["各原则应用效果良好"]

# 测试函数
def test_integrated_engine():
    """测试综合集成引擎"""
    engine = IntegratedMaoAnalysisEngine()
    
    # 测试数据
    test_organization = {
        "basic_info": {
            "组织名称": "测试科技公司",
            "组织类型": "科技企业",
            "规模": "中型",
            "成立时间": "2018年"
        },
        "description": """
        某科技公司拥有明确的管理层级和部门结构。CEO拥有最终决策权，各部门负责人负责具体业务。
        同时，公司内部有几位技术专家在技术决策方面具有重要影响力。员工通过定期会议参与决策讨论。
        公司强调创新文化和团队合作，重视员工意见和建议。
        """,
        "decision_description": """
        公司面临市场竞争加剧，管理层经过市场调研和数据分析，召开了多次会议听取各部门意见。
        最终决定调整产品战略，重点发展高附加值产品，并制定了详细的实施计划。
        决策过程中充分考虑了员工建议和客户需求。
        """,
        "context": {
            "行业环境": "科技行业竞争激烈",
            "发展阶段": "成长期",
            "战略重点": "创新驱动发展"
        }
    }
    
    result = engine.comprehensive_analysis(test_organization)
    
    print("=== 毛泽东思想综合集成分析结果 ===")
    print(f"分析时间: {result['分析时间']}")
    print(f"组织名称: {result['组织基本信息']['组织名称']}")
    print(f"综合得分: {result['综合评估报告']['综合得分']}")
    print(f"综合等级: {result['综合评估报告']['综合等级']}")
    
    print("\n=== 各维度得分 ===")
    for area, score in result['综合评估报告']['各维度得分'].items():
        print(f"{area}: {score}分")
    
    print("\n=== 优势领域 ===")
    for strength in result['综合评估报告']['优势领域']:
        print(f"• {strength}")
    
    print("\n=== 综合改进方案 ===")
    plan = result['综合改进方案']
    print(f"方案类型: {plan['改进方案类型']}")
    print("重点措施:")
    for i, measure in enumerate(plan['具体改进措施'][:5], 1):
        print(f"{i}. {measure}")
    
    print("\n=== 毛泽东思想应用总结 ===")
    mao_summary = result['毛泽东思想应用总结']
    print(f"总体应用水平: {mao_summary['总体应用水平']}")
    print("成功应用原则:")
    for principle in mao_summary['成功应用案例']:
        print(f"• {principle}")

if __name__ == "__main__":
    test_integrated_engine()