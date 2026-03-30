#!/usr/bin/env python3
"""
矛盾论分析模块 v2.0 - 基于毛泽东思想哲学原理的分析引擎
增强功能：场景识别、历史案例类比、反教条自检
"""

import json
from typing import Dict, List, Any, Optional

# 场景化推荐矩阵
SCENARIO_MATRIX = {
    "复杂问题": {"primary": "矛盾论", "secondary": "调查研究", "case": "遵义会议", "template": "A"},
    "重要决策": {"primary": "实事求是", "secondary": "实践论", "case": "寻乌调查", "template": "B"},
    "弱者竞争": {"primary": "农村包围城市", "secondary": "军事战略", "case": "井冈山", "template": "B"},
    "合作伙伴": {"primary": "统一战线", "secondary": "群众路线", "case": "重庆谈判", "template": "B"},
    "团队矛盾": {"primary": "批评与自我批评", "secondary": "民主集中制", "case": "延安整风", "template": "C"},
    "组织转型": {"primary": "自我革命", "secondary": "调查研究", "case": "遵义会议", "template": "C"},
    "方案推广": {"primary": "试点推广", "secondary": "群众工作", "case": "深圳特区", "template": "A"},
    "危机处理": {"primary": "军事战略", "secondary": "矛盾论", "case": "三大战役", "template": "B"},
    "个人成长": {"primary": "实践论", "secondary": "调查研究", "case": None, "template": "A"},
    "说服影响": {"primary": "群众路线", "secondary": "统一战线", "case": None, "template": "A"},
}

# 关键词到场景的映射
KEYWORD_SCENARIOS = {
    "问题很多": "复杂问题", "一团乱麻": "复杂问题", "复杂": "复杂问题", "不知从何下手": "复杂问题",
    "做决定": "重要决策", "选A还是选B": "重要决策", "决策": "重要决策",
    "创业": "弱者竞争", "大厂": "弱者竞争", "竞争不过": "弱者竞争", "资源不够": "弱者竞争",
    "合作": "合作伙伴", "联盟": "合作伙伴", "伙伴": "合作伙伴",
    "团队矛盾": "团队矛盾", "效率低下": "团队矛盾", "不团结": "团队矛盾", "沟通不畅": "团队矛盾",
    "转型": "组织转型", "变革": "组织转型", "创新": "组织转型", "跟不上": "组织转型",
    "推广": "方案推广", "新制度": "方案推广", "新产品": "方案推广",
    "危机": "危机处理", "紧急": "危机处理", "出了问题": "危机处理",
    "职业": "个人成长", "成长": "个人成长", "能力提升": "个人成长",
    "说服": "说服影响", "影响": "说服影响", "沟通": "说服影响",
}

# 历史案例库摘要
HISTORICAL_CASES = {
    "遵义会议": {
        "year": "1935",
        "core_lesson": "教条主义的危害，实事求是的力量。照搬外部经验而不结合自身实际，可能导致灾难性后果。",
        "modern_mapping": "企业危机中的战略纠偏、创新vs模仿、领导力危机处理"
    },
    "井冈山": {
        "year": "1927-1930",
        "core_lesson": "弱者如何在强者的缝隙中生存和发展。在对手薄弱处建立根据地，积蓄力量后逐步扩展。",
        "modern_mapping": "创业公司vs大企业、利基市场战略、下沉市场"
    },
    "延安整风": {
        "year": "1942-1945",
        "core_lesson": "思想统一是组织统一的前提。通过批评与自我批评实现深度认知对齐，而非通过强制手段。",
        "modern_mapping": "企业文化建设、认知对齐、学习型组织建设"
    },
    "重庆谈判": {
        "year": "1945",
        "core_lesson": "谈判桌上要有实力后盾，道义上争取主动可以改变力量对比。'有理有利有节'的灵活运用。",
        "modern_mapping": "商业谈判、竞争关系管理、弱势方争取主动"
    },
    "三大战役": {
        "year": "1948-1949",
        "core_lesson": "把握战略决战时机，集中使用力量。军事斗争与政治争取相结合。",
        "modern_mapping": "关键项目的资源集中、市场竞争的决战时机"
    },
    "古田会议": {
        "year": "1929",
        "core_lesson": "组织必须解决'为谁服务'的根本问题。思想建党政治建军是组织建设的根基。",
        "modern_mapping": "企业文化建设、使命定义、领导力建设"
    },
    "深圳特区": {
        "year": "1980",
        "core_lesson": "试点-总结-推广的经典实践。从个别到一般、从点到面的方法论典范。",
        "modern_mapping": "MVP、A/B测试、灰度发布、渐进式改革"
    },
}

