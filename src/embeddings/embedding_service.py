from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
from config.settings import EMBEDDING_MODEL
from src.utils.logger import get_logger
from src.utils.error_handler import EmbeddingError

logger = get_logger(__name__)

def get_openai_embedding(text: str) -> list[float]:
    logger.info("Generating OpenAI embedding...")
    embedding = None
    if not text:
        raise EmbeddingError("Text must not be empty")

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.embeddings.create(
            input=text,
            model=EMBEDDING_MODEL
        )
        embedding = response.data[0].embedding
        logger.info("OpenAI embedding generated successfully")
        logger.debug(f"Embedding generated: {len(embedding)} dimensions")
        return embedding
    except Exception as e:
        logger.error(f"Failed to get OpenAI embedding: {str(e)}")
        raise EmbeddingError(f"Failed to get OpenAI embedding: {str(e)}")