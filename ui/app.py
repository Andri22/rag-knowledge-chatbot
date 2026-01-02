import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.document_processing.loaders import loadfile
from src.document_processing.chunking import chunk_text
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP, COLLECTION_NAME
from src.vector_store.qdrant_client import create_collection, add_documents
from src.embeddings.embedding_service import get_openai_embedding

def main():
    raw_text = loadfile("data/sample_docs/coba.txt")
    chunks = chunk_text(raw_text, CHUNK_SIZE, CHUNK_OVERLAP)
    embeddings = [get_openai_embedding(chunk) for chunk in chunks]
    create_collection(COLLECTION_NAME)
    add_documents(COLLECTION_NAME, chunks, embeddings)
    print(f"✅ Documents added to Qdrant: {len(chunks)}")
    
if __name__ == "__main__":
    main()