from typing import Any, Dict, List


class XAIEngine:
    """
    Explainability engine.

    Converts internal safety decisions
    into human-readable explanations.

    This module does not diagnose.

    It explains:
    - final risk decision
    - contributing factors
    - model reasoning
    - memory influence
    """

    def __init__(self):
        pass

    # =====================================
    # Risk Summary
    # =====================================

    def _summary(self, level: str, score: float) -> str:

        summaries = {
            "Critical Emergency": (
                "The system detected a critical "
                "safety pattern requiring immediate "
                "attention."
            ),
            "High Risk": (
                "The system detected multiple "
                "elevated safety indicators and "
                "recommends closer monitoring."
            ),
            "Moderate Risk": (
                "The system detected emotional "
                "distress indicators requiring "
                "continued observation."
            ),
            "Mild Concern": ("The system detected mild concern " "signals."),
            "Safe": ("No significant safety risk indicators " "were detected."),
        }

        return summaries.get(level, "Risk assessment completed.")

    # =====================================
    # Signal Explanation
    # =====================================

    def _explain_signals(self, signals: Dict[str, Any]) -> List[Dict[str, Any]]:

        mapping = {
            "crisis_signal": {"factor": "Crisis language", "impact": "High"},
            "critical_crisis": {
                "factor": "Emergency crisis indicator",
                "impact": "Critical",
            },
            "emotional_escalation": {
                "factor": "Negative emotional escalation",
                "impact": "Medium",
            },
            "conversation_deterioration": {
                "factor": "Conversation deterioration",
                "impact": "Medium",
            },
            "history_increase": {"factor": "Risk increase in history", "impact": "Low"},
            "context_risk_high": {"factor": "High contextual risk", "impact": "High"},
        }

        result = []

        for key, value in signals.items():

            if value and key in mapping:

                result.append(
                    {
                        "factor": mapping[key]["factor"],
                        "impact": mapping[key]["impact"],
                        "signal": key,
                        "active": True,
                    }
                )

        return result

    # =====================================
    # Reasoning Chain
    # =====================================

    def _reasoning_chain(self, signals: Dict[str, Any]) -> List[str]:

        chain = []

        rules = {
            "critical_crisis": "Critical crisis indicator increased emergency priority",
            "crisis_signal": "Crisis language increased safety risk",
            "emotional_escalation": "Negative emotional escalation detected",
            "conversation_deterioration": "Conversation deterioration pattern detected",
            "history_increase": "Previous risk history increased concern",
            "context_risk_high": "High contextual safety risk detected",
        }

        for key, text in rules.items():

            if signals.get(key):

                chain.append(text)

        return chain

    # =====================================
    # Generate
    # =====================================

    def generate(
        self, decision: Dict[str, Any], memory_context: Dict[str, Any] = None
    ) -> Dict[str, Any]:

        memory_context = memory_context or {}

        level = decision.get("final_risk_level", "Unknown")

        score = decision.get("final_risk_score", 0)

        signals = decision.get("signals", {})

        reasons = decision.get("decision_reasons", [])

        actions = decision.get("recommended_actions", [])

        signal_analysis = self._explain_signals(signals)

        reasoning = self._reasoning_chain(signals)

        return {
            "risk_level": level,
            "risk_score": score,
            "summary": self._summary(level, score),
            # Old tests compatibility
            "key_factors": signal_analysis,
            "reasons": reasons,
            "recommended_actions": actions,
            "signal_analysis": signal_analysis,
            "model_reasoning": {
                "decision_score": score,
                "active_signals": [key for key, value in signals.items() if value],
                "reasoning_chain": reasoning,
            },
            "memory_influence": {
                "risk_change": memory_context.get("risk_change", 0),
                "trend": memory_context.get("trend", "Unknown"),
                "previous_risk": memory_context.get("previous_risk", "Unknown"),
            },
        }


# =====================================
# Backward Compatibility
# =====================================

# ==================================
# Backward Compatibility Layer
# ==================================


class ExplainabilityEngine(XAIEngine):
    """
    Backward compatible wrapper.

    Old tests and external modules
    can still use ExplainabilityEngine.
    """

    def explain(self, decision, memory_context=None):

        result = self.generate(decision, memory_context)

        # Old test expects key_factors
        result["key_factors"] = result.get("signal_analysis", [])

        return result
