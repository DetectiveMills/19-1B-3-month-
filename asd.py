import schedule
import time
import requests

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import logging, asyncio, sqlite3, time
from config import TOKEN

def test():
    print("Hello Geeks")
    print(time.ctime())

def get_btc_price():
    print("=====BTC=====")
    url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    response = requests.get(url=url).json()
    # print(response)
    price = response.get('price')
    print(f"Стоимость биткоина {price}, {time.ctime()}")

get_btc_price()

# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at('19:27').do(test)
# schedule.every().thursday.at("19:29").do(test)
# schedule.every().day.at("19:30", "Asia/Bishkek").do(test)
# schedule.every().hour.at(":25").do(test)
schedule.every(2).seconds.do(get_btc_price)

while True:
    schedule.run_pending()