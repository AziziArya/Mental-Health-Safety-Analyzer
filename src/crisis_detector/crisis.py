import re
from typing import Dict, List


class CrisisDetector:
    """Hybrid rule-based crisis detector."""

    def __init__(self):
        self.high_risk_patterns: List[str] = [
            r"i don't want to live",
            r"i want to die",
            r"end my life",
            r"kill myself",
            r"suicide",
            r"no reason to live",
            r"better off dead",
            r"hurt myself",
            r"self harm",
            r"cut myself",
        ]

        self.medium_risk_patterns: List[str] = [
            r"hopeless",
            r"worthless",
            r"can't go on",
            r"give up",
            r"exhausted with life",
            r"alone forever",
        ]

    def analyze(self, text: str) -> Dict[str, object]:
        text_lower = text.lower()

        high_matches = [
            pattern for pattern in self.high_risk_patterns if re.search(pattern, text_lower)
        ]
        medium_matches = [
            pattern for pattern in self.medium_risk_patterns if re.search(pattern, text_lower)
        ]

        if high_matches:
            probability = min(0.90 + 0.02 * len(high_matches), 0.99)
            level = "critical"
        elif medium_matches:
            probability = min(0.45 + 0.05 * len(medium_matches), 0.79)
            level = "high"
        else:
            probability = 0.05
            level = "safe"

        return {
            "risk_level": level,
            "crisis_probability": round(probability, 4),
            "is_emergency": probability >= 0.80,
            "matched_high_risk_patterns": high_matches,
            "matched_medium_risk_patterns": medium_matches,
        }