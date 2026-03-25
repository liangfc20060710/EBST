import json
import time
from datetime import datetime
from typing import Dict, List, Any
import random

# 导入所有智能体模块
from cfo_agent import CFOAgent
from coo_agent import COOAgent
from cto_agent import CTOAgent


class BusinessContext:
    """企业上下文数据 - 包含所有业务数据"""

    def __init__(self):
        # 财务数据
        self.financial_data = {
            "revenue": 1500000,
            "cost": 1200000,
            "profit": 300000,
            "cash_flow": 500000,
            "profit_margin": 20.0,
            "accounts_receivable": 200000,
            "accounts_payable": 150000,
            "inventory_value": 800000
        }

        # 运营数据
        self.operational_data = {
            "inventory_turnover": 12.5,
            "supplier_count": 45,
            "supplier_on_time_rate": 92.0,
            "purchase_cost": 500000,
            "logistics_cost": 80000,
            "production_efficiency": 87.0,
            "capacity_utilization": 78.0,
            "defect_rate": 2.5,
            "equipment_oee": 85.0,
            "order_fulfillment_rate": 95.0,
            "order_lead_time": 7,
            "return_rate": 3.2,
            "employee_count": 280,
            "productivity_per_employee": 5300,
            "overtime_hours": 450,
            "turnover_rate": 8.5
        }

        # 市场数据
        self.market_data = {
            "customer_satisfaction": 4.2,
            "market_share": 15.8,
            "competitor_count": 8,
            "growth_rate": 25.0
        }

        # 技术数据
        self.technical_data = {
            "system_count": 24,
            "microservice_count": 18,
            "api_count": 156,
            "server_count": 35,
            "debt_score": 65,
            "legacy_system_count": 6,
            "code_smell_count": 45,
            "bug_count": 12,
            "deployment_frequency": 12,
            "lead_time": 3.5,
            "test_coverage": 78.5,
            "review_efficiency": 85.0,
            "avg_response_time": 120,
            "system_uptime": 99.5,
            "error_rate": 0.5,
            "throughput": 1500,
            "rd_budget": 300000,
            "rd_team_size": 25,
            "rd_project_count": 8
        }

        # 风险数据
        self.risk_data = {
            "financial_risk": "中",
            "supply_risk": "低",
            "market_risk": "中",
            "tech_risk": "中"
        }

    def to_dict(self) -> Dict[str, Any]\

        :
    """转换为标准格式 - 供所有智能体使用"""
    return {
        "financial": self.financial_data,
        "operational": self.operational_data,
        "market": self.market_data,
        "technical": self.technical_data,
        "risk": self.risk_data,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def update_random(self):
    """模拟数据变化"""
    # 财务数据波动
    self.financial_data['revenue'] *= random.uniform(0.95, 1.05)
    self.financial_data['profit_margin'] += random.uniform(-1, 1)

    # 运营数据波动
    self.operational_data['production_efficiency'] += random.uniform(-2, 2)
    self.operational_data['defect_rate'] += random.uniform(-0.3, 0.3)

    # 技术数据波动
    self.technical_data['debt_score'] += random.uniform(-2, 2)
    self.technical_data['avg_response_time'] += random.uniform(-10, 10)


class ExecutiveTeam:
    """
    高管团队指挥中心
    整合CEO、CFO、COO、CTO四大智能体，实现多智能体协作决策
    """

    def __init__(self):
        print("🚀 正在初始化企业数字大脑系统...")

        # 初始化所有智能体
        self.ceo = CEOAgent()  # 总指挥
        self.cfo = CFOAgent()  # 财务专家
        self.coo = COOAgent()  # 运营专家
        self.cto = CTOAgent()  # 技术专家

        # 企业数据上下文
        self.context = BusinessContext()

        # 决策历史
        self.decision_history = []

        print("✅ 高管团队智能体初始化完成！")
        print(f"   👑 CEO: {self.ceo.name}")
        print(f"   💰 CFO: {self.cfo.name}")
        print(f"   ⚙️ COO: {self.coo.name}")
        print(f"   💻 CTO: {self.cto.name}")
        print("=" * 60)

    def execute_monthly_review(self):
        """
        月度经营分析会
        模拟企业每月的高管会议
        """
        print("\n" + "=" * 60)
        print("📅 月度经营分析会启动")
        print("=" * 60)

        # CEO开场
        print(f"\n👑 {self.ceo.name}：'各位，开始月度复盘！'")

        # 1. CFO财务汇报
        print(f"\n💰 {self.cfo.name}：'下面是财务分析...'")
        financial_report = self.cfo.analyze_financial_health(self.context.to_dict())
        time.sleep(1)

        # 2. COO运营汇报
        print(f"\n⚙️ {self.coo.name}：'运营状况如下...'")
        operational_report = self.coo.analyze_operations(self.context.to_dict())
        time.sleep(1)

        # 3. CTO技术汇报
        print(f"\n💻 {self.cto.name}：'技术架构评估...'")
        technical_report = self.cto.analyze_technology(self.context.to_dict())
        time.sleep(1)
        # 4. CEO综合决策
        print(f"\n👑 {self.ceo.name}：'基于各部门汇报，我做如下决策...'")
        decision = self.ceo._synthesize_decision_v2(
            financial_report, operational_report, technical_report
        )

        # 5. 决策执行
        self.ceo.execute(decision)

        # 记录历史
        self.decision_history.append({
            "时间": datetime.now().isoformat(),
            "财务报告": financial_report,
            "运营报告": operational_report,
            "技术报告": technical_report,
            "决策": decision
        })

        return {
            "财务报告": financial_report,
            "运营报告": operational_report,
            "技术报告": technical_report,
            "决策": decision
        }

    def crisis_simulation(self, crisis_type: str):
        """
        危机模拟处理
        测试智能体在突发情况下的协作能力
        """
        print("\n" + "=" * 60)
        print(f"🚨 危机模拟启动: {crisis_type}")
        print("=" * 60)

        # 模拟危机数据
        if crisis_type == "供应链中断":
            self.context.operational_data['supplier_on_time_rate'] = 45
            self.context.operational_data['order_fulfillment_rate'] = 60
            print("   ⚠️ 主要供应商工厂停工，交付受到严重影响")

        elif crisis_type == "财务危机":
            self.context.financial_data['cash_flow'] = 50000
            self.context.financial_data['profit_margin'] = 5
            print("   ⚠️ 现金流严重不足，利润率骤降至5%")

        elif crisis_type == "技术故障":
            self.context.technical_data['system_uptime'] = 85
            self.context.technical_data['error_rate'] = 8
            print("   ⚠️ 核心系统故障，可用性降至85%")

        # CEO紧急决策
        print(f"\n👑 {self.ceo.name}：'启动应急预案！'")
        decision = self.ceo.make_decision(self.context)

        return decision

    def get_dashboard(self) -> Dict[str, Any]\

        :
    """
    企业运营仪表盘
    汇总各智能体关键指标
    """
    print("\n" + "=" * 60)
    print("📊 企业运营仪表盘")
    print("=" * 60)

    # 获取最新数据
    context = self.context.to_dict()

    # 各维度健康度
    dashboard = {
        "时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "财务健康": {
            "利润率": f"{context['financial']['profit_margin']\:.1f}%",
            "现金流": f"{context['financial']['cash_flow']\:,.0f}元",
            "状态": "良好" if context['financial']['profit_margin'] > 15 else "预警"
        },
        "运营健康": {
            "生产效率": f"{context['operational']['production_efficiency']\:.1f}%",
            "交付满足率": f"{context['operational']['order_fulfillment_rate']\:.1f}%",
            "状态": "良好" if context['operational']['production_efficiency'] > 85 else "预警"
        },
        "技术健康": {
            "系统可用性": f"{context['technical']['system_uptime']\:.1f}%",
            "债务评分": context['technical']['debt_score'],
            "状态": "良好" if context['technical']['system_uptime'] > 99 else "预警"
        },
        "风险提示": self._aggregate_risks()
    }

    print(f"\n📈 财务健康: {dashboard['财务健康']['状态']} (利润率{dashboard['财务健康']['利润率']})")
    print(f"⚙️ 运营健康: {dashboard['运营健康']['状态']} (效率{dashboard['运营健康']['生产效率']})")
    print(f"💻 技术健康: {dashboard['技术健康']['状态']} (可用性{dashboard['技术健康']['系统可用性']})")

    return dashboard

    def _aggregate_risks(self) -> List[str]\

        :
    """汇总各智能体识别的风险"""
    risks = []

    # CFO风险
    if self.context.financial_data['profit_margin'] < 10:
        risks.append("财务风险：利润率偏低")

    # COO风险
    if self.context.operational_data['defect_rate'] > 3:
        risks.append("运营风险：产品质量问题")

    # CTO风险
    if self.context.technical_data['system_uptime'] < 99:
        risks.append("技术风险：系统稳定性不足")

    return risks if risks else ["暂无重大风险"]

    def strategic_planning(self, quarters: int = 4):
        """
    战略规划
    制定未来几个季度的战略计划
    """
        print("\n" + "=" * 60)
        print(f"🎯 战略规划启动 (未来{quarters}个季度)")
        print("=" * 60)

        # 各智能体提供专业建议
        context = self.context.to_dict()

        print("\n1️⃣ 财务规划建议：")
        financial_recs = self.cfo._generate_recommendations(
            self.cfo.financial_ratios,
            [{"风险等级": "中", "风险类型": "盈利风险"}]
        )
        for rec in financial_recs:
            print(f"   • {rec}")

        print("\n2️⃣ 运营规划建议：")
        operational_recs = self.coo._generate_operational_recommendations(
            {"综合得分": 70, "等级": "一般"},
            [{"等级": "中", "风险类型": "效率风险"}],
            context
        )
        for rec in operational_recs:
            print(f"   • {rec}")

        print("\n3️⃣ 技术规划建议：")
        tech_recs = self.cto._generate_investment_recommendations(
            {"综合得分": 70, "等级": "一般"},
            [{"等级": "中", "风险类型": "技术债务"}]
        )
        for rec in tech_recs:
            print(f"   • {rec}")

        # CEO综合决策
        print(f"\n👑 {self.ceo.name}：'基于各部门规划，制定以下战略...'")

        strategy = {
            "目标": "提升企业整体运营效率20%",
            "Q1": "财务优化和成本控制",
            "Q2": "运营流程再造和自动化",
            "Q3": "技术架构升级和中台建设",
            "Q4": "全面数字化转型评估"
        }

        for k, v in strategy.items():
            if k != "目标":
                print(f"   {k}: {v}")

        return strategy

        class CEOAgent:
            """CEO智能体（精简版，用于整合）"""

            def __init__(self, name: str = "CEO智能体"):
                self.name = name
                self.role = "企业战略决策总指挥"
                self.memory = []

            def _synthesize_decision_v2(self, financial_report, operational_report, technical_report):
                """综合各智能体报告，形成最终决策"""
                print(f"\n{'=' * 60}")
                print(f"🎯 {self.name} 综合决策中...")
                print(f"{'=' * 60}")

                # 提取关键指标
                finance_score = financial_report['财务健康度评分']['综合评分']
                op_score = operational_report['综合运营评分']['综合得分']
                tech_score = technical_report['综合技术评分']['综合得分']

                print(f"\n📊 各部门评分：")
                print(f"   💰 CFO: {finance_score}分 ({financial_report['财务健康度评分']['健康等级']})")
                print(f"   ⚙️ COO: {op_score}分 ({operational_report['综合运营评分']['等级']})")
                print(f"   💻 CTO: {tech_score}分 ({technical_report['综合技术评分']['等级']})")

                # 战略决策逻辑
                if finance_score < 60:
                    strategy = "紧急财务优化，控制成本，提升现金流"
                    priority = "财务"
                elif op_score < 60:
                    strategy = "运营流程再造，提升生产效率"
                    priority = "运营"
                elif tech_score < 60:
                    strategy = "技术架构升级，偿还技术债务"
                    priority = "技术"
                else:
                    strategy = "整体运营良好，适度扩张市场份额"
                    priority = "市场"

                # 汇总各部门关键建议
                key_recommendations = []

                # CFO建议
                for rec in financial_report['建议措施'][:2]\:
                    key_recommendations.append(f"【财务】{rec}")

                # COO建议
                for rec in operational_report['核心建议'][:2]\:
                    key_recommendations.append(f"【运营】{rec}")

                # CTO建议
                for rec in technical_report['技术投资建议'][:2]\:
                    key_recommendations.append(f"【技术】{rec}")

                decision = {
                    "战略目标": strategy,
                    "优先领域": priority,
                    "财务健康评分": finance_score,
                    "运营健康评分": op_score,
                    "技术健康评分": tech_score,
                    "核心建议": key_recommendations,
                    "执行步骤": [
                        f"1. 立即启动{priority}优化专项",
                        "2. 每周召开执行进度会议",
                        "3. 建立KPI监控体系",
                        "4. 月度复盘调整策略",
                        "5. 季度评估整体效果"
                    ],
                    "关键KPI": f"{priority}健康评分提升20%",
                    "预期效果": "3个月内企业整体运营效率提升15%"
                }

                print(f"\n📋 最终战略决策：")
                print(f"🎯 核心目标: {strategy}")
                print(f"📊 优先领域: {priority}")
                print(f"\n💡 核心建议:")
                for i, rec in enumerate(key_recommendations[:4], 1):
                    print(f"   {i}. {rec}")

                return decision

            def make_decision(self, context: BusinessContext):
                """CEO决策入口"""
                # 这里简化处理，实际会调用更复杂的逻辑
                return self._synthesize_decision_v2(
                    {"财务健康度评分": {"综合评分": 70, "健康等级": "良好"}, "建议措施": []},
                    {"综合运营评分": {"综合得分": 75, "等级": "良好"}, "核心建议": []},
                    {"综合技术评分": {"综合得分": 72, "等级": "良好"}, "技术投资建议": []}
                )

            def execute(self, decision: Dict):
                """执行决策"""
                print(f"\n{'=' * 60}")
                print(f"⚡ {self.name} 开始执行决策...")
                print(f"{'=' * 60}")

                print(f"战略目标：{decision['战略目标']}")
                print("\n执行计划：")
                for step in decision['执行步骤']\:
                    print(f"   → {step}")

                print(f"\n✅ 决策执行启动完成！")
                print(f"📊 目标: {decision['关键KPI']}")
                print(f"📈 预期: {decision['预期效果']}")

        def main_menu():
            """主菜单 - 演示完整系统功能"""
            print("=" * 70)
            print("🧠 企业数字大脑系统 - 多智能体协作指挥中心")
            print("=" * 70)

            # 创建指挥中心
            team = ExecutiveTeam()

            while True:
                print("\n" + "=" * 70)
                print("请选择操作模式：")
                print("1. 📅 月度经营分析会（完整流程）")
                print("2. 🚨 危机模拟处理")
                print("3. 📊 企业运营仪表盘")
                print("4. 🎯 战略规划")
                print("5. 🔄 刷新数据（模拟新数据）")
                print("6. 💰 CFO独立分析")
                print("7. ⚙️ COO独立分析")
                print("8. 💻 CTO独立分析")
                print("0. ❌ 退出系统")
                print("=" * 70)

                choice = input("\n请输入选项编号：").strip()

                if choice == "1":
                    print("\n🎬 启动月度经营分析会...")
                    result = team.execute_monthly_review()

                elif choice == "2":
                    print("\n🎬 启动危机模拟...")
                    print("可选危机类型：")
                    print("   1. 供应链中断")
                    print("   2. 财务危机")
                    print("   3. 技术故障")
                    crisis_choice = input("请选择危机类型（1-3）：").strip()

                    crisis_types = ["", "供应链中断", "财务危机", "技术故障"]
                    if 1 <= int(crisis_choice) <= 3:
                        team.crisis_simulation(crisis_types[int(crisis_choice)])
                    else:
                        print("❌ 无效的危机类型")
                        elif choice == "3":
                        team.get_dashboard()

                    elif choice == "4":
                    team.strategic_planning()

                elif choice == "5":
                    print("\n🔄 正在刷新企业数据...")
                    team.context.update_random()
                    print("✅ 数据刷新完成！")
                    dashboard = team.get_dashboard()

                elif choice == "6":
                    print("\n💰 CFO财务智能体独立分析...")
                    report = team.cfo.analyze_financial_health(team.context.to_dict())

                elif choice == "7":
                    print("\n⚙️ COO运营智能体独立分析...")
                    report = team.coo.analyze_operations(team.context.to_dict())

                elif choice == "8":
                    print("\n💻 CTO技术智能体独立分析...")
                    report = team.cto.analyze_technology(team.context.to_dict())

                elif choice == "0":
                    print("\n👋 感谢使用企业数字大脑系统！")
                    break

                else:
                    print("❌ 无效的选项，请重新输入！")

                if __name__ == "__main__":
                    main_menu()




