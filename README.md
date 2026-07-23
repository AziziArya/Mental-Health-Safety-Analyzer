# Mental Health Safety Analyzer

An AI-powered mental health conversation safety analysis system designed to detect emotional distress, crisis signals, conversation deterioration, and generate explainable safety decisions.

## Overview

Mental Health Safety Analyzer is a modular AI pipeline that analyzes user conversations and estimates safety risk levels.

The system combines multiple analysis components:

- Emotion analysis
- Distress detection
- Crisis phrase detection
- Conversation pattern analysis
- Context fusion
- Risk decision engine
- Explainable AI (XAI)
- Safety response generation

The goal is not medical diagnosis, but early identification of safety-related signals and recommendation of appropriate review actions.

---

# Key Features

## Emotion Analysis

Detects emotional states from conversation messages and evaluates their potential safety impact.

Supported signals include:

- Sadness
- Fear
- Anger
- Grief
- Remorse
- Nervousness
- Disappointment

---

## Distress Detection

Analyzes psychological distress indicators and generates a distress score.

---

## Crisis Detection

Detects high-risk language patterns and crisis-related expressions.

Examples of detected signals:

- Self-harm related statements
- Severe hopelessness indicators
- Explicit crisis phrases

---

## Conversation Analysis

The system evaluates conversations over time and detects:

- Risk escalation
- Negative emotional progression
- Social isolation patterns
- Conversation deterioration

---

# System Architecture

```
User Conversation
        |
        v
+---------------------+
| Emotion Analyzer    |
+---------------------+
        |
        v
+---------------------+
| Distress Detector   |
+---------------------+
        |
        v
+---------------------+
| Crisis Detector     |
+---------------------+
        |
        v
+---------------------+
| Fusion Engine       |
+---------------------+
        |
        v
+---------------------+
| Decision Engine     |
+---------------------+
        |
        +----------------+
        |                |
        v                v
+-------------+   +----------------+
| XAI Report  |   | Safety Response|
+-------------+   +----------------+
```

---

# Risk Decision System

The final safety score is calculated by combining multiple subsystems:

```
Final Risk Score =

Emotion Score    × 0.25
+
Distress Score  × 0.35
+
Crisis Score    × 0.40
```

Risk levels:

| Score | Level |
|---|---|
| 0.00 - 0.20 | Safe |
| 0.20 - 0.40 | Mild Concern |
| 0.40 - 0.60 | Moderate Risk |
| 0.60 - 0.80 | High Risk |
| 0.80 - 1.00 | Critical Emergency |

---

# Explainable AI (XAI)

The system provides:

- Risk factors
- Detected signals
- Reasoning chain
- Recommended actions
- Safety explanations

Example:

```json
{
 "risk_level": "High Risk",
 "risk_score": 0.75,
 "signals": [
   "Crisis language",
   "Emotional escalation",
   "Conversation deterioration"
 ]
}
```

---

# Project Structure

```
src/

├── emotion_analyzer/
├── distress_detector/
├── crisis_detector/
├── fusion_engine/
├── decision_engine/
├── conversation_analyzer/
├── conversation_pattern/
├── context_fusion/
├── context_memory/
├── explainability/
├── response_generator/
├── privacy_guard/
└── pipeline/
```

---

# Testing

The project includes automated tests.

Current status:

```
12 / 12 tests passed
```

Coverage:

```
80%
```

Tested components:

- API endpoints
- Full analysis pipeline
- Crisis detection
- Distress detection
- Conversation escalation
- Response generation
- Explainability output

---

# Installation

Clone the repository:

```bash
git clone https://github.com/AziziArya/Mental-Health-Safety-Analyzer.git

cd Mental-Health-Safety-Analyzer
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run:

```bash
pytest -v
```

Coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

---

# API Example

Input:

```json
{
 "message": "I don't want to live anymore."
}
```

Output:

```json
{
 "risk_level": "Critical Emergency",
 "recommended_action": "Immediate human review required"
}
```

---

# Safety Notice

This project is a safety-support research prototype.

It does not provide medical diagnosis or replace professional mental health services.

---

# Release

Current version:

```
v1.0.0
```

Stable release including:

- Conversation analysis pipeline
- Risk fusion engine
- Explainable AI module
- Automated safety responses

---

# License

MIT License