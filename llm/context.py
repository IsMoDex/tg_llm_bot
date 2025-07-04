from collections import defaultdict
from config import SYSTEM_PROMPT

# Хранилище контекстов: chat_id -> list[{"role": ..., "content": ...}]
_context_store = defaultdict(list)

def _ensure_system_prompt(chat_id: int):
    """Если в начале контекста нет system, вставляем SYSTEM_PROMPT."""
    ctx = _context_store[chat_id]
    if not ctx or ctx[0]["role"] != "system":
        # Вставляем на 0-ю позицию
        ctx.insert(0, {"role": "system", "content": SYSTEM_PROMPT})

def add_to_context(chat_id: int, role: str, content: str):
    """Добавить любое сообщение в контекст."""
    _ensure_system_prompt(chat_id)
    _context_store[chat_id].append({"role": role, "content": content})

def get_context(chat_id: int) -> list[dict]:
    """
    Возвращает текущий контекст, гарантируя,
    что первым будет system-сообщение из конфига.
    """
    _ensure_system_prompt(chat_id)
    return _context_store[chat_id]

def set_system_prompt(chat_id: int, prompt: str):
    """
    Позволяет переопределить системный prompt для конкретного чата.
    Если он уже был, заменяем, иначе вставляем.
    """
    ctx = _context_store[chat_id]
    if ctx and ctx[0]["role"] == "system":
        ctx[0]["content"] = prompt
    else:
        ctx.insert(0, {"role": "system", "content": prompt})

def clear_context(chat_id: int):
    """Полностью сбросить историю данного чата."""
    _context_store[chat_id].clear()
