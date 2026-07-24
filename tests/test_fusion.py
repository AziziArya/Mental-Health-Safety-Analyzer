from src.fusion_engine.fusion import FusionEngine

fusion = FusionEngine()

emotion_result = [
    {"emotion": "sadness", "score": 0.8443},
    {"emotion": "disappointment", "score": 0.2119},
]

distress_result = {
    "distress_score": 0.3883,
}

crisis_result = {
    "crisis_probability": 0.92,
    "matched_high_risk_patterns": ["i don't want to live"],
    "matched_medium_risk_patterns": [],
}

result = fusion.analyze(emotion_result, distress_result, crisis_result)

print("=== FUSION RESULT ===")
for key, value in result.items():
    print(f"{key}: {value}")
