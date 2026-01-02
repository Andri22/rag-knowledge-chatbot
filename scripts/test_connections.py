# Cuma 15 baris!
from dotenv import load_dotenv
import os
from groq import Groq
from qdrant_client import QdrantClient
from openai import OpenAI
load_dotenv()

def test_groq():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Say hello!"}],
        max_tokens=10
    )
    return print(response.choices[0].message.content)


def test_qdrant():
    client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
    )
    collections = client.get_collections()
    return print(f"✅ Qdrant connected! Collections: {len(collections.collections)}")

def test_openai():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input="Hello world"
    )
    return print(f"✅ OpenAI connected! Embedding dim: {len(response.data[0].embedding)}")

def main():
    test_groq()
    test_qdrant()
    test_openai()

if __name__ == "__main__":
    main()