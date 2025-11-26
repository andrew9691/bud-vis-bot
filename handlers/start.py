import logging
import sqlalchemy as sa

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from app import settings
from db.models import User
from db.session import provide_session

logger = logging.getLogger(__name__)
start_router = Router()


@start_router.message(CommandStart())
@provide_session
async def cmd_start(session: AsyncSession, message: Message) -> None:
    user_id = message.from_user.id
    if user_id != settings.BOT_ADMIN_ID:
        await message.answer('You are not allowed to use this bot!')
        return

    user = await session.scalar(sa.select(User).where(User.id == user_id))
    if user:
        await message.answer('Welcome back!')
    else:
        new_user = User(
            id=user_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        session.add(new_user)
        await session.commit()
        logger.info('User %s registered', user_id)
        await message.answer(f'Welcome to budget visualizer bot, {message.from_user.first_name}!')
