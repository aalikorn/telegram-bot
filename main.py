import asyncio

from handlers import about, form, help, start

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from antiflood import AntiFloodMiddleware

from database import start_db


bot = Bot('7158563123:AAE5nQ3TxgT0huEwdpVk25FJ9zQDc0iAKBE')
dp = Dispatcher()


async def main():
    await start_db()
    dp.message.middleware(AntiFloodMiddleware())
    dp.include_routers(
        start.router,
        form.router,
        help.router,
        about.router,
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


