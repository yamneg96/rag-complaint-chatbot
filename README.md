# CrediTrust Complaint Chatbot

A Retrieval-Augmented Generation (RAG) system that turns unstructured financial complaints into insights for product and compliance teams.

## 💼 Features
- Semantic search over customer complaint narratives
- Retrieval using ChromaDB
- Generation with LLMs (Mistral, LLaMA, etc.)
- Streamlit user interface

## 🚀 How to Run
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py