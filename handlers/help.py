from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.responses import get_response

router = Router()

@router.message(Command("help"))
async def handle_help(message: Message):
    # Берём ответ из JSON по ключу "help"
    await message.answer(get_response("help"))
