from aiogram import Bot, Dispatcher
from database import Database
TOKEN = "7854951293:AAGIE1n0w1qLNfXLogTpAqKpp3AQx2bRg9s"

bot = Bot(token=TOKEN)
dp = Dispatcher()
database = Database("db.sqlite3")