from dotenv import load_dotenv
import os

load_dotenv()

# =====================
# API KEYS
# =====================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# =====================
# VECTOR STORE (QDRANT)
# =====================
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "rag_demo")

# =====================
# EMBEDDINGS
# =====================
EMBEDDING_PROVIDER = "openai"  # openai | local
EMBEDDING_MODEL = "text-embedding-3-small"

# =====================
# LLM CONFIG
# =====================
# LLM_PROVIDER = "openai"  # openai | anthropic | groq
# LLM_MODEL = "gpt-4o-mini"

LLM_PROVIDER = "groq"  # Ubah dari "openai"
LLM_MODEL = "llama-3.1-8b-instant"  # Model Groq

LLM_TEMPERATURE = 0.2
LLM_MAX_TOKENS = 1024

# =====================
# CHUNKING
# =====================
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# =====================
# RETRIEVAL
# =====================
TOP_K = 5
SIMILARITY_THRESHOLD = 0.6

# =====================
# FEATURE FLAGS
# =====================
ENABLE_RERANKING = False
ENABLE_QUERY_EXPANSION = False
# 