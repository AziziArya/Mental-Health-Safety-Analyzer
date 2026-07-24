from src.emotion_evolution.evolution import EmotionEvolutionAnalyzer

analyzer = EmotionEvolutionAnalyzer()


history = [
    [{"emotion": "sadness", "score": 0.40}],
    [{"emotion": "sadness", "score": 0.70}, {"emotion": "fear", "score": 0.30}],
    [{"emotion": "sadness", "score": 0.90}],
]


result = analyzer.analyze(history)


print(result)
