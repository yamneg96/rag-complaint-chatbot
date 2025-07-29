import streamlit as st
from src.rag_pipeline import retrieve_context, generate_answer

st.title("CrediTrust Complaint Chatbot")
query = st.text_input("Ask a question about customer complaints")

if st.button("Submit"):
    with st.spinner("Retrieving and answering..."):
        results = retrieve_context(query)
        docs = results['documents'][0]
        answer = generate_answer(query, docs)
        st.markdown("### 💬 Answer")
        st.write(answer)

        st.markdown("### 📄 Sources")
        for i, doc in enumerate(docs):
            st.markdown(f"**Chunk {i+1}:** {doc}")