import asyncio
import logging
from aiogram.types import Message

from aiogram import Bot, Dispatcher

from core.routers import main_router, registration
from core.db.config import settings


def register_messages(dp: Dispatcher):
    """
    Routers registration
    :param dp:
    """
    dp.include_router(registration.router)
    dp.include_router(main_router.router)


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(settings.TOKEN)
    dp = Dispatcher()

    register_messages(dp=dp)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.exception(e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info("Shutting down")
    ...
