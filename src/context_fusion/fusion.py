from typing import Dict


class ContextFusionEngine:
    """
    Context Fusion Engine

    Combines:

    - Base mental health analysis
    - Emotion evolution
    - Conversation patterns
    - Memory history
    - Crisis override signals


    This module does not diagnose.

    It only calculates contextual safety risk.
    """



    def __init__(self):

        self.weights = {

            "base_risk": 0.45,

            "emotion_evolution": 0.20,

            "conversation_pattern": 0.20,

            "memory": 0.15

        }



    # ---------------------------------
    # Helpers
    # ---------------------------------

    def _normalize_score(
        self,
        value
    ) -> float:

        try:

            return max(
                0.0,
                min(
                    float(value),
                    1.0
                )
            )

        except Exception:

            return 0.0




    def _extract_score(
        self,
        data,
        key="score"
    ):

        if not data:

            return 0.0


        if isinstance(
            data,
            (float,int)
        ):

            return self._normalize_score(
                data
            )


        return self._normalize_score(
            data.get(
                key,
                0
            )
        )



    # ---------------------------------
    # Emotion Evolution
    # ---------------------------------

    def _emotion_context_score(
        self,
        emotion_data: Dict
    ) -> float:


        if not emotion_data:

            return 0.0



        score = emotion_data.get(

            "safety_emotion_score",

            emotion_data.get(

                "current_negative_emotion_score",

                0

            )

        )



        score = self._normalize_score(
            score
        )



        if emotion_data.get(

            "escalation_detected",

            False

        ):

            score += 0.15



        return min(
            score,
            1.0
        )



    # ---------------------------------
    # Conversation Pattern
    # ---------------------------------

    def _pattern_score(
        self,
        pattern_data: Dict
    ) -> float:


        if not pattern_data:

            return 0.0



        score = 0.0



        score += (

            self._normalize_score(

                pattern_data.get(
                    "isolation_score",
                    0
                )

            )
            *
            0.30

        )



        score += (

            self._normalize_score(

                pattern_data.get(
                    "hopelessness_score",
                    0
                )

            )
            *
            0.30

        )



        score += (

            self._normalize_score(

                pattern_data.get(
                    "crisis_language_score",
                    0
                )

            )
            *
            0.40

        )



        escalation = pattern_data.get(

            "conversation_escalation",

            {}

        )



        if escalation.get(

            "escalation_detected",

            False

        ):

            score += 0.20



        return min(
            score,
            1.0
        )



    # ---------------------------------
    # Memory
    # ---------------------------------

    def _memory_score(
        self,
        memory_data: Dict
    ) -> float:


        if not memory_data:

            return 0.0



        change = memory_data.get(

            "risk_change",

            0

        )


        return self._normalize_score(
            change
        )



    # ---------------------------------
    # Crisis Override
    # ---------------------------------

    def _crisis_override(
        self,
        base_risk
    ) -> Dict:


        crisis = {}


        if isinstance(
            base_risk,
            dict
        ):

            crisis = base_risk.get(

                "crisis",

                {}

            )



        probability = self._normalize_score(

            crisis.get(

                "crisis_probability",

                0

            )

        )



        emergency = crisis.get(

            "is_emergency",

            False

        )



        return {

            "crisis_probability":
                probability,

            "is_emergency":
                emergency

        }



    # ---------------------------------
    # Main Fusion
    # ---------------------------------

    def fuse(
        self,
        base_risk: Dict,
        emotion_evolution: Dict = None,
        conversation_patterns: Dict = None,
        memory_context: Dict = None
    ) -> Dict:



        if base_risk is None:

            base_risk = {}



        base_score = self._extract_score(

            base_risk

        )



        emotion_score = self._emotion_context_score(

            emotion_evolution

        )



        pattern_score = self._pattern_score(

            conversation_patterns

        )



        memory_score = self._memory_score(

            memory_context

        )



        final_score = (

            base_score *
            self.weights["base_risk"]

            +

            emotion_score *
            self.weights["emotion_evolution"]

            +

            pattern_score *
            self.weights["conversation_pattern"]

            +

            memory_score *
            self.weights["memory"]

        )



        crisis = self._crisis_override(

            base_risk

        )



        crisis_override = False



        if crisis["crisis_probability"] >= 0.80:

            final_score = max(

                final_score,

                0.80

            )

            crisis_override = True



        if crisis["is_emergency"]:

            final_score = 1.0

            crisis_override = True



        final_score = round(

            min(
                final_score,
                1.0
            ),

            4

        )



        # Risk level

        if final_score >= 0.80:

            level = "Critical Emergency"


        elif final_score >= 0.60:

            level = "High Risk"


        elif final_score >= 0.40:

            level = "Moderate Risk"


        elif final_score >= 0.20:

            level = "Mild Concern"


        else:

            level = "Safe"




        reasons = []



        if emotion_score >= 0.6:

            reasons.append(

                "Negative emotional evolution detected"

            )



        if pattern_score >= 0.4:

            reasons.append(

                "Conversation deterioration pattern detected"

            )



        if memory_score >= 0.2:

            reasons.append(

                "Previous risk history increases concern"

            )



        if crisis_override:

            reasons.append(

                "Crisis signal override applied"

            )




        return {


            "contextual_risk_score":

                final_score,


            "contextual_risk_level":

                level,


            "final_context_score":

                final_score,


            "final_context_level":

                level,


            "emotion_context_score":

                round(
                    emotion_score,
                    4
                ),


            "pattern_context_score":

                round(
                    pattern_score,
                    4
                ),


            "memory_context_score":

                round(
                    memory_score,
                    4
                ),


            "crisis_override":

                crisis_override,


            "crisis_probability":

                crisis["crisis_probability"],


            "context_reasons":

                reasons

        }



    # Compatibility

    def analyze(
        self,
        emotion_evolution=None,
        conversation_patterns=None,
        memory_context=None,
        base_risk=None
    ):


        return self.fuse(

            base_risk or {
                "score":0
            },

            emotion_evolution,

            conversation_patterns,

            memory_context

        )