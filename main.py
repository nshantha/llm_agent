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

    # Initialize session state for history if it doesn't exist
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if "qa" not in st.session_state:
        st.session_state.qa = None

    # File upload  
    uploaded_file = st.file_uploader("Upload Lecture Notes (PDF)", type="pdf")  

    if uploaded_file:  
        # Process PDF and build RAG only if not already processed
        if "processed_file" not in st.session_state or st.session_state.processed_file != uploaded_file.name:
            with st.spinner("Crunching your notes..."):  
                text_chunks = process_pdf(uploaded_file)  
                qa_chain = build_rag_pipeline(
                    text_chunks=text_chunks,
                    openai_key=openai_key,
                    use_openai=True
                )  
                st.session_state.qa = qa_chain
                st.session_state.processed_file = uploaded_file.name
                st.session_state.history = []  # Reset history for new document

        # Display chat history
        for message in st.session_state.history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if question := st.chat_input("Ask a question about your notes:"):
            # Add user message to history
            st.session_state.history.append({"role": "user", "content": question})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(question)

            # Generate and display assistant response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = st.session_state.qa.run(question)
                st.markdown(response)
            
            # Add assistant response to history
            st.session_state.history.append({"role": "assistant", "content": response})

if __name__ == "__main__":  
    main()  