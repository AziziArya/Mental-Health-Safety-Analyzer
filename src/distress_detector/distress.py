from typing import Dict

from transformers import pipeline


class DistressDetector:
    """Estimate distress level from emotional signals."""

    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None,
        )

    def analyze(self, text: str) -> Dict[str, float]:
        results = self.classifier(text)[0]
        scores = {item["label"]: float(item["score"]) for item in results}

        distress_score = (
            scores.get("sadness", 0) * 0.4
            + scores.get("fear", 0) * 0.3
            + scores.get("anger", 0) * 0.2
            + scores.get("disgust", 0) * 0.1
        )

        return {
            "distress_score": round(distress_score, 4),
            "emotions": {k: round(v, 4) for k, v in scores.items()},
        }
