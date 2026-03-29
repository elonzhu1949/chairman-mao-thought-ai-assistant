#!/usr/bin/env python3
"""
决策过程还原分析引擎 - 第三阶段升级
基于毛主席思想的决策过程分析和优化工具
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime

class DecisionProcessAnalyzer:
    """决策过程分析器 - 基于毛泽东思想原则"""
    
    def __init__(self):
        # 决策类型
        self.decision_types = {
            "战略决策": "涉及组织发展方向和重大问题的决策",
            "战术决策": "为实现战略目标而采取的具体措施决策",
            "操作决策": "日常运作中的具体执行决策",
            "危机决策": "应对突发情况和危机的决策"
        }
        
        # 毛泽东思想决策原则
        self.mao_decision_principles = {
            "实事求是": "决策必须从实际出发",
            "群众路线": "决策必须依靠群众智慧",
            "民主集中制": "在民主基础上集中，在集中指导下民主",
            "矛盾分析": "抓住主要矛盾进行决策",
            "实践检验": "决策效果需要通过实践检验"
        }
        
        # 决策质量评估标准
        self.quality_standards = {
            "科学性": "决策是否符合客观规律",
            "民主性": "决策是否充分发扬民主",
            "可行性": "决策是否具有可操作性",
            "时效性": "决策是否及时有效",
            "前瞻性": "决策是否具有长远眼光"
        }
    
    def analyze_decision_process(self, decision_description: str, context: Dict = None) -> Dict[str, Any]:
        """分析决策过程"""
        
        # 还原决策过程
        process_reconstruction = self._reconstruct_decision_process(decision_description, context)
        
        # 评估决策质量
        quality_assessment = self._assess_decision_quality(process_reconstruction)
        
        # 毛泽东思想原则应用评估
        mao_application_assessment = self._assess_mao_application(process_reconstruction)
        
        # 决策效果预测
        effect_prediction = self._predict_decision_effects(process_reconstruction, quality_assessment)
        
        # 优化建议
        optimization_suggestions = self._generate_optimization_suggestions(process_reconstruction, quality_assessment)
        
        return {
            "决策描述": decision_description,
            "决策过程还原": process_reconstruction,
            "决策质量评估": quality_assessment,
            "毛泽东思想原则应用评估": mao_application_assessment,
            "决策效果预测": effect_prediction,
            "优化建议": optimization_suggestions,
            "综合评估报告": self._generate_comprehensive_report(process_reconstruction, quality_assessment)
        }
    
    def _reconstruct_decision_process(self, description: str, context: Dict) -> Dict[str, Any]:
        """还原决策过程"""
        
        # 识别决策类型
        decision_type = self._identify_decision_type(description)
        
        # 分析决策参与者
        participants = self._identify_participants(description)
        
        # 还原决策步骤
        decision_steps = self._reconstruct_decision_steps(description)
        
        # 分析决策依据
        decision_basis = self._analyze_decision_basis(description)
        
        # 识别关键转折点
        turning_points = self._identify_turning_points(description)
        
        return {
            "决策类型": decision_type,
            "决策参与者": participants,
            "决策步骤": decision_steps,
            "决策依据": decision_basis,
            "关键转折点": turning_points,
            "决策时间框架": self._estimate_time_frame(description),
            "决策环境分析": self._analyze_decision_environment(description, context)
        }
    
    def _assess_decision_quality(self, process_reconstruction: Dict) -> Dict[str, Any]:
        """评估决策质量"""
        
        quality_scores = {}
        total_score = 0
        
        # 科学性评估
        scientific_score = self._evaluate_scientific_quality(process_reconstruction)
        quality_scores["科学性"] = scientific_score
        total_score += scientific_score
        
        # 民主性评估
        democratic_score = self._evaluate_democratic_quality(process_reconstruction)
        quality_scores["民主性"] = democratic_score
        total_score += democratic_score
        
        # 可行性评估
        feasibility_score = self._evaluate_feasibility_quality(process_reconstruction)
        quality_scores["可行性"] = feasibility_score
        total_score += feasibility_score
        
        # 时效性评估
        timeliness_score = self._evaluate_timeliness_quality(process_reconstruction)
        quality_scores["时效性"] = timeliness_score
        total_score += timeliness_score
        
        # 前瞻性评估
        forward_looking_score = self._evaluate_forward_looking_quality(process_reconstruction)
        quality_scores["前瞻性"] = forward_looking_score
        total_score += forward_looking_score
        
        # 计算总体质量
        average_score = total_score / len(quality_scores) if quality_scores else 0
        quality_level = self._determine_quality_level(average_score)
        
        return {
            "质量维度得分": quality_scores,
            "总体质量得分": round(average_score, 2),
            "质量等级": quality_level,
            "优势分析": self._analyze_strengths(quality_scores),
            "改进领域": self._identify_improvement_areas(quality_scores),
            "质量趋势": self._assess_quality_trend(process_reconstruction)
        }
    
    def _assess_mao_application(self, process_reconstruction: Dict) -> Dict[str, Any]:
        """评估毛泽东思想原则应用"""
        
        application_scores = {}
        principles_applied = []
        
        # 实事求是原则应用
        practical_score = self._evaluate_practical_application(process_reconstruction)
        application_scores["实事求是"] = practical_score
        if practical_score >= 7:
            principles_applied.append("实事求是")
        
        # 群众路线原则应用
        mass_line_score = self._evaluate_mass_line_application(process_reconstruction)
        application_scores["群众路线"] = mass_line_score
        if mass_line_score >= 7:
            principles_applied.append("群众路线")
        
        # 民主集中制原则应用
        democratic_centralism_score = self._evaluate_democratic_centralism_application(process_reconstruction)
        application_scores["民主集中制"] = democratic_centralism_score
        if democratic_centralism_score >= 7:
            principles_applied.append("民主集中制")
        
        # 矛盾分析原则应用
        contradiction_score = self._evaluate_contradiction_application(process_reconstruction)
        application_scores["矛盾分析"] = contradiction_score
        if contradiction_score >= 7:
            principles_applied.append("矛盾分析")
        
        # 实践检验原则应用
        practice_score = self._evaluate_practice_application(process_reconstruction)
        application_scores["实践检验"] = practice_score
        if practice_score >= 7:
            principles_applied.append("实践检验")
        
        total_score = sum(application_scores.values()) / len(application_scores) if application_scores else 0
        
        return {
            "原则应用得分": application_scores,
            "总体应用水平": round(total_score, 2),
            "成功应用原则": principles_applied,
            "需要加强原则": [p for p in application_scores if application_scores[p] < 7],
            "原则应用效果": self._evaluate_application_effectiveness(principles_applied),
            "改进建议": self._generate_principle_improvement_suggestions(application_scores)
        }
    
    def _predict_decision_effects(self, process_reconstruction: Dict, quality_assessment: Dict) -> Dict[str, Any]:
        """预测决策效果"""
        
        quality_level = quality_assessment.get("质量等级", "")
        
        # 基于决策质量预测效果
        if quality_level == "优秀":
            effect_prediction = {
                "短期效果": "决策得到有效执行，问题得到较好解决",
                "中期效果": "组织能力提升，发展势头良好",
                "长期效果": "实现可持续发展，竞争力增强",
                "风险预警": "风险较低，需要持续优化"
            }
        elif quality_level == "良好":
            effect_prediction = {
                "短期效果": "决策基本有效，部分问题需要调整",
                "中期效果": "组织稳步发展，需要持续改进",
                "长期效果": "具备发展潜力，需要战略引导",
                "风险预警": "存在一定风险，需要加强监控"
            }
        else:
            effect_prediction = {
                "短期效果": "决策效果有限，可能出现问题",
                "中期效果": "组织发展受阻，需要重大调整",
                "长期效果": "面临较大挑战，需要根本改革",
                "风险预警": "风险较高，需要立即采取措施"
            }
        
        return {
            "效果预测": effect_prediction,
            "预测依据": "基于决策质量评估和毛泽东思想原则",
            "不确定性分析": self._analyze_uncertainty(process_reconstruction),
            "关键成功因素": self._identify_success_factors(process_reconstruction),
            "风险应对策略": self._generate_risk_response_strategies(quality_level)
        }
    
    # 辅助方法实现
    def _identify_decision_type(self, description: str) -> Dict[str, Any]:
        """识别决策类型"""
        
        type_keywords = {
            "战略决策": ["战略", "方向", "规划", "目标", "愿景"],
            "战术决策": ["战术", "措施", "方法", "方案", "策略"],
            "操作决策": ["操作", "执行", "日常", "常规", "流程"],
            "危机决策": ["危机", "紧急", "突发", "应急", "风险"]
        }
        
        matched_types = []
        for decision_type, keywords in type_keywords.items():
            matches = [kw for kw in keywords if kw in description]
            if matches:
                matched_types.append({
                    "决策类型": decision_type,
                    "匹配关键词": matches,
                    "置信度": len(matches) * 0.2  # 每个关键词0.2分
                })
        
        # 选择置信度最高的类型
        if matched_types:
            primary_type = max(matched_types, key=lambda x: x["置信度"])
            return {
                "主要类型": primary_type["决策类型"],
                "置信度": primary_type["置信度"],
                "可能类型": [t["决策类型"] for t in matched_types if t != primary_type]
            }
        
        return {"主要类型": "未识别", "置信度": 0, "可能类型": []}
    
    def _identify_participants(self, description: str) -> List[Dict[str, Any]]:
        """识别决策参与者"""
        
        participant_keywords = {
            "领导者": ["领导", "负责人", "主管", "经理", "CEO"],
            "专家": ["专家", "顾问", "技术人员", "专业人员"],
            "群众代表": ["员工", "成员", "代表", "参与者", "利益相关者"],
            "外部顾问": ["外部", "顾问", "咨询", "第三方"]
        }
        
        participants = []
        for role, keywords in participant_keywords.items():
            matches = [kw for kw in keywords if kw in description]
            if matches:
                participants.append({
                    "角色": role,
                    "参与程度": "高" if len(matches) >= 2 else "中" if len(matches) >= 1 else "低",
                    "关键词匹配": matches,
                    "作用": self._determine_participant_role(role)
                })
        
        return participants
    
    def _reconstruct_decision_steps(self, description: str) -> List[Dict[str, Any]]:
        """还原决策步骤"""
        
        steps = []
        
        # 基于毛泽东思想的标准决策步骤
        standard_steps = [
            {"步骤": "调查研究", "内容": "深入实际了解情况"},
            {"步骤": "矛盾分析", "内容": "识别主要矛盾和次要矛盾"},
            {"步骤": "群众参与", "内容": "听取群众意见和智慧"},
            {"步骤": "民主讨论", "内容": "充分发扬民主，集中智慧"},
            {"步骤": "集中决策", "内容": "在民主基础上实行正确集中"},
            {"步骤": "实践检验", "内容": "通过实践检验决策效果"}
        ]
        
        # 分析描述中提到的步骤
        mentioned_steps = []
        for step in standard_steps:
            step_keywords = ["调查", "研究", "矛盾", "群众", "民主", "集中", "实践", "检验"]
            if any(kw in description for kw in step_keywords if kw in step["步骤"]):
                mentioned_steps.append({
                    "步骤": step["步骤"],
                    "内容": step["内容"],
                    "提及程度": "明确提及"
                })
            else:
                mentioned_steps.append({
                    "步骤": step["步骤"],
                    "内容": step["内容"],
                    "提及程度": "未明确提及"
                })
        
        return mentioned_steps
    
    def _analyze_decision_basis(self, description: str) -> Dict[str, Any]:
        """分析决策依据"""
        
        basis_types = {
            "事实依据": ["数据", "事实", "实际情况", "调研", "研究"],
            "理论依据": ["理论", "原理", "规律", "模型", "框架"],
            "经验依据": ["经验", "教训", "历史", "案例", "实践"],
            "群众意见": ["意见", "建议", "反馈", "需求", "期望"]
        }
        
        basis_analysis = {}
        for basis_type, keywords in basis_types.items():
            matches = [kw for kw in keywords if kw in description]
            if matches:
                basis_analysis[basis_type] = {
                    "依据强度": len(matches) * 0.25,  # 每个关键词0.25分
                    "关键词匹配": matches,
                    "评估": "充分" if len(matches) >= 3 else "一般" if len(matches) >= 1 else "不足"
                }
        
        return basis_analysis
    
    def _evaluate_scientific_quality(self, process_reconstruction: Dict) -> float:
        """评估科学性"""
        score = 5.0  # 基础分
        
        # 分析决策依据
        basis_analysis = process_reconstruction.get("决策依据", {})
        if "事实依据" in basis_analysis:
            score += basis_analysis["事实依据"]["依据强度"] * 2
        if "理论依据" in basis_analysis:
            score += basis_analysis["理论依据"]["依据强度"] * 1.5
        
        return min(10.0, max(1.0, score))
    
    def _evaluate_democratic_quality(self, process_reconstruction: Dict) -> float:
        """评估民主性"""
        score = 5.0  # 基础分
        
        # 分析参与者
        participants = process_reconstruction.get("决策参与者", [])
        mass_participants = [p for p in participants if p["角色"] in ["群众代表", "外部顾问"]]
        
        if mass_participants:
            score += len(mass_participants) * 1.0
        
        # 分析决策步骤
        steps = process_reconstruction.get("决策步骤", [])
        democratic_steps = [s for s in steps if s["步骤"] in ["群众参与", "民主讨论"] and s["提及程度"] == "明确提及"]
        
        if democratic_steps:
            score += len(democratic_steps) * 1.5
        
        return min(10.0, max(1.0, score))
    
    def _evaluate_feasibility_quality(self, process_reconstruction: Dict) -> float:
        """评估可行性"""
        score = 6.0  # 基础分较高，因为大多数决策都有一定可行性
        
        # 分析决策类型
        decision_type = process_reconstruction.get("决策类型", {}).get("主要类型", "")
        
        if decision_type in ["操作决策", "战术决策"]:
            score += 2.0  # 操作性决策可行性较高
        elif decision_type == "战略决策":
            score += 1.0  # 战略决策可行性需要更多分析
        
        return min(10.0, max(1.0, score))
    
    def _evaluate_timeliness_quality(self, process_reconstruction: Dict) -> float:
        """评估时效性"""
        score = 5.0  # 基础分
        
        # 分析决策环境
        environment = process_reconstruction.get("决策环境分析", {})
        if environment.get("时间压力", ""):
            score += 2.0  # 有时间压力说明重视时效性
        
        return min(10.0, max(1.0, score))
    
    def _evaluate_forward_looking_quality(self, process_reconstruction: Dict) -> float:
        """评估前瞻性"""
        score = 4.0  # 基础分较低，前瞻性需要专门分析
        
        decision_type = process_reconstruction.get("决策类型", {}).get("主要类型", "")
        
        if decision_type == "战略决策":
            score += 3.0  # 战略决策通常具有较强前瞻性
        
        # 分析决策依据
        basis_analysis = process_reconstruction.get("决策依据", {})
        if "经验依据" in basis_analysis:
            score += basis_analysis["经验依据"]["依据强度"] * 1.0
        
        return min(10.0, max(1.0, score))
    
    def _determine_quality_level(self, score: float) -> str:
        """确定质量等级"""
        if score >= 8.5:
            return "优秀"
        elif score >= 7.0:
            return "良好"
        elif score >= 5.5:
            return "一般"
        else:
            return "需要改进"
    
    def _evaluate_practical_application(self, process_reconstruction: Dict) -> float:
        """评估实事求是原则应用"""
        score = 5.0
        
        basis_analysis = process_reconstruction.get("决策依据", {})
        if "事实依据" in basis_analysis:
            score += basis_analysis["事实依据"]["依据强度"] * 2.5
        
        return min(10.0, score)
    
    def _evaluate_mass_line_application(self, process_reconstruction: Dict) -> float:
        """评估群众路线原则应用"""
        score = 5.0
        
        participants = process_reconstruction.get("决策参与者", [])
        mass_participants = [p for p in participants if p["角色"] == "群众代表"]
        
        if mass_participants:
            score += len(mass_participants) * 1.5
        
        steps = process_reconstruction.get("决策步骤", [])
        mass_steps = [s for s in steps if s["步骤"] == "群众参与" and s["提及程度"] == "明确提及"]
        
        if mass_steps:
            score += 2.0
        
        return min(10.0, score)
    
    def _generate_optimization_suggestions(self, process_reconstruction: Dict, quality_assessment: Dict) -> List[str]:
        """生成优化建议"""
        
        suggestions = []
        quality_level = quality_assessment.get("质量等级", "")
        
        if quality_level in ["需要改进", "一般"]:
            suggestions.extend([
                "加强调查研究，确保决策基于事实",
                "扩大群众参与，充分听取群众意见",
                "完善民主集中制，提高决策科学性",
                "建立决策后评估机制，持续改进决策质量"
            ])
        elif quality_level == "良好":
            suggestions.extend([
                "优化决策流程，提高决策效率",
                "加强前瞻性分析，提高战略眼光",
                "完善决策监督机制，确保决策执行",
                "加强决策人才培养，提高决策能力"
            ])
        else:
            suggestions.extend([
                "保持优秀决策水平，持续创新",
                "总结成功经验，形成决策范式",
                "引领决策科学发展，树立标杆",
                "加强决策理论研究，贡献智慧"
            ])
        
        return suggestions
    
    def _generate_comprehensive_report(self, process_reconstruction: Dict, quality_assessment: Dict) -> Dict[str, Any]:
        """生成综合评估报告"""
        
        return {
            "报告摘要": "基于毛泽东思想的决策过程综合评估报告",
            "评估结论": f"决策质量等级：{quality_assessment.get('质量等级', '未知')}",
            "主要发现": self._summarize_key_findings(process_reconstruction, quality_assessment),
            "改进建议": self._generate_detailed_improvement_suggestions(quality_assessment),
            "后续行动": self._recommend_follow_up_actions(quality_assessment)
        }
    
    # 其他辅助方法（简略实现）
    def _determine_participant_role(self, role: str) -> str:
        """确定参与者作用"""
        role_descriptions = {
            "领导者": "决策主导者和最终责任人",
            "专家": "提供专业知识和建议",
            "群众代表": "反映群众意见和需求",
            "外部顾问": "提供外部视角和专业咨询"
        }
        return role_descriptions.get(role, "参与者")
    
    def _estimate_time_frame(self, description: str) -> str:
        """估计决策时间框架"""
        if "长期" in description or "战略" in description:
            return "长期决策"
        elif "中期" in description or "规划" in description:
            return "中期决策"
        elif "短期" in description or "紧急" in description:
            return "短期决策"
        else:
            return "常规决策"
    
    def _analyze_decision_environment(self, description: str, context: Dict) -> Dict[str, Any]:
        """分析决策环境"""
        return {
            "环境复杂性": "需要进一步分析",
            "时间压力": "存在" if "紧急" in description or "时间" in description else "一般",
            "资源约束": "需要具体评估",
            "利益相关者": "需要识别具体对象"
        }
    
    def _analyze_strengths(self, quality_scores: Dict) -> List[str]:
        """分析优势"""
        strengths = []
        for dimension, score in quality_scores.items():
            if score >= 7.0:
                strengths.append(f"{dimension}表现优秀")
        return strengths if strengths else ["各维度均有提升空间"]
    
    def _identify_improvement_areas(self, quality_scores: Dict) -> List[str]:
        """识别改进领域"""
        improvements = []
        for dimension, score in quality_scores.items():
            if score < 6.0:
                improvements.append(f"{dimension}需要加强")
        return improvements if improvements else ["各维度表现均衡"]
    
    def _assess_quality_trend(self, process_reconstruction: Dict) -> str:
        """评估质量趋势"""
        return "需要历史数据支持的趋势分析"
    
    def _evaluate_democratic_centralism_application(self, process_reconstruction: Dict) -> float:
        """评估民主集中制应用"""
        return 6.0  # 简化实现
    
    def _evaluate_contradiction_application(self, process_reconstruction: Dict) -> float:
        """评估矛盾分析应用"""
        return 5.5  # 简化实现
    
    def _evaluate_practice_application(self, process_reconstruction: Dict) -> float:
        """评估实践检验应用"""
        return 5.0  # 简化实现
    
    def _evaluate_application_effectiveness(self, principles_applied: List[str]) -> str:
        """评估应用效果"""
        if len(principles_applied) >= 3:
            return "效果显著"
        elif len(principles_applied) >= 1:
            return "效果一般"
        else:
            return "效果有限"
    
    def _generate_principle_improvement_suggestions(self, application_scores: Dict) -> List[str]:
        """生成原则改进建议"""
        suggestions = []
        for principle, score in application_scores.items():
            if score < 7.0:
                suggestions.append(f"加强{principle}原则的应用")
        return suggestions if suggestions else ["毛泽东思想原则应用良好"]
    
    def _analyze_uncertainty(self, process_reconstruction: Dict) -> Dict[str, Any]:
        """分析不确定性"""
        return {
            "不确定性来源": ["环境变化", "执行效果", "外部影响"],
            "不确定性程度": "需要具体评估",
            "应对策略": "建立弹性机制，加强监控"
        }
    
    def _identify_success_factors(self, process_reconstruction: Dict) -> List[str]:
        """识别成功因素"""
        return ["领导支持", "群众参与", "科学决策", "有效执行"]
    
    def _generate_risk_response_strategies(self, quality_level: str) -> List[str]:
        """生成风险应对策略"""
        if quality_level in ["需要改进", "一般"]:
            return ["加强监控", "建立应急预案", "及时调整决策"]
        else:
            return ["持续优化", "防范风险", "保持优势"]
    
    def _summarize_key_findings(self, process_reconstruction: Dict, quality_assessment: Dict) -> List[str]:
        """总结主要发现"""
        return [
            f"决策质量等级：{quality_assessment.get('质量等级', '未知')}",
            f"毛泽东思想原则应用水平：{quality_assessment.get('毛泽东思想原则应用评估', {}).get('总体应用水平', '未知')}",
            "需要进一步加强决策科学性和民主性"
        ]
    
    def _generate_detailed_improvement_suggestions(self, quality_assessment: Dict) -> List[str]:
        """生成详细改进建议"""
        return [
            "建立完善的决策流程和机制",
            "加强决策人才培养和能力建设",
            "完善决策监督和评估体系",
            "推动决策科学化和民主化"
        ]
    
    def _recommend_follow_up_actions(self, quality_assessment: Dict) -> List[str]:
        """推荐后续行动"""
        return [
            "定期评估决策效果",
            "持续优化决策流程",
            "加强决策经验总结",
            "推动决策理论创新"
        ]
    
    def _identify_turning_points(self, description: str) -> List[Dict[str, Any]]:
        """识别关键转折点"""
        return [{
            "转折点": "决策关键节点",
            "时间": "需要具体分析",
            "影响": "对决策结果产生重要影响",
            "应对": "需要充分准备和灵活应对"
        }]

# 测试函数
def test_decision_analysis():
    """测试决策过程分析"""
    analyzer = DecisionProcessAnalyzer()
    
    # 测试用例
    test_decision = """
    公司面临市场竞争加剧，管理层经过市场调研和数据分析，召开了多次会议听取各部门意见。
    最终决定调整产品战略，重点发展高附加值产品，并制定了详细的实施计划。
    决策过程中充分考虑了员工建议和客户需求。
    """
    
    result = analyzer.analyze_decision_process(test_decision)
    
    print("=== 决策过程分析结果 ===")
    print(f"决策类型: {result['决策过程还原']['决策类型']['主要类型']}")
    print(f"决策质量等级: {result['决策质量评估']['质量等级']}")
    print(f"总体质量得分: {result['决策质量评估']['总体质量得分']}")
    print(f"毛泽东思想原则应用水平: {result['毛泽东思想原则应用评估']['总体应用水平']}")
    
    print("\n=== 优化建议 ===")
    for i, suggestion in enumerate(result['优化建议'], 1):
        print(f"{i}. {suggestion}")

if __name__ == "__main__":
    test_decision_analysis()