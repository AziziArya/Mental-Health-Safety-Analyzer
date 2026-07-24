from typing import Dict, List


class FinalDecisionEngine:
    """
    Final safety decision layer.

    Combines all conversation signals
    and produces final safety decision.

    This module does not diagnose.
    It only estimates safety priority.
    """

    def __init__(self):

        self.levels = {
            "Safe": 0.0,
            "Mild Concern": 0.2,
            "Moderate Risk": 0.4,
            "High Risk": 0.6,
            "Critical Emergency": 0.8,
        }

    def _calculate_final_score(self, base_risk: Dict, context_fusion: Dict) -> float:

        base_score = base_risk.get("score", 0)

        context_score = context_fusion.get("contextual_risk_score", 0)

        # Context has priority over single message

        score = base_score * 0.4 + context_score * 0.6

        return round(min(score, 1.0), 4)

    def _detect_level(self, score: float) -> str:

        if score >= 0.80:

            return "Critical Emergency"

        elif score >= 0.60:

            return "High Risk"

        elif score >= 0.40:

            return "Moderate Risk"

        elif score >= 0.20:

            return "Mild Concern"

        return "Safe"

    def _generate_reasons(
        self, emotion: Dict, patterns: Dict, memory: Dict, base_risk: Dict
    ) -> List[str]:

        reasons = []

        if base_risk.get("score", 0) >= 0.6:

            reasons.append("High individual message risk detected")

        if emotion.get("escalation_detected", False):

            reasons.append("Negative emotional escalation detected")

        if patterns.get("conversation_escalation", {}).get(
            "escalation_detected", False
        ):

            reasons.append("Conversation deterioration pattern detected")

        if memory.get("trend") == "Risk Increasing":

            reasons.append("Risk increased across conversation history")

        if patterns.get("crisis_language_score", 0) > 0:

            reasons.append("Crisis-related language detected")

        return reasons

    def _recommended_action(self, level: str) -> str:

        if level == "Critical Emergency":

            return "Immediate human review required"

        if level == "High Risk":

            return "Priority safety monitoring required"

        if level == "Moderate Risk":

            return "Continue supportive monitoring"

        if level == "Mild Concern":

            return "Provide supportive response"

        return "No immediate safety action required"

    def decide(
        self,
        base_risk: Dict,
        context_fusion: Dict,
        emotion_evolution: Dict = None,
        conversation_patterns: Dict = None,
        memory_context: Dict = None,
    ) -> Dict:

        emotion_evolution = emotion_evolution or {}

        conversation_patterns = conversation_patterns or {}

        memory_context = memory_context or {}

        final_score = self._calculate_final_score(base_risk, context_fusion)

        final_level = self._detect_level(final_score)

        reasons = self._generate_reasons(
            emotion_evolution, conversation_patterns, memory_context, base_risk
        )

        return {
            "final_risk_score": final_score,
            "final_risk_level": final_level,
            "decision_reasons": reasons,
            "recommended_action": self._recommended_action(final_level),
        }
