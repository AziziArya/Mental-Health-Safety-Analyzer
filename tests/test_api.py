from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def print_section(title):

    print("\n" + "=" * 50)

    print(title)

    print("=" * 50)


# =====================================
# HOME TEST
# =====================================


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    print_section("HOME TEST")

    print(data)

    assert "message" in data


# =====================================
# HEALTH TEST
# =====================================


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    print_section("HEALTH TEST")

    print(data)

    assert data["status"] == "healthy"


# =====================================
# SINGLE MESSAGE TEST
# =====================================


def test_single_message_analysis():

    payload = {"message": "I feel hopeless and very sad"}

    response = client.post("/analyze", json=payload)

    assert response.status_code == 200

    data = response.json()

    print_section("SINGLE MESSAGE ANALYSIS")

    print(data)

    assert "risk_assessment" in data

    assert "level" in data["risk_assessment"]

    assert "score" in data["risk_assessment"]


# =====================================
# CONVERSATION TEST
# =====================================


def test_conversation():

    payload = {
        "messages": [
            "I feel sad today.",
            "Nobody understands me and I feel alone.",
            "I don't want to live anymore.",
        ]
    }

    response = client.post("/conversation", json=payload)

    assert response.status_code == 200

    data = response.json()

    print_section("CONVERSATION TEST")

    print(data)

    assert "conversation_id" in data

    assert data["message_count"] == 3

    assert "decision" in data

    assert "safety_response" in data


# =====================================
# DATABASE STATUS TEST
# =====================================


def test_database_status():

    response = client.get("/database/status")

    assert response.status_code == 200

    data = response.json()

    print_section("DATABASE STATUS")

    print(data)

    assert data["database"] == "connected"


# =====================================
# RUN ALL
# =====================================

if __name__ == "__main__":

    test_home()

    test_health()

    test_single_message_analysis()

    test_conversation()

    test_database_status()

    print("\n")

    print("ALL API TESTS PASSED")
