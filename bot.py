import asyncio
from aiogram import Bot, Dispatcher
from config import TELEGRAM_BOT_TOKEN
from handlers import register_handlers
from utils.logger import logger  # Подключаем логгер
import sys
import traceback


async def main():
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        dp = Dispatcher()
        register_handlers(dp)

        logger.info("🤖 Бот запущен и готов к работе.")
        await dp.start_polling(bot)

    except Exception as e:
        logger.critical("❌ Ошибка при запуске бота:", exc_info=True)
        print("❌ Произошла ошибка при запуске бота. Подробности в логах.")
        # Можно также выводить в консоль трассировку, если нужно:
        traceback.print_exc()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("🛑 Бот остановлен пользователем.")
        sys.exit()
    except Exception as e:
        logger.critical("🔥 Критическая ошибка вне main():", exc_info=True)
        sys.exit(1)
