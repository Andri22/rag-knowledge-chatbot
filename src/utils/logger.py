import logging
from config.settings import LOG_LEVEL

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    handler = logging.StreamHandler()
    handler.setLevel(getattr(logging, LOG_LEVEL))
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
