from src.context_fusion.fusion import ContextFusionEngine


fusion = ContextFusionEngine()


result = fusion.fuse(

    base_risk={
        "level": "Critical Emergency",
        "score": 0.66
    },


    emotion_evolution={
        "safety_emotion_score": 0.92,
        "escalation_detected": True
    },


    conversation_patterns={

        "isolation_score":0.33,

        "hopelessness_score":0.33,

        "crisis_language_score":0.33,

        "conversation_escalation":{
            "escalation_detected":True
        }

    },


    memory_context={

        "risk_change":0.28

    }

)


print("\n=== CONTEXT FUSION ===")

print(result)