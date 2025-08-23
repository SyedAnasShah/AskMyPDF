import os
import shutil
import threading
import socket

import gradio as gr
import PyPDF2
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import nest_asyncio
from fastapi import FastAPI, UploadFile, Form, File
import uvicorn

# =========================
# 🔹 Embeddings + LLM
# =========================
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = None
llm = None

qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512,
    temperature=0.8,
    top_p=0.9,
)
llm = HuggingFacePipeline(pipeline=qa_pipeline)


# =========================
# 🔹 Load PDF
# =========================
def load_pdf(pdf_file):
    global db
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text.strip() + " "

    if not text:
        return "❌ No text could be extracted from this PDF. Make sure it is not scanned."

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    db = FAISS.from_texts(chunks, embedding_model)
    return "✅ PDF uploaded & processed successfully!"


# =========================
# 🔹 Answer Questions
# =========================
def answer_question(question):
    global db
    if db is None:
        return "⚠️ Please upload a PDF first."

    docs = db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    is_factual = any(word.lower() in context.lower() for word in question.split())

    if is_factual:
        prompt = f"""
You are a helpful assistant. Answer ONLY using the context below.
Do NOT add any information that is not present in the context.
If the answer is not available, say: "The answer is not available in the document."

Context:
{context}

Question: {question}
Answer:
"""
    else:
        prompt = f"""
You are a helpful assistant. Answer using the context below.
You can be creative and blend relevant insights or related info.
Do not invent unrelated facts.

Context:
{context}

Question: {question}
Answer:
"""

    result = llm(prompt)
    if isinstance(result, list):
        return result[0]['generated_text']
    elif isinstance(result, str):
        return result
    else:
        return str(result)


# =========================
# 🔹 FastAPI Setup
# =========================
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "✅ FastAPI PDF Assistant is running! Use /upload_pdf and /ask_question endpoints."}

@app.get("/status")
async def status():
    return {"status": "connected", "db_ready": db is not None}

@app.post("/upload_pdf")
async def upload_pdf_file(file: UploadFile = File(...)):
    upload_dir = "uploaded_pdfs"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "status": "uploaded successfully"}

@app.post("/ask_question")
async def ask_question_api(question: str = Form(...)):
    answer = answer_question(question)
    return {"question": question, "answer": answer}


# =========================
# 🔹 Gradio UI
# =========================
with gr.Blocks() as demo:
    gr.Markdown("##  AI PDF Assistant – Creative & Adaptive Chat")

    with gr.Group():
        gr.Markdown("### Step 1: Upload your PDF")
        pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
        upload_btn = gr.Button("Process PDF")
        status = gr.Textbox(label="Status", interactive=False)

    with gr.Group():
        gr.Markdown("### Step 2: Ask questions about your PDF")
        question = gr.Textbox(label="Type your question here")
        ask_btn = gr.Button("Get Answer")
        answer = gr.Textbox(label="Answer", interactive=False)

    upload_btn.click(load_pdf, inputs=pdf_input, outputs=status)
    ask_btn.click(answer_question, inputs=question, outputs=answer)


# =========================
# 🔹 Main Entry
# =========================
def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    nest_asyncio.apply()
    threading.Thread(target=run_fastapi, daemon=True).start()
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
