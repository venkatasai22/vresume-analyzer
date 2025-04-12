import streamlit as st
from typing import Dict
from analyzer import INDUSTRY_KEYWORDS

def display_results(analysis: Dict[str, float]):
    """Display the enhanced analysis results in the Streamlit UI."""
    st.subheader("Comprehensive Resume Analysis")
    
    # Score breakdown
    with st.expander("Score Breakdown", expanded=True):
        cols = st.columns(3)
        cols[0].metric("Overall ATS Score", f"{analysis['ats_score']:.1f}/100",
                      help="Combined score based on sections, keywords and industry relevance")
        cols[1].metric("Keywords", f"{analysis['keywords']['density']:.1f}% density",
                      help=f"{analysis['keywords']['unique']} unique keywords")
        primary_industry = max(analysis['keywords']['industry_matches'].items(), key=lambda x: x[1])[0]
        cols[2].metric("Industry Match", primary_industry.capitalize(),
                      help=f"Best match from {len(INDUSTRY_KEYWORDS)} industries")
    
    # Section analysis
    st.subheader("Section Analysis")
    cols = st.columns(3)
    for i, (section, found) in enumerate(analysis['sections'].items()):
        cols[i].metric(
            section.capitalize(),
            "✅ Present" if found else "❌ Missing",
            help="Section found" if found else "Consider adding this section"
        )
    
    # Industry keyword matches
    st.subheader("Industry Keyword Matches")
    for industry, count in analysis['keywords']['industry_matches'].items():
        st.progress(count/10, text=f"{industry.capitalize()}: {count} keywords matched")
    
    # Personalized suggestions
    st.subheader("Personalized Suggestions")
    for i, suggestion in enumerate(analysis['suggestions'], 1):
        if "missing sections" in suggestion:
            st.error(f"{i}. {suggestion}")
        elif "density" in suggestion:
            st.warning(f"{i}. {suggestion}")
        else:
            st.info(f"{i}. {suggestion}")
