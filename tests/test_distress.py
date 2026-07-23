from src.distress_detector.distress import DistressDetector

detector = DistressDetector()

text = "I cannot handle this anymore. I feel exhausted, hopeless, and scared about tomorrow."

result = detector.analyze(text)

print("=== DISTRESS RESULT ===")
print(result)