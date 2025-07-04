import json
from pathlib import Path

# Определяем путь к responses.json в корне проекта
RESPONSES_FILE = Path(__file__).parent.parent / "responses.json"

try:
    with open(RESPONSES_FILE, encoding="utf-8") as f:
        RESPONSES = json.load(f)
except FileNotFoundError:
    RESPONSES = {}

def get_response(key: str) -> str:
    """Возвращает текст ответа по ключу или пустую строку, если ключ не найден."""
    return RESPONSES.get(key, "")
