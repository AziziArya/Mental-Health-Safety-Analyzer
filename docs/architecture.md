# System Architecture

## Overview

Mental Health Safety Analyzer is a privacy-aware AI system designed to
analyze anonymous mental health conversations and identify emotional
distress, crisis indicators, and changes in conversation risk over time.

The project is designed as a modular pipeline where each component
performs a specific analysis task. The final decision is created by
combining multiple signals instead of relying on a single prediction.

The system is not a medical diagnosis tool. It is a safety assistance
prototype designed to support monitoring, early warning, and human
review.

------------------------------------------------------------------------

# High-Level Architecture

The complete processing flow is:

    Conversation Input

            ↓

    Privacy Guard Layer

            ↓

    Text Preprocessing

            ↓

    Emotion Analysis Module

            ↓

    Distress Detection Module

            ↓

    Crisis Detection Module

            ↓

    Conversation Pattern Analyzer

            ↓

    Context Fusion Engine

            ↓

    Risk Decision Engine

            ↓

    Explainable AI Report Generator

            ↓

    Safety Dashboard / API Output

------------------------------------------------------------------------

# Component Description

## 1. Conversation Input Layer

This layer receives the conversation data that needs to be analyzed.

Input examples:

-   User messages
-   Anonymous conversation logs
-   Chat-based interactions

The input layer is responsible for preparing raw conversation data
before analysis.

------------------------------------------------------------------------

## 2. Privacy Guard Layer

Privacy protection is one of the main requirements of the project.

Before any AI analysis happens, sensitive information is detected and
removed.

The privacy layer can identify:

-   Names
-   Phone numbers
-   Email addresses
-   Addresses
-   Identification numbers
-   Other personally identifiable information

The goal is to allow analysis while reducing privacy risks.

------------------------------------------------------------------------

## 3. Text Preprocessing Layer

This module prepares the text for AI models.

Main operations:

-   Cleaning unnecessary characters
-   Normalizing text
-   Preparing model input
-   Tokenization

This step ensures that the input format is compatible with the analysis
models.

------------------------------------------------------------------------

## 4. Emotion Analysis Module

The emotion analysis component studies emotional signals inside the
conversation.

Detected emotional states may include:

-   Sadness
-   Fear
-   Anger
-   Happiness
-   Hopelessness
-   Emotional instability

Instead of analyzing a single message, the system can evaluate emotional
changes throughout the conversation.

------------------------------------------------------------------------

## 5. Distress Detection Module

This module focuses on identifying signs of emotional difficulty.

Examples:

-   High stress indicators
-   Severe sadness
-   Isolation signals
-   Loss of motivation
-   Emotional deterioration

The output is a distress level estimation.

------------------------------------------------------------------------

## 6. Crisis Detection Module

The crisis detector searches for stronger safety-related signals.

Examples:

-   Self-harm related expressions
-   Emergency situations
-   Extreme hopelessness
-   Dangerous escalation patterns

The goal is early identification of high-risk conversations.

------------------------------------------------------------------------

## 7. Conversation Pattern Analyzer

This module analyzes the overall structure of the conversation.

Important signals:

-   Emotional trend
-   Message length changes
-   Repeated negative patterns
-   Sudden tone changes
-   Increasing risk over time

This allows the system to understand conversation evolution instead of
isolated sentences.

------------------------------------------------------------------------

## 8. Context Fusion Engine

Different AI modules produce different signals.

The context fusion engine combines:

-   Emotion results
-   Distress score
-   Crisis indicators
-   Conversation patterns
-   Confidence values

The purpose is to create a more reliable final understanding.

------------------------------------------------------------------------

## 9. Risk Decision Engine

This module converts all collected information into a final safety
decision.

Possible outputs:

-   Safe
-   Mild Concern
-   Moderate Risk
-   High Risk
-   Critical Emergency

The decision engine also considers model confidence and uncertainty.

------------------------------------------------------------------------

## 10. Explainable AI Report Generator

The system should not only provide a result.

It should explain why the decision was made.

Generated explanations may include:

-   Important detected signals
-   Emotional changes
-   Risk factors
-   Confidence score
-   Recommended next action

This improves transparency and trust.

------------------------------------------------------------------------

# API Architecture

The backend service is built to expose analysis functionality through
APIs.

Main responsibilities:

-   Receive conversation data
-   Execute the analysis pipeline
-   Return structured safety results
-   Provide explainable outputs

Technology:

-   FastAPI
-   Python
-   AI inference modules

------------------------------------------------------------------------

# Design Principles

## Modular Design

Each component is separated to allow:

-   Easier development
-   Independent testing
-   Future model replacement
-   Better maintainability

------------------------------------------------------------------------

## Privacy First

The system prioritizes:

-   Anonymous processing
-   Data minimization
-   Protection of sensitive information

------------------------------------------------------------------------

## Explainability

Every important decision should provide understandable reasons.

The system avoids becoming a black-box classifier.

------------------------------------------------------------------------

## Human Review Support

For uncertain or high-risk cases, the system supports human evaluation
instead of fully automated decisions.

------------------------------------------------------------------------

# Future Architecture Expansion

Possible future improvements:

-   Multi-model AI fusion
-   Advanced transformer-based models
-   Real-time monitoring dashboard
-   Fairness evaluation module
-   Human review workflow
-   Better risk prediction models
