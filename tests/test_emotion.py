from src.emotion_analyzer.emotion import EmotionAnalyzer

analyzer = EmotionAnalyzer()

text = "I feel completely alone and hopeless. Nobody understands me anymore."

result = analyzer.analyze(text)

print("=== INPUT ===")
print(text)

print("\n=== DETECTED EMOTIONS ===")
for item in result:
    print(f"{item['emotion']}: {item['score']}")