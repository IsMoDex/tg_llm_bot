from aiogram import Router, F
from aiogram.types import Message

from llm.context import add_to_context, get_context
from llm.api_llm_route import get_llm_response

router = Router()

@router.message(F.text)
async def handle_message(message: Message):
    chat_id = message.chat.id
    user_text = message.text

    # Добавляем сообщение пользователя в контекст
    add_to_context(chat_id, "user", user_text)

    # Получаем весь контекст (включая system)
    context = get_context(chat_id)

    # Отправляем в LLM
    response = await get_llm_response(context)

    # Добавляем ответ бота в контекст
    add_to_context(chat_id, "assistant", response)

    await message.answer(response)
