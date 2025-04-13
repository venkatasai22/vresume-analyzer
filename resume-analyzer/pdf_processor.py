import fitz  # PyMuPDF #type: ignore
from typing import Optional

def extract_text_from_pdf(pdf_path: str) -> Optional[str]:
    """Extract text content from PDF resume.
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        Extracted text or None if error occurs
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None

def extract_text_from_upload(uploaded_file) -> Optional[str]:
    """Extract text from Streamlit file uploader object.
    
    Args:
        uploaded_file: Streamlit file uploader object
        
    Returns:
        Extracted text or None if error occurs
    """
    try:
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        return extract_text_from_pdf("temp_resume.pdf")
    except Exception as e:
        print(f"Error processing uploaded file: {e}")
        return None
