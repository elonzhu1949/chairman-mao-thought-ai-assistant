#!/usr/bin/env python3
"""
矛盾论分析模块 - 增强版（集成军事战略原则）
基于毛主席矛盾论思想的问题分析工具，集成军事战略原则和统一战线思想
"""

import json
from typing import Dict, List, Any

class ContradictionAnalyzer:
    """矛盾分析器 - 增强版（组织韧性评估框架）"""
    
    def __init__(self):
        # 基础矛盾论原则
        self.contradiction_types = {
            "主要矛盾": "决定事物性质和发展方向的根本矛盾",
            "次要矛盾": "处于从属地位但影响事物发展的矛盾",
            "对抗性矛盾": "根本利益冲突的矛盾",
            "非对抗性矛盾": "根本利益一致但存在差异的矛盾"
        }
        
        # 军事战略原则集成
        self.military_strategies = {
            "你打你的，我打我的": "保持战略主动，发挥自身优势",
            "集中优势兵力，各个歼灭敌人": "聚焦关键问题，逐个击破",
            "不打无准备之仗": "充分准备，稳扎稳打",
            "保存自己，消灭敌人": "在保护自身的同时解决问题"
        }
        
        # 统一战线原则
        self.united_front_principles = {
            "团结一切可以团结的力量": "扩大同盟，孤立主要对手",
            "利用矛盾，争取多数": "分化瓦解，争取支持",
            "孤立少数，各个击破": "集中力量解决主要矛盾",
            "又联合又斗争": "保持原则性和灵活性"
        }
        
        # 组织韧性评估指标
        self.resilience_factors = {
            "矛盾识别能力": "准确识别主要矛盾和次要矛盾",
            "矛盾转化能力": "将不利矛盾转化为有利条件",
            "战略部署能力": "运用军事战略原则解决问题的能力",
            "统一战线构建能力": "团结各方力量共同解决问题"
        }
    
    def analyze_problem(self, problem_description: str) -> Dict[str, Any]:
        """分析问题中的矛盾 - 增强版（集成军事战略和统一战线）"""
        
        # 识别矛盾要素
        contradictions = self._identify_contradictions(problem_description)
        
        # 确定主要矛盾
        main_contradiction = self._determine_main_contradiction(contradictions)
        
        # 分析矛盾转化
        transformation = self._analyze_transformation(contradictions)
        
        # 军事战略应用（新增功能）
        military_strategy = self._apply_military_strategy(contradictions, main_contradiction)
        
        # 统一战线构建（新增功能）
        united_front_plan = self._build_united_front(contradictions)
        
        # 组织韧性评估（新增功能）
        resilience_assessment = self._assess_organizational_resilience(contradictions, main_contradiction)
        
        return {
            "问题描述": problem_description,
            "矛盾识别": contradictions,
            "主要矛盾": main_contradiction,
            "矛盾转化分析": transformation,
            "解决建议": self._generate_solutions(contradictions, main_contradiction),
            # 新增：军事战略和统一战线集成
            "军事战略应用": military_strategy,
            "统一战线构建": united_front_plan,
            "组织韧性评估": resilience_assessment,
            "综合解决方案": self._generate_comprehensive_solution(contradictions, main_contradiction)
        }
    
    def _identify_contradictions(self, problem: str) -> List[Dict]:
        """识别问题中的各种矛盾"""
        contradictions = []
        
        # 这里可以根据具体问题类型进行更复杂的分析
        # 目前使用简单的关键词匹配
        
        contradiction_keywords = {
            "资源有限": "需求与资源的矛盾",
            "时间紧张": "任务与时间的矛盾", 
            "意见分歧": "不同观点的矛盾",
            "利益冲突": "利益分配的矛盾",
            "目标冲突": "不同目标的矛盾"
        }
        
        for keyword, contradiction in contradiction_keywords.items():
            if keyword in problem:
                contradictions.append({
                    "类型": contradiction,
                    "描述": f"问题中存在{contradiction}",
                    "关键词": keyword
                })
        
        return contradictions
    
    def _determine_main_contradiction(self, contradictions: List[Dict]) -> Dict:
        """确定主要矛盾"""
        if not contradictions:
            return {"类型": "未识别到明显矛盾", "说明": "需要更多信息进行分析"}
        
        # 简单的优先级判断
        priority_keywords = ["资源", "时间", "利益", "目标", "意见"]
        
        for keyword in priority_keywords:
            for contradiction in contradictions:
                if keyword in contradiction["类型"]:
                    return {
                        "主要矛盾": contradiction["类型"],
                        "判断依据": f"{keyword}相关矛盾通常是主要矛盾",
                        "解决优先级": "高"
                    }
        
        # 默认返回第一个矛盾
        return {
            "主要矛盾": contradictions[0]["类型"],
            "判断依据": "按出现顺序确定",
            "解决优先级": "中"
        }
    
    def _analyze_transformation(self, contradictions: List[Dict]) -> Dict:
        """分析矛盾转化规律"""
        return {
            "转化规律": "矛盾在一定条件下可以相互转化",
            "转化条件": "需要创造适当的条件",
            "转化方向": "次要矛盾可能转化为主要矛盾"
        }
    
    def _generate_solutions(self, contradictions: List[Dict], main_contradiction: Dict) -> List[str]:
        """生成解决建议 - 增强版（集成军事战略）"""
        solutions = []
        
        # 基于矛盾论的基本解决原则
        solutions.append("抓住主要矛盾，集中力量解决")
        solutions.append("创造条件，促进矛盾向有利方向转化")
        solutions.append("统筹兼顾，处理好次要矛盾")
        
        # 根据具体矛盾类型给出建议
        if "资源" in main_contradiction.get("主要矛盾", ""):
            solutions.append("优化资源配置，提高资源利用效率")
            solutions.append("采用'集中优势兵力'原则，优先保障关键资源")
        elif "时间" in main_contradiction.get("主要矛盾", ""):
            solutions.append("科学安排时间，分清轻重缓急")
            solutions.append("实施'不打无准备之仗'原则，充分准备后再行动")
        elif "利益" in main_contradiction.get("主要矛盾", ""):
            solutions.append("平衡各方利益，寻求共赢方案")
            solutions.append("运用统一战线原则，团结多数，孤立少数")
        
        # 军事战略原则应用
        solutions.extend(self._apply_military_solutions(main_contradiction))
        
        return solutions
    
    def _apply_military_strategy(self, contradictions: List[Dict], main_contradiction: Dict) -> Dict[str, Any]:
        """应用军事战略原则"""
        
        strategies = []
        
        # 根据矛盾特点选择战略
        contradiction_text = main_contradiction.get("主要矛盾", "")
        
        if "复杂" in contradiction_text or "多个" in contradiction_text:
            strategies.append({
                "战略": "集中优势兵力，各个歼灭敌人",
                "应用": "将复杂问题分解，逐个击破",
                "具体措施": "识别关键节点，集中资源突破"
            })
        
        if "困难" in contradiction_text or "挑战" in contradiction_text:
            strategies.append({
                "战略": "你打你的，我打我的",
                "应用": "保持战略主动，发挥自身优势",
                "具体措施": "分析自身优势，制定差异化解决方案"
            })
        
        if "紧迫" in contradiction_text or "紧急" in contradiction_text:
            strategies.append({
                "战略": "不打无准备之仗",
                "应用": "充分准备，确保行动成功",
                "具体措施": "制定详细计划，充分准备资源"
            })
        
        # 默认战略
        if not strategies:
            strategies.append({
                "战略": "保存自己，消灭敌人",
                "应用": "在保护自身的同时解决问题",
                "具体措施": "平衡风险与收益，实现可持续发展"
            })
        
        return {
            "适用战略": strategies,
            "战略原则": "战略上藐视困难，战术上重视细节",
            "实施建议": "根据矛盾特点灵活运用不同战略"
        }
    
    def _build_united_front(self, contradictions: List[Dict]) -> Dict[str, Any]:
        """构建统一战线"""
        
        # 分析可以团结的力量
        ally_forces = []
        opponent_forces = []
        
        for contradiction in contradictions:
            contradiction_type = contradiction.get("类型", "")
            if "利益一致" in contradiction_type or "非对抗性" in contradiction_type:
                ally_forces.append({
                    "力量类型": "可团结对象",
                    "矛盾性质": "非对抗性矛盾",
                    "团结策略": "争取支持，共同解决问题"
                })
            elif "利益冲突" in contradiction_type or "对抗性" in contradiction_type:
                opponent_forces.append({
                    "力量类型": "需要化解的对象",
                    "矛盾性质": "对抗性矛盾",
                    "应对策略": "分化瓦解，争取转化"
                })
        
        return {
            "统一战线原则": "团结一切可以团结的力量",
            "可团结力量": ally_forces,
            "需要化解力量": opponent_forces,
            "构建策略": [
                "识别共同利益，建立合作基础",
                "争取中间力量，扩大同盟范围",
                "分化主要对手，减少敌对力量",
                "建立长期稳定的合作关系"
            ],
            "注意事项": "坚持原则的坚定性和策略的灵活性"
        }
    
    def _assess_organizational_resilience(self, contradictions: List[Dict], main_contradiction: Dict) -> Dict[str, Any]:
        """评估组织韧性"""
        
        resilience_score = 0
        indicators = []
        
        # 评估矛盾识别能力
        identification_score = len(contradictions) * 2  # 每个矛盾得2分
        resilience_score += min(10, identification_score)
        indicators.append({
            "指标": "矛盾识别能力",
            "得分": min(10, identification_score),
            "评估": "高" if identification_score >= 8 else "中" if identification_score >= 5 else "低",
            "说明": "识别矛盾的数量和质量"
        })
        
        # 评估主要矛盾识别准确性
        main_contradiction_score = 8 if main_contradiction.get("解决优先级", "") == "高" else 5
        resilience_score += main_contradiction_score
        indicators.append({
            "指标": "主要矛盾识别准确性",
            "得分": main_contradiction_score,
            "评估": "高" if main_contradiction_score >= 8 else "中",
            "说明": "准确识别主要矛盾的能力"
        })
        
        # 计算总体韧性得分
        total_score = resilience_score
        resilience_level = "高" if total_score >= 15 else "中" if total_score >= 10 else "低"
        
        return {
            "总体韧性得分": total_score,
            "韧性等级": resilience_level,
            "评估指标": indicators,
            "改进建议": self._generate_resilience_improvements(total_score),
            "军事战略支持": self._suggest_military_support(total_score)
        }
    
    def _generate_comprehensive_solution(self, contradictions: List[Dict], main_contradiction: Dict) -> Dict[str, Any]:
        """生成综合解决方案"""
        
        return {
            "解决思路": "运用毛主席思想的综合方法论",
            "核心原则": [
                "实事求是：从实际出发分析问题",
                "群众路线：依靠群众智慧解决问题",
                "矛盾论：抓住主要矛盾，促进矛盾转化",
                "军事战略：运用战略原则指导行动",
                "统一战线：团结一切可以团结的力量"
            ],
            "实施步骤": [
                "第一步：深入调查研究，掌握实际情况",
                "第二步：分析主要矛盾，确定解决方向",
                "第三步：制定军事战略，明确行动方案",
                "第四步：构建统一战线，争取广泛支持",
                "第五步：实践检验优化，不断改进提升"
            ],
            "预期效果": "实现问题的根本解决和组织的持续发展"
        }
    
    def _apply_military_solutions(self, main_contradiction: Dict) -> List[str]:
        """应用军事战略解决方案"""
        solutions = []
        
        contradiction_text = main_contradiction.get("主要矛盾", "")
        
        if "资源" in contradiction_text:
            solutions.append("实施'集中优势兵力'原则，优先保障关键资源")
            solutions.append("运用'保存自己'原则，确保基本资源安全")
        
        if "时间" in contradiction_text:
            solutions.append("采用'不打无准备之仗'原则，充分准备后再行动")
            solutions.append("实施'你打你的，我打我的'原则，保持节奏主动")
        
        if "利益" in contradiction_text:
            solutions.append("运用统一战线原则，扩大利益同盟")
            solutions.append("实施'各个击破'原则，分化利益对立面")
        
        return solutions
    
    def _generate_resilience_improvements(self, total_score: int) -> List[str]:
        """生成韧性改进建议"""
        
        if total_score < 10:
            return [
                "加强矛盾识别训练，提高问题分析能力",
                "学习毛主席矛盾论，掌握矛盾分析方法",
                "实践军事战略原则，提升问题解决能力"
            ]
        elif total_score < 15:
            return [
                "深化矛盾转化能力，提升问题解决效果",
                "加强统一战线建设，扩大问题解决支持",
                "优化军事战略应用，提高行动效率"
            ]
        else:
            return [
                "保持高水平矛盾分析能力",
                "持续优化统一战线策略",
                "创新军事战略应用方法"
            ]
    
    def _suggest_military_support(self, total_score: int) -> List[str]:
        """建议军事战略支持"""
        
        if total_score < 10:
            return [
                "重点学习'不打无准备之仗'原则，加强基础建设",
                "实践'保存自己'原则，确保组织安全",
                "逐步应用'集中优势兵力'原则，积累经验"
            ]
        elif total_score < 15:
            return [
                "全面应用军事战略原则，提升问题解决能力",
                "加强'你打你的，我打我的'原则应用，保持主动",
                "优化'各个击破'策略，提高效率"
            ]
        else:
            return [
                "创新军事战略应用，实现跨越式发展",
                "深化战略战术结合，提升综合能力",
                "引领发展方向，创造新的竞争优势"
            ]

def main():
    """测试函数"""
    analyzer = ContradictionAnalyzer()
    
    # 测试用例
    test_problems = [
        "项目时间紧张，但团队成员意见分歧很大",
        "资源有限，但需求很多，不知道如何分配",
        "部门间利益冲突，目标不一致"
    ]
    
    for problem in test_problems:
        print(f"\n问题: {problem}")
        result = analyzer.analyze_problem(problem)
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()