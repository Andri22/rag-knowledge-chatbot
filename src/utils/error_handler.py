# 1. Base exception
class RAGException(Exception):
    pass

# 2. Exception untuk Document Processing
class DocumentProcessingError(RAGException):
    pass

# 3. Exception untuk Embedding
class EmbeddingError(RAGException):
    pass

# 4. Exception untuk Vector Store
class VectorStoreError(RAGException):
    pass

# 5. Exception untuk Retrieval
class RetrievalError(RAGException):
    pass

# 6. Exception untuk Generation
class GenerationError(RAGException):
    pass