from utils import create_word, create_pdf
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Prompt Library",
    page_icon="🤖",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🤖 AI Prompt Library")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🤖 Prompt Generator",
            "ℹ About"
        ]
    )

    st.markdown("---")

    st.subheader("Prompt History")

    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history), 1):
            st.write(f"Prompt {i}")
    else:
        st.caption("No prompts generated yet.")

    st.markdown("---")
    st.info("Version 1.0")

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "🏠 Home":

    st.title("🤖 AI Prompt Library")

    st.markdown("""
## Welcome!

Generate professional AI prompts for HR and business use cases.

### Features

✅ Job Description Generator

✅ Interview Question Generator *(Coming Soon)*

✅ Email Generator *(Coming Soon)*

✅ Performance Review Generator *(Coming Soon)*

---

### Technology

- Python
- Streamlit
- Prompt Engineering
- Gemini API (Upcoming)
""")

# ==========================================================
# ABOUT PAGE
# ==========================================================

elif page == "ℹ About":

    st.title("About AI Prompt Library")

    st.write("""
### Version
1.0

### Developer
Anushree Sinha

### Built Using

- Python
- Streamlit
- Prompt Engineering

### Future Features

- Gemini AI Integration
- PDF Export
- Word Export
- Saved Prompt Library
- Resume Generator
- Interview Question Generator

This project is part of an AI Product Management portfolio.
""")

# ==========================================================
# PROMPT GENERATOR
# ==========================================================

elif page == "🤖 Prompt Generator":

    st.title("🤖 Job Description Prompt Generator")

    category = st.selectbox(
        "Business Use Case",
        [
            "Job Description",
            "Interview Questions",
            "Emails",
            "Performance Reviews"
        ]
    )

    st.header("Enter Job Details")

    job_title = st.text_input("Job Title")

    company_name = st.text_input("Company Name")

    experience_level = st.selectbox(
        "Experience Level",
        [
            "Entry-Level",
            "Mid-Level",
            "Senior",
            "Executive"
        ]
    )

    work_mode = st.selectbox(
        "Work Mode",
        [
            "Remote",
            "Hybrid",
            "On-site"
        ]
    )

    location = st.text_input("Location")

    employment_type = st.selectbox(
        "Employment Type",
        [
            "Full-time",
            "Part-time",
            "Contract",
            "Internship"
        ]
    )

    skills = st.text_area(
        "Key Skills",
        placeholder="Example: SQL, Excel, Power BI, Python..."
    )

    generate = st.button("🚀 Generate Prompt")

    if generate:

        if not job_title or not company_name or not location or not skills:

            st.warning("⚠ Please fill all required fields.")

        else:

            prompt = f"""
Create a professional Job Description.

Company: {company_name}

Job Title: {job_title}

Experience Level: {experience_level}

Employment Type: {employment_type}

Work Mode: {work_mode}

Location: {location}

Key Skills:
{skills}

Generate:

1. Professional Job Summary

2. Key Responsibilities

3. Required Skills

4. Preferred Qualifications

5. Benefits

6. Company Overview

Make the tone professional and ATS-friendly.
"""

            st.session_state.history.append(prompt)

            st.success("✅ Prompt Generated Successfully!")

            st.subheader("Generated Prompt")

            st.text_area(
                "Copy this prompt into ChatGPT/Gemini",
                prompt,
                height=350
            )
            word_file = create_word(prompt)
            pdf_file = create_pdf(prompt)

            col1, col2, col3 = st.columns(3)

        with col1:
            st.download_button(
            "📄 Download TXT",
            data=prompt,
            file_name="JobDescription.txt",
            mime="text/plain"
        )

        with col2:
            st.download_button(
            "📝 Download Word",
            data=word_file,
            file_name="JobDescription.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        with col3:
            st.download_button(
            "📕 Download PDF",
            data=pdf_file,
            file_name="JobDescription.pdf",
            mime="application/pdf"
    )

            st.download_button(
                label="📄 Download Prompt",
                data=prompt,
                file_name="Job_Description_Prompt.txt",
                mime="text/plain"
            )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | AI Product Management Portfolio")