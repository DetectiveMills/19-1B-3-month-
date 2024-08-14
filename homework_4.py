from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import logging, asyncio, sqlite3, time
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    direction = State()
    photo = State()

async def cancel_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Процесс отменен. Если хочешь заново начать нажми на /start")

dp.message.register(cancel_command, Command(commands="cancel"))

@dp.message(Command('start'))
async def start(message : Message, state : FSMContext):
    await state.set_state(Form.name)
    await message.reply("Привет, как тебя зовут?")

@dp.message(Form.name)
async def name(message : Message, state : FSMContext):
    await state.update_data(name = message.text)
    data = await state.get_data()
    name = data.get('name')
    await state.set_state(Form.direction)
    await message.answer(f"Привет, {name}. Напиши какое ты направление")

@dp.message(Form.direction)
async def direction(message : Message, state : FSMContext):
    await state.update_data(direction = message.text)
    await state.set_state(Form.photo)
    await message.answer("Отправь фото")

@dp.message(Form.photo, F.content_type.in_(['photo']))
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    direction = data.get('direction')
    photo_1 = message.photo[-1].file_id

    info_text = f'Имя: {name}\nНаправление: {direction}'
    await bot.send_message(chat_id = -4255458461, text = info_text)
    await bot.send_photo(chat_id = -4255458461, photo=photo_1)
    await state.clear()
    await message.answer("Спасибо! Все данные сохранены")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())

