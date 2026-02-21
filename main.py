import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import router
from database import init_db

init_db()
#TOKEN = os.getenv("BOT_TOKEN")
TOKEN = "8277724959:AAHBIylRRcVnuAD1_1ytjQhStvRzx2LdHbo"



bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
