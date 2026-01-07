class ContextManager:
    def __init__(self, max_tokens: int = 4000):
        self.max_tokens = max_tokens
    
    def count_tokens(self, text: str) -> int:
        return len(text.split())
    
    def truncate_context(self, context: str) -> str:
        if self.count_tokens(context) <= self.max_tokens:
            return context
        words = context.split()
        return " ".join(words[:self.max_tokens])