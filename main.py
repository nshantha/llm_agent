import streamlit as st  
from utils.processor import process_pdf  
from utils.rag import build_rag_pipeline  
import os
from dotenv import load_dotenv
from ui.components import (
    init_mathjax, 
    format_latex_equation, 
    render_sidebar,
    render_chat_history
)
from ui.session import init_session_state, update_chat_history

def process_uploaded_file(uploaded_file, openai_key):
    """Process the uploaded PDF file and build RAG pipeline."""
    with st.spinner("Analyzing the research paper..."):  
        text_chunks = process_pdf(uploaded_file)  
        qa_chain = build_rag_pipeline(
            text_chunks=text_chunks,
            openai_key=openai_key,
            use_openai=True
        )  
        st.session_state.qa = qa_chain
        st.session_state.processed_file = uploaded_file.name
        st.session_state.history = []
        st.success("Paper analyzed! Ask any questions about the research.")

def handle_user_input(question):
    """Handle user input and generate response."""
    update_chat_history("user", question)
    
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = st.session_state.qa.run(question)
        format_latex_equation(response)
    
    update_chat_history("assistant", response)

def main():  
    # Load environment variables
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")

    # Initialize components
    init_mathjax()
    init_session_state()

    # Render UI
    st.title("Research Paper Assistant 📚")  
    st.subheader("Your AI Research Companion")  
    render_sidebar()

    # File upload  
    uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type="pdf")  

    if uploaded_file:  
        # Process PDF if new file
        if st.session_state.processed_file != uploaded_file.name:
            process_uploaded_file(uploaded_file, openai_key)

        # Display chat history
        render_chat_history(st.session_state.history)

        # Handle user input
        if question := st.chat_input("Ask about any aspect of the paper:"):
            handle_user_input(question)

if __name__ == "__main__":  
    main()  