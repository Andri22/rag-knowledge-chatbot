import re
from src.utils.logger import get_logger

logger = get_logger(__name__)

def clean_text(text: str) -> str:
    cleaned = re.sub(r'\s+', ' ', text).strip()
    return cleaned

def remove_special_chars(text: str, keep_punctuation: bool = True) -> str:
    if keep_punctuation:
        pattern = r'[^\w\s.,!?;:]'
    else:
        pattern = r'[^\w\s]'
    return re.sub(pattern, '', text)

def normalize_text(text: str, keep_punctuation: bool = True) -> str:
    cleaned = clean_text(text)
    return remove_special_chars(cleaned, keep_punctuation)