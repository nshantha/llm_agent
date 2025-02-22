from langchain_community.vectorstores import FAISS  
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain.chains import RetrievalQA  
from langchain_openai import ChatOpenAI
from prompts.research_prompts import get_research_prompt
from config.settings import (
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    EMBEDDING_MODEL,
    RETRIEVAL_K
)

def build_rag_pipeline(text_chunks, openai_key=None, use_openai=True):  
    """Build RAG pipeline with configured settings."""
    
    # Use configured embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )  

    # Create FAISS vector store
    vector_store = FAISS.from_texts(text_chunks, embeddings)  

    # Configure LLM
    if use_openai:  
        if not openai_key:
            raise ValueError("OpenAI API key is required when use_openai=True")
        llm = ChatOpenAI(
            model=DEFAULT_MODEL, 
            temperature=DEFAULT_TEMPERATURE,
            api_key=openai_key
        )  
    else:  
        # For HuggingFace models (requires API token):  
        # from langchain_community.llms import HuggingFaceHub  
        # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")  
        raise ValueError("OpenAI is recommended for this demo")  

    # Build QA chain with configured settings
    qa_chain = RetrievalQA.from_chain_type(  
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(
            search_kwargs={"k": RETRIEVAL_K}
        ),
        chain_type_kwargs={
            "prompt": get_research_prompt()
        }
    )  
    return qa_chain  