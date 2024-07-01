import asyncio
import logging
import executor
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os
from tracking import get_status

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

# Логирование
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        await send_message_to_user()


@dp.message()
async def send_message_to_user(message: types.Message):
    result = get_status()
    await message.answer(result)


@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я буду присылать тебе результаты каждые полчаса.")


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(scheduled(1800))  # 1800 секунд = 30 минут
    dp.run_polling(bot)
