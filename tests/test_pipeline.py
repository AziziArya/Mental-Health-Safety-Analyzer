from src.pipeline.analyzer import MentalHealthAnalyzer

text = """
I feel completely hopeless.
Nobody understands me.
I don't want to live anymore.
"""


analyzer = MentalHealthAnalyzer()

result = analyzer.analyze(text)


print("\n=== FINAL ANALYSIS ===")

print(result["report"])
