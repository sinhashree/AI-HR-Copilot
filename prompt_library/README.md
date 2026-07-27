
# 🤖 AI HR Copilot

![Python](https://img.shields.io/badge/Python-3.12-blue)

![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

![Status](https://img.shields.io/badge/Status-MVP-success)

![License](https://img.shields.io/badge/License-MIT-green)

## Problem Statement

Recruiters often spend 20–40 minutes creating structured job descriptions.

The process is repetitive and maintaining ATS-friendly formatting across multiple hiring requests is challenging.


## Product Vision

Build an AI-powered HR Copilot that helps recruiters create, improve and manage hiring documents using Generative AI.

## Overview

## Overview

AI HR Copilot is a Streamlit-based web application that helps recruiters and hiring managers create structured, ATS-friendly job description prompts.

The application simplifies the process of drafting professional job descriptions and allows users to export prompts in TXT, Word, and PDF formats. It is designed as an AI Product Management portfolio project that demonstrates product thinking, prompt engineering, rapid prototyping, and user-focused design.

## Target Users

- HR Professionals

- Recruiters

- Startup Founders

- Hiring Managers

- Recruitment Agencies

## Completed Features

- Streamlit-based multi-page interface with:
  - Home page
  - Prompt Generator page
  - About page
- Job Description prompt generator with input fields for:
  - Job title
  - Company name
  - Experience level
  - Work mode
  - Location
  - Employment type
  - Key skills
- Prompt validation to require essential input fields before generation
- Prompt history display in the sidebar
- Download options for generated prompt:
  - Plain text (`.txt`)
  - Word document (`.docx`)
  - PDF document (`.pdf`)
- Utility functions to generate Word and PDF files from prompt text
- App configuration for page title, icon, and wide layout

## Success Metrics

- Time taken to generate a prompt

- Number of prompts generated

- Downloads

- User satisfaction

- Repeat users


## Product Decisions

Why Streamlit?

- Rapid prototyping

- Fast UI development

- Easy deployment

Why prompt generation first?

- Lowest engineering effort

- Fast MVP

- Easy user validation


Version 1.0

✔ Prompt Generator

✔ Export

✔ History

Version 2.0

✔ Gemini Integration

✔ Resume Generator

✔ JD Optimizer

Version 3.0

✔ Resume Matching

✔ ATS Score

✔ Multi-user Workspace

## How to Run

1. Install dependencies:

```powershell
cd C:\projects\prompt_library
pip install -r requirements.txt
```

2. Run the Streamlit app:

```powershell
streamlit run app.py
```

## File Structure

- `app.py` — main Streamlit application
- `utils.py` — helper functions for creating Word and PDF downloads
- `requirements.txt` — Python package requirements
- `README.md` — project documentation
- `docs/` — placeholder documentation for product planning

## Notes for an AI Product Management Portfolio

This project is framed as a product experiment for AI-powered business workflows. It highlights:

- product scoping of AI prompt generation
- prioritization of core MVP functionality
- a clean UX for generating and exporting prompts
- a roadmap for broader AI assistant capabilities

## Dependencies

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `python-docx`
- `reportlab`
