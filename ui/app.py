import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.document_processing.loaders import loadfile
from src.document_processing.chunking import chunk_text
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def main():
    raw_text = loadfile("data/sample_docs/Tiger.pdf")
    chunks = chunk_text(raw_text, CHUNK_SIZE, CHUNK_OVERLAP)
    print(chunks)
if __name__ == "__main__":
    main()