# Contributing Guide

Thank you for your interest in contributing to the Mental Health Safety Analyzer project.

This document explains how developers can contribute improvements, report issues, and maintain project quality.


## Project Overview

Mental Health Safety Analyzer is an AI research prototype designed to analyze mental health conversations, detect emotional distress, identify crisis signals, and generate explainable safety decisions.

The project focuses on:

- Privacy-aware AI systems
- Explainable AI safety analysis
- Human-in-the-loop review
- Responsible AI development
- Research-oriented mental health safety monitoring

This project is not a replacement for professional mental health care and should only be used as an assistive safety analysis system.


## Development Setup

Before contributing to this project, make sure your environment contains:

- Python 3.10
- Git
- Virtual environment
- Required project dependencies


## Clone Repository

Run:

git clone https://github.com/AziziArya/Mental-Health-Safety-Analyzer.git


Move into the project directory:

cd Mental-Health-Safety-Analyzer


## Create Virtual Environment

Create environment:

python -m venv .venv


Activate environment:

Windows:

.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate


## Install Dependencies

Install required packages:

pip install -r requirements.txt

## Project Structure

The project follows a modular architecture to keep different components separated and maintainable.

Main directories:

src/

Contains the main application source code including:

- AI analysis modules
- Safety detection pipeline
- API implementation
- Core processing components


tests/

Contains automated tests for validating:

- API functionality
- Full pipeline behavior
- Safety analysis logic


docs/

Contains detailed project documentation including:

- System architecture
- AI models information
- Privacy and safety considerations
- Testing and evaluation details
- API documentation


.github/

Contains GitHub automation workflows.

Current workflows include:

- Automated testing using GitHub Actions
- Continuous integration checks


## Contribution Workflow

All contributions should follow this workflow:

1. Create an issue or discuss the proposed change.

2. Fork the repository.

3. Create a new branch for your changes.

Example:

git checkout -b feature/new-feature


4. Implement your changes.

5. Add or update tests if required.

6. Run the test suite locally.

Example:

pytest -v


7. Commit your changes with a clear message.

Example:

git commit -m "Add new safety analysis feature"


8. Push your branch.

Example:

git push origin feature/new-feature


9. Create a Pull Request.


## Branch Naming Convention

Use clear branch names.

Examples:

Feature:

feature/add-new-detector


Bug fix:

fix/api-validation-error


Documentation:

docs/update-readme


Improvement:

improve/model-performance


## Commit Message Guidelines

Commit messages should be clear and descriptive.

Good examples:

Add crisis detection module

Improve API error handling

Update architecture documentation

Fix pipeline validation issue


Avoid unclear messages:

update

changes

test

fix stuff

## Code Style Guidelines

To keep the project maintainable, all contributions should follow clean coding practices.

General rules:

- Write readable and understandable code.
- Use meaningful variable and function names.
- Avoid unnecessary complexity.
- Keep functions small and focused.
- Add comments only when the logic is not obvious.
- Follow Python best practices.


## Python Guidelines

The project follows standard Python conventions.

Recommended:

- Use type hints where possible.
- Keep imports organized.
- Follow PEP 8 style.
- Handle exceptions properly.
- Avoid hard-coded values.


Example:

Good:

def analyze_conversation(text: str) -> dict:
    ...


Avoid:

def a(x):
    ...


## Testing Requirements

Every new feature should include appropriate tests.

Before submitting changes, run:

pytest -v


All existing tests must pass.

Current project testing includes:

- API endpoint tests
- Full pipeline tests
- Safety analysis component validation


## Adding New Features

When adding a new capability:

1. Create the required module inside the appropriate source directory.

2. Add tests for the new functionality.

3. Update documentation if the feature changes system behavior.

4. Make sure existing functionality is not affected.

5. Run the complete test suite before submitting.


## Documentation Updates

Documentation should be updated when:

- New modules are added.
- API endpoints change.
- AI models are modified.
- System architecture changes.
- New limitations or safety considerations are introduced.


Documentation files are located in:

docs/

## Reporting Issues

If you find a bug, unexpected behavior, or have a suggestion, please create a GitHub Issue.

A good issue report should include:

- Clear description of the problem.
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- Relevant logs or screenshots if available.
- Environment information.


Example:

Title:

API endpoint returns invalid safety score


Description:

The safety analysis endpoint returns an unexpected result when processing specific conversation inputs.


Steps to reproduce:

1. Run the API server.
2. Send the provided input.
3. Observe the returned response.


## Pull Request Guidelines

Before creating a Pull Request:

- Make sure all tests pass.
- Ensure the code follows project standards.
- Update documentation if necessary.
- Keep changes focused on a specific purpose.


Pull Requests should include:

- Summary of changes.
- Reason for the change.
- Testing performed.
- Possible limitations or known issues.


Example:

## Description

Added an improved crisis detection validation module.

## Testing

Executed:

pytest -v

Result:

12/12 tests passed.


## Security and Privacy

Because this project handles mental health related conversations, contributors must follow responsible AI development practices.

Important rules:

- Do not include real user mental health data.
- Do not upload private conversations.
- Do not commit API keys or credentials.
- Avoid exposing sensitive information in logs.
- Keep privacy protections enabled.


## Code of Responsibility

Contributors should consider:

- User safety.
- Model limitations.
- Potential false positives and false negatives.
- Ethical AI practices.


This project is designed as a research and safety assistance prototype and does not provide medical diagnosis or professional mental health treatment.


## Final Notes

Thank you for helping improve Mental Health Safety Analyzer.

Every contribution should improve one or more of the following:

- Reliability
- Explainability
- Safety
- Maintainability
- Research quality