from typing import List, Dict, Any


class EmotionEvolutionAnalyzer:
    """
    Analyze emotional evolution across conversation timeline.

    Detects:
    - Negative emotion persistence
    - Emotional escalation
    - Crisis override signals
    - Conversation emotional direction

    This module does not diagnose.
    It only analyzes emotional changes.
    """

    def __init__(self):

        self.negative_emotions = {
            "sadness",
            "fear",
            "anger",
            "disappointment",
            "grief",
            "remorse",
            "nervousness"
        }



    def _normalize_emotions(
        self,
        emotions: Any
    ) -> List[Dict]:
        """
        Convert different emotion formats into:

        [
            {
                "emotion": "sadness",
                "score": 0.9
            }
        ]
        """

        normalized = []


        if emotions is None:
            return normalized



        # Case 1:
        # [
        #   {"emotion":"sadness","score":0.9}
        # ]

        if isinstance(emotions, list):

            for item in emotions:

                if isinstance(item, dict):

                    if (
                        "emotion" in item
                        and "score" in item
                    ):

                        normalized.append(
                            {
                                "emotion":
                                    item.get("emotion"),

                                "score":
                                    float(
                                        item.get(
                                            "score",
                                            0
                                        )
                                    )
                            }
                        )


                    else:

                        # Dict style inside list
                        # {"sadness":0.9}

                        for key, value in item.items():

                            if key in self.negative_emotions:

                                normalized.append(
                                    {
                                        "emotion": key,
                                        "score": float(value)
                                    }
                                )



                elif isinstance(item, str):

                    normalized.append(
                        {
                            "emotion": item,
                            "score": 1.0
                        }
                    )



        # Case 2:
        # {
        #   "sadness":0.9,
        #   "fear":0.1
        # }

        elif isinstance(emotions, dict):

            if (
                "emotion" in emotions
                and "score" in emotions
            ):

                normalized.append(
                    {
                        "emotion":
                            emotions.get("emotion"),

                        "score":
                            float(
                                emotions.get(
                                    "score",
                                    0
                                )
                            )
                    }
                )


            else:

                for key, value in emotions.items():

                    if key in self.negative_emotions:

                        normalized.append(
                            {
                                "emotion": key,
                                "score": float(value)
                            }
                        )



        return normalized




    def _calculate_negative_score(
        self,
        emotions
    ) -> float:


        normalized = self._normalize_emotions(
            emotions
        )


        score = 0.0


        for emotion in normalized:


            if emotion.get(
                "emotion"
            ) in self.negative_emotions:


                score += emotion.get(
                    "score",
                    0
                )



        return round(
            min(score, 1.0),
            4
        )




    def _detect_trend(
        self,
        scores: List[float]
    ) -> str:


        if len(scores) < 2:

            return "Insufficient data"



        difference = (
            scores[-1]
            -
            scores[0]
        )



        if difference >= 0.15:

            return "Increasing Negative Emotion"



        elif difference <= -0.15:

            return "Improving Emotional State"



        return "Stable"




    def _apply_crisis_adjustment(
        self,
        emotion_scores: List[float],
        crisis_history: List[Dict]
    ) -> List[float]:


        effective_scores = []



        for index, score in enumerate(
            emotion_scores
        ):


            adjusted = score



            if (
                crisis_history
                and index < len(crisis_history)
            ):


                crisis_item = crisis_history[index]



                if isinstance(
                    crisis_item,
                    dict
                ):

                    crisis_score = crisis_item.get(
                        "crisis_probability",
                        0
                    )



                    if crisis_score >= 0.80:


                        adjusted = max(
                            adjusted,
                            min(
                                adjusted + 0.15,
                                1.0
                            )
                        )



            effective_scores.append(
                round(
                    adjusted,
                    4
                )
            )



        return effective_scores





    def _detect_escalation(
        self,
        raw_scores,
        effective_scores,
        crisis_history
    ):


        reasons = []

        escalation = False



        if (
            effective_scores[-1]
            >
            effective_scores[0]
            +
            0.10
        ):

            escalation = True

            reasons.append(
                "Effective emotional risk increased across conversation"
            )



        if crisis_history:


            last = crisis_history[-1]


            if isinstance(
                last,
                dict
            ):


                crisis_score = last.get(
                    "crisis_probability",
                    0
                )


                if crisis_score >= 0.80:

                    escalation = True

                    reasons.append(
                        "High crisis signal overrides emotional decrease"
                    )



        if (
            len(raw_scores) >= 2
            and escalation
            and raw_scores[-1] <= raw_scores[0]
        ):

            reasons.append(
                "Negative emotion persisted despite score fluctuation"
            )



        return (
            escalation,
            reasons
        )





    def analyze(
        self,
        emotion_history: List[Any],
        crisis_history: List[Dict] = None
    ) -> Dict:


        if crisis_history is None:

            crisis_history = []



        emotion_scores = []



        for emotions in emotion_history:


            score = self._calculate_negative_score(
                emotions
            )


            emotion_scores.append(
                score
            )



        if not emotion_scores:


            return {

                "emotion_scores": [],

                "effective_scores": [],

                "raw_emotion_trend": "No data",

                "emotion_trend": "No data",

                "current_negative_emotion_score": 0,

                "safety_emotion_score": 0,

                "escalation_detected": False,

                "escalation_reasons": []

            }




        effective_scores = self._apply_crisis_adjustment(
            emotion_scores,
            crisis_history
        )



        raw_trend = self._detect_trend(
            emotion_scores
        )



        effective_trend = self._detect_trend(
            effective_scores
        )



        escalation, reasons = self._detect_escalation(
            emotion_scores,
            effective_scores,
            crisis_history
        )



        final_trend = effective_trend



        if escalation:

            final_trend = "Negative Escalation"



        return {


            "emotion_scores":

                emotion_scores,



            "effective_scores":

                effective_scores,



            "raw_emotion_trend":

                raw_trend,



            "emotion_trend":

                final_trend,



            "current_negative_emotion_score":

                effective_scores[-1],



            "safety_emotion_score":

                effective_scores[-1],



            "escalation_detected":

                escalation,



            "escalation_reasons":

                reasons

        }