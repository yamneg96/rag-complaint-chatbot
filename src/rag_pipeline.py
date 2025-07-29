from sentence_transformers import SentenceTransformer
import chromadb
from transformers import pipeline

prompt_template = (
    "You are a financial analyst assistant for CrediTrust. "
    "Use only the following retrieved complaint excerpts to answer the user's question. "
    "If the context is insufficient, say so.\n\n"
    "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
)

def retrieve_context(query, k=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vec = model.encode(query)
    db = chromadb.Client()
    collection = db.get_collection('complaints')
    results = collection.query(query_embeddings=[query_vec], n_results=k)
    return results

def generate_answer(question, context_chunks):
    context = "\n".join(context_chunks)
    prompt = prompt_template.format(context=context, question=question)
    llm = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")
    return llm(prompt, max_length=512)[0]['generated_text']