from src.crisis_detector.crisis import CrisisDetector

detector = CrisisDetector()

text = "I don't want to live anymore. I have been thinking about ending my life."

result = detector.analyze(text)

print("=== CRISIS RESULT ===")
print(result)
