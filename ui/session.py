import streamlit as st

def init_session_state():
    """Initialize session state variables."""
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if "qa" not in st.session_state:
        st.session_state.qa = None
    
    if "processed_file" not in st.session_state:
        st.session_state.processed_file = None

def update_chat_history(role, content):
    """Update chat history with new message."""
    st.session_state.history.append({
        "role": role,
        "content": content
    }) 