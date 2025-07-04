from collections import defaultdict
from utils.logger import logger

# Хранилище: user_id -> list[dict(role, content)]
user_history = defaultdict(list)

def add_message(user_id: int, role: str, content: str):
    """Добавляет сообщение в историю пользователя."""
    if role not in {"system", "user", "assistant"}:
        logger.warning(f"⚠️ Неизвестная роль: {role}")
        return
    user_history[user_id].append({"role": role, "content": content})
    logger.debug(f"💬 [{role}] {user_id}: {content}")

def get_history(user_id: int, limit: int = 20) -> list[dict]:
    """Возвращает последние сообщения пользователя в формате [{role, content}, ...]."""
    history = user_history[user_id][-limit:]
    logger.debug(f"📜 История пользователя {user_id}: {history}")
    return history

def clear_history(user_id: int):
    """Очищает историю сообщений пользователя."""
    user_history[user_id].clear()
    logger.info(f"🧹 История пользователя {user_id} очищена.")
