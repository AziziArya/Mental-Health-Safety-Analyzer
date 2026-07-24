from src.decision_engine.decision import DecisionEngine

engine = DecisionEngine()


def run_case(name, base, fusion, expected):

    result = engine.decide(base_risk=base, context_fusion=fusion)

    print("\n====================")
    print(name)
    print("====================")

    print(result)

    assert result["final_risk_level"] == expected


# 1) Safe case

run_case(
    "SAFE CASE",
    {"score": 0.05, "level": "Safe"},
    {"contextual_risk_score": 0.05},
    "Safe",
)


# 2) Mild concern

run_case(
    "MILD CASE",
    {"score": 0.30, "level": "Mild Concern"},
    {"contextual_risk_score": 0.25},
    "Mild Concern",
)


# 3) Moderate

run_case(
    "MODERATE CASE",
    {"score": 0.50, "level": "Moderate Risk"},
    {"contextual_risk_score": 0.50},
    "Moderate Risk",
)


# 4) Critical

run_case(
    "CRITICAL CASE",
    {"score": 0.90, "level": "Critical Emergency"},
    {"contextual_risk_score": 0.90},
    "Critical Emergency",
)


print("\nALL DECISION SCENARIOS PASSED")
