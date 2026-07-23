# Mental Health Safety Analyzer — System Architecture

## Project Goal

Build an AI-powered system that analyzes anonymous mental-health conversations, detects emotional changes, estimates distress and crisis risk, explains its decisions, and generates a structured safety report.

---

# High-Level Pipeline

Conversation Input
↓
Privacy Guard
↓
Emotion Analyzer
↓
Distress Detector
↓
Crisis Detector
↓
Decision Fusion Engine
↓
Risk Scoring Engine
↓
Explainable AI (XAI)
↓
Safety Report Generator
↓
Interactive Dashboard

---

# AI Modules

## 1. Privacy Guard

Purpose: Remove or anonymize personally identifiable information (PII).

Detect and anonymize:

* Names
* Phone numbers
* Emails
* Addresses
* IDs and other sensitive information

Planned tools:

* Microsoft Presidio
* Piiranha

Example:
Input: “My name is Ali and my phone is 0912...”
Output: “My name is [NAME] and my phone is [PHONE]”

---

## 2. Emotion Analyzer

Purpose: Detect multiple emotions in each message.

Model: SamLowe/roberta-base-go_emotions

Output example:

* Sadness: 0.82
* Fear: 0.41
* Anger: 0.12
* Joy: 0.05

Supports:

* Emotion evolution
* Emotional heatmap
* Conversation fingerprint

---

## 3. Distress Detector

Purpose: Estimate psychological distress severity.

Planned model: Distress / sentiment model (CPU-friendly).

Output example:

* Low: 0.10
* Medium: 0.25
* High: 0.65

---

## 4. Crisis Detector

Purpose: Detect self-harm or suicide-related risk.

Planned model: sentinetyd/suicidal-bert

Output example:

* Crisis probability: 0.91
* Emergency: True

---

# Conversation Pattern Analysis

This module is rule-based and statistical (no separate model required).

Features:

* Sudden emotion changes
* Increasing negative language
* Message length changes
* Repeated hopeless statements
* Conversation stability score

---

# Decision Fusion Engine

Combine outputs from all AI models.

Inputs:

* Emotion scores
* Distress probability
* Crisis probability
* Pattern-analysis features

Output:

* Unified risk score (0–100)
* Confidence score

---

# Multi-Level Risk Analysis

Risk levels:

* Safe
* Mild Concern
* Moderate Risk
* High Risk
* Critical Emergency

Example:

* Emotion sadness > 0.8
* Distress > 0.7
* Crisis > 0.8
  → Critical Emergency

---

# Explainable AI (XAI)

The system must explain why a prediction was made.

Example:

* High hopelessness indicators
* Isolation language detected
* Self-harm keywords detected
* Strong negative emotion trend

Planned tools:

* Attention visualization
* SHAP (future)
* Keyword extraction

---

# Human Review Mode

If confidence is low, the system will not make a final automated decision.

Example:

* Confidence < 0.60
* Risk near threshold
  → “Requires Human Review”

---

# Safety Report Generator

The final report should contain:

* Risk level
* Confidence score
* Emotion timeline
* Crisis factors
* Explanation of the decision
* Conversation summary
* Recommended action

---

# Dashboard (Future UI)

Planned visual components:

* Risk meter
* Emotion timeline chart
* Emotional heatmap
* Confidence indicator
* Crisis-factor panel
* AI reasoning panel
* Exportable safety report

---

# Backend Stack

Planned technologies:

* Python 3.11+
* FastAPI
* Transformers
* PyTorch (CPU inference)
* Pandas / NumPy
* Uvicorn

---

# Frontend Stack (Planned)

Option 1 (faster):

* Streamlit

Option 2 (more professional):

* React + FastAPI

---

# Deployment Strategy

Local development: CPU-only inference.

Future options:

* HuggingFace Spaces
* Render
* Railway
* VPS with GPU (only if future fine-tuning is needed)

---

# Current Development Phase

Phase 1 — Model acquisition and inference testing.

Immediate tasks:

1. Download emotion model
2. Download distress model
3. Download crisis model
4. Download privacy model
5. Verify inference on sample conversations
6. Implement Fusion Engine
7. Build FastAPI backend
8. Build interactive dashboard

---

# Notes

* The system is NOT a medical diagnostic tool.
* All outputs are decision-support signals.
* High-risk conversations should be flagged for human review.
* Privacy protection must happen before any AI analysis.
* The architecture is modular so each model can be replaced independently in the future.
