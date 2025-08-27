# uv run -m utils.generateSentence

from lib.openai import openai_client
import re

def generate_sentence(word: str) -> str:
    response = openai_client.responses.create(
        model="gpt-5-mini",
        reasoning={"effort": "minimal"},
        input=f"Generate a bland/boring short sentence which uses the word '{word}' one time. Only return the sentence."
    )
    return response.output_text

def split_sentence(sentence: str, word: str):
    m = re.search(rf'\b{re.escape(word)}\b', sentence, flags=re.IGNORECASE)
    if not m:
        raise ValueError("Word not found as a standalone token.")
    start, end = m.span()
    return {
        "prefix": sentence[:start].strip() or None,
        "word": sentence[start:end].strip(),
        "suffix": sentence[end:].strip() or None,
    }

if __name__ == "__main__":
    word = "go"
    sentence = generate_sentence(word=word)
    print(sentence)
    print(split_sentence(sentence, word))