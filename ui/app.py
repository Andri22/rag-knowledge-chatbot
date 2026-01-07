import sys
import streamlit as st
import hashlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.document_processing.loaders import load_multiple_files
from src.document_processing.chunking import chunk_text
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP, COLLECTION_NAME, SIMILARITY_THRESHOLD, TOP_K
from src.vector_store.qdrant_client import create_collection, add_documents,delete_by_source
from src.embeddings.embedding_service import get_openai_embedding
from src.pipeline.rag_pipeline import ask
from src.memory.conversation_buffer import ConversationBuffer
from src.generation.response_formatter import format_with_sources
from src.generation.citation_handler import add_citations, extract_citations

# 1. Page config
st.set_page_config(page_title="RAG Knowledge Chatbot", layout="wide", page_icon="🐯")

# 2. Title
st.title("RAG Knowledge Chatbot")

#3. File uploader
uploaded_files = st.file_uploader("Upload PDF", type=["pdf", "txt", "doc", "docx"], accept_multiple_files=True)
process_btn = st.button("Process Documents") if uploaded_files else False

if "buffer" not in st.session_state:
    st.session_state.buffer = ConversationBuffer(max_messages=10)

if process_btn and uploaded_files:
    with st.spinner("Processing..."):
        raw_text = load_multiple_files(uploaded_files)
        # Buat source_id SETELAH raw_text ada
        filenames = ", ".join([f.name for f in uploaded_files])
        content_hash = hashlib.md5(raw_text.encode()).hexdigest()[:8]
        source_id = f"{content_hash}"

        chunks = chunk_text(raw_text, CHUNK_SIZE, CHUNK_OVERLAP)
        embeddings = [get_openai_embedding(chunk) for chunk in chunks]
        create_collection(COLLECTION_NAME)
        delete_by_source(COLLECTION_NAME, source=source_id)
        add_documents(COLLECTION_NAME, chunks, embeddings, source=source_id, filename=filenames)
        st.session_state.indexed = True
        st.success(f"✅ Processed {filenames} (ID: {source_id})")


if not uploaded_files:
    st.session_state.indexed = False
    st.info("📄 Please upload and process documents first")

from src.retrieval.retriever import search
from config.settings import TOP_K, SIMILARITY_THRESHOLD

# 5. Chat history
if st.session_state.get("indexed"):
    query = st.text_input("Ask a question:")
    if query:
        with st.spinner("Thinking..."):
            st.session_state.buffer.add_message("user",query)
            # Tambah ini untuk ambil sources:
            results = search(query, TOP_K, SIMILARITY_THRESHOLD)
            response = ask(query)
            st.session_state.buffer.add_message("assistant",response)
            formatted_response = add_citations(response, results)
            st.write(formatted_response)




