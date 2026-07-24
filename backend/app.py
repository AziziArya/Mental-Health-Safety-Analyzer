from fastapi import FastAPI
from pydantic import BaseModel

from src.context_fusion.fusion import ContextFusionEngine
from src.context_memory.memory import ConversationMemory
from src.conversation_analyzer.conversation import ConversationAnalyzer
from src.conversation_pattern.pattern import ConversationPatternAnalyzer
from src.emotion_evolution.evolution import EmotionEvolutionAnalyzer
from src.pipeline.analyzer import MentalHealthAnalyzer

app = FastAPI(
    title="Mental Health Safety Analyzer",
    description="AI system for mental health conversation safety analysis",
    version="1.0",
)


# =====================================
# Core Analyzer
# =====================================

analyzer = MentalHealthAnalyzer()


# =====================================
# Conversation Intelligence Modules
# =====================================

emotion_evolution = EmotionEvolutionAnalyzer()


pattern_analyzer = ConversationPatternAnalyzer()


memory = ConversationMemory()


context_fusion = ContextFusionEngine()


# =====================================
# Advanced Conversation Analyzer
# =====================================

conversation_analyzer = ConversationAnalyzer(
    analyzer,
    emotion_evolution=emotion_evolution,
    pattern_analyzer=pattern_analyzer,
    memory=memory,
    context_fusion=context_fusion,
)


# =====================================
# Request Models
# =====================================


class TextRequest(BaseModel):

    text: str


class ConversationRequest(BaseModel):

    messages: list[str]


# =====================================
# Routes
# =====================================


@app.get("/")
def home():

    return {"message": "Mental Health Safety Analyzer API is running"}


@app.post("/analyze")
def analyze_text(request: TextRequest):

    result = analyzer.analyze(request.text)

    return result["report"]


@app.post("/analyze-conversation")
def analyze_conversation(request: ConversationRequest):

    result = conversation_analyzer.analyze_conversation(request.messages)

    return result
