import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict

# =====================================
# Audit Directory
# =====================================

AUDIT_DIR = "logs/audit"


if not os.path.exists(AUDIT_DIR):

    os.makedirs(AUDIT_DIR)


# =====================================
# Audit Engine
# =====================================


class AuditLogger:
    """
    Audit Trail System

    Responsibilities:
    - Track important system events
    - Store decisions
    - Keep explainability records
    - Support future database migration
    """

    def __init__(self):

        self.events = []

    # =================================
    # Create Audit Event
    # =================================

    def log_event(self, event_type: str, data: Dict[str, Any]) -> Dict:

        event = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "data": data,
        }

        self.events.append(event)

        self._save_event(event)

        return event

    # =================================
    # Decision Audit
    # =================================

    def log_decision(self, decision: Dict) -> Dict:

        return self.log_event("decision", decision)

    # =================================
    # Conversation Audit
    # =================================

    def log_conversation(self, conversation_id: str, result: Dict) -> Dict:

        return self.log_event(
            "conversation_analysis",
            {
                "conversation_id": conversation_id,
                "risk": result.get("overall_risk", {}),
            },
        )

    # =================================
    # Get History
    # =================================

    def get_events(self):

        return self.events

    # =================================
    # Save To File
    # =================================

    def _save_event(self, event: Dict):

        filename = os.path.join(AUDIT_DIR, "audit.json")

        history = []

        if os.path.exists(filename):

            try:

                with open(filename, "r", encoding="utf-8") as file:

                    history = json.load(file)

            except Exception:

                history = []

        history.append(event)

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(history, file, indent=4, ensure_ascii=False)
