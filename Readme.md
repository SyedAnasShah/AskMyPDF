📖 AI PDF Assistant

An AI-powered PDF Question Answering Assistant that lets you upload PDFs, split them into chunks, and ask natural language questions about their contents.

Built with cutting-edge tools for semantic search and retrieval-augmented generation (RAG).

🚀 Key Features

📂 Smart PDF Processing

Upload PDFs and extract text.

Handles large documents by splitting into manageable chunks.

(Note: Scanned PDFs without OCR are not supported by default).

🔍 Semantic Search with FAISS

Store embeddings in FAISS for fast similarity search.

Powered by Sentence-Transformers & LangChain.

🤖 Adaptive Question Answering

Factual Mode → Strictly uses document context.

Creative Mode → Blends document context with external insights.

🖥️ Two Interfaces

Gradio UI → Interactive web app.

FastAPI Endpoints → Programmatic access via REST API.

⚡ Optimized for CPU & GPU

Runs on CPU out of the box.

GPU acceleration recommended for faster embedding + inference.

🏗️ Tech Stack

LangChain
 – Orchestration of LLM pipelines

Sentence-Transformers
 – Embeddings

Hugging Face Transformers
 – Q&A models

FAISS
 – Vector database

Gradio
 – Web UI

FastAPI
 – REST API backend

📂 Project Structure
.
├── app.py              # Main FastAPI + Gradio app
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container setup
├── README.md           # Documentation
└── uploaded_pdfs/      # Stored uploaded files

🟢 Running in Google Colab

This project can be run in Google Colab with ngrok tunneling for public access.

!pip install pyngrok gradio PyPDF2 sentence-transformers faiss-cpu transformers langchain langchain-community


Run the notebook → You’ll get two URLs:

🌍 FastAPI Public URL → REST API access

🌍 Gradio Public URL → Web UI

🖥️ Running Locally (No Colab / ngrok)
1️⃣ Install Requirements
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

2️⃣ Run the App
python app.py


FastAPI API → http://localhost:8000

Gradio UI → http://localhost:7860

🐳 Running with Docker

Build and run the containerized app:

docker build -t pdf-assistant .
docker run -p 8000:8000 -p 7860:7860 pdf-assistant

📡 FastAPI Endpoints
Method	Endpoint	Description
GET	/	Root health check
GET	/status	Check DB readiness
POST	/upload_pdf	Upload a PDF file
POST	/ask_question	Ask a question (form-data: question)

Swagger UI → http://localhost:8000/docs

🎨 Gradio UI

Upload a PDF

Ask questions interactively

👉 Accessible at http://localhost:7860

📸 Example Screenshots
Upload PDF

Ask a Question

API Status

⚠️ Notes

Scanned PDFs (image-based) require OCR (e.g., Tesseract) for text extraction.

Default Q&A model → flan-t5-base (can be swapped with any Hugging Face model).

⚡ GPU Support

Highly recommended for large documents & fast inference.

Ensure CUDA is installed with PyTorch:

pip install torch --index-url https://download.pytorch.org/whl/cu121

✨ Summary

With AI PDF Assistant, you can:
✔️ Upload PDFs
✔️ Query them in natural language
✔️ Use either Web UI or API
✔️ Run seamlessly on Colab, Local, or Docker