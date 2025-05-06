# AI Resume Analyzer

An AI-powered tool that analyzes resumes and provides insights to improve them using Natural Language Processing.

## Features
- Upload your resume (PDF format)
- Get a score based on keyword matching and formatting
- Suggests improvements for skills, formatting, and structure

## Tech Stack
- Python
- Streamlit (Frontend)
- spaCy / scikit-learn (NLP)
- PyPDF2 (PDF parsing)

## How It Works
1. The PDF is parsed and cleaned.
2. Keywords are extracted and compared with job descriptions.
3. Scores are generated and areas of improvement are suggested.

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
