import streamlit as st  
from pdf_processor import extract_text_from_upload
from analyzer import analyze_resume   
from ui import display_results   

def main():
    st.title("AI Resume Analyzer")
    st.write("Upload your resume for ATS analysis")

    # File uploader
    resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

    if resume_file:
        if st.button("Analyze"):
            with st.spinner("Analyzing resume..."):
                # Extract text from resume
                resume_text = extract_text_from_upload(resume_file)
                
                if resume_text:
                    # Analyze the resume
                    analysis = analyze_resume(resume_text)
                    
                    # Display results
                    display_results(analysis)
                else:
                    st.error("Failed to process the resume file")

if __name__ == "__main__":
    main()

