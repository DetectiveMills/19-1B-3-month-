from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
import logging, sqlite3, asyncio, time
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("user.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
        id INT, 
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        user_name VARCHAR(100),
        created VARCHAR(100)     
);
""")

@dp.message(Command("start"))
async def start(message:Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id}")
    users_result = cursor.fetchall()
    print(users_result)
    if users_result == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?);", 
                (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, time.ctime()))
        connection.commit()
        await message.reply(f'Привет {message.from_user.first_name}')
    else:
        await message.answer('Вы уже были добавлены в табель')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())