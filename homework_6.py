from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand
from config import TOKEN
import requests, time, asyncio, aioschedule, logging

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

monitoring_btc = False
monitoring_etc = False
monitoring_ltc = False

reporting_btc = False
reporting_etc = False
reporting_ltc = False

async def get_btc_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    try:
        response = requests.get(url=url).json()
        price = response.get('price')
        if price:
            return f"Стоимость биткоина на {time.ctime()}, {price}"
        else:
            return f"Не удалось получить цену биткоина"
        
    except requests.RequestException as error:
        logging.error(f"Ошибка запроса BTC: {error}")
        return "Ошибка при запросе цены биткоина."
    
async def get_etc_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT"
    try:
        response = requests.get(url=url).json()
        price = response.get('price')
        if price:
            return f"Стоимость эфира на {time.ctime()}, {price}"
        else:
            return f"Не удалось получить цену эфира"
        
    except requests.RequestException as error:
        logging.error(f"Ошибка запроса BTC: {error}")
        return "Ошибка при запросе цены биткоина."
        
async def get_ltc_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=LTCUSDT"
    try: 
        response = requests.get(url=url).json()
        price = response.get('price')
        if price:
            return f"Стоимость литкоина на {time.ctime()}, {price}"
        else:
            return f"Не удалось получить цену литкоина"
        
    except requests.RequestException as error:
        logging.error(f"Ошибка запроса BTC: {error}")
        return "Ошибка при запросе цены биткоина."
           
async def schedule_btc():
    logging.info("Мониторинг BTC начат")
    while monitoring_btc:
        message = await get_btc_price()
        await bot.send_message(chat_id, message)
        logging.info(f"Цена BTC обновлена: {message}")
        await asyncio.sleep(1)
    logging.info("Мониторинг BTC остановлен") 
    
async def schedule_etc():
    logging.info("Мониторинг ETC начат")
    while monitoring_etc:
        message = await get_etc_price()
        await bot.send_message(chat_id, message)
        logging.info(f"Цена ETC обновлена: {message}")
        await asyncio.sleep(1)
    logging.info("Мониторинг ETC остановлен") 
        
async def schedule_ltc():
    logging.info("Мониторинг LTC начат")
    while monitoring_ltc:
        message = await get_ltc_price()
        await bot.send_message(chat_id, message)
        logging.info(f"Цена LTC обновлена: {message}")
        await asyncio.sleep(1)
    logging.info("Мониторинг LTC остановлен") 

async def report_btc():
    global chat_id
    message = await get_btc_price()
    await bot.send_message(chat_id, f"Периодический отчет. Последняя цена BTC: {message}")
    logging.info(f"Периодический отчет BTC был отправлен для чата {chat_id}")

async def report_etc():
    global chat_id
    message = await get_etc_price()
    await bot.send_message(chat_id, f"Периодический отчет. Последняя цена ETC: {message}")
    logging.info(f"Периодический отчет ETC был отправлен для чата {chat_id}")

async def report_ltc():
    global chat_id
    message = await get_ltc_price()
    await bot.send_message(chat_id, f"Периодический отчет. Последняя цена LTC: {message}")
    logging.info(f"Периодический отчет LTC был отправлен для чата {chat_id}")

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f"""
Привет, {message.from_user.full_name}. Мой бот способен на многие вещи!

Команды:
/start - запуск бота

/btc - получать отчеты каждые 10 мин по последним ценам BTC
/stop_btc_reports - отключить оповещение отчетов BTC 
/etc - получать отчеты каждые 10 мин по последним ценам ETC
/stop_etc_reports - отключить оповещение отчетов ETC 
/ltc - получать отчеты каждые 10 мин по последним ценам LTC
/stop_ltc_reports - отключить оповещение отчетов LTC 

/start_btc - начать прямой мониторинг цен BTC
/stop_btc - остановить мониторинг BTC
/start_etc - начать прямой мониторинг цен ETC
/stop_etc - остановить мониторинг ETC
/start_ltc - начать прямой мониторинг цен LTC
/stop_ltc - остановить мониторинг LTC
""")

@dp.message(Command('start_btc'))
async def btc(message:Message):
    global chat_id, monitoring_btc
    chat_id = message.chat.id
    monitoring_btc = True
    await message.answer("Начало мониторинга")
    logging.info(f"Мониторинг BTC запущен для чата {chat_id}")
    asyncio.create_task(schedule_btc())

@dp.message(Command('stop_btc'))
async def stop_btc(message:Message):
    global monitoring_btc
    monitoring_btc = False
    await message.answer("Мониторинг цены биткоина остановлен")
    logging.info(f"Мониторинг BTC остановлен для чата {chat_id}")

