import re
from src.utils.logger import get_logger

logger = get_logger(__name__)

def clean_text(text: str) -> str:
    """
    Clean text:
    1. Normalize whitespace (multiple spaces → single)
    2. Remove extra newlines
    3. Strip leading/trailing whitespace
    """
    cleaned = re.sub(r'\s+', ' ', text).strip()
    return cleaned

def remove_special_chars(text: str, keep_punctuation: bool = True) -> str:
    """
    Remove special characters.
    If keep_punctuation=True, keep .,!?;:
    """
    if keep_punctuation:
        pattern = r'[^\w\s.,!?;:]'
    else:
        pattern = r'[^\w\s]'
    return re.sub(pattern, '', text)

def normalize_text(text: str, keep_punctuation: bool = True) -> str:
    """
    Full normalization:
    1. clean_text()
    2. remove_special_chars()
    3. lowercase (optional)
    """
    cleaned = clean_text(text)
    return remove_special_chars(cleaned, keep_punctuation)