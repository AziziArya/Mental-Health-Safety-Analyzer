from typing import List

from sqlalchemy.orm import Session

from src.database.models import Conversation, Decision, Message


class DatabaseRepository:
    """
    Database Repository Layer

    Responsibilities:
    - Save conversations
    - Save messages
    - Save decisions
    - Retrieve history
    """

    def __init__(self, db: Session):

        self.db = db

    # =====================================
    # Conversation
    # =====================================

    def create_conversation(
        self, conversation_id: str, risk_level: str = None, risk_score: float = 0
    ):

        conversation = Conversation(
            id=conversation_id, risk_level=risk_level, risk_score=risk_score
        )

        self.db.add(conversation)

        self.db.commit()

        self.db.refresh(conversation)

        return conversation

    def get_conversation(self, conversation_id: str):

        return (
            self.db.query(Conversation)
            .filter(Conversation.id == conversation_id)
            .first()
        )

    # =====================================
    # Messages
    # =====================================

    def add_message(
        self,
        conversation_id: str,
        message: str,
        risk_level: str,
        risk_score: float,
        emotion_score: float = None,
    ):

        item = Message(
            conversation_id=conversation_id,
            message=message,
            risk_level=risk_level,
            risk_score=risk_score,
            emotion_score=emotion_score,
        )

        self.db.add(item)

        self.db.commit()

        self.db.refresh(item)

        return item

    def get_messages(self, conversation_id: str) -> List[Message]:

        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.created_at)
            .all()
        )

    # =====================================
    # Decisions
    # =====================================

    def save_decision(self, conversation_id: str, decision: dict):

        item = Decision(
            conversation_id=conversation_id,
            final_score=decision.get("final_risk_score", 0),
            final_level=decision.get("final_risk_level", "Unknown"),
            priority=decision.get("priority", "LOW"),
            human_review=decision.get("requires_human_review", False),
        )

        self.db.add(item)

        self.db.commit()

        self.db.refresh(item)

        return item

    def get_latest_decision(self, conversation_id: str):

        return (
            self.db.query(Decision)
            .filter(Decision.conversation_id == conversation_id)
            .order_by(Decision.created_at.desc())
            .first()
        )

    # =====================================
    # Full History
    # =====================================

    def get_conversation_history(self, conversation_id: str):

        messages = self.get_messages(conversation_id)

        decision = self.get_latest_decision(conversation_id)

        return {
            "conversation_id": conversation_id,
            "messages": [
                {
                    "message": m.message,
                    "risk_level": m.risk_level,
                    "risk_score": m.risk_score,
                    "emotion_score": m.emotion_score,
                    "created_at": m.created_at.isoformat(),
                }
                for m in messages
            ],
            "decision": (
                {
                    "final_risk_score": decision.final_score,
                    "final_risk_level": decision.final_level,
                    "priority": decision.priority,
                    "human_review": decision.human_review,
                }
                if decision
                else None
            ),
        }
