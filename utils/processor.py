from PyPDF2 import PdfReader  
from langchain.text_splitter import RecursiveCharacterTextSplitter  

def process_pdf(uploaded_file):  
    # Extract text from PDF  
    pdf_reader = PdfReader(uploaded_file)  
    text = ""  
    for page in pdf_reader.pages:  
        text += page.extract_text()  

    # Split text into chunks  
    text_splitter = RecursiveCharacterTextSplitter(  
        chunk_size=1000,  
        chunk_overlap=200  
    )  
    chunks = text_splitter.split_text(text)  
    return chunks  