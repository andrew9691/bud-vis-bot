from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.const import KB_TEXT_CREATE_FIGURE, KB_TEXT_UPLOAD_FILE


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=KB_TEXT_CREATE_FIGURE)],
        [KeyboardButton(text=KB_TEXT_UPLOAD_FILE)],
    ],
    resize_keyboard=True,
)
