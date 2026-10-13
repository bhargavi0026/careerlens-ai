# CareerLens AI

An explainable job-skill matching and skill-gap analysis tool for internship seekers.

## Problem
Students often struggle to identify which skills are required for different internships and which skills they still need to develop.

## Current Features
- Recognizes skills from sample job descriptions.
- Compares job requirements with a candidate's listed skills.
- Calculates a transparent skill-match percentage.
- Lists matched and missing skills.
- Includes basic tests for the matching logic.

## Technology Stack
- Python
- Pandas
- Regular expressions
- Google Colab

## How the Match Score Works
Match Score = (Number of Matched Skills / Number of Recognized Required Skills) × 100

The score measures keyword overlap only. It is not a probability of getting hired.

## Current Limitations
- Uses a predefined list of skills.
- Uses sample job descriptions rather than verified live listings.
- Does not validate a candidate's actual proficiency.
- Does not use a trained machine-learning model yet.

## Planned Improvements
- Add a larger and more diverse job-description dataset.
- Analyze in-demand skills using Pandas.
- Add a dashboard to compare jobs interactively.
- Evaluate matching quality using manually reviewed examples.
- Add automated tests and better error handling.
