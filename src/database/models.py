from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from src.database.database import Base

# =====================================
# Conversation Model
# =====================================


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(String, primary_key=True, index=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    risk_level = Column(String, nullable=True)

    risk_score = Column(Float, default=0.0)

    # Relations

    messages = relationship(
        "Message", back_populates="conversation", cascade="all, delete"
    )

    decisions = relationship(
        "Decision", back_populates="conversation", cascade="all, delete"
    )


# =====================================
# Message Model
# =====================================


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)

    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False)

    message = Column(Text, nullable=False)

    risk_level = Column(String, nullable=True)

    risk_score = Column(Float, default=0.0)

    emotion_score = Column(Float, nullable=True)

    distress_score = Column(Float, nullable=True)

    crisis_score = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relations

    conversation = relationship("Conversation", back_populates="messages")


# =====================================
# Decision Model
# =====================================


class Decision(Base):

    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False)

    final_score = Column(Float, default=0.0)

    final_level = Column(String, nullable=True)

    priority = Column(String, nullable=True)

    human_review = Column(Boolean, default=False)

    escalation = Column(Boolean, default=False)

    decision_reason = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relations

    conversation = relationship("Conversation", back_populates="decisions")
