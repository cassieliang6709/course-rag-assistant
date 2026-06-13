from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    text: str
    source: str
    index: int


def chunk_text(text: str, source: str, max_words: int = 120) -> list[Chunk]:
    words = text.split()
    chunks: list[Chunk] = []

    for start in range(0, len(words), max_words):
        chunk_words = words[start : start + max_words]
        chunks.append(Chunk(text=" ".join(chunk_words), source=source, index=len(chunks)))

    return chunks
