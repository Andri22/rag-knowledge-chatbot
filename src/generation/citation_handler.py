import re

def add_citations(response: str, sources: list[dict]) -> str:
    if not isinstance(response, str):
        response = str(response)
    
    formatted = response.strip()
    
    citation_map = {}
    lines_to_append = []
    
    for i, src in enumerate(sources, start=1):
        text = src.get("text")
        source_file = src.get("source")
        if text and source_file:
            pattern = re.escape(text)
            if pattern in formatted:
                formatted = re.sub(pattern, f"{text} [{i}]", formatted)
            citation_map[text] = i
            lines_to_append.append(f"[{i}] {source_file}")
    
    if lines_to_append:
        formatted += "\n\n📚 References:\n" + "\n".join(lines_to_append)
    
    return formatted

def extract_citations(response: str) -> list[str]:
    if not isinstance(response, str):
        response = str(response)
    
    matches = re.findall(r"\[(\d+)\]", response)
    return matches
