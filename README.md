rag-knowledge-chatbot/
│
├── README.md                          # Project overview, setup instructions, architecture
├── requirements.txt                   # All Python dependencies
├── .env.example                       # Example environment variables
├── .gitignore                         # Git ignore file
│
├── config/
│   ├── __init__.py
│   ├── settings.py                    # Configuration management (API keys, model settings)
│   └── prompts.py                     # All prompt templates stored here
│
├── data/
│   ├── raw/                           # Uploaded documents stored here
│   │   ├── pdfs/
│   │   ├── docs/
│   │   └── txt/
│   ├── processed/                     # Processed/chunked documents
│   └── sample_docs/                   # Demo documents for portfolio
│
├── src/
│   ├── __init__.py
│   │
│   ├── document_processing/
│   │   ├── __init__.py
│   │   ├── loaders.py                 # Document loaders (PDF, DOCX, CSV, web)
│   │   ├── chunking.py                # Chunking strategies (semantic, recursive, etc.)
│   │   ├── metadata_extractor.py     # Extract metadata from documents
│   │   └── preprocessor.py           # Clean and normalize text
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   ├── embedding_service.py      # Generate embeddings (OpenAI, sentence-transformers)
│   │   └── embedding_cache.py        # Cache embeddings to save costs
│   │
│   ├── vector_store/
│   │   ├── __init__.py
│   │   ├── qdrant_client.py          # Qdrant vector database operations
│   │   ├── collection_manager.py     # Create, delete, manage collections
│   │   └── indexing.py               # Index documents into vector store
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── retriever.py              # Main retrieval logic
│   │   ├── query_transformer.py      # Query expansion, reformulation, HyDE
│   │   ├── reranker.py               # Reranking logic (Cohere, cross-encoder)
│   │   ├── hybrid_search.py          # Combine semantic + keyword search
│   │   └── filters.py                # Metadata filtering logic
│   │
│   ├── generation/
│   │   ├── __init__.py
│   │   ├── llm_service.py            # LLM API calls (Claude, OpenAI, Groq)
│   │   ├── prompt_builder.py         # Build prompts with context
│   │   ├── response_formatter.py     # Format and structure responses
│   │   └── citation_handler.py       # Add source citations to answers
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── conversation_buffer.py    # Store conversation history
│   │   ├── context_manager.py        # Manage conversation context
│   │   └── summarizer.py             # Summarize long conversations
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── rag_pipeline.py           # Main RAG orchestration
│   │   ├── ingestion_pipeline.py     # Document ingestion workflow
│   │   └── query_pipeline.py         # Query processing workflow
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py                 # Logging configuration
│       ├── error_handler.py          # Error handling utilities
│       └── helpers.py                # General utility functions
│
├── evaluation/
│   ├── __init__.py
│   ├── test_dataset.json             # Test questions and ground truth answers
│   ├── metrics.py                    # Evaluation metrics (RAGAS, custom)
│   ├── evaluator.py                  # Run evaluations
│   └── benchmark_results.json        # Store evaluation results
│
├── ui/
│   ├── app.py                        # Main Streamlit application
│   ├── components/
│   │   ├── __init__.py
│   │   ├── sidebar.py                # Sidebar configuration UI
│   │   ├── chat_interface.py         # Chat UI components
│   │   ├── document_uploader.py      # File upload interface
│   │   └── source_display.py         # Display retrieved sources
│   └── styles/
│       └── custom.css                # Custom CSS styling
│
├── tests/
│   ├── __init__.py
│   ├── test_document_processing.py
│   ├── test_embeddings.py
│   ├── test_retrieval.py
│   ├── test_generation.py
│   └── test_pipeline.py
│
├── notebooks/
│   ├── 01_chunking_experiments.ipynb      # Test different chunking strategies
│   ├── 02_retrieval_comparison.ipynb      # Compare retrieval methods
│   ├── 03_reranking_analysis.ipynb        # Measure reranking impact
│   └── 04_evaluation_results.ipynb        # Visualize evaluation metrics
│
├── scripts/
│   ├── setup_vector_db.py            # Initialize Qdrant collection
│   ├── ingest_documents.py           # Batch document ingestion
│   ├── run_evaluation.py             # Run full evaluation suite
│   └── export_data.py                # Export vector store data
│
├── docs/
│   ├── architecture.md               # System architecture documentation
│   ├── setup_guide.md                # Detailed setup instructions
│   ├── api_reference.md              # API documentation
│   ├── chunking_analysis.md          # Results from chunking experiments
│   └── evaluation_report.md          # Evaluation results and insights
│
├── deployment/
│   ├── Dockerfile                    # Docker container configuration
│   ├── docker-compose.yml            # Multi-container setup
│   ├── requirements-prod.txt         # Production dependencies
│   └── streamlit_config.toml         # Streamlit deployment config
│
└── assets/
    ├── architecture_diagram.png      # System architecture visual
    ├── demo_screenshot.png           # UI screenshot for README
    └── logo.png                      # Project logo (optional)