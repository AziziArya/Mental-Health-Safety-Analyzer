from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)



VALID_RISK_LEVELS = [
    "Safe",
    "Mild Concern",
    "Moderate Risk",
    "High Risk",
    "Critical Emergency"
]



def test_home_endpoint():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "message" in data

    assert (
        "Mental Health Safety Analyzer"
        in data["message"]
    )





def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"





def test_single_message_pipeline_structure():

    payload = {
        "text":
        "I feel hopeless and nobody understands me."
    }


    response = client.post(
        "/analyze",
        json=payload
    )


    assert response.status_code == 200


    data = response.json()


    # Core outputs

    assert "risk_assessment" in data

    assert "detected_factors" in data

    assert "recommended_action" in data

    assert "safety_note" in data



    risk = data["risk_assessment"]


    assert "level" in risk

    assert "score" in risk


    assert risk["level"] in VALID_RISK_LEVELS


    assert 0 <= risk["score"] <= 1





def test_single_message_distress_detection():


    payload = {

        "text":

        "I feel hopeless and very sad"

    }


    response = client.post(
        "/analyze",
        json=payload
    )


    assert response.status_code == 200


    data = response.json()


    factors = data["detected_factors"]


    assert factors["emotion_score"] >= 0


    assert factors["distress_score"] >= 0


    assert factors["crisis_score"] >= 0





def test_high_risk_conversation_escalation():


    payload = {

        "messages":

        [

            "I feel sad today.",

            "Nobody understands me.",

            "I don't want to live anymore."

        ]

    }



    response = client.post(

        "/analyze-conversation",

        json=payload

    )


    assert response.status_code == 200



    data = response.json()



    # Conversation

    assert data["message_count"] == 3


    assert len(data["timeline"]) == 3



    # Required modules

    assert "emotion_evolution" in data

    assert "conversation_patterns" in data

    assert "memory_context" in data

    assert "decision" in data

    assert "explainability" in data

    assert "safety_response" in data




    decision = data["decision"]



    assert decision["final_risk_level"] in VALID_RISK_LEVELS



    assert decision["final_risk_score"] >= 0



    assert "signals" in decision



    signals = decision["signals"]



    assert (

        signals["crisis_signal"]

        or

        signals["critical_crisis"]

    )



    assert decision["escalation"] is True



    assert decision["requires_human_review"] is True





def test_crisis_response_generation():


    payload = {


        "messages":

        [

            "I cannot continue anymore",

            "I want to disappear",

            "I don't want to live anymore"

        ]

    }



    response = client.post(

        "/analyze-conversation",

        json=payload

    )



    assert response.status_code == 200



    data = response.json()



    safety = data["safety_response"]



    assert "message" in safety


    assert len(
        safety["message"]
    ) > 20



    assert safety["response_type"] in [

        "safety_support",

        "crisis_support"

    ]



    assert safety["priority"] in [

        "HIGH",

        "CRITICAL"

    ]





def test_xai_output_quality():


    payload = {


        "messages":

        [

            "I feel alone",

            "Everything is getting worse",

            "I don't want to live anymore"

        ]

    }



    response = client.post(

        "/analyze-conversation",

        json=payload

    )


    assert response.status_code == 200



    data = response.json()


    xai = data["explainability"]



    assert "summary" in xai


    assert len(
        xai["summary"]
    ) > 10



    assert (

        "reasons" in xai

        or

        "key_factors" in xai

    )





if __name__ == "__main__":


    test_home_endpoint()

    test_health_endpoint()

    test_single_message_pipeline_structure()

    test_single_message_distress_detection()

    test_high_risk_conversation_escalation()

    test_crisis_response_generation()

    test_xai_output_quality()


    print(
        "\nFULL PIPELINE TEST PASSED"
    )