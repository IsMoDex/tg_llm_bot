from . import start, help, unknown, message
from utils.logger import logger
from aiogram import Router, Dispatcher

def register_handlers(dp: Dispatcher):
    try:
        dp.include_router(start.router)
        logger.info("✅ Роутер 'start' зарегистрирован")
    except Exception as e:
        logger.exception("❌ Ошибка при регистрации 'start' роутера")

    try:
        dp.include_router(help.router)
        logger.info("✅ Роутер 'help' зарегистрирован")
    except Exception as e:
        logger.exception("❌ Ошибка при регистрации 'help' роутера")

    try:
        dp.include_router(message.router)
        logger.info("✅ Роутер 'message' зарегистрирован")
    except Exception as e:
        logger.exception("❌ Ошибка при регистрации 'message' роутера")

    try:
        dp.include_router(unknown.router)
        logger.info("✅ Роутер 'unknown' зарегистрирован")
    except Exception as e:
        logger.exception("❌ Ошибка при регистрации 'unknown' роутера")
