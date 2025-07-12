# LLM-Document-Summarization-QA-System
LLM-Powered Document Summarization and QA System using NeMo/Hugging Face, TensorRT optimization, and Triton inference serving.
# LLM-Powered Document Summarization & QA System

This project allows users to upload PDF or text documents, get a high-level summary, and ask questions on the content. Built with Hugging Face models and Streamlit UI. Optimized for deployment with Triton Inference Server and TensorRT.

## Features

- 📄 Upload and preview PDF/TXT documents
- 📝 Generate abstractive summaries using BART
- ❓ Ask questions about the content using DistilBERT
- 🧪 Easily extensible to run on Triton + TensorRT
- 🐳 Docker-ready

## 📦 Installation

```bash
git clone https://github.com/srivinyadonepudi/LLM-Document-Summarization-QA-System.git
cd LLM-Document-Summarization-QA-System
pip install -r requirements.txt
streamlit run app.py
```
Docker Usage
```bash
docker build -t llm-qa-app .
docker run -p 8501:8501 llm-qa-app
```



