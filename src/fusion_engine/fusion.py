from typing import Any, Dict, List


class FusionEngine:
    """
    Combine emotion, distress, and crisis outputs
    into a final safety decision.

    Supports:
    - Old emotion format:
        [
            {
                "emotion": "sadness",
                "score": 0.8
            }
        ]

    - New emotion format:
        {
            "sadness": 0.8,
            "fear": 0.2
        }
    """

    def __init__(self):

        self.weights = {
            "emotion": 0.25,
            "distress": 0.35,
            "crisis": 0.40,
        }

        self.risk_emotions = {
            "sadness": 1.0,
            "fear": 0.8,
            "anger": 0.6,
            "disappointment": 0.5,
            "grief": 1.0,
            "remorse": 0.7,
            "nervousness": 0.6,
            "hopelessness": 1.0,
            "despair": 1.0,
            "loneliness": 0.8,
        }

    # =====================================
    # Emotion normalization
    # =====================================

    def _normalize_emotions(self, emotions) -> List[Dict[str, Any]]:

        normalized = []

        if not emotions:

            return normalized

        # New format:
        #
        # {
        #   "sadness":0.5,
        #   "fear":0.2
        # }
        #

        if isinstance(emotions, dict):

            for emotion, score in emotions.items():

                normalized.append({"emotion": emotion, "score": float(score)})

            return normalized

        # Old format:
        #
        # [
        #   {
        #       emotion:"sadness",
        #       score:0.5
        #   }
        # ]

        if isinstance(emotions, list):

            for item in emotions:

                if not isinstance(item, dict):

                    continue

                normalized.append(
                    {
                        "emotion": item.get("emotion", ""),
                        "score": float(item.get("score", 0)),
                    }
                )

        return normalized

    # =====================================
    # Emotion score
    # =====================================

    def _compute_emotion_score(self, emotions) -> float:

        emotions = self._normalize_emotions(emotions)

        score = 0.0

        for item in emotions:

            emotion = item["emotion"]

            probability = item["score"]

            score += probability * self.risk_emotions.get(emotion.lower(), 0.0)

        return min(score, 1.0)

    # =====================================
    # Risk level
    # =====================================

    def _determine_risk_level(self, score) -> str:

        if score < 0.20:

            return "Safe"

        elif score < 0.40:

            return "Mild Concern"

        elif score < 0.60:

            return "Moderate Risk"

        elif score < 0.80:

            return "High Risk"

        return "Critical Emergency"

    # =====================================
    # Reasons
    # =====================================

    def _build_reasons(self, emotions, distress, crisis):

        reasons = []

        emotions = self._normalize_emotions(emotions)

        for item in emotions[:3]:

            if item["score"] >= 0.5:

                reasons.append(
                    f"Strong {item['emotion']} detected " f"({item['score']:.2f})"
                )

        if distress.get("distress_score", 0) >= 0.30:

            reasons.append(
                f"Elevated distress score " f"({distress['distress_score']:.2f})"
            )

        if crisis.get("crisis_probability", 0) >= 0.80:

            reasons.append(
                f"High crisis probability " f"({crisis['crisis_probability']:.2f})"
            )

        for pattern in crisis.get("matched_high_risk_patterns", []):

            reasons.append(f"Explicit high-risk phrase: '{pattern}'")

        for pattern in crisis.get("matched_medium_risk_patterns", []):

            reasons.append(f"Concerning phrase: '{pattern}'")

        return reasons if reasons else ["No significant risk indicators detected"]

    # =====================================
    # Main analysis
    # =====================================

    def analyze(
        self, emotion_result, distress_result, crisis_result
    ) -> Dict[str, object]:

        emotion_score = self._compute_emotion_score(emotion_result)

        distress_score = float(distress_result.get("distress_score", 0))

        crisis_score = float(crisis_result.get("crisis_probability", 0))

        final_score = (
            emotion_score * self.weights["emotion"]
            + distress_score * self.weights["distress"]
            + crisis_score * self.weights["crisis"]
        )

        final_score = round(min(final_score, 1.0), 4)

        risk_level = self._determine_risk_level(final_score)

        # Crisis override

        if crisis_score >= 0.90 and crisis_result.get("matched_high_risk_patterns"):

            risk_level = "Critical Emergency"

        confidence = round(max(emotion_score, distress_score, crisis_score), 4)

        return {
            "risk_level": risk_level,
            "final_risk_score": final_score,
            "confidence": confidence,
            "emotion_score": round(emotion_score, 4),
            "distress_score": round(distress_score, 4),
            "crisis_score": round(crisis_score, 4),
            "recommended_action": self._recommended_action(risk_level),
            "reasons": self._build_reasons(
                emotion_result, distress_result, crisis_result
            ),
        }

    def _recommended_action(self, risk_level):

        actions = {
            "Critical Emergency": "Immediate human review required",
            "High Risk": "Urgent human review recommended",
            "Moderate Risk": "Continue monitoring and review if symptoms escalate",
            "Mild Concern": "Monitor conversation for changes",
            "Safe": "No immediate action required",
        }

        return actions.get(risk_level, "Monitor conversation")
