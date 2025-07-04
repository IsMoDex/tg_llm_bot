from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.responses import get_response

router = Router()

@router.message(Command("unknown"))
async def unknown_command(message: Message):
    # Ответ для неизвестных команд
    await message.answer(get_response("unknown"))
