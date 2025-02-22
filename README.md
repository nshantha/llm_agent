# StudyMate AI 🚀

StudyMate AI is an intelligent study assistant that allows users to upload PDF lecture notes and ask questions about the content. It uses RAG (Retrieval Augmented Generation) with OpenAI's GPT models to provide accurate, context-aware answers.

## Features
- PDF document processing
- Question-answering based on document content
- Interactive chat interface
- Uses advanced RAG pipeline for accurate responses

## Prerequisites
- Python 3+
- OpenAI API key

## Installation

1. Clone the repository:
bash
git clone <repository-url>
cd studymate-ai

2. Install dependencies:
bash
pip install -r requirements.txt

3. Create a `.env` file in the project root and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Project Structure
```
studymate-ai/
├── main.py              # Main Streamlit application
├── utils/
│   ├── processor.py    # PDF processing utilities
│   └── rag.py          # RAG pipeline implementation
├── .env                # Environment variables (not in git)
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py --server.fileWatcherType none
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload a PDF document and start asking questions!

## Dependencies
- streamlit
- langchain
- langchain-community
- langchain-openai
- langchain-huggingface
- python-dotenv
- PyPDF2
- faiss-cpu
- sentence-transformers

## Configuration

The application can be configured through environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Troubleshooting

If you encounter the PyTorch file watcher error, run Streamlit with:
```bash
streamlit run main.py --server.fileWatcherType none
```

Or add to `.streamlit/config.toml`:
```toml
[server]
fileWatcherType = "none"
```

