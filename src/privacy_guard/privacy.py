import re
from typing import Dict, List


class PrivacyGuard:
    """Simple regex-based PII anonymizer."""

    def __init__(self):
        self.patterns = {
            "EMAIL": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
            "PHONE": re.compile(r"(\+?\d[\d\-\s]{7,}\d)"),
            "URL": re.compile(r"https?://\S+|www\.\S+"),
            "IP": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
        }

    def analyze(self, text: str) -> Dict[str, List[str]]:
        findings: Dict[str, List[str]] = {}
        for entity_type, pattern in self.patterns.items():
            matches = pattern.findall(text)
            if matches:
                findings[entity_type] = matches
        return findings

    def anonymize(self, text: str) -> str:
        anonymized = text
        for entity_type, pattern in self.patterns.items():
            anonymized = pattern.sub(f"[{entity_type}]", anonymized)
        return anonymized

    def process(self, text: str) -> Dict[str, object]:
        findings = self.analyze(text)
        anonymized = self.anonymize(text)

        return {
            "original_text": text,
            "anonymized_text": anonymized,
            "detected_entities": findings,
            "entity_count": sum(len(v) for v in findings.values()),
        }