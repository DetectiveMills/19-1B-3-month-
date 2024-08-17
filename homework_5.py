from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db import Database
from config import TOKEN
import logging, asyncio, sqlite3, time

from bs4 import BeautifulSoup
import requests

from db_hw5 import create_database
from db_hw5 import save_news


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
create_database()

logging.basicConfig(level=logging.INFO)

class NewsStates(StatesGroup):
    waiting_for_news = State()

def take_news():
    url = 'https://24.kg'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_news = soup.find_all('div', class_='title')

    news_list = []
    for news in all_news:
        news_list.append(news.text)
    return news_list

async def send_news(message: Message, news_list, state: FSMContext):
    for news in news_list:
        if await state.get_state() is None:
            return
        
        save_news(news)
        await message.answer(news)
        await asyncio.sleep(2)  

@dp.message(Command('start'))
async def start(message: Message):
    await message.reply("Привет! Команда /news присылает тебе новости. Если хочешь остановиться, воспользуйся командой /stop.")

@dp.message(Command('news'))
async def news_start(message: Message, state: FSMContext):
    await state.set_state(NewsStates.waiting_for_news)
    await message.reply("Начинаеться парсинг новостей. Пожалуйста, подождите...")
    
    news_list = take_news()
    await send_news(message, news_list, state)

@dp.message(Command('stop'))
async def stop(message: Message, state: FSMContext):
    await state.clear()
    await message.reply("Парсинг новостей остановлен")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())