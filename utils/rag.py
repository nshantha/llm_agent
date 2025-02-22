from langchain_community.vectorstores import FAISS  
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain.chains import RetrievalQA  
from langchain_openai import ChatOpenAI  

def build_rag_pipeline(text_chunks, openai_key=None, use_openai=True):  
    # Use HuggingFace for embeddings  
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  

    # Create FAISS vector store  
    vector_store = FAISS.from_texts(text_chunks, embeddings)  

    # Choose LLM  
    if use_openai:  
        if not openai_key:
            raise ValueError("OpenAI API key is required when use_openai=True")
        llm = ChatOpenAI(
            model="gpt-3.5-turbo", 
            temperature=0,
            api_key=openai_key
        )  
    else:  
        # For HuggingFace models (requires API token):  
        # from langchain_community.llms import HuggingFaceHub  
        # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")  
        raise ValueError("OpenAI is recommended for this demo")  

    # Build QA chain  
    qa_chain = RetrievalQA.from_chain_type(  
        llm=llm,  
        chain_type="stuff",  
        retriever=vector_store.as_retriever()  
    )  
    return qa_chain  