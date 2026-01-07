from typing import List, Dict
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ConversationBuffer:
    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages: List[Dict] = []
    
    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)
    
    def get_messages(self) -> List[Dict]:
        return self.messages
    
    def clear(self):
        self.messages = []
    
    def get_last_n_messages(self, n: int) -> List[Dict]:
        return self.messages[-n:]