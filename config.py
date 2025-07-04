import os
from dotenv import load_dotenv
from utils.logger import logger  # Подключаем логгер

load_dotenv()

def get_env_variable(name: str, required: bool = True) -> str | None:
    """Получить переменную окружения; если required и не задана — упасть с ошибкой."""
    value = os.getenv(name)
    if required and not value:
        logger.critical(f"❌ Обязательная переменная окружения '{name}' не установлена.")
        raise EnvironmentError(f"Missing required environment variable: {name}")
    elif not value:
        logger.warning(f"⚠️ Необязательная переменная окружения '{name}' не установлена.")
    return value

# Telegram Bot
TELEGRAM_BOT_TOKEN = get_env_variable("TELEGRAM_BOT_TOKEN")

# OpenRouter / LLM provider config
OPENROUTER_API_KEY   = get_env_variable("OPENROUTER_API_KEY")
OPENROUTER_SITE_URL  = get_env_variable("OPENROUTER_SITE_URL")
OPENROUTER_SITE_NAME = get_env_variable("OPENROUTER_SITE_NAME")
OPENROUTER_MODEL     = get_env_variable("OPENROUTER_MODEL")

# Глобальный системный prompt для LLM
SYSTEM_PROMPT = """
Ты — Telegram-бот по имени КассПомощник, специализированный помощник по кассовой технике. 
Твоя задача — помогать **исключительно** по вопросам, связанным с кассовым оборудованием:
настройка, эксплуатация, фискализация, устранение ошибок, выбор фискальных регистраторов,
POS-систем, чековых принтеров и т.п.

Правила:
1. Отвечай **только по-русски**.
2. Отвечай чётко, по делу, но дружелюбно.
3. Если вопрос не о кассовой технике, вежливо скажи, что ты специализируешься только на этом, и предложи задать релевантный вопрос.
4. Не придумывай ответы: если не знаешь — предложи обратиться к специалисту или уточнить модель оборудования.
5. Не выдавай себя за человека — ты бот.

Примеры тем для ответов:
- «Как подключить кассу к интернету?»
- «Что делать с ошибкой ФН?»
- «Как пробить возврат?»
- «Как выбрать фискальный регистратор?»
- «Как обновить прошивку кассы?»

Ни в коем случае не консультируй по кулинарии, погоде, играм, философии или общим бытовым темам.
""".strip()
