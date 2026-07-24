from src.conversation_pattern.pattern import ConversationPatternAnalyzer

analyzer = ConversationPatternAnalyzer()


messages = [
    "I feel sad today.",
    "Nobody understands me and I feel alone.",
    "Everything is hopeless and nothing will change.",
]


result = analyzer.analyze(messages)


print("=== PATTERN ANALYSIS ===")
print(result)
