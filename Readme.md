# 📖 AI PDF Assistant

An **AI-powered PDF Question Answering Assistant** that lets you upload PDFs, split them into chunks, and ask **natural language questions** about their contents.  

Built with cutting-edge tools for **semantic search and retrieval-augmented generation (RAG)**.  

---

## 🚀 Features

### 📂 Smart PDF Processing
- Upload PDFs and extract text.  
- Splits large documents into manageable chunks.  
- *(Note: Scanned PDFs without OCR are not supported by default).*  

### 🔍 Semantic Search with FAISS
- Embeddings stored in **FAISS** for fast similarity search.  
- Powered by **Sentence-Transformers & LangChain**.  

### 🤖 Adaptive Question Answering
- **Factual Mode** → strictly uses document context.  
- **Creative Mode** → blends context with broader insights.  

### 🖥️ Two Interfaces
- **Gradio UI** → Interactive web app.  
- **FastAPI Endpoints** → REST API for programmatic access.  

### ⚡ Optimized for CPU & GPU
- Runs on **CPU** out of the box.  
- **GPU acceleration** recommended for faster embeddings & inference.  

---

## 🏗️ Tech Stack

- **LangChain** – Orchestration of LLM pipelines  
- **Sentence-Transformers** – Embeddings  
- **Hugging Face Transformers** – Q&A models  
- **FAISS** – Vector database  
- **Gradio** – Web UI  
- **FastAPI** – REST API backend  

---

## 📂 Project Structure

```bash
.
├── app.py              # Main FastAPI + Gradio app
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container setup
├── README.md           # Documentation
└── uploaded_pdfs/      # Stored uploaded files
```

---

## 🟢 Running in Google Colab

This project can be run in **Google Colab** with **ngrok tunneling** for public access:

```bash
!pip install pyngrok gradio PyPDF2 sentence-transformers faiss-cpu transformers langchain langchain-community
```

After execution, you’ll get:

- 🌍 **FastAPI Public URL** → REST API access  
- 🌍 **Gradio Public URL** → Web UI  

---

## 🖥️ Running Locally

### 1️⃣ Install Requirements
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 2️⃣ Run the App
```bash
python app.py
```

- FastAPI → [http://localhost:8000](http://localhost:8000)  
- Gradio → [http://localhost:7860](http://localhost:7860)  

---

## 🐳 Running with Docker

```bash
docker build -t pdf-assistant .
docker run -p 8000:8000 -p 7860:7860 pdf-assistant
```

---

## 📡 FastAPI Endpoints

| Method | Endpoint        | Description                          |
|--------|----------------|--------------------------------------|
| GET    | `/`            | Root health check                    |
| GET    | `/status`      | Check DB readiness                   |
| POST   | `/upload_pdf`  | Upload a PDF file                    |
| POST   | `/ask_question`| Ask a question (form-data: `question`)|

👉 Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)  

---

## 🎨 Gradio UI

1. Upload a PDF  
2. Ask questions interactively  

👉 Accessible at [http://localhost:7860](http://localhost:7860)  

---

## 📸 Example Screenshots

- **Upload PDF**  
  ![Upload PDF](Screenshots/upload.png)  

- **Ask a Question**  
  ![QA](Screenshots/QA.png)  

- **API Status**  
  ![Status](Screenshots/status.png)  

---

## ⚠️ Notes

- Scanned PDFs (image-based) require OCR (e.g., **Tesseract**) for text extraction.  
- Default Q&A model → **flan-t5-base** (can be swapped with any Hugging Face model).  

---

## ⚡ GPU Support

- **Recommended** for large documents & faster inference.  
- Ensure CUDA is installed with PyTorch:  

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

---

## ✨ Summary

With **AI PDF Assistant**, you can:  
✔️ Upload PDFs  
✔️ Query them in natural language  
✔️ Use either **Web UI** or **API**  
✔️ Run seamlessly on **Colab, Local, or Docker**  

---

⚡ Next Steps: Add **OCR support**, try **larger models**, or integrate with enterprise knowledge bases.  
