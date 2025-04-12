import spacy #type: ignore
from typing import Dict, List
from config import INDUSTRY_KEYWORDS, SECTION_HEADERS #type: ignore

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_resume(text: str) -> Dict[str, float]:
    """Analyze the resume text and provide comprehensive ATS scoring and quality assessment.
    
    Args:
        text: The resume text
        
    Returns:
        A dictionary with scores and detailed analysis
    """
    resume_doc = nlp(text)
    
    # Improved section detection using config
    text_lower = text.lower()
    sections = {
        section: any(header in text_lower for header in SECTION_HEADERS[section])
        for section in SECTION_HEADERS
    }
    
    # Calculate keyword metrics
    keywords = [token.text.lower() for token in resume_doc if token.is_alpha and not token.is_stop]
    total_words = len(keywords)
    unique_keywords = len(set(keywords))
    keyword_density = (unique_keywords / total_words) * 100 if total_words > 0 else 0
    
    # Industry keyword matching
    industry_matches = {
        industry: len([kw for kw in keywords if kw in terms])
        for industry, terms in INDUSTRY_KEYWORDS.items()
    }
    
    # Calculate comprehensive score
    section_score = sum(sections.values()) / len(sections) * 40  # 40% weight
    keyword_score = min(keyword_density, 100) * 0.4  # 40% weight
    industry_score = (sum(industry_matches.values()) / (len(keywords) + 1)) * 100 * 0.2  # 20% weight
    
    return {
        "ats_score": section_score + keyword_score + industry_score,
        "keywords": {
            "total": total_words,
            "unique": unique_keywords,
            "density": keyword_density,
            "industry_matches": industry_matches
        },
        "sections": sections,
        "suggestions": generate_suggestions(sections, keyword_density, industry_matches)
    }

def generate_suggestions(sections: Dict[str, bool], keyword_density: float, 
                        industry_matches: Dict[str, int]) -> List[str]:
    """Generate personalized improvement suggestions."""
    suggestions = []
    
    # Section suggestions
    missing_sections = [s for s, found in sections.items() if not found]
    if missing_sections:
        suggestions.append(f"Add missing sections: {', '.join(missing_sections)}")
    
    # Keyword suggestions
    if keyword_density < 30:
        suggestions.append("Improve keyword density by adding more relevant skills and experience")
    
    # Industry-specific suggestions
    primary_industry = max(industry_matches.items(), key=lambda x: x[1])[0]
    suggestions.append(f"Focus on {primary_industry} keywords: {', '.join(INDUSTRY_KEYWORDS[primary_industry][:3])}...")
    
    return suggestions