@dp.message(Command('start_etc'))
async def etc(message:Message):
    global chat_id, monitoring_etc
    chat_id = message.chat.id
    monitoring_etc = True
    await message.answer("Начало мониторинга")
    logging.info(f"Мониторинг ETC запущен для чата {chat_id}")
    asyncio.create_task(schedule_etc())

@dp.message(Command('stop_etc'))
async def stop_etc(message:Message):
    global monitoring_etc
    monitoring_etc = False
    await message.answer("Мониторинг цены эфира остановлен")
    logging.info(f"Мониторинг ETC остановлен для чата {chat_id}")

@dp.message(Command('start_ltc'))
async def ltc(message:Message):
    global chat_id, monitoring_ltc
    chat_id = message.chat.id
    monitoring_ltc = True
    await message.answer("Начало мониторинга")
    logging.info(f"Мониторинг LTC запущен для чата {chat_id}")
    asyncio.create_task(schedule_ltc())

@dp.message(Command('stop_ltc'))
async def stop_ltc(message:Message):
    global monitoring_ltc
    monitoring_ltc = False
    await message.answer("Мониторинг цены литкоина остановлен")
    logging.info(f"Мониторинг LTC остановлен для чата {chat_id}")

@dp.message(Command('btc'))
async def btc_report(message: Message):
    global chat_id, reporting_btc
    chat_id = message.chat.id
    reporting_btc = True
    await message.answer("Вы подписаны на периодические отчеты о BTC.")
    logging.info(f"Подписка на отчеты BTC для чата {chat_id}")
    aioschedule.every(10).minutes.do(lambda: asyncio.create_task(report_btc()))

@dp.message(Command('stop_btc_reports'))
async def stop_btc_reports(message: Message):
    global reporting_btc
    reporting_btc = False
    await message.answer("Отчеты о BTC остановлены.")
    logging.info(f"Отчеты о BTC остановлены для чата {chat_id}")

@dp.message(Command('etc'))
async def etc_report(message: Message):
    global chat_id, reporting_etc
    chat_id = message.chat.id
    reporting_etc = True
    await message.answer("Вы подписаны на периодические отчеты о ETC.")
    logging.info(f"Подписка на отчеты ETC для чата {chat_id}")
    aioschedule.every(10).minutes.do(lambda: asyncio.create_task(report_etc()))

@dp.message(Command('stop_etc_reports'))
async def stop_etc_reports(message: Message):
    global reporting_etc
    reporting_etc = False
    await message.answer("Отчеты о ETC остановлены.")
    logging.info(f"Отчеты о ETC остановлены для чата {chat_id}")

@dp.message(Command('ltc'))
async def ltc_report(message: Message):
    global chat_id, reporting_ltc
    chat_id = message.chat.id
    reporting_ltc = True
    await message.answer("Вы подписаны на периодические отчеты о LTC.")
    logging.info(f"Подписка на отчеты LTC для чата {chat_id}")
    aioschedule.every(10).minutes.do(lambda: asyncio.create_task(report_ltc()))

@dp.message(Command('stop_ltc_reports'))
async def stop_ltc_reports(message: Message):
    global reporting_ltc
    reporting_ltc = False
    await message.answer("Отчеты о LTC остановлены.")
    logging.info(f"Отчеты о LTC остановлены для чата {chat_id}")

async def on():
    await bot.set_my_commands([
        BotCommand(command="/start", description='Start bot'),
        BotCommand(command="/start_btc", description='Start BTC monitoring'),
        BotCommand(command="/stop_btc", description='Stop BTC monitoring'),
        BotCommand(command="/start_etc", description='Start ETC monitoring'),
        BotCommand(command="/stop_etc", description='Stop ETC monitoring'),
        BotCommand(command="/start_ltc", description='Start LTC monitoring'),
        BotCommand(command="/stop_ltc", description='Stop LTC monitoring'),
        BotCommand(command="/btc", description='BTC reports on'),
        BotCommand(command="/stop_btc_report", description='BTC reports off'),
        BotCommand(command="/etc", description='ETC reports on'),
        BotCommand(command="/stop_etc_report", description='ETC reports off'),
        BotCommand(command="/ltc", description='LTC reports on'),
        BotCommand(command="/stop_ltc_report", description='ETC reports off')
        
    ])
    logging.info("БОТ ЗАПУЩЕН")
    aioschedule.every(1).seconds.do(lambda: asyncio.create_task(schedule_btc()))
    aioschedule.every(1).seconds.do(lambda: asyncio.create_task(schedule_etc()))
    aioschedule.every(1).seconds.do(lambda: asyncio.create_task(schedule_ltc()))


async def scheduler():
    while True:
        aioschedule.run_pending()
        await asyncio.sleep(1)

async def main():
    dp.startup.register(on)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    asyncio.run(main())
  