from src.context_fusion.fusion import ContextFusionEngine
from src.context_memory.memory import ConversationMemory
from src.conversation_analyzer.conversation import ConversationAnalyzer
from src.conversation_pattern.pattern import ConversationPatternAnalyzer
from src.decision_engine.decision import DecisionEngine
from src.emotion_evolution.evolution import EmotionEvolutionAnalyzer
from src.explainability.xai import ExplainabilityEngine
from src.pipeline.analyzer import MentalHealthAnalyzer
from src.response_generator.generator import SafetyResponseGenerator

# ============================
# Main Analyzer
# ============================

analyzer = MentalHealthAnalyzer()


# ============================
# Conversation Modules
# ============================

emotion_evolution = EmotionEvolutionAnalyzer()


pattern_analyzer = ConversationPatternAnalyzer()


memory = ConversationMemory()


context_fusion = ContextFusionEngine()


decision_engine = DecisionEngine()


xai_engine = ExplainabilityEngine()


response_generator = SafetyResponseGenerator()


# ============================
# Conversation Analyzer
# ============================

conversation = ConversationAnalyzer(
    analyzer=analyzer,
    emotion_evolution=emotion_evolution,
    pattern_analyzer=pattern_analyzer,
    memory=memory,
    context_fusion=context_fusion,
    decision_engine=decision_engine,
    xai_engine=xai_engine,
    response_generator=response_generator,
)


# ============================
# Test Conversation
# ============================

messages = [
    "I feel a little sad today.",
    "Nobody understands me and I feel alone.",
    "I don't want to live anymore.",
]


# ============================
# Run Analysis
# ============================

result = conversation.analyze_conversation(messages)


print("\n=== CONVERSATION ANALYSIS ===")

print(result)


# ============================
# Checks
# ============================

print("\n=== CHECKS ===")


assert "conversation_id" in result

assert "timeline" in result

assert "overall_risk" in result

assert "emotion_evolution" in result

assert "conversation_patterns" in result

assert "memory_context" in result

assert "decision" in result

assert "explainability" in result

assert "safety_response" in result


print("Conversation ID:", result["conversation_id"])


print("Overall Risk:", result["overall_risk"])


print("Decision:", result["decision"])


print("Safety Response:", result["safety_response"])


print("\nCONVERSATION TEST PASSED")
