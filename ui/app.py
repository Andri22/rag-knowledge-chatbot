import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.document_processing.loaders import loadfile
from src.document_processing.chunking import chunk_text
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP, COLLECTION_NAME, SIMILARITY_THRESHOLD, TOP_K
from src.vector_store.qdrant_client import create_collection, add_documents,delete_by_source
from src.embeddings.embedding_service import get_openai_embedding
from src.retrieval.retriever import search

def main():
    source = "data/sample_docs/Tiger.pdf"
    raw_text = loadfile(source)
    chunks = chunk_text(raw_text, CHUNK_SIZE, CHUNK_OVERLAP)
    embeddings = [get_openai_embedding(chunk) for chunk in chunks]
    create_collection(COLLECTION_NAME)
    delete_by_source(COLLECTION_NAME, source=source)
    add_documents(COLLECTION_NAME, chunks, embeddings, source=source)
    search("siapa sih saya?", TOP_K, SIMILARITY_THRESHOLD)
    print(f"✅ Documents added to Qdrant: {len(chunks)}")
    results = search("tiger diet", TOP_K, SIMILARITY_THRESHOLD)
    for r in results:
        print(f"Score: {r['score']:.3f} | {r['text'][:80]}...")
if __name__ == "__main__":
    main()