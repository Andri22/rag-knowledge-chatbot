from typing import List, Dict
class Summarizer:
    def summarize(self, messages: List[Dict]) -> str:
        text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
        return text