from src.decision_engine.decision import DecisionEngine

engine = DecisionEngine()


base_risk = {"level": "Critical Emergency", "score": 0.66, "confidence": 0.92}


context_fusion = {
    "contextual_risk_score": 0.64,
    "contextual_risk_level": "High Risk",
    "emotion_context_score": 1.0,
    "pattern_context_score": 0.41,
    "memory_context_score": 0.28,
}


emotion_evolution = {
    "emotion_trend": "Negative Escalation",
    "escalation_detected": True,
    "safety_emotion_score": 0.92,
}


conversation_patterns = {
    "crisis_language_score": 0.33,
    "conversation_escalation": {"escalation_detected": True},
}


memory_context = {"risk_change": 0.28, "trend": "Risk Increasing"}


result = engine.decide(
    base_risk=base_risk,
    context_fusion=context_fusion,
    emotion_evolution=emotion_evolution,
    conversation_patterns=conversation_patterns,
    memory_context=memory_context,
)


print("\n=== DECISION ENGINE TEST ===")

print(result)


assert "final_risk_score" in result

assert "final_risk_level" in result

assert "recommended_actions" in result

assert isinstance(result["recommended_actions"], list)

assert len(result["recommended_actions"]) > 0


print("\nDECISION TEST PASSED")
