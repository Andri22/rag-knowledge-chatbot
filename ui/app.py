import sys
import streamlit as st
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.document_processing.loaders import loadfile
from src.document_processing.chunking import chunk_text
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP, COLLECTION_NAME, SIMILARITY_THRESHOLD, TOP_K
from src.vector_store.qdrant_client import create_collection, add_documents,delete_by_source
from src.embeddings.embedding_service import get_openai_embedding
from src.retrieval.retriever import search
from src.pipeline.rag_pipeline import ask

# 1. Page config
st.set_page_config(page_title="RAG Knowledge Chatbot", layout="wide", page_icon="🐯")

# 2. Title
st.title("RAG Knowledge Chatbot")

# 3. Load document
# ✅ Hanya load sekali
if "indexed" not in st.session_state:
    with st.spinner("Loading document..."):
        source = "data/sample_docs/Tiger.pdf"
        raw_text = loadfile(source)
        chunks = chunk_text(raw_text, CHUNK_SIZE, CHUNK_OVERLAP)
        embeddings = [get_openai_embedding(chunk) for chunk in chunks]
        create_collection(COLLECTION_NAME)
        delete_by_source(COLLECTION_NAME, source=source)
        add_documents(COLLECTION_NAME, chunks, embeddings, source=source)
    st.session_state.indexed = True

# 4. Chat input
query = st.text_input("Ask a question about tigers:")

# 5. Chat history
if query:
    with st.spinner("Thinking..."):
        response = ask(query)
    st.write(response)

