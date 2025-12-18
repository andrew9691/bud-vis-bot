import asyncio

from aiogram import Bot, Dispatcher

from app import settings
from bot.handlers import start_router, upload_file_router


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(upload_file_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
