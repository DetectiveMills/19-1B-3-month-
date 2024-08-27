"""
Нужно написать телеграм бот который выдает персональный код клиента и адрес склада в Китае 24/7
Даёт шаблон заполнения в китайских приложениях, и также все данные сохраняет у себя в базе данных.
От клиента мы получаем имя, фамилия, телефонный номер далее выдаем 7 значный  персональный код по типу
KRE-145
и потом сохраните это все у тебя в базе данных
"""

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext 
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup

import asyncio, logging, sqlite3, random
from config import TOKEN
from cod import code
from test_3_db import create_database, save_emails

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

router = Router()
create_database()

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    surname = State()
    phone_number = State()
    
@router.message(CommandStart())
async def start(message:Message, state:FSMContext):
    await state.set_state(Form.name)
    await message.answer("Здравствуйте! Пожалуйста введите свое имя: ")

@router.message(Form.name)
async def name(message:Message, state:FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Form.surname)
    await message.answer("Хорошо, теперь введите свое фамилие: ")

@router.message(Form.surname)
async def surname(message:Message, state:FSMContext):
    await state.update_data(surname = message.text)
    await state.set_state(Form.phone_number)
    await message.answer("Теперь свой контактный номер: ")

@router.message(Form.phone_number)
async def phone_number(message:Message, state:FSMContext):
    await state.update_data(phone_number = message.text)
    data = await state.get_data()
    name = data.get('name')
    surname = data.get('surname')
    phone_number = data.get('phone_number')
    cod = random.choice(list(code))
    await bot.send_message(
        message.chat.id,
        f'Твое имя: {name}\nФамилие: {surname}\nНомер: {phone_number}\nКод: {cod}',
    )
    await state.clear()
    save_emails(name, surname, phone_number, cod)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())