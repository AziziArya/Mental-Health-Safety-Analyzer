from src.report_generator.report import SafetyReportGenerator


fusion_result = {
    "risk_level": "Critical Emergency",
    "final_risk_score": 0.7415,
    "confidence": 0.9503,
    "emotion_score": 0.9503,
    "distress_score": 0.3883,
    "crisis_score": 0.92,
    "recommended_action": "Immediate human review required",
    "reasons": [
        "Strong sadness detected (0.84)",
        "Elevated distress score (0.39)",
        "High crisis probability (0.92)",
        "Explicit high-risk phrase: i don't want to live"
    ]
}


generator = SafetyReportGenerator()

report = generator.generate(fusion_result)


print("=== SAFETY REPORT ===")

for key, value in report.items():
    print(key, ":", value)