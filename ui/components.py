import streamlit as st
import re

def init_mathjax():
    """Initialize MathJax for LaTeX rendering."""
    st.markdown("""
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        <script>
            MathJax.Hub.Config({
                tex2jax: {
                    inlineMath: [['$','$'], ['\\(','\\)']],
                    displayMath: [['$$','$$'], ['\\[','\\]']],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center'
            });
        </script>
    """, unsafe_allow_html=True)

def format_latex_equation(text):
    """Format LaTeX equations for Streamlit rendering."""
    parts = re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))', text, flags=re.DOTALL)
    
    for part in parts:
        if part.strip():
            if part.startswith('\\[') and part.endswith('\\]'):
                equation = part[2:-2].strip()
                st.latex(equation)
            elif part.startswith('\\(') and part.endswith('\\)'):
                equation = part[2:-2].strip()
                st.latex(equation)
            else:
                st.markdown(part)

def render_sidebar():
    """Render the sidebar with information and suggestions."""
    with st.sidebar:
        st.header("About")
        st.write("""
        This AI assistant helps you understand research papers by:
        - Explaining complex concepts
        - Breaking down mathematical equations
        - Identifying key contributions
        - Clarifying methodologies
        - Connecting ideas to broader context
        """)
        
        st.header("Suggested Questions")
        st.write("""
        Try asking about:
        - Main research contributions
        - Methodology explanation
        - Mathematical formulations
        - Experimental setup
        - Results interpretation
        - Future research directions
        """)

def render_chat_history(history):
    """Render the chat history."""
    for message in history:
        with st.chat_message(message["role"]):
            format_latex_equation(message["content"]) 