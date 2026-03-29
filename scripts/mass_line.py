#!/usr/bin/env python3
"""
群众路线模块
基于毛主席群众路线思想的用户需求收集工具
"""

import json
from typing import Dict, List, Any
from datetime import datetime

class MassLineAnalyzer:
    """群众路线分析器 - 增强版（组织韧性评估框架）"""
    
    def __init__(self):
        # 基础群众路线原则
        self.principles = {
            "一切为了群众": "工作的出发点和落脚点",
            "一切依靠群众": "力量的源泉",
            "从群众中来": "智慧的来源",
            "到群众中去": "实践的归宿"
        }
        
        # 组织韧性评估指标
        self.resilience_indicators = {
            "群众基础稳固度": "组织获得群众支持的程度",
            "统一战线构建能力": "团结各方力量的能力",
            "矛盾转化能力": "将不利因素转化为有利因素的能力",
            "实践创新能力": "在实践中检验和创新的能力",
            "自我革新能力": "自我革命和持续改进的能力"
        }
        
        # 军事战略原则应用
        self.military_strategies = {
            "你打你的，我打我的": "保持战略主动，发挥自身优势",
            "集中优势兵力，各个歼灭敌人": "聚焦关键问题，逐个击破",
            "不打无准备之仗": "充分准备，稳扎稳打",
            "保存自己，消灭敌人": "在保护自身的同时解决问题"
        }
    
    def collect_user_needs(self, user_input: str, context: Dict = None) -> Dict[str, Any]:
        """收集和分析用户需求 - 增强版（包含组织韧性评估）"""
        
        # 分析用户需求的层次
        need_levels = self._analyze_need_levels(user_input)
        
        # 识别群众利益
        mass_interests = self._identify_mass_interests(user_input, context)
        
        # 制定群众参与方案
        participation_plan = self._create_participation_plan(user_input, need_levels)
        
        # 生成群众意见汇总
        opinion_summary = self._summarize_mass_opinions(user_input)
        
        # 组织韧性评估（新增功能）
        resilience_assessment = self._assess_organizational_resilience(user_input, context)
        
        # 军事战略原则应用（新增功能）
        military_strategy_applications = self._apply_military_strategies(user_input)
        
        return {
            "用户输入": user_input,
            "需求层次分析": need_levels,
            "群众利益识别": mass_interests,
            "群众参与方案": participation_plan,
            "意见汇总": opinion_summary,
            "群众路线原则应用": self._apply_mass_line_principles(user_input),
            # 新增：组织韧性评估框架
            "组织韧性评估": resilience_assessment,
            "军事战略原则应用": military_strategy_applications,
            "统一战线构建建议": self._build_united_front(user_input)
        }
    
    def _assess_organizational_resilience(self, user_input: str, context: Dict = None) -> Dict[str, Any]:
        """评估组织韧性"""
        
        resilience_score = 0
        indicators = []
        
        # 评估群众基础稳固度
        mass_base_score = self._evaluate_mass_base(user_input)
        resilience_score += mass_base_score
        indicators.append({
            "指标": "群众基础稳固度",
            "得分": mass_base_score,
            "评估": "高" if mass_base_score >= 8 else "中" if mass_base_score >= 5 else "低",
            "改进建议": "加强群众联系，提高群众参与度"
        })
        
        # 评估统一战线构建能力
        united_front_score = self._evaluate_united_front_capability(user_input)
        resilience_score += united_front_score
        indicators.append({
            "指标": "统一战线构建能力",
            "得分": united_front_score,
            "评估": "高" if united_front_score >= 8 else "中" if united_front_score >= 5 else "低",
            "改进建议": "扩大团结范围，优化合作策略"
        })
        
        # 评估矛盾转化能力
        contradiction_transformation_score = self._evaluate_contradiction_transformation(user_input)
        resilience_score += contradiction_transformation_score
        indicators.append({
            "指标": "矛盾转化能力",
            "得分": contradiction_transformation_score,
            "评估": "高" if contradiction_transformation_score >= 8 else "中" if contradiction_transformation_score >= 5 else "低",
            "改进建议": "加强矛盾分析，提升转化能力"
        })
        
        # 计算总体韧性得分（满分30分）
        total_score = resilience_score
        resilience_level = "高" if total_score >= 24 else "中" if total_score >= 15 else "低"
        
        return {
            "总体韧性得分": total_score,
            "韧性等级": resilience_level,
            "评估指标": indicators,
            "改进建议": self._generate_resilience_improvement_suggestions(total_score),
            "军事战略应用": self._suggest_military_strategies(total_score)
        }
    
    def _evaluate_mass_base(self, user_input: str) -> int:
        """评估群众基础稳固度"""
        score = 5  # 基础分
        
        # 分析关键词加分
        mass_keywords = ["群众", "团队", "集体", "大家", "我们", "共同"]
        for keyword in mass_keywords:
            if keyword in user_input:
                score += 1
        
        # 分析个人主义倾向减分
        individualism_keywords = ["我", "自己", "个人", "独自"]
        individual_count = sum(1 for keyword in individualism_keywords if keyword in user_input)
        if individual_count > len(mass_keywords):
            score -= 2
        
        return max(1, min(10, score))
    
    def _evaluate_united_front_capability(self, user_input: str) -> int:
        """评估统一战线构建能力"""
        score = 5  # 基础分
        
        # 分析合作倾向加分
        cooperation_keywords = ["合作", "协作", "联合", "团结", "共赢", "互利"]
        for keyword in cooperation_keywords:
            if keyword in user_input:
                score += 1
        
        # 分析冲突倾向减分
        conflict_keywords = ["对抗", "冲突", "反对", "抵制", "排斥"]
        for keyword in conflict_keywords:
            if keyword in user_input:
                score -= 1
        
        return max(1, min(10, score))
    
    def _evaluate_contradiction_transformation(self, user_input: str) -> int:
        """评估矛盾转化能力"""
        score = 5  # 基础分
        
        # 分析问题解决倾向加分
        solution_keywords = ["解决", "转化", "优化", "改进", "创新", "突破"]
        for keyword in solution_keywords:
            if keyword in user_input:
                score += 1
        
        # 分析消极态度减分
        negative_keywords = ["困难", "问题", "挑战", "障碍", "困境"]
        negative_count = sum(1 for keyword in negative_keywords if keyword in user_input)
        if negative_count > 3:
            score -= 1
        
        return max(1, min(10, score))
    
    def _generate_resilience_improvement_suggestions(self, total_score: int) -> List[str]:
        """生成韧性改进建议"""
        suggestions = []
        
        if total_score < 15:
            suggestions.extend([
                "加强群众基础建设，提高群众参与度",
                "扩大统一战线，团结更多可以团结的力量",
                "提升矛盾转化能力，将不利因素转化为有利因素",
                "加强实践创新，通过实践检验和优化方案"
            ])
        elif total_score < 24:
            suggestions.extend([
                "巩固现有群众基础，深化群众联系",
                "优化统一战线策略，提高合作效率",
                "加强矛盾分析能力，提升转化效果",
                "持续实践创新，不断优化改进"
            ])
        else:
            suggestions.extend([
                "保持高水平群众基础，防止脱离群众",
                "维护统一战线成果，持续扩大团结范围",
                "深化矛盾转化能力，实现更高水平发展",
                "坚持实践创新，引领发展方向"
            ])
        
        return suggestions
    
    def _apply_military_strategies(self, user_input: str) -> Dict[str, Any]:
        """应用军事战略原则"""
        
        strategies = []
        
        # 分析适用战略
        if "困难" in user_input or "挑战" in user_input:
            strategies.append({
                "战略": "你打你的，我打我的",
                "应用": "保持战略主动，发挥自身优势，避免被动应对",
                "具体措施": "分析自身优势，制定差异化竞争策略"
            })
        
        if "复杂" in user_input or "多个" in user_input:
            strategies.append({
                "战略": "集中优势兵力，各个歼灭敌人",
                "应用": "聚焦关键问题，逐个击破，避免分散力量",
                "具体措施": "识别主要矛盾，集中资源解决核心问题"
            })
        
        if "决策" in user_input or "计划" in user_input:
            strategies.append({
                "战略": "不打无准备之仗",
                "应用": "充分准备，稳扎稳打，确保行动成功",
                "具体措施": "制定详细计划，充分准备资源，确保执行效果"
            })
        
        # 默认战略
        if not strategies:
            strategies.append({
                "战略": "保存自己，消灭敌人",
                "应用": "在保护自身的同时解决问题，实现双赢",
                "具体措施": "平衡自身利益和问题解决，寻求最佳方案"
            })
        
        return {
            "适用战略": strategies,
            "战略原则": "战略上藐视困难，战术上重视细节",
            "实施建议": "根据具体情况灵活运用不同战略"
        }
    
    def _suggest_military_strategies(self, total_score: int) -> List[str]:
        """根据韧性得分建议军事战略"""
        
        if total_score < 15:
            return [
                "采用防御性战略：保存实力，等待时机",
                "重点实施'不打无准备之仗'原则",
                "加强内部建设，巩固群众基础"
            ]
        elif total_score < 24:
            return [
                "采用攻守兼备战略：积极防御，主动出击",
                "实施'集中优势兵力，各个歼灭敌人'原则",
                "稳步推进，逐步扩大战果"
            ]
        else:
            return [
                "采用进攻性战略：主动出击，扩大优势",
                "全面实施'你打你的，我打我的'原则",
                "快速推进，实现跨越式发展"
            ]
    
    def _build_united_front(self, user_input: str) -> Dict[str, Any]:
        """构建统一战线建议"""
        
        return {
            "统一战线原则": "团结一切可以团结的力量",
            "构建策略": [
                "识别可以团结的对象和力量",
                "制定团结合作的具体措施",
                "建立长期稳定的合作关系",
                "实现互利共赢的合作目标"
            ],
            "注意事项": [
                "坚持原则的坚定性和策略的灵活性",
                "又联合又斗争，保持独立自主",
                "以我为主，为我所用"
            ]
        }
    
    def _analyze_need_levels(self, user_input: str) -> List[Dict]:
        """分析需求层次"""
        
        need_hierarchy = [
            {"层次": "基本需求", "关键词": ["解决", "帮助", "需要", "问题"], "说明": "用户最迫切的需求"},
            {"层次": "发展需求", "关键词": ["提升", "改进", "优化", "更好"], "说明": "用户的发展性需求"},
            {"层次": "价值需求", "关键词": ["意义", "价值", "贡献", "影响"], "说明": "用户的价值实现需求"}
        ]
        
        matched_levels = []
        for level in need_hierarchy:
            keywords_found = [kw for kw in level["关键词"] if kw in user_input]
            if keywords_found:
                matched_levels.append({
                    "需求层次": level["层次"],
                    "匹配关键词": keywords_found,
                    "说明": level["说明"],
                    "优先级": "高" if level["层次"] == "基本需求" else "中"
                })
        
        return matched_levels
    
    def _identify_mass_interests(self, user_input: str, context: Dict = None) -> Dict[str, Any]:
        """识别群众利益"""
        
        interests = {
            "个人利益": "用户个人的需求和利益",
            "集体利益": "相关群体的共同利益", 
            "社会利益": "更广泛的社会利益"
        }
        
        # 分析利益相关方
        stakeholders = self._identify_stakeholders(user_input)
        
        return {
            "利益分析": interests,
            "利益相关方": stakeholders,
            "利益平衡原则": "个人利益服从集体利益，集体利益服从社会利益",
            "群众利益最大化": "寻求最大多数人的最大利益"
        }
    
    def _identify_stakeholders(self, user_input: str) -> List[Dict]:
        """识别利益相关方"""
        
        stakeholder_keywords = {
            "团队": ["团队", "同事", "成员", "伙伴"],
            "用户": ["用户", "客户", "消费者", "受众"],
            "组织": ["公司", "部门", "机构", "单位"],
            "社会": ["社会", "公众", "社区", "环境"]
        }
        
        stakeholders = []
        for role, keywords in stakeholder_keywords.items():
            found_keywords = [kw for kw in keywords if kw in user_input]
            if found_keywords:
                stakeholders.append({
                    "角色": role,
                    "相关关键词": found_keywords,
                    "利益诉求": f"关注{role}的利益和需求"
                })
        
        # 默认包含用户本人
        if not any(s["角色"] == "个人" for s in stakeholders):
            stakeholders.insert(0, {
                "角色": "个人",
                "相关关键词": ["我", "自己"],
                "利益诉求": "用户个人的需求和利益"
            })
        
        return stakeholders
    
    def _create_participation_plan(self, user_input: str, need_levels: List[Dict]) -> List[Dict]:
        """制定群众参与方案"""
        
        plan = []
        
        # 基础参与方法
        plan.extend([
            {
                "参与方式": "意见收集",
                "具体措施": "通过问卷、访谈等方式收集群众意见",
                "适用场景": "需求分析阶段"
            },
            {
                "参与方式": "民主讨论",
                "具体措施": "组织讨论会，让群众充分发表意见",
                "适用场景": "方案制定阶段"
            },
            {
                "参与方式": "实践参与",
                "具体措施": "让群众参与具体实践过程",
                "适用场景": "实施阶段"
            }
        ])
        
        # 根据需求层次调整参与方式
        for level in need_levels:
            if level["需求层次"] == "基本需求":
                plan.append({
                    "参与方式": "紧急响应",
                    "具体措施": "优先解决群众最迫切的需求",
                    "适用场景": "紧急问题处理"
                })
            elif level["需求层次"] == "发展需求":
                plan.append({
                    "参与方式": "共同规划",
                    "具体措施": "与群众共同制定发展规划",
                    "适用场景": "长期发展计划"
                })
        
        return plan
    
    def _summarize_mass_opinions(self, user_input: str) -> Dict[str, Any]:
        """汇总群众意见"""
        
        return {
            "意见收集原则": "广泛收集，重点听取",
            "意见分析方法": "分类整理，去粗取精",
            "意见采纳标准": "符合大多数群众利益，具有可行性",
            "意见反馈机制": "及时向群众反馈意见采纳情况"
        }
    
    def _apply_mass_line_principles(self, user_input: str) -> List[str]:
        """应用群众路线原则"""
        
        applications = []
        
        applications.append("一切为了群众：以用户需求为出发点")
        applications.append("一切依靠群众：充分发挥集体智慧")
        applications.append("从群众中来：深入理解用户真实需求")
        applications.append("到群众中去：将解决方案落实到实践中")
        
        # 根据具体内容添加针对性应用
        if "决策" in user_input:
            applications.append("重大决策要充分听取群众意见")
        if "问题" in user_input:
            applications.append("问题解决要依靠群众的力量")
        
        return applications

def main():
    """测试函数"""
    analyzer = MassLineAnalyzer()
    
    # 测试用例
    test_inputs = [
        "我需要帮助团队提高工作效率",
        "如何让用户更满意我们的产品",
        "个人职业发展遇到瓶颈，需要指导"
    ]
    
    for user_input in test_inputs:
        print(f"\n用户输入: {user_input}")
        result = analyzer.collect_user_needs(user_input)
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()