import streamlit as st  
from utils.processor import process_pdf  
from utils.rag import build_rag_pipeline  
import os
from dotenv import load_dotenv

def main():  
    # Load environment variables
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")

    st.title("StudyMate AI 🚀")  
    st.subheader("Upload PDF notes → Ask questions!")  

    # Remove the API key input from sidebar since we're using .env
    with st.sidebar:  
        st.header("Settings")  

    # File upload  
    uploaded_file = st.file_uploader("Upload Lecture Notes (PDF)", type="pdf")  

    if uploaded_file:  
        # Process PDF and build RAG  
        with st.spinner("Crunching your notes..."):  
            text_chunks = process_pdf(uploaded_file)  
            qa_chain = build_rag_pipeline(
                text_chunks=text_chunks,
                openai_key=openai_key,
                use_openai=True  # Always True since we're using .env
            )  
            st.session_state.qa = qa_chain  

        # Chat interface  
        user_question = st.text_input("Ask a question:")  
        if user_question and "qa" in st.session_state:  
            answer = st.session_state.qa.run(user_question)  
            st.markdown(f"**Answer:** {answer}")  

if __name__ == "__main__":  
    main()  