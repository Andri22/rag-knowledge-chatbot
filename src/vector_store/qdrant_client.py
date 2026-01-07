from qdrant_client import QdrantClient, models
from qdrant_client.models import Distance, VectorParams, PointStruct
from config.settings import QDRANT_URL, QDRANT_API_KEY
from src.utils.logger import get_logger
from src.utils.error_handler import VectorStoreError

logger = get_logger(__name__)

def get_client():
    return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def create_collection(name: str, vector_size: int = 1536):
    client = get_client()
    # Cek apakah collection sudah ada
    collections = [c.name for c in client.get_collections().collections]
    if name in collections:
        logger.info(f"Collection '{name}' already exists, skipping creation")
        # Pastikan index ada (kalau belum)
        try:
            client.create_payload_index(
                collection_name=name,
                field_name="source",
                field_schema="keyword"
            )
        except Exception:
            pass  # Index mungkin sudah ada
        return False

    client.create_collection(
        collection_name=name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
    
    client.create_payload_index(
        collection_name=name,
        field_name="source",
        field_schema="keyword"
    )

    logger.info(f"Collection '{name}' created successfully")
    return True

def add_documents(collection_name: str, chunks: list[str], embeddings: list, source: str, filename: str = None):
    client = get_client()
    points = [
        PointStruct(id=i, vector=emb, payload={"text": chunk, "source": source, "filename": filename or source})
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings))
    ]
    client.upsert(collection_name=collection_name, points=points)
    logger.info(f"Documents added to collection '{collection_name}'")
    return len(chunks)

def delete_by_source(collection_name: str, source: str):
    """Hapus semua points dari file tertentu"""
    try:
        existing_sources = list_sources(collection_name)
    except Exception:
        logger.info(f"Collection '{collection_name}' not ready, skipping delete")
        return 

    # Cek apakah source ada
    if source not in existing_sources:
        logger.info(f"Source '{source}' not found, nothing to delete")
        return  # Skip, tidak perlu delete

    try:
        client = get_client()
        client.delete(
            collection_name=collection_name,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[models.FieldCondition(
                        key="source",
                        match=models.MatchValue(value=source)
                    )]
                )
            )
        )
    except Exception as e:
        logger.error(f"Failed to delete documents from collection '{collection_name}': {str(e)}")
        raise VectorStoreError(f"Failed to delete documents from collection '{collection_name}': {str(e)}")

def list_sources(collection_name: str) -> list[str]:
    """List semua file yang sudah di-index"""
    client = get_client()
    
    # Scroll semua points dan ambil unique sources
    results = client.scroll(
        collection_name=collection_name,
        limit=1000,
        with_payload=["source"]
    )
    
    sources = set()
    for point in results[0]:
        if point.payload and "source" in point.payload:
            sources.add(point.payload["source"])
    
    logger.info(f"Found {len(sources)} unique sources in collection '{collection_name}'")
    return list(sources)