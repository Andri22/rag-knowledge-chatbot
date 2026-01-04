# src/retrieval/retriever.py
from src.vector_store.qdrant_client import get_client
from config.settings import COLLECTION_NAME
from src.embeddings.embedding_service import get_openai_embedding
from src.utils.logger import get_logger

logger = get_logger(__name__)

def search(query: str, top_k: int, similarity_threshold: float) -> list[dict]:
    """
    1. Embed query pakai get_openai_embedding()
    2. Search di Qdrant pakai client.search()
    3. Return hasil dengan text dan score
    """
    client = get_client()
    query_embedding = get_openai_embedding(query)
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k
    ).points
    filtered_results = [r for r in results if r.score >= similarity_threshold]
    logger.info(f"Found {len(filtered_results)} results for query '{query}'")
    return [{"text": r.payload["text"], "score": r.score,"source": r.payload["source"]} for r in filtered_results]