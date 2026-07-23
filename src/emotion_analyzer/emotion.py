from transformers import pipeline
from typing import List, Dict


class EmotionAnalyzer:
    """GoEmotions-based multi-label emotion analyzer."""

    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            top_k=None,
        )

    def analyze(self, text: str, threshold: float = 0.10) -> List[Dict]:
        results = self.classifier(text)[0]

        filtered = [
            {
                "emotion": item["label"],
                "score": round(float(item["score"]), 4),
            }
            for item in results
            if item["score"] >= threshold
        ]

        filtered.sort(key=lambda x: x["score"], reverse=True)
        return filtered