# 反教条自检清单
ANTI_DOGMA_CHECKLIST = [
    ("具体化检查", "分析是否基于用户的具体情况，还是泛泛而谈？"),
    ("适用性检查", "推荐的方法论是否确实适用于这个场景？"),
    ("边界检查", "有没有指出方法论的使用边界和常见误用？"),
    ("操作性检查", "建议是否有可操作性，还是停留在理论层面？"),
    ("反面检查", "是否考虑了与建议相反的观点？"),
    ("实事求是不检查", "是否做到了不夸大方法论的适用范围？"),
]


class ContradictionAnalyzer:
    """矛盾分析器 v2.0 - 集成场景识别、案例类比和反教条自检"""

    def __init__(self):
        self.contradiction_types = {
            "主要矛盾": "决定事物性质和发展方向的根本矛盾",
            "次要矛盾": "处于从属地位但影响事物发展的矛盾",
            "对抗性矛盾": "根本利益冲突的矛盾",
            "非对抗性矛盾": "根本利益一致但存在差异的矛盾"
        }

        self.military_strategies = {
            "你打你的，我打我的": "保持战略主动，发挥自身优势",
            "集中优势兵力，各个歼灭敌人": "聚焦关键问题，逐个击破",
            "不打无准备之仗": "充分准备，稳扎稳打",
            "保存自己，消灭敌人": "在保护自身的同时解决问题"
        }

        self.united_front_principles = {
            "团结一切可以团结的力量": "扩大同盟，孤立主要对手",
            "利用矛盾，争取多数": "分化瓦解，争取支持",
            "孤立少数，各个击破": "集中力量解决主要矛盾",
            "又联合又斗争": "保持原则性和灵活性"
        }

    def identify_scenario(self, problem: str) -> Dict[str, Any]:
        """识别问题场景，推荐方法论组合"""
        matched_scenarios = []
        for keyword, scenario in KEYWORD_SCENARIOS.items():
            if keyword in problem:
                matched_scenarios.append(scenario)

        if not matched_scenarios:
            # 默认使用复杂问题场景
            matched_scenarios = ["复杂问题"]

        # 去重并取推荐矩阵
        recommendations = []
        seen = set()
        for scenario in matched_scenarios:
            if scenario in SCENARIO_MATRIX and scenario not in seen:
                rec = SCENARIO_MATRIX[scenario]
                recommendations.append({
                    "场景": scenario,
                    "首选方法论": rec["primary"],
                    "次选方法论": rec["secondary"],
                    "参考案例": rec["case"],
                    "输出模板": rec["template"]
                })
                seen.add(scenario)

        return recommendations

    def find_historical_analogy(self, problem: str, scenario: str = "") -> List[Dict]:
        """找到最相关的历史案例"""
        analogies = []
        for case_name, case_info in HISTORICAL_CASES.items():
            # 根据场景匹配案例
            scenario_case_map = {
                "复杂问题": ["遵义会议"],
                "弱者竞争": ["井冈山"],
                "团队矛盾": ["延安整风"],
                "合作伙伴": ["重庆谈判"],
                "组织转型": ["遵义会议", "延安整风"],
                "方案推广": ["深圳特区"],
                "危机处理": ["三大战役"],
            }
            recommended_cases = scenario_case_map.get(scenario, [])

            if case_name in recommended_cases:
                analogies.append({
                    "案例名称": case_name,
                    "时间": case_info["year"],
                    "核心教训": case_info["core_lesson"],
                    "现代映射": case_info["modern_mapping"],
                    "相关度": "高"
                })
            elif len(analogies) < 2:
                analogies.append({
                    "案例名称": case_name,
                    "时间": case_info["year"],
                    "核心教训": case_info["core_lesson"],
                    "现代映射": case_info["modern_mapping"],
                    "相关度": "中"
                })

        return analogies[:3]  # 最多返回3个案例

    def anti_dogma_check(self, analysis_result: Dict) -> Dict[str, Any]:
        """反教条自检 - 检查分析是否存在教条主义倾向"""
        warnings = []
        passed = []

        for check_name, check_desc in ANTI_DOGMA_CHECKLIST:
            # 简单的启发式检查
            result_text = json.dumps(analysis_result, ensure_ascii=False)

            if check_name == "具体化检查":
                if len(result_text) < 200:
                    warnings.append(f"[{check_name}] 分析过于简略，可能缺乏具体化")
                else:
                    passed.append(f"[{check_name}] 通过")
            elif check_name == "反面检查":
                if "风险" not in result_text and "局限" not in result_text and "误用" not in result_text:
                    warnings.append(f"[{check_name}] 未包含反面思考或风险提示")
                else:
                    passed.append(f"[{check_name}] 通过")
            elif check_name == "操作性检查":
                if "行动" in result_text or "步骤" in result_text or "建议" in result_text:
                    passed.append(f"[{check_name}] 通过")
                else:
                    warnings.append(f"[{check_name}] 缺乏可操作的行动建议")
            else:
                passed.append(f"[{check_name}] 通过（需人工确认）")

        return {
            "检查结果": "通过" if not warnings else "需关注",
            "通过项": passed,
            "警告项": warnings,
            "改进建议": [f"建议人工复核：{w}" for w in warnings]
        }

    def analyze_problem(self, problem_description: str) -> Dict[str, Any]:
        """分析问题中的矛盾 - v2.0（场景识别+案例类比+反教条自检）"""

        # Step 1: 场景识别
        scenario_recs = self.identify_scenario(problem_description)
        primary_scenario = scenario_recs[0]["场景"] if scenario_recs else "复杂问题"

        # Step 2: 识别矛盾要素
        contradictions = self._identify_contradictions(problem_description)

        # Step 3: 确定主要矛盾
        main_contradiction = self._determine_main_contradiction(contradictions)

        # Step 4: 矛盾转化分析
        transformation = self._analyze_transformation(contradictions)

        # Step 5: 军事战略应用
        military_strategy = self._apply_military_strategy(contradictions, main_contradiction)

        # Step 6: 统一战线构建
        united_front_plan = self._build_united_front(contradictions)

        # Step 7: 历史案例类比（新增）
        historical_analogies = self.find_historical_analogy(problem_description, primary_scenario)

        # Step 8: 生成解决建议
        solutions = self._generate_solutions(contradictions, main_contradiction)

        # 构建初步分析结果
        result = {
            "问题描述": problem_description,
            "场景识别": scenario_recs,
            "矛盾识别": contradictions,
            "主要矛盾": main_contradiction,
            "矛盾转化分析": transformation,
            "军事战略应用": military_strategy,
            "统一战线构建": united_front_plan,
            "历史案例类比": historical_analogies,
            "解决建议": solutions,
            "综合解决方案": self._generate_comprehensive_solution(
                contradictions, main_contradiction, primary_scenario, historical_analogies
            )
        }

        # Step 9: 反教条自检（新增）
        result["反教条自检"] = self.anti_dogma_check(result)

        return result

    # --- 以下为内部方法（与v1相同，略作精简）---

    def _identify_contradictions(self, problem: str) -> List[Dict]:
        contradictions = []
        contradiction_keywords = {
            "资源有限": "需求与资源的矛盾",
            "时间紧张": "任务与时间的矛盾",
            "意见分歧": "不同观点的矛盾",
            "利益冲突": "利益分配的矛盾",
            "目标冲突": "不同目标的矛盾",
            "竞争": "竞争与合作的矛盾",
            "危机": "生存与发展的矛盾",
            "效率低": "目标与能力的矛盾",
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
        if not contradictions:
            return {"类型": "未识别到明显矛盾", "说明": "需要更多信息进行分析"}
        priority_keywords = ["资源", "时间", "利益", "目标", "生存", "竞争"]
        for keyword in priority_keywords:
            for c in contradictions:
                if keyword in c["类型"]:
                    return {"主要矛盾": c["类型"], "判断依据": f"{keyword}相关矛盾通常是主要矛盾", "解决优先级": "高"}
        return {"主要矛盾": contradictions[0]["类型"], "判断依据": "按出现顺序确定", "解决优先级": "中"}

    def _analyze_transformation(self, contradictions: List[Dict]) -> Dict:
        return {"转化规律": "矛盾在一定条件下可以相互转化", "转化条件": "需要创造适当的条件", "转化方向": "次要矛盾可能转化为主要矛盾"}

    def _apply_military_strategy(self, contradictions: List[Dict], main_contradiction: Dict) -> Dict[str, Any]:
        strategies = []
        ct = main_contradiction.get("主要矛盾", "")
        if "复杂" in ct or "多个" in ct:
            strategies.append({"战略": "集中优势兵力，各个歼灭敌人", "应用": "将复杂问题分解，逐个击破"})
        if "困难" in ct or "挑战" in ct:
            strategies.append({"战略": "你打你的，我打我的", "应用": "保持战略主动，发挥自身优势"})
        if "紧迫" in ct or "紧急" in ct or "时间" in ct:
            strategies.append({"战略": "不打无准备之仗", "应用": "充分准备，确保行动成功"})
        if not strategies:
            strategies.append({"战略": "保存自己，消灭敌人", "应用": "在保护自身的同时解决问题"})
        return {"适用战略": strategies, "战略原则": "战略上藐视困难，战术上重视细节"}

    def _build_united_front(self, contradictions: List[Dict]) -> Dict[str, Any]:
        return {"统一战线原则": "团结一切可以团结的力量", "构建策略": ["识别共同利益，建立合作基础", "争取中间力量，扩大同盟范围", "分化主要对手，减少敌对力量"]}

    def _generate_solutions(self, contradictions: List[Dict], main_contradiction: Dict) -> List[str]:
        solutions = ["抓住主要矛盾，集中力量解决", "创造条件，促进矛盾向有利方向转化", "统筹兼顾，处理好次要矛盾"]
        ct = main_contradiction.get("主要矛盾", "")
        if "资源" in ct:
            solutions.extend(["优化资源配置，提高利用效率", "采用'集中优势兵力'原则，优先保障关键资源"])
        elif "时间" in ct:
            solutions.extend(["科学安排时间，分清轻重缓急", "实施'不打无准备之仗'原则"])
        elif "利益" in ct:
            solutions.extend(["平衡各方利益，寻求共赢方案", "运用统一战线原则，团结多数"])
        return solutions

    def _generate_comprehensive_solution(self, contradictions: List[Dict], main_contradiction: Dict,
                                         scenario: str, analogies: List[Dict]) -> Dict[str, Any]:
        analogy_text = ""
        if analogies:
            top_analogy = analogies[0]
            analogy_text = f"参考历史案例：{top_analogy['案例名称']}（{top_analogy['时间']}）— {top_analogy['核心教训']}"

        return {
            "解决思路": "运用毛主席思想的综合方法论",
            "场景建议": scenario,
            "核心原则": ["实事求是：从实际出发分析问题", "矛盾论：抓住主要矛盾，促进矛盾转化", "实践论：方案验证，持续迭代"],
            "实施步骤": [
                "第一步：深入调查研究，掌握实际情况",
                "第二步：分析主要矛盾，确定解决方向",
                "第三步：制定具体方案，明确行动路径",
                "第四步：小规模试点验证，及时调整优化",
                "第五步：逐步推广，在实践中不断完善"
            ],
            "历史启示": analogy_text,
            "注意事项": "本分析基于方法论框架，具体执行需结合实际情况灵活调整。避免机械套用方法论——实事求是是第一原则。"
        }


def main():
    """测试函数"""
    analyzer = ContradictionAnalyzer()

    test_problems = [
        "我的创业公司面对大厂竞争，资源不够，应该怎么制定竞争策略？",
        "团队内部意见分歧大，效率低下，项目时间紧张",
        "公司需要转型创新，但内部阻力很大",
        "需要说服其他部门配合我们的新方案推广"
    ]

    for problem in test_problems:
        print(f"\n{'='*60}")
        print(f"问题: {problem}")
        print('='*60)
        result = analyzer.analyze_problem(problem)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
