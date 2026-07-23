from datetime import datetime
import uuid





class ConversationAnalyzer:
    """
    Full conversation safety pipeline.

    Pipeline:

    Messages
        |
        v
    MentalHealthAnalyzer
        |
        v
    Emotion Evolution
        |
        v
    Conversation Patterns
        |
        v
    Context Fusion
        |
        v
    Decision Engine
        |
        v
    XAI Explanation
        |
        v
    Safety Response
    """



    def __init__(
        self,
        analyzer,
        emotion_evolution,
        pattern_analyzer,
        memory,
        context_fusion,
        decision_engine,
        xai_engine,
        response_generator
    ):

        self.analyzer = analyzer
        self.emotion_evolution = emotion_evolution
        self.pattern_analyzer = pattern_analyzer
        self.memory = memory
        self.context_fusion = context_fusion
        self.decision_engine = decision_engine
        self.xai_engine = xai_engine
        self.response_generator = response_generator






    def _timestamp(self):

        return datetime.utcnow().isoformat()






    def _normalize_emotion(
        self,
        emotion
    ):

        """
        Convert emotion output:

        [
            {
                "emotion":"sadness",
                "score":0.9
            }
        ]

        into:

        {
            "sadness":0.9
        }
        """

        if isinstance(emotion, dict):

            return emotion



        if isinstance(emotion, list):

            result = {}

            for item in emotion:

                if isinstance(item, dict):

                    name = item.get(
                        "emotion"
                    )

                    score = item.get(
                        "score",
                        0
                    )

                    if name:

                        result[name] = score


            return result



        return {}







    def _safe_dict(
        self,
        value
    ):

        if isinstance(value, dict):

            return value


        return {}







    def _analyze_single_messages(
        self,
        messages
    ):

        results = []



        for index, message in enumerate(messages):


            analysis = self.analyzer.analyze(
                message
            )


            risk = analysis.get(
                "risk_assessment",
                {}
            )



            results.append({

                "message_number":
                    index + 1,


                "timestamp":
                    self._timestamp(),


                "message":
                    message,


                "risk_level":
                    risk.get(
                        "level",
                        "Unknown"
                    ),


                "risk_score":
                    risk.get(
                        "score",
                        0
                    )

            })


        return results







    def analyze_conversation(
        self,
        messages
    ):


        conversation_id = str(
            uuid.uuid4()
        )



        # =============================
        # Message Timeline
        # =============================


        timeline = self._analyze_single_messages(
            messages
        )





        # =============================
        # Analyze all messages once
        # =============================


        analyses = []


        for message in messages:

            analyses.append(

                self.analyzer.analyze(
                    message
                )

            )





        emotion_history = [

            self._normalize_emotion(
                item.get(
                    "emotion",
                    {}
                )
            )

            for item in analyses

        ]



        crisis_history = [

            self._safe_dict(
                item.get(
                    "crisis",
                    {}
                )
            )

            for item in analyses

        ]







        # =============================
        # Emotion Evolution
        # =============================


        emotion_evolution_result = (

            self.emotion_evolution.analyze(

                emotion_history,

                crisis_history

            )

        ) or {}







        # =============================
        # Conversation Pattern
        # =============================


        pattern_result = (

            self.pattern_analyzer.analyze(
                messages
            )

        ) or {}







        # =============================
        # Latest Analysis
        # =============================


        latest_full_analysis = analyses[-1]





        base_risk = latest_full_analysis.get(

            "risk_assessment",

            {
                "score":0,
                "level":"Safe"
            }

        )







        # =============================
        # Context Fusion
        # =============================


        context_result = self.context_fusion.analyze(

            self._normalize_emotion(

                latest_full_analysis.get(
                    "emotion",
                    {}
                )

            ),


            self._safe_dict(

                latest_full_analysis.get(
                    "distress",
                    {}
                )

            ),


            self._safe_dict(

                latest_full_analysis.get(
                    "crisis",
                    {}
                )

            )

        ) or {}







        # =============================
        # Memory
        # =============================


        memory_context = {

            "conversation_length":
                len(messages),


            "previous_risk":
                "Unknown",


            "current_risk_score":
                0,


            "risk_change":
                0,


            "trend":
                "Stable"

        }







        # =============================
        # Decision
        # =============================


        decision = self.decision_engine.decide(

            base_risk,

            context_result,

            emotion_evolution_result,

            pattern_result,

            memory_context

        )







        # =============================
        # XAI
        # =============================


        explanation = self.xai_engine.generate(

            decision,

            memory_context

        )







        # =============================
        # Safety Response
        # =============================


        safety_response = (

            self.response_generator.generate(

                decision,

                messages[-1]

            )

        )








        # =============================
        # Risk Trend
        # =============================


        scores = [

            item["risk_score"]

            for item in timeline

        ]



        if len(scores) > 1 and scores[-1] > scores[0]:

            risk_trend = "Increasing"


        elif len(scores) > 1 and scores[-1] < scores[0]:

            risk_trend = "Decreasing"


        else:

            risk_trend = "Stable"







        return {


            "conversation_id":
                conversation_id,


            "message_count":
                len(messages),


            "timeline":
                timeline,


            "overall_risk":{


                "level":

                    decision.get(
                        "final_risk_level"
                    ),


                "score":

                    decision.get(
                        "final_risk_score"
                    )

            },



            "risk_trend":

                risk_trend,



            "emotion_evolution":

                emotion_evolution_result,



            "conversation_patterns":

                pattern_result,



            "memory_context":

                memory_context,



            "context_fusion":

                context_result,



            "decision":

                decision,



            "explainability":

                explanation,



            "safety_response":

                safety_response

        }