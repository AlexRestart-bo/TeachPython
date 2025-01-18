import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from alex_bot_config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_message(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
