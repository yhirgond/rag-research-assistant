# 📄 Research Paper RAG Assistant

A powerful AI-powered application that lets you upload research papers (PDFs) and ask questions about them in natural language. The app retrieves relevant content from your documents and generates accurate, grounded answers using a Large Language Model.

---

## 🧠 What is RAG?

**RAG (Retrieval Augmented Generation)** is an AI technique that combines two things:
1. **Retrieval** — Finding the most relevant parts of your documents
2. **Generation** — Using an AI model to generate answers based on those parts

Instead of the AI making things up (hallucinating), it only answers based on what's actually in your documents. This makes it accurate and trustworthy.

---

## 🏗️ How It Works (Step by Step)
```
PDF Upload → Text Extraction → Chunking → Embedding → Vector Store
                                                              ↓
User Question → Embed Question → Search Vector Store → Retrieve Chunks
                                                              ↓
                                              Build Prompt → LLM → Answer
```

1. **PDF Parsing** — Extracts text from uploaded PDF files page by page
2. **Chunking** — Splits the text into smaller overlapping pieces (chunks) for better search
3. **Embedding** — Converts each chunk into a numerical vector using a sentence transformer model
4. **Vector Store** — Stores all vectors in a FAISS index for fast similarity search
5. **Retrieval** — When you ask a question, it finds the most similar chunks
6. **Generation** — Sends the question + retrieved chunks to Groq LLM for a final answer

---

## 🛠️ Tech Stack

| Component | Tool | Purpose |
|---|---|---|
| UI | Streamlit | Web interface |
| PDF Parsing | PyMuPDF (fitz) | Extract text from PDFs |
| Text Splitting | LangChain | Split text into chunks |
| Embeddings | sentence-transformers | Convert text to vectors |
| Vector Database | FAISS | Store and search vectors |
| LLM | Groq (LLaMA3-8b) | Generate answers |
| Config | PyYAML | Manage configuration |
| Secrets | python-dotenv | Manage API keys |

---

## 📁 Project Structure
```
rag-research-assistant/
├── app.py
├── config.yaml
├── .env
├── requirements.txt
├── src/
│   ├── ingestion/
│   │   ├── pdf_parser.py
│   │   ├── preprocessor.py
│   │   └── chunker.py
│   ├── embeddings/
│   │   └── embedder.py
│   ├── retrieval/
│   │   ├── vector_store.py
│   │   └── retriever.py
│   ├── generation/
│   │   ├── prompt_builder.py
│   │   └── llm_handler.py
│   └── utils/
│       └── helpers.py
└── data/
    ├── raw_pdfs/
    └── vectorstore/
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9 or higher
- VS Code (recommended)
- A free Groq API key ([get one here](https://console.groq.com))

### 1. Clone the Repository
```bash
git clone https://github.com/yhirgond/rag-research-assistant.git
cd rag-research-assistant
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🚀 How to Use

### Uploading and Indexing Papers
1. Click **Browse files** in the left sidebar
2. Select one or more text-based PDF files
3. Click **Index Papers** button
4. Wait for the progress bar to complete

### Asking Questions
1. Go to the **Ask a Question** tab
2. Type your question in the text box
3. Click **Get Answer**
4. View the answer and source chunks below

### Summarizing Papers
1. Go to the **Summarize Paper** tab
2. Select a paper from the dropdown
3. Click **Summarize**

---

## ⚠️ Important Notes

- Only use text-based PDFs (not scanned/image PDFs)
- Never commit your .env file to GitHub
- First run downloads the embedding model (~90MB, cached after that)

---

## 🔮 Future Improvements

- Support for scanned PDFs using OCR
- Multiple language support
- Chat history and conversation memory
- Export answers as PDF or Word
- Support for other LLM providers

---

## 👨‍💻 Author

**Yogesh Hirgond**
- GitHub: [@yhirgond](https://github.com/yhirgond)

---

## 📄 License

This project is open source and available under the MIT License.
