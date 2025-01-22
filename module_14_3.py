import asyncio
import logging
from aiogram.fsm.state import StatesGroup, State
from aiogram import Bot, Dispatcher, F
from m_config import TOKEN
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)



kb0 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать')], [KeyboardButton(text='information')],
                         [KeyboardButton(text='Купить')]],
                         resize_keyboard=True)

kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')], [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
])

kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying')], [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
    [InlineKeyboardButton(text='Product3', callback_data='product_buying')], [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
])

d = {}

bot = Bot(token=TOKEN)
dp = Dispatcher()

class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()

@dp.message(F.text == 'Купить')
async def get_buying_list(message: Message):
    for number in range(1, 5):
        await message.answer(f'Название: Product{number} | Описание: описание {number} | Цена: {number * 100}')
        await  message.answer_photo(photo=FSInputFile(path=f'prod{number}.jpg'))
    await message.answer('Выберите продукт для покупки:', reply_markup=kb2)

@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=kb1)

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb0)

@dp.message(F.text == 'information')
async def get_info(message: Message, state: FSMContext):
    global d
    for key, value in d.items():
        await message.answer(str(key) + ': ' + str(value))

@dp.callback_query(F.data == 'calories')
async def set_sex(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.sex)
    await callback.answer('')
    await callback.message.answer('Write your sex (male / female)')

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
@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('for men: calories = 10*weight + 6.25*growth - 5*age + 5\nfor women: calories = 10*weight + 6.25*growth - 5*age + 161')
async def main():
    await dp.start_polling(bot)

@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы успешно приобрели продукт!')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())