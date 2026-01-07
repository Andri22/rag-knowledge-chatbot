from src.utils.logger import get_logger

logger = get_logger(__name__)

def format_response(response: str) -> str:
    if not isinstance(response, str):
        logger.warning("format_response: response bukan string, converting to str")
        response = str(response)
    return response.strip()

def format_with_sources(response: str, sources: list[str]) -> str:
    if not isinstance(response, str):
        logger.warning("format_with_sources: response bukan string, converting to str")
        response = str(response)
    formatted = response.strip()
    if sources:
        formatted += "\n\n📚 Sources:\n"
        for source in sources:
            if not isinstance(source, str):
                logger.warning("format_with_sources: source bukan string, converting to str")
                source = str(source)
            formatted += f"- {source}\n"
    return formatted

def format_error(error_message: str) -> str:
    if not isinstance(error_message, str):
        logger.warning("format_error: error_message bukan string, converting to str")
        error_message = str(error_message)
    return f"⚠️ Error: {error_message}"