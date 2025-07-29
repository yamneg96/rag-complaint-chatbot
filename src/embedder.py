from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb

def chunk_text(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return [splitter.split_text(text) for text in texts]

def generate_embeddings(text_chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return [model.encode(chunk) for chunk in text_chunks]

def store_in_chroma(chunks, embeddings, metadata):
    db = chromadb.Client()
    collection = db.get_or_create_collection('complaints')
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            metadatas=[metadata[i]],
            ids=[str(i)]
        )