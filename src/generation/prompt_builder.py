def build_rag_prompt(query: str, context: list[str]) -> str:
    # Gabungkan query + context hasil search jadi prompt RAG
    context_str = "\n".join(context)

    prompt = f"""Based ONLY on the following information:
{context_str}

Question: {query}

INSTRUCTIONS:
- Answer ONLY based on the information above
- DO NOT add information from outside the document
- Keep your answer in English
- If information is not available, say "Information not found in the document"
"""
    return prompt