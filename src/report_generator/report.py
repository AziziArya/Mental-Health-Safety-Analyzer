class SafetyReportGenerator:

    def generate(self, fusion_result):

        report = {
            "system": "Mental Health Safety Analyzer",

            "risk_assessment": {
                "level": fusion_result.get("risk_level"),
                "score": fusion_result.get("final_risk_score"),
                "confidence": fusion_result.get("confidence")
            },

            "detected_factors": {
                "emotion_score": fusion_result.get("emotion_score"),
                "distress_score": fusion_result.get("distress_score"),
                "crisis_score": fusion_result.get("crisis_score")
            },

            "reasons": fusion_result.get("reasons", []),

            "recommended_action":
                fusion_result.get("recommended_action"),

            "safety_note":
                "This system provides risk assessment support and does not provide medical diagnosis."
        }

        return report