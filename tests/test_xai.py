from src.explainability.xai import ExplainabilityEngine


engine = ExplainabilityEngine()


decision = {

    "final_risk_score": 0.65,

    "final_risk_level": "High Risk",

    "signals": {

        "crisis_signal": True,

        "emotional_escalation": True,

        "conversation_deterioration": True,

        "history_increase": True,

        "context_risk_high": True

    },

    "decision_reasons": [

        "Crisis-related language detected"

    ]

}



result = engine.explain(
    decision
)


print("\n=== XAI RESULT ===")

print(result)


assert "summary" in result

assert "key_factors" in result


print("\nXAI TEST PASSED")