from typing import Dict, Any


class ResponseGenerator:
    """
    Generates safe supportive responses
    based on final safety decision.

    This module does not diagnose.
    It only generates communication guidance.
    """


    def __init__(self):

        self.crisis_keywords = [

            "kill myself",
            "end my life",
            "don't want to live",
            "suicide",
            "harm myself"

        ]



    def _base_response(
        self,
        response_type: str,
        message: str,
        priority: str,
        actions=None
    ):

        return {

            "response_type":
                response_type,


            "message":
                message,


            "priority":
                priority,


            "actions":
                actions or []

        }



    def _normal_response(self):

        return self._base_response(

            "normal_support",

            (
                "Thank you for sharing how you feel. "
                "It is okay to experience difficult moments. "
                "Taking care of yourself and staying connected "
                "with supportive people can help."
            ),

            "LOW",

            [
                "Continue normal supportive communication"
            ]

        )



    def _moderate_response(self):

        return self._base_response(

            "emotional_support",

            (
                "I'm sorry that you are going through "
                "a difficult time. Your feelings are important. "
                "Talking with someone you trust may help "
                "you feel supported."
            ),

            "MEDIUM",

            [

                "Continue emotional monitoring",

                "Encourage supportive communication"

            ]

        )



    def _high_risk_response(self):

        return self._base_response(

            "safety_support",

            (
                "I'm really sorry you are feeling this way. "
                "You do not have to handle everything alone. "
                "If possible, consider reaching out to someone "
                "you trust and stay connected with supportive people."
            ),

            "HIGH",

            [

                "Increase supportive communication",

                "Encourage trusted-person contact",

                "Monitor conversation closely"

            ]

        )



    def _crisis_response(self):

        return self._base_response(

            "crisis_support",

            (
                "I'm really sorry you are experiencing "
                "such a painful moment. Your safety matters. "
                "If you feel you may harm yourself, please "
                "try to contact someone you trust immediately "
                "and avoid being alone."
            ),

            "CRITICAL",

            [

                "Encourage immediate human support",

                "Recommend emergency support if immediate danger exists",

                "Maintain calm supportive conversation"

            ]

        )



    def _contains_crisis_language(
        self,
        message: str
    ) -> bool:


        if not message:

            return False


        text = message.lower()


        for keyword in self.crisis_keywords:

            if keyword in text:

                return True


        return False




    def _select_response(
        self,
        risk_level: str,
        decision: Dict[str, Any],
        last_message: str
    ):


        signals = decision.get(
            "signals",
            {}
        )


        # Highest priority override

        if (

            risk_level == "Critical Emergency"

            or

            signals.get(
                "critical_crisis",
                False
            )

            or

            self._contains_crisis_language(
                last_message
            )

        ):

            return self._crisis_response()



        if risk_level == "High Risk":

            return self._high_risk_response()



        if risk_level == "Moderate Risk":

            return self._moderate_response()



        return self._normal_response()




    def generate(
        self,
        decision: Dict,
        last_message: str = ""
    ) -> Dict:


        decision = decision or {}


        risk_level = decision.get(

            "final_risk_level",

            "Safe"

        )


        response = self._select_response(

            risk_level,

            decision,

            last_message

        )



        response.update({

            "risk_level":
                risk_level,


            "risk_score":
                round(

                    decision.get(

                        "final_risk_score",

                        0

                    ),

                    4

                ),


            "safety_note":

                (
                    "This response is generated "
                    "for safety support and does not "
                    "provide medical diagnosis."
                )

        })



        return response




# Backward compatibility

SafetyResponseGenerator = ResponseGenerator