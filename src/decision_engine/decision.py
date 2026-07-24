from typing import Dict


class DecisionEngine:
    """
    Final safety decision engine.

    Combines:
    - Base risk
    - Context fusion
    - Emotion evolution
    - Conversation patterns
    - Memory history
    - Crisis override

    Does not diagnose.
    Estimates safety priority.
    """

    def __init__(self):

        self.thresholds = {
            "critical": 0.80,
            "high": 0.60,
            "moderate": 0.40,
            "mild": 0.20,
        }

    # =====================================
    # Risk Level
    # =====================================

    def _risk_level(self, score):

        if score >= self.thresholds["critical"]:
            return "Critical Emergency"

        if score >= self.thresholds["high"]:
            return "High Risk"

        if score >= self.thresholds["moderate"]:
            return "Moderate Risk"

        if score >= self.thresholds["mild"]:
            return "Mild Concern"

        return "Safe"

    # =====================================
    # Priority
    # =====================================

    def _priority(self, score):

        if score >= 0.80:
            return "CRITICAL"

        if score >= 0.60:
            return "HIGH"

        if score >= 0.40:
            return "MEDIUM"

        return "LOW"

    # =====================================
    # Signals
    # =====================================

    def _collect_signals(self, context, emotion, patterns, memory, base):

        context = context or {}
        emotion = emotion or {}
        patterns = patterns or {}
        memory = memory or {}
        base = base or {}

        crisis = base.get("crisis", {})

        return {
            "crisis_signal": (
                crisis.get("crisis_probability", 0) >= 0.5
                or patterns.get("crisis_language_score", 0) > 0
            ),
            "critical_crisis": crisis.get("is_emergency", False),
            "emotional_escalation": emotion.get("escalation_detected", False),
            "conversation_deterioration": patterns.get(
                "conversation_escalation", {}
            ).get("escalation_detected", False),
            "history_increase": memory.get("risk_change", 0) > 0.15,
            "context_risk_high": context.get("contextual_risk_score", 0) >= 0.60,
        }

    # =====================================
    # Score Calculation
    # =====================================

    def _calculate_score(self, base, context, signals):

        base_score = base.get("score", 0)

        context_score = context.get("contextual_risk_score", 0)

        # Normal weighted fusion
        score = base_score * 0.55 + context_score * 0.45

        reasoning = []

        # Critical preservation

        if base_score >= 0.80:

            score = max(score, 0.80)

            reasoning.append("High base risk preserved")

        if context_score >= 0.80:

            score = max(score, 0.80)

            reasoning.append("High contextual risk preserved")

        # Crisis overrides

        if signals["crisis_signal"]:

            score = max(score, 0.65)

            reasoning.append("Crisis signal increased risk")

        if signals["critical_crisis"]:

            score = 1.0

            reasoning.append("Critical emergency override")

        if signals["emotional_escalation"]:

            score += 0.05

            reasoning.append("Emotion escalation detected")

        if signals["conversation_deterioration"]:

            score += 0.05

            reasoning.append("Conversation deterioration detected")

        return (round(min(score, 1.0), 4), reasoning)

    # =====================================
    # Actions
    # =====================================

    def _actions(self, level):

        actions = {
            "Critical Emergency": [
                "Immediate safety assessment recommended",
                "Encourage human intervention",
                "Maintain supportive communication",
            ],
            "High Risk": [
                "Priority monitoring required",
                "Increase observation",
                "Provide supportive response",
            ],
            "Moderate Risk": ["Continue monitoring", "Review emotional changes"],
            "Mild Concern": ["Normal supportive monitoring"],
            "Safe": ["No additional action required"],
        }

        return actions.get(level, [])

    # =====================================
    # Main Decision
    # =====================================

    def decide(
        self,
        base_risk: Dict,
        context_fusion: Dict,
        emotion_evolution=None,
        conversation_patterns=None,
        memory_context=None,
    ):

        emotion_evolution = emotion_evolution or {}

        conversation_patterns = conversation_patterns or {}

        memory_context = memory_context or {}

        signals = self._collect_signals(
            context_fusion,
            emotion_evolution,
            conversation_patterns,
            memory_context,
            base_risk,
        )

        score, reasoning = self._calculate_score(base_risk, context_fusion, signals)

        level = self._risk_level(score)

        return {
            "final_risk_score": score,
            "final_risk_level": level,
            "priority": self._priority(score),
            "requires_human_review": score >= 0.60,
            "escalation": any(signals.values()),
            "signals": signals,
            "reasoning_chain": reasoning,
            "decision_reasons": reasoning,
            "recommended_actions": self._actions(level),
        }
