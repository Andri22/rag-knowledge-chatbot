from dotenv import load_dotenv
load_dotenv()
from config.settings import GROQ_API_KEY, LLM_MODEL
from src.utils.logger import get_logger

logger = get_logger(__name__)
from groq import Groq

def generate_response(prompt: str) -> str:
    try:
        client = Groq(
            api_key=GROQ_API_KEY,
        )
        chat_completion = client.chat.completions.create(
            messages=[
            {
            "role": "user",
            "content": prompt,
            }],
            model=LLM_MODEL,
        )
        result = chat_completion.choices[0].message.content
        logger.info(f"Generated response: {result}")
        return result

    except Exception as e:
        logger.error(f"Failed to generate response: {str(e)}")
        raise RuntimeError(f"Failed to generate response: {str(e)}")