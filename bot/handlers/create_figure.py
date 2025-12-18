from aiogram import F, Router
from aiogram.types import Message

from app.const import KB_TEXT_CREATE_FIGURE

create_figure_router = Router()


@create_figure_router.message(F.text == KB_TEXT_CREATE_FIGURE)
async def message_handler(message: Message) -> None:
    await message.answer('Create figure logic!')
