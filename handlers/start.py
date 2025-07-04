from aiogram import Router, F
from aiogram.types import Message
from utils.responses import get_response

router = Router()

@router.message(F.text.lower() == "/start")
async def start_handler(message: Message):
    # Просто отправляем приветствие — системный prompt уже
    # подставится автоматически при первом add_to_context/get_context
    await message.answer(get_response("start"))
