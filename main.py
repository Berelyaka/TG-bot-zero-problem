import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import router



TOKEN = os.getenv("8277724959:AAHBIylRRcVnuAD1_1ytjQhStvRzx2LdHbo") # токен через переменную окружения

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
