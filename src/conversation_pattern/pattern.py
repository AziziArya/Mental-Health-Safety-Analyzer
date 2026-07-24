from typing import Dict, List


class ConversationPatternAnalyzer:
    """
    Analyze conversation-level psychological patterns.

    Detects:
    - Social isolation
    - Hopelessness
    - Negative language
    - Escalation patterns
    - Emotional deterioration

    This module does not diagnose.
    It provides conversation risk signals.
    """

    def __init__(self):

        self.isolation_keywords = [
            "alone",
            "lonely",
            "nobody understands",
            "no one understands",
            "nobody cares",
            "no one cares",
        ]

        self.hopelessness_keywords = [
            "hopeless",
            "nothing will change",
            "no future",
            "cannot continue",
            "there is no hope",
            "give up",
            "pointless",
        ]

        self.negative_keywords = [
            "sad",
            "depressed",
            "empty",
            "tired",
            "broken",
            "lost",
            "worthless",
        ]

        self.crisis_keywords = [
            "don't want to live",
            "do not want to live",
            "want to die",
            "kill myself",
            "end my life",
        ]

    def _contains_pattern(self, text: str, keywords: List[str]) -> bool:

        text = text.lower()

        for keyword in keywords:

            if keyword in text:
                return True

        return False

    def _count_patterns(self, messages: List[str], keywords: List[str]) -> int:

        count = 0

        for message in messages:

            if self._contains_pattern(message, keywords):

                count += 1

        return count

    def _detect_escalation(self, messages: List[str]) -> Dict:

        stages = []

        for message in messages:

            text = message.lower()

            if self._contains_pattern(text, self.negative_keywords):
                stages.append("negative_emotion")

            if self._contains_pattern(text, self.isolation_keywords):
                stages.append("social_isolation")

            if self._contains_pattern(text, self.hopelessness_keywords):
                stages.append("hopelessness")

            if self._contains_pattern(text, self.crisis_keywords):
                stages.append("crisis_signal")

        escalation = False

        if (
            ("negative_emotion" in stages and "social_isolation" in stages)
            or ("negative_emotion" in stages and "hopelessness" in stages)
            or ("social_isolation" in stages and "hopelessness" in stages)
            or ("crisis_signal" in stages)
        ):
            escalation = True

        return {"sequence": stages, "escalation_detected": escalation}

    def analyze(self, messages: List[str]) -> Dict:

        total_messages = max(len(messages), 1)

        isolation_count = self._count_patterns(messages, self.isolation_keywords)

        hopelessness_count = self._count_patterns(messages, self.hopelessness_keywords)

        negative_count = self._count_patterns(messages, self.negative_keywords)

        crisis_count = self._count_patterns(messages, self.crisis_keywords)

        result = {
            "isolation_score": round(min(isolation_count / total_messages, 1), 4),
            "hopelessness_score": round(min(hopelessness_count / total_messages, 1), 4),
            "negative_language_score": round(
                min(negative_count / total_messages, 1), 4
            ),
            "crisis_language_score": round(min(crisis_count / total_messages, 1), 4),
        }

        escalation = self._detect_escalation(messages)

        result["conversation_escalation"] = escalation

        risk_indicators = []

        if result["isolation_score"] > 0:

            risk_indicators.append("Social isolation indicators detected")

        if result["hopelessness_score"] > 0:

            risk_indicators.append("Hopelessness indicators detected")

        if result["negative_language_score"] >= 0.5:

            risk_indicators.append("Frequent negative language detected")

        if result["crisis_language_score"] > 0:

            risk_indicators.append("Crisis-related language detected")

        if escalation["escalation_detected"]:

            risk_indicators.append("Conversation deterioration pattern detected")

        result["risk_indicators"] = risk_indicators

        return result
