from src.retrieval.retriever import search
from src.generation.prompt_builder import build_rag_prompt
from src.generation.llm_service import generate_response
from config.settings import TOP_K, SIMILARITY_THRESHOLD
from src.utils.logger import get_logger
logger = get_logger(__name__)

def ask(query: str) -> str:
    """
    Pipeline untuk melakukan RAG
    """
    #1. Search di Qdrant
    results = search(query, TOP_K, SIMILARITY_THRESHOLD)
    #2. Extract context
    context = [r["text"] for r in results]  # Hanya ambil text saja
    #3. Build prompt
    prompt = build_rag_prompt(query, context)
    #4. Generate response
    logger.info(f"Generated prompt: {prompt}")
    return generate_response(prompt)