from qdrant_client import QdrantClient, models
from qdrant_client.models import Distance, VectorParams, PointStruct
from config.settings import QDRANT_URL, QDRANT_API_KEY

def get_client():
    return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def create_collection(name: str, vector_size: int = 1536):
    client = get_client()
    # Cek apakah collection sudah ada
    collections = [c.name for c in client.get_collections().collections]
    if name in collections:
        print(f"Collection '{name}' sudah ada, skip create")
        return False
    
    client.create_collection(
        collection_name=name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
    return True

def add_documents(collection_name: str, chunks: list[str], embeddings: list, source: str):
    client = get_client()
    points = [
        PointStruct(id=i, vector=emb, payload={"text": chunk, "source": source})
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings))
    ]
    client.upsert(collection_name=collection_name, points=points)
    return len(chunks)

def delete_by_source(collection_name: str, source: str):
    """Hapus semua points dari file tertentu"""
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
        print(f"Skip delete (no data or index): {source}")

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
    
    return list(sources)