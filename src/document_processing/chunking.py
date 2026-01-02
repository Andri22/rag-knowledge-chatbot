import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.helpers import save_json

def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
    # Validasi input
    if not text:  # Kosong atau None
        return []
    
    if chunk_size <= 0:
        raise ValueError("chunk_size harus > 0")
    
    if chunk_overlap >= chunk_size:
        raise ValueError("overlap harus < chunk_size")
    step = chunk_size - chunk_overlap  # ← Ini kunci overlap!
    chunks = [text[i : i + chunk_size] for i in range(0, len(text), step)]
    save_json("data/processed/text_chunks.json", chunks)
    return chunks