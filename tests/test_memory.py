from src.context_memory.memory import ContextMemory


memory = ContextMemory()


memory.add_entry(

    "I feel sad",

    {
        "risk_assessment": {
            "level": "Mild Concern",
            "score": 0.38,
            "confidence": 0.90
        },

        "detected_factors": {

            "emotion_score": 0.90,

            "distress_score": 0.39,

            "crisis_score": 0.0

        }

    }

)



memory.add_entry(

    "I don't want to live anymore",

    {
        "risk_assessment": {

            "level": "Critical Emergency",

            "score": 0.66,

            "confidence": 0.92

        },

        "detected_factors": {

            "emotion_score": 0.52,

            "distress_score": 0.38,

            "crisis_score": 0.92

        }

    }

)



print("\n=== MEMORY HISTORY ===")

print(memory.get_history())


print("\n=== CONTEXT SUMMARY ===")

print(memory.get_context_summary())