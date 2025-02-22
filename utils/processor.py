import camelot
import pandas as pd
import io
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

def extract_equations(text):
    """Extract and format mathematical equations with better preservation."""
    # Pattern for equation numbers in parentheses
    equation_pattern = r'(\([\d]+\))'
    
    # Pattern for display math with equation numbers
    display_math = re.findall(r'(\$\$.*?\$\$|\\\[.*?\\\])\s*(' + equation_pattern + ')?', text, re.DOTALL)
    
    # Format equations with their numbers for better context
    for match in display_math:
        eq = match[0]
        eq_num = match[1] if match[1] else ''
        
        # Preserve the exact equation formatting
        formatted_eq = f"\nEQUATION:\n{eq} {eq_num}\n"
        text = text.replace(eq + eq_num, formatted_eq)
    
    # Clean up any artifacts
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('EQUATION: EQUATION:', 'EQUATION:')
    
    return text

def extract_tables(file_path):
    """Extract tables from PDF using camelot."""
    try:
        # Read tables from PDF
        tables = camelot.read_pdf(file_path, pages='all', flavor='lattice')
        
        # Convert tables to markdown format for better context preservation
        table_texts = []
        for idx, table in enumerate(tables):
            df = table.df
            # Convert DataFrame to markdown
            markdown_table = f"Table {idx + 1}:\n" + df.to_markdown(index=False)
            table_texts.append(markdown_table)
        
        return "\n\n".join(table_texts)
    except Exception as e:
        print(f"Error extracting tables: {e}")
        return ""

def process_pdf(uploaded_file):
    """Process PDF with enhanced equation preservation."""
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Extract tables
    table_text = extract_tables("temp.pdf")
    
    # Extract text and process equations
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        # Process equations in the text
        text += extract_equations(page_text)

    # Combine all content
    combined_text = f"{text}\n\nEXTRACTED TABLES:\n{table_text}"

    # Split text into larger chunks to keep equations together
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,  # Increased for better equation context
        chunk_overlap=600,  # Increased overlap
        separators=["\nEQUATION:", "\n\n", "\n", " ", ""],
        keep_separator=True
    )
    chunks = text_splitter.split_text(combined_text)
    
    # Clean up
    import os
    if os.path.exists("temp.pdf"):
        os.remove("temp.pdf")
    
    return chunks  