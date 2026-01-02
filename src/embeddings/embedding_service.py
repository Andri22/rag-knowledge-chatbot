from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
from config.settings import EMBEDDING_MODEL


def get_openai_embedding(text: str) -> list[float]:
    if not text:
        raise ValueError("Text must not be empty")

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.embeddings.create(
            input=text,
            model=EMBEDDING_MODEL
        )
        return response.data[0].embedding
    except Exception as e:
        raise RuntimeError(f"Failed to get OpenAI embedding: {str(e)}")