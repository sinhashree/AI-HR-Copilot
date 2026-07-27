# System Architecture

# AI HR Copilot

**Version:** 1.0

**Author:** Anushree Sinha

---

# Overview

AI HR Copilot follows a simple modular architecture designed for rapid prototyping while keeping the codebase maintainable and scalable.

The current version focuses on prompt generation and document export. Future versions will integrate Generative AI capabilities using the Google Gemini API.

---

# High-Level Architecture

```text
                        +----------------------+
                        |      End User        |
                        +----------+-----------+
                                   |
                                   |
                          User Inputs
                                   |
                                   ▼
                     +---------------------------+
                     |     Streamlit UI Layer    |
                     +---------------------------+
                                   |
                                   |
                         Form Validation
                                   |
                                   ▼
                    +----------------------------+
                    |      Prompt Builder        |
                    +----------------------------+
                                   |
                     Generates Structured Prompt
                                   |
          +------------+------------+------------+
          |            |                         |
          ▼            ▼                         ▼
     TXT Export   Word Export             PDF Export
          |            |                         |
          +------------+------------+------------+
                                   |
                                   ▼
                           Download to User
```

---

# Future Architecture (With AI)

```text
                        +----------------------+
                        |      End User        |
                        +----------+-----------+
                                   |
                                   ▼
                         Streamlit Application
                                   |
                     User enters job information
                                   |
                                   ▼
                         Prompt Builder Module
                                   |
                                   ▼
                         Gemini API Integration
                                   |
                                   ▼
                     AI Generated Job Description
                                   |
          +------------+------------+------------+
          |            |                         |
          ▼            ▼                         ▼
     TXT Export   Word Export             PDF Export
                                   |
                                   ▼
                             User Download
```

---

# Components

## 1. User Interface

Technology

- Streamlit

Responsibilities

- Display forms
- Collect user input
- Display generated prompts
- Provide download options
- Handle navigation

---

## 2. Prompt Builder

Responsibilities

- Collect user inputs
- Validate mandatory fields
- Create structured prompt templates

Output

- Formatted prompt text

---

## 3. Export Module

Current Formats

- TXT
- Word (.docx)
- PDF

Responsibilities

- Convert prompt into downloadable files
- Preserve formatting
- Handle file generation

---

## 4. AI Integration (Future)

Technology

- Google Gemini API

Responsibilities

- Generate complete job descriptions
- Improve prompt quality
- Produce recruiter-ready content

---

# Data Flow

1. User opens AI HR Copilot.
2. User enters job details.
3. Streamlit validates required fields.
4. Prompt Builder creates a structured prompt.
5. Prompt is displayed to the user.
6. User downloads the prompt in the preferred format.
7. Future versions will send the prompt to Gemini for AI-generated output.

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Export | python-docx, reportlab |
| AI (Future) | Google Gemini API |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

# Design Principles

The architecture follows these principles:

- Simplicity
- Modularity
- Scalability
- Maintainability
- Rapid Prototyping

---

# Future Enhancements

Planned architectural improvements include:

- Authentication and user accounts
- Cloud database integration
- Prompt history persistence
- AI-generated outputs
- Resume parsing services
- ATS integrations
- Analytics dashboard
- Team collaboration features

---

# Scalability Considerations

As the product evolves, the architecture can be extended by:

- Separating frontend and backend services
- Introducing REST APIs
- Adding cloud storage
- Integrating external HR platforms
- Supporting multiple AI providers

---

# Security Considerations

Future versions should include:

- Secure API key management
- User authentication
- Role-based access control
- Data encryption
- Input sanitization
- Rate limiting for AI API requests

---

# Conclusion

The current architecture is intentionally lightweight to support rapid MVP development while providing a solid foundation for future AI-powered capabilities. Its modular design allows new features such as Gemini integration, resume screening, and recruiter collaboration to be added with minimal changes to the existing codebase.