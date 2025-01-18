import asyncio
import logging
from aiogram.fsm.state import StatesGroup, State
from aiogram import Bot, Dispatcher
from alex_bot_config import TOKEN
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/calculate')],
                                   [KeyboardButton(text='/info')]],
                         resize_keyboard=True)

d = {}

bot = Bot(token=TOKEN)
dp = Dispatcher()

class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message(Command('info'))
async def get_info(message: Message, state: FSMContext):
    global d
    for key, value in d.items():
        await message.answer(str(key) + ': ' + str(value))

@dp.message(Command('calculate'))
async def set_sex(message: Message, state: FSMContext):
    await state.set_state(UserState.sex)
    await message.answer('Write your sex (male / female)')

@dp.message(UserState.sex)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(UserState.age)
    await message.answer('Write your age')

@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer('Write your growth')

@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Write your weight')

@dp.message(UserState.weight)
async def set_calories(message: Message, state: FSMContext):
    global d
    await state.update_data(weight=message.text)
    data = await state.get_data()
    d = data
    if data["sex"] == "male":
        calorie = (10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5)
    else:
        calorie = (10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161)

    await message.answer(f'Thank you! Your calorie allowance: {calorie}')
    await state.clear()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())