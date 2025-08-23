# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for FAISS
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI (8000) and Gradio (7860)
EXPOSE 8000
EXPOSE 7860

# Run app.py
CMD ["python", "app.py"]
