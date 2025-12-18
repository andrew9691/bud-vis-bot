import pandas as pd

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.methods.get_file import GetFile
from aiogram.types import Message

from app.const import KB_TEXT_UPLOAD_FILE
from bot.states import UploadState

upload_file_router = Router()


@upload_file_router.message(F.text == KB_TEXT_UPLOAD_FILE)
async def upload_file_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(UploadState.waiting_file)
    await message.answer('Send a file')


@upload_file_router.message(UploadState.waiting_file, F.document)
async def upload_file_finish_handler(message: Message, state: FSMContext, bot: Bot) -> None:

    file = await bot(GetFile(file_id=message.document.file_id))
    content = await bot.download_file(file.file_path)
    df = pd.read_excel(content.read())
    h = df.head()
    print(h)

    await state.clear()
    await message.answer('File data saved!')
