from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from config.settings import QDRANT_URL, QDRANT_API_KEY

def get_client():
    return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def create_collection(name: str, vector_size: int = 1536):
    client = get_client()
    client.create_collection(
        collection_name=name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
    return True

def add_documents(collection_name: str, chunks: list[str], embeddings: list):
    client = get_client()
    points = [
        PointStruct(id=i, vector=emb, payload={"text": chunk})
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings))
    ]
    client.upsert(collection_name=collection_name, points=points)
    return len(chunks)