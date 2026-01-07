import re

def add_citations(response: str, sources: list[dict]) -> str:
    if not isinstance(response, str):
        response = str(response)
    
    formatted = response.strip()
    
    citation_map = {}
    seen_files = set()  # Track unique filenames
    lines_to_append = []
    citation_num = 0
    
    for src in sources:
        text = src.get("text")
        source_file = src.get("filename") or src.get("source")
        if text and source_file and source_file not in seen_files:
            citation_num += 1
            seen_files.add(source_file)
            pattern = re.escape(text)
            if pattern in formatted:
                formatted = re.sub(pattern, f"{text} [{citation_num}]", formatted)
            citation_map[text] = citation_num
            lines_to_append.append(f"[{citation_num}] {source_file}")
    
    if lines_to_append:
        formatted += "\n\n📚 References:\n" + "\n".join(lines_to_append)
    
    return formatted

def extract_citations(response: str) -> list[str]:
    if not isinstance(response, str):
        response = str(response)
    
    matches = re.findall(r"\[(\d+)\]", response)
    return matches
