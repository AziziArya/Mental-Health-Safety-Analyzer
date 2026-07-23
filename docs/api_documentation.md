# API Documentation

## Overview

The Mental Health Safety Analyzer provides an API layer that allows
applications to send conversation data and receive AI-based safety
analysis results.

The API is designed to connect the analysis pipeline with external
interfaces such as web applications, dashboards, and testing
environments.

------------------------------------------------------------------------

# API Architecture

The API follows a simple request-response structure:

    Client Application

            ↓

    API Endpoint

            ↓

    Safety Analysis Pipeline

            ↓

    Analysis Result

            ↓

    JSON Response

------------------------------------------------------------------------

# Installation and Running

Install project dependencies:

    pip install -r requirements.txt

Run the API service:

    uvicorn src.api.main:app --reload

The API will start locally and become available through the configured
host and port.

------------------------------------------------------------------------

# Main Endpoint

## Health Check

### Endpoint

    GET /health

### Purpose

Checks whether the API service is running correctly.

### Example Response

``` json
{
  "status": "healthy"
}
```

------------------------------------------------------------------------

# Conversation Analysis Endpoint

## Analyze Conversation

### Endpoint

    POST /analyze

### Purpose

Receives a conversation and returns a safety analysis report.

------------------------------------------------------------------------

## Request Example

``` json
{
  "conversation": [
    {
      "role": "user",
      "message": "I feel very hopeless recently."
    }
  ]
}
```

------------------------------------------------------------------------

## Response Example

``` json
{
  "risk_level": "moderate",
  "confidence": 0.82,
  "detected_signals": [
    "negative emotion",
    "hopelessness indicators"
  ]
}
```

------------------------------------------------------------------------

# Response Fields

## Risk Level

Possible values:

-   Safe
-   Mild Concern
-   Moderate Risk
-   High Risk
-   Critical Emergency

------------------------------------------------------------------------

## Confidence Score

Represents the model confidence in the prediction.

Example:

    confidence: 0.85

means the system has 85% confidence in the generated result.

------------------------------------------------------------------------

## Detected Signals

Contains important factors detected during analysis.

Examples:

-   Emotional distress
-   Negative sentiment
-   Crisis-related patterns
-   Conversation deterioration

------------------------------------------------------------------------

# Error Handling

The API returns structured errors.

Example:

``` json
{
  "error": "Invalid input format"
}
```

Common errors:

-   Missing conversation data
-   Invalid request format
-   Internal processing errors

------------------------------------------------------------------------

# API Documentation Interface

The project can expose automatic API documentation using FastAPI
documentation tools.

Available interfaces:

    /docs

and

    /redoc

These provide interactive API testing and endpoint descriptions.

------------------------------------------------------------------------

# Security Considerations

Recommended security practices:

-   Validate all incoming data
-   Avoid storing raw private conversations
-   Apply privacy filtering before analysis
-   Protect API access in production deployment

------------------------------------------------------------------------

# Future API Improvements

Possible future improvements:

-   Authentication system
-   User management
-   Real-time analysis endpoint
-   Streaming conversation analysis
-   Dashboard integration
-   Advanced reporting endpoints

------------------------------------------------------------------------

# Conclusion

The API layer provides a simple interface for connecting the Mental
Health Safety Analyzer engine with external applications while
maintaining privacy, explainability, and safety principles.
