#!/usr/bin/env python3
"""
权力结构动态演化模型 - 第二阶段升级
基于毛主席思想的权力结构分析和演化预测工具
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

class PowerStructureAnalyzer:
    """权力结构分析器 - 基于毛泽东思想原则"""
    
    def __init__(self):
        # 权力结构类型
        self.power_types = {
            "正式权力": "组织赋予的法定权力和职位权力",
            "非正式权力": "基于个人影响力、专业能力、人际关系形成的权力",
            "群众权力": "基于群众基础和群众支持形成的权力",
            "思想权力": "基于理论水平和思想影响力形成的权力"
        }
        
        # 权力演化规律
        self.evolution_principles = {
            "矛盾驱动": "权力结构的变化由内在矛盾推动",
            "群众基础决定": "权力稳固程度取决于群众支持程度",
            "实践检验": "权力合法性需要通过实践检验",
            "自我革命": "权力结构需要不断自我革新"
        }
        
        # 毛泽东思想中的权力原则
        self.mao_principles = {
            "民主集中制": "在民主基础上的集中，在集中指导下的民主",
            "群众路线": "一切为了群众，一切依靠群众",
            "批评与自我批评": "坚持真理，修正错误",
            "实事求是": "从实际出发，理论联系实际"
        }
    
    def analyze_power_structure(self, organization_description: str) -> Dict[str, Any]:
        """分析组织权力结构"""
        
        # 识别权力要素
        power_elements = self._identify_power_elements(organization_description)
        
        # 分析权力分布
        power_distribution = self._analyze_power_distribution(power_elements)
        
        # 评估权力稳固性
        stability_assessment = self._assess_power_stability(power_elements)
        
        # 预测权力演化趋势
        evolution_prediction = self._predict_evolution(power_elements, power_distribution)
        
        # 毛泽东思想原则应用
        mao_application = self._apply_mao_principles(power_elements)
        
        return {
            "组织描述": organization_description,
            "权力要素识别": power_elements,
            "权力分布分析": power_distribution,
            "权力稳固性评估": stability_assessment,
            "权力演化预测": evolution_prediction,
            "毛泽东思想原则应用": mao_application,
            "优化建议": self._generate_optimization_suggestions(power_elements, stability_assessment)
        }
    
    def _identify_power_elements(self, description: str) -> List[Dict[str, Any]]:
        """识别权力要素"""
        
        elements = []
        
        # 分析关键词识别权力类型
        keywords_mapping = {
            "正式权力": ["职位", "职务", "领导", "管理", "部门", "机构"],
            "非正式权力": ["影响力", "威望", "经验", "专业", "人脉", "关系"],
            "群众权力": ["群众", "员工", "团队", "支持", "拥护", "信任"],
            "思想权力": ["理论", "思想", "观点", "理念", "价值观", "文化"]
        }
        
        for power_type, keywords in keywords_mapping.items():
            matches = [kw for kw in keywords if kw in description]
            if matches:
                elements.append({
                    "权力类型": power_type,
                    "关键词匹配": matches,
                    "权重": len(matches) * 2,  # 每个关键词2分
                    "说明": self.power_types[power_type]
                })
        
        return elements
    
    def _analyze_power_distribution(self, power_elements: List[Dict]) -> Dict[str, Any]:
        """分析权力分布"""
        
        total_weight = sum(element["权重"] for element in power_elements)
        
        # 计算各权力类型占比
        distribution = {}
        for element in power_elements:
            power_type = element["权力类型"]
            weight = element["权重"]
            percentage = (weight / total_weight * 100) if total_weight > 0 else 0
            
            distribution[power_type] = {
                "权重": weight,
                "占比": round(percentage, 1),
                "评估": self._evaluate_distribution_level(percentage)
            }
        
        # 分析权力集中度
        concentration_score = self._calculate_concentration_score(distribution)
        
        return {
            "权力分布": distribution,
            "权力集中度": concentration_score,
            "分布类型": self._determine_distribution_type(distribution),
            "平衡性评估": self._assess_balance(distribution)
        }
    
    def _assess_power_stability(self, power_elements: List[Dict]) -> Dict[str, Any]:
        """评估权力稳固性"""
        
        stability_score = 0
        stability_factors = []
        
        # 群众基础评估
        mass_base_score = self._evaluate_mass_base(power_elements)
        stability_score += mass_base_score
        stability_factors.append({
            "因素": "群众基础",
            "得分": mass_base_score,
            "评估": "高" if mass_base_score >= 8 else "中" if mass_base_score >= 5 else "低",
            "说明": "权力稳固程度取决于群众支持"
        })
        
        # 民主集中制评估
        democratic_centralism_score = self._evaluate_democratic_centralism(power_elements)
        stability_score += democratic_centralism_score
        stability_factors.append({
            "因素": "民主集中制",
            "得分": democratic_centralism_score,
            "评估": "高" if democratic_centralism_score >= 8 else "中" if democratic_centralism_score >= 5 else "低",
            "说明": "民主与集中的平衡程度"
        })
        
        # 自我革新能力评估
        self_revolution_score = self._evaluate_self_revolution(power_elements)
        stability_score += self_revolution_score
        stability_factors.append({
            "因素": "自我革新能力",
            "得分": self_revolution_score,
            "评估": "高" if self_revolution_score >= 8 else "中" if self_revolution_score >= 5 else "低",
            "说明": "权力结构适应变化的能力"
        })
        
        # 计算总体稳固性
        total_score = stability_score
        stability_level = "高" if total_score >= 20 else "中" if total_score >= 12 else "低"
        
        return {
            "总体稳固性得分": total_score,
            "稳固性等级": stability_level,
            "稳定性因素": stability_factors,
            "风险预警": self._generate_risk_warnings(total_score),
            "加固建议": self._generate_strengthening_suggestions(stability_factors)
        }
    
    def _predict_evolution(self, power_elements: List[Dict], distribution: Dict) -> Dict[str, Any]:
        """预测权力演化趋势"""
        
        # 分析当前趋势
        current_trend = self._analyze_current_trend(power_elements)
        
        # 预测未来演化
        future_scenarios = self._generate_future_scenarios(power_elements, distribution)
        
        # 毛泽东思想指导原则
        mao_guidance = self._provide_mao_guidance(current_trend)
        
        return {
            "当前演化趋势": current_trend,
            "未来演化预测": future_scenarios,
            "毛泽东思想指导": mao_guidance,
            "演化驱动因素": self._identify_driving_factors(power_elements),
            "关键转折点": self._predict_turning_points(power_elements)
        }
    
    def _apply_mao_principles(self, power_elements: List[Dict]) -> Dict[str, Any]:
        """应用毛泽东思想原则"""
        
        applications = []
        
        # 民主集中制应用
        applications.append({
            "原则": "民主集中制",
            "应用": "实现民主与集中的辩证统一",
            "具体措施": [
                "建立健全民主决策机制",
                "在民主基础上实行正确集中",
                "个人服从组织，少数服从多数"
            ]
        })
        
        # 群众路线应用
        applications.append({
            "原则": "群众路线",
            "应用": "权力来源于群众，服务于群众",
            "具体措施": [
                "深入群众了解实际情况",
                "集中群众智慧制定决策",
                "接受群众监督和改进"
            ]
        })
        
        # 批评与自我批评应用
        applications.append({
            "原则": "批评与自我批评",
            "应用": "保持权力结构的先进性和纯洁性",
            "具体措施": [
                "建立批评与自我批评机制",
                "坚持真理，修正错误",
                "惩前毖后，治病救人"
            ]
        })
        
        return {
            "毛泽东思想原则应用": applications,
            "原则指导意义": "毛泽东思想为权力结构建设提供根本遵循",
            "实践要求": "将原则转化为具体制度和工作方法"
        }
    
    # 辅助方法实现
    def _evaluate_distribution_level(self, percentage: float) -> str:
        """评估分布水平"""
        if percentage >= 40:
            return "主导地位"
        elif percentage >= 20:
            return "重要地位"
        elif percentage >= 10:
            return "一般地位"
        else:
            return "次要地位"
    
    def _calculate_concentration_score(self, distribution: Dict) -> float:
        """计算权力集中度得分"""
        if not distribution:
            return 0
        
        percentages = [dist["占比"] for dist in distribution.values()]
        max_percentage = max(percentages) if percentages else 0
        
        # 集中度计算公式：最大占比与平均占比的比值
        avg_percentage = sum(percentages) / len(percentages) if percentages else 0
        concentration = max_percentage / avg_percentage if avg_percentage > 0 else 1
        
        return round(concentration, 2)
    
    def _determine_distribution_type(self, distribution: Dict) -> str:
        """确定分布类型"""
        concentration = self._calculate_concentration_score(distribution)
        
        if concentration >= 3:
            return "高度集中型"
        elif concentration >= 2:
            return "相对集中型"
        elif concentration >= 1.5:
            return "平衡分布型"
        else:
            return "分散分布型"
    
    def _assess_balance(self, distribution: Dict) -> Dict[str, Any]:
        """评估平衡性"""
        concentration = self._calculate_concentration_score(distribution)
        
        if concentration >= 3:
            return {"平衡性": "差", "建议": "需要加强权力制衡机制"}
        elif concentration >= 2:
            return {"平衡性": "一般", "建议": "适度优化权力分布"}
        elif concentration >= 1.5:
            return {"平衡性": "良好", "建议": "保持现有平衡状态"}
        else:
            return {"平衡性": "优秀", "建议": "理想的权力分布状态"}
    
    def _evaluate_mass_base(self, power_elements: List[Dict]) -> int:
        """评估群众基础"""
        mass_elements = [e for e in power_elements if e["权力类型"] == "群众权力"]
        
        if not mass_elements:
            return 3  # 基础分
        
        mass_weight = sum(e["权重"] for e in mass_elements)
        total_weight = sum(e["权重"] for e in power_elements)
        
        mass_percentage = (mass_weight / total_weight * 100) if total_weight > 0 else 0
        
        if mass_percentage >= 30:
            return 10
        elif mass_percentage >= 20:
            return 8
        elif mass_percentage >= 10:
            return 6
        else:
            return 4
    
    def _evaluate_democratic_centralism(self, power_elements: List[Dict]) -> int:
        """评估民主集中制"""
        # 分析正式权力和非正式权力的平衡
        formal_power = sum(e["权重"] for e in power_elements if e["权力类型"] == "正式权力")
        informal_power = sum(e["权重"] for e in power_elements if e["权力类型"] == "非正式权力")
        
        total_power = formal_power + informal_power
        
        if total_power == 0:
            return 5  # 中等分
        
        ratio = formal_power / total_power
        
        # 理想的民主集中制应该是正式权力略高于非正式权力
        if 0.4 <= ratio <= 0.6:
            return 9
        elif 0.3 <= ratio <= 0.7:
            return 7
        else:
            return 4
    
    def _evaluate_self_revolution(self, power_elements: List[Dict]) -> int:
        """评估自我革新能力"""
        # 分析思想权力和批评机制的存在
        thought_power = sum(1 for e in power_elements if e["权力类型"] == "思想权力")
        criticism_mechanism = sum(1 for e in power_elements if "批评" in str(e.get("关键词匹配", [])))
        
        score = 5  # 基础分
        
        if thought_power > 0:
            score += 2
        if criticism_mechanism > 0:
            score += 3
        
        return min(10, score)
    
    def _generate_risk_warnings(self, total_score: int) -> List[str]:
        """生成风险预警"""
        warnings = []
        
        if total_score < 12:
            warnings.extend([
                "⚠️ 权力稳固性较低，存在较大风险",
                "⚠️ 群众基础薄弱，需要加强群众联系",
                "⚠️ 民主集中制不健全，需要完善制度"
            ])
        elif total_score < 20:
            warnings.extend([
                "⚠️ 权力稳固性一般，需要持续关注",
                "⚠️ 部分权力因素需要加强建设"
            ])
        
        return warnings
    
    def _generate_strengthening_suggestions(self, stability_factors: List[Dict]) -> List[str]:
        """生成加固建议"""
        suggestions = []
        
        for factor in stability_factors:
            if factor["得分"] < 6:
                if factor["因素"] == "群众基础":
                    suggestions.append("加强群众基础建设，提高群众支持度")
                elif factor["因素"] == "民主集中制":
                    suggestions.append("完善民主集中制，平衡民主与集中")
                elif factor["因素"] == "自我革新能力":
                    suggestions.append("加强自我革新，适应环境变化")
        
        return suggestions if suggestions else ["权力结构相对稳固，继续保持"]
    
    def _analyze_current_trend(self, power_elements: List[Dict]) -> Dict[str, Any]:
        """分析当前趋势"""
        # 简化的趋势分析
        trend_indicators = []
        
        # 分析权力类型变化趋势
        power_types_count = len(power_elements)
        if power_types_count >= 3:
            trend_indicators.append({"趋势": "权力多元化", "强度": "强"})
        elif power_types_count >= 2:
            trend_indicators.append({"趋势": "权力适度集中", "强度": "中"})
        else:
            trend_indicators.append({"趋势": "权力高度集中", "强度": "弱"})
        
        return {
            "主要趋势": trend_indicators,
            "趋势持续时间": "需要长期观察",
            "趋势驱动因素": "内在矛盾和发展需求"
        }
    
    def _generate_future_scenarios(self, power_elements: List[Dict], distribution: Dict) -> List[Dict]:
        """生成未来演化场景"""
        scenarios = []
        
        # 场景1：优化发展
        scenarios.append({
            "场景": "优化发展",
            "概率": "高",
            "特征": "权力结构更加合理，民主集中制完善",
            "实现条件": "坚持群众路线，加强制度建设"
        })
        
        # 场景2：维持现状
        scenarios.append({
            "场景": "维持现状",
            "概率": "中",
            "特征": "权力结构基本稳定，小幅调整",
            "实现条件": "保持现有政策和机制"
        })
        
        # 场景3：风险演化
        scenarios.append({
            "场景": "风险演化",
            "概率": "低",
            "特征": "权力结构失衡，出现不稳定因素",
            "实现条件": "忽视群众基础，制度不健全"
        })
        
        return scenarios
    
    def _provide_mao_guidance(self, current_trend: Dict) -> Dict[str, Any]:
        """提供毛泽东思想指导"""
        return {
            "指导原则": "实事求是，群众路线，民主集中制",
            "具体指导": [
                "从实际出发分析权力结构问题",
                "依靠群众智慧优化权力配置",
                "坚持民主集中制原则",
                "在实践中检验和完善权力结构"
            ],
            "预期效果": "建立更加科学合理的权力结构"
        }
    
    def _identify_driving_factors(self, power_elements: List[Dict]) -> List[str]:
        """识别驱动因素"""
        factors = []
        
        if any(e["权力类型"] == "群众权力" for e in power_elements):
            factors.append("群众需求变化")
        
        if any(e["权力类型"] == "思想权力" for e in power_elements):
            factors.append("理论创新推动")
        
        factors.extend(["组织发展需求", "环境变化影响", "内在矛盾推动"])
        
        return factors
    
    def _predict_turning_points(self, power_elements: List[Dict]) -> List[Dict]:
        """预测关键转折点"""
        turning_points = []
        
        # 转折点1：群众基础重大变化
        turning_points.append({
            "转折点": "群众基础变化",
            "时间": "中长期",
            "影响": "权力合法性基础变化",
            "应对策略": "加强群众联系，完善民主机制"
        })
        
        # 转折点2：制度重大改革
        turning_points.append({
            "转折点": "制度重大改革",
            "时间": "中期",
            "影响": "权力运行机制变化",
            "应对策略": "适应新制度，优化权力配置"
        })
        
        return turning_points
    
    def _generate_optimization_suggestions(self, power_elements: List[Dict], stability_assessment: Dict) -> List[str]:
        """生成优化建议"""
        suggestions = []
        
        stability_level = stability_assessment.get("稳固性等级", "")
        
        if stability_level == "低":
            suggestions.extend([
                "立即加强群众基础建设",
                "完善民主集中制机制",
                "建立权力制衡体系",
                "加强权力监督机制"
            ])
        elif stability_level == "中":
            suggestions.extend([
                "持续优化权力配置",
                "加强制度建设",
                "提高权力运行透明度",
                "建立定期评估机制"
            ])
        else:
            suggestions.extend([
                "保持良好权力结构",
                "持续完善制度机制",
                "加强创新和适应性",
                "引领权力结构发展方向"
            ])
        
        return suggestions

# 测试函数
def test_power_structure_analyzer():
    """测试权力结构分析器"""
    analyzer = PowerStructureAnalyzer()
    
    # 测试用例
    test_organization = """
    某科技公司拥有明确的管理层级和部门结构。CEO拥有最终决策权，各部门负责人负责具体业务。
    同时，公司内部有几位技术专家在技术决策方面具有重要影响力。员工通过定期会议参与决策讨论。
    公司强调创新文化和团队合作，重视员工意见和建议。
    """
    
    result = analyzer.analyze_power_structure(test_organization)
    
    print("=== 权力结构分析结果 ===")
    print(f"组织描述: {result['组织描述'][:100]}...")
    print(f"权力要素识别: {len(result['权力要素识别'])}个要素")
    print(f"权力分布类型: {result['权力分布分析']['分布类型']}")
    print(f"权力稳固性等级: {result['权力稳固性评估']['稳固性等级']}")
    print(f"总体稳固性得分: {result['权力稳固性评估']['总体稳固性得分']}")
    
    print("\n=== 优化建议 ===")
    for i, suggestion in enumerate(result['优化建议'], 1):
        print(f"{i}. {suggestion}")

if __name__ == "__main__":
    test_power_structure_analyzer()