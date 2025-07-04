import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Папка и файл логов
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "bot.log"

# Настройка логгера
logger = logging.getLogger("tg_llm_bot")
logger.setLevel(logging.DEBUG)  # Глобальный уровень логгера

# Формат логов
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Файловый логгер (с ротацией и utf-8)
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding='utf-8'
)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Консольный логгер (stdout, для всех уровней включая ошибки)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Добавляем обработчики
logger.addHandler(file_handler)
logger.addHandler(console_handler)
