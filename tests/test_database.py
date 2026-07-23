from src.database.database import engine, Base, SessionLocal

from src.database.models import (
    Conversation,
    Message,
    Decision
)

import uuid



def print_section(title):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)




# ======================================
# Create Tables
# ======================================

print_section(
    "DATABASE CREATION"
)


Base.metadata.create_all(
    bind=engine
)


print(
    "DATABASE CREATED"
)




# ======================================
# Database Session
# ======================================


db = SessionLocal()



try:


    print_section(
        "INSERT TEST"
    )


    conversation_id = str(
        uuid.uuid4()
    )



    conversation = Conversation(

        id=conversation_id

    )


    db.add(
        conversation
    )

    db.commit()



    print(
        "Conversation inserted:",
        conversation_id
    )




    message = Message(

        conversation_id=conversation_id,

        message="I feel sad",

        risk_level="Mild Concern",

        risk_score=0.38,

        emotion_score=0.9,

        distress_score=0.4,

        crisis_score=0.0

    )



    db.add(
        message
    )

    db.commit()



    print(
        "Message inserted"
    )





    # ======================================
    # Query Test
    # ======================================


    print_section(
        "QUERY TEST"
    )



    result = (

        db.query(
            Message
        )

        .filter(

            Message.conversation_id

            ==

            conversation_id

        )

        .first()

    )



    assert result is not None



    print({

        "message":
            result.message,

        "risk":
            result.risk_level,

        "score":
            result.risk_score

    })



    print(
        "QUERY PASSED"
    )




    # ======================================
    # Decision Test
    # ======================================


    print_section(
        "DECISION INSERT TEST"
    )


    decision = Decision(

        conversation_id=conversation_id,

        final_score=0.38,

        final_level="Mild Concern",

        priority="LOW",

        human_review=False,

        escalation=False,

        decision_reason="Normal emotional distress monitoring"

    )


    db.add(
        decision
    )

    db.commit()



    print(
        "Decision inserted"
    )



    print(
        "\nDATABASE TEST PASSED"
    )



finally:


    db.close()