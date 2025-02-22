# Research Paper Assistant 📚

A Streamlit-based application that helps researchers understand academic papers using AI. The assistant can explain complex concepts, break down mathematical equations, and answer questions about research papers.

## Features

- 📄 PDF paper analysis
- ⚡ Real-time question answering
- 🔢 LaTeX equation rendering
- 📊 Table extraction and analysis
- 💬 Chat-based interface
- 🧮 Mathematical notation support

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/research-paper-assistant.git
cd research-paper-assistant
```
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```


4. Set up environment variables:
Create a `.env` file in the root directory with:

```bash
OPENAI_API_KEY=<your_openai_api_key>
```


## Project Structure

```
project/
├── main.py                  # Main application entry point
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
├── config/
│   └── settings.py        # Configuration settings
├── prompts/
│   └── research_prompts.py  # LLM prompt templates
├── ui/
│   ├── components.py      # UI components
│   └── session.py         # Session state management
└── utils/
    ├── processor.py       # PDF processing utilities
    └── rag.py            # RAG pipeline implementation
```


## Usage

1. Run the application:

```bash
streamlit run main.py
```

2. Upload a research paper (PDF format)

3. Ask questions about the paper in the chat interface

## Features in Detail

### PDF Processing
- Extracts text and tables from research papers
- Preserves mathematical equations and formatting
- Handles complex LaTeX notation

### Question Answering
- Uses RAG (Retrieval Augmented Generation) for accurate responses
- Maintains context across conversations
- Provides precise equation explanations

### UI Components
- Clean, intuitive chat interface
- LaTeX equation rendering
- Progress indicators for processing
- Helpful sidebar with suggestions

## Dependencies

- streamlit
- langchain
- openai
- pdfplumber
- camelot-py
- python-dotenv
- faiss-cpu
- sentence-transformers

## Configuration

Key settings can be modified in `config/settings.py`:
- Model parameters (temperature, etc.)
- Embedding settings
- Retrieval parameters
- File handling options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- OpenAI for GPT models
- Langchain for RAG implementation
- Streamlit for the web interface
- HuggingFace for embeddings

## Support

For support, please open an issue in the GitHub repository or contact [your-email].

