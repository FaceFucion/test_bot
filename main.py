import asyncio
import logging

from config import dp, bot, database
from handlers import opros_router


async def on_startup(bot):
    database.create_tables()


async def main():
    dp.include_router(opros_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())