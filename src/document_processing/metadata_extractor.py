from pathlib import Path
from datetime import datetime
from src.utils.logger import get_logger
from src.utils.error_handler import DocumentProcessingError

logger = get_logger(__name__)

def extract_file_metadata(file_input) -> dict:

    metadata = {}

    # Cek apakah Streamlit UploadedFile
    if hasattr(file_input, "name") and hasattr(file_input, "size"):
        metadata["filename"] = file_input.name
        metadata["extension"] = Path(file_input.name).suffix
        metadata["size_bytes"] = file_input.size
        # UploadedFile tidak selalu punya created/modified
        metadata["created_at"] = None
        metadata["modified_at"] = None
        logger.info(f"File metadata: {metadata}")

    else:  # Anggap file path
        path = Path(file_input)
        if not path.exists():
            logger.error(f"File not found: {file_input}")
            raise DocumentProcessingError(f"File not found: {file_input}")

        metadata["filename"] = path.name
        metadata["extension"] = path.suffix
        metadata["size_bytes"] = path.stat().st_size
        metadata["created_at"] = datetime.fromtimestamp(path.stat().st_ctime)
        metadata["modified_at"] = datetime.fromtimestamp(path.stat().st_mtime)
        logger.info(f"File metadata: {metadata}")
    return metadata

def extract_chunk_metadata(text: str, chunk_index: int) -> dict:
    metadata = {
        "chunk_index": chunk_index,
        "char_count": len(text),
        "word_count": len(text.split()),
    }
    return metadata