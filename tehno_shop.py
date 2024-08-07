import logging, asyncio 
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN
import time

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

start_buttons = [
    [types.KeyboardButton(text='Товары'), types.KeyboardButton(text='О нас')],
    [types.KeyboardButton(text='Заказать'), types.KeyboardButton(text='Контакты')]
]
start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

product_button = [
    [types.KeyboardButton(text='228'), types.KeyboardButton(text='1488')],
    [types.KeyboardButton(text='777'), types.KeyboardButton(text='52')],
    [types.KeyboardButton(text='7'), types.KeyboardButton(text='Назад')]
]
product_keyboard = types.ReplyKeyboardMarkup(keyboard=product_button, resize_keyboard=True)


@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}", 
    reply_markup=start_keyboard)

@dp.message(F.text == 'О нас')
async def about_us(message:Message):
    await message.reply("Tehno Shop — это одна из немногих магазинов, где вы сможете купить смартфоны сразу по цене двух! Мы уже более 10 лет работаем на черном рынке, но ни разу не попали под лапы злых офицеров. Хорошая и главное - гениальное склеивание смартфонов выделяет нас из остальных скучных шопов. Смешные цены и удачные торги. Ну же, чего ты ждешь? Быстрее покупай пока нас не посадили!")

@dp.message(F.text == 'Контакты')
async def contacts(message:Message):
    await message.reply_contact(phone_number="+996500182663", first_name="Detective", last_name="Mills")

@dp.message(F.text == 'Товары')
async def product(message:Message):
    time.sleep(1)
    await message.answer_photo(photo="https://i.pinimg.com/564x/ef/4d/f8/ef4df842d095f3285b68e3fa40507b27.jpg" , caption="Описание: Легенда всех телефонов - NOKIA 3310 которым владели наши предки. Просто неубиваемый зверь\nЦена: 9999 сом\nАртикул: 228")
    time.sleep(1)
    await message.answer_photo(photo="https://i.pinimg.com/564x/f8/91/b4/f891b4a3e98e3947a987d830e9fdb0fc.jpg" , caption="Описание: Полупрозрачный смартфон XYZ будущего. Невидимая сталь посейдона\nЦена: 123914 сом\nАртикул: 777")
    time.sleep(1)
    await message.answer_photo(photo="https://i.pinimg.com/564x/6f/9e/93/6f9e93e4121136ed43dfd9965f729ae2.jpg" , caption="Описание: Отец всех телефонов - 'кирпич' от компании Motorola. Говорят, он весил как реальный кирпич\nЦена: 1049 сом\nАртикул: 1488")
    time.sleep(1)
    await message.answer_photo(photo="https://i.pinimg.com/564x/93/08/9f/93089f446b578c1bef52269e154947c0.jpg" , caption="Описание: ИПХОН 14 ПРО МАКС. Нужная штука чтобы снимать качественные влоги\nЦена: 91384 сом\nАртикул: 52")
    time.sleep(1)
    await message.answer_photo(photo="https://i.pinimg.com/564x/79/78/1f/79781f5a05cba63713a896766e814bfa.jpg" , caption="Описание: Телефонная будка. Для любителей эстетики и для людей которые любят по философствовать\nЦена: 12491193 сом\nАртикул: 7")

@dp.message(F.text == 'Заказать')
async def order_tovar(message:Message):
    await message.reply("Нажмите на артикул товара", reply_markup=product_keyboard)

@dp.message(F.text == '228')
async def application(message:Message):
    contact_info = "Заявка на товар \nАртикул товара: 228"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    buutton = [[types.KeyboardButton(text='Отправить контактные данные', request_contact=True)]]
    keyboarf = types.ReplyKeyboardMarkup(keyboard=buutton, resize_keyboard=True)
    await message.reply("Теперь пожалуйста, отправьте свои контактные данные", reply_markup=keyboarf) 

@dp.message(F.contact)
async def get_contact(message:Message):
    contact_info = f"Имя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    await message.answer("Спасибо, что заказали наш товар!")
    await message.answer(f"Вы вернулись на главное меню", reply_markup=start_keyboard)

@dp.message(F.text == '777')
async def application(message:Message):
    contact_info = "Заявка на товар \nАртикул товара: 777"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    buutton = [[types.KeyboardButton(text='Отправить контактные данные', request_contact=True)]]
    keyboarf = types.ReplyKeyboardMarkup(keyboard=buutton, resize_keyboard=True)
    await message.reply("Теперь пожалуйста, отправьте свои контактные данные", reply_markup=keyboarf) 

@dp.message(F.contact)
async def get_contact(message:Message):
    contact_info = f"Имя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    await message.answer("Спасибо, что заказали наш товар!")
    await message.answer(f"Вы вернулись на главное меню", reply_markup=start_keyboard)

@dp.message(F.text == '1488')
async def application(message:Message):
    contact_info = "Заявка на товар \nАртикул товара: 1488"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    buutton = [[types.KeyboardButton(text='Отправить контактные данные', request_contact=True)]]
    keyboarf = types.ReplyKeyboardMarkup(keyboard=buutton, resize_keyboard=True)
    await message.reply("Теперь пожалуйста, отправьте свои контактные данные", reply_markup=keyboarf) 

@dp.message(F.contact)
async def get_contact(message:Message):
    contact_info = f"Имя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    await message.answer("Спасибо, что заказали наш товар!")
    await message.answer(f"Вы вернулись на главное меню", reply_markup=start_keyboard)

@dp.message(F.text == '52')
async def application(message:Message):
    contact_info = "Заявка на товар \nАртикул товара: 52"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    buutton = [[types.KeyboardButton(text='Отправить контактные данные', request_contact=True)]]
    keyboarf = types.ReplyKeyboardMarkup(keyboard=buutton, resize_keyboard=True)
    await message.reply("Теперь пожалуйста, отправьте свои контактные данные", reply_markup=keyboarf) 

@dp.message(F.contact)
async def get_contact(message:Message):
    contact_info = f"Имя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    await message.answer("Спасибо, что заказали наш товар!")
    await message.answer(f"Вы вернулись на главное меню", reply_markup=start_keyboard)

@dp.message(F.text == '7')
async def application(message:Message):
    contact_info = "Заявка на товар \nАртикул товара: 7"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    buutton = [[types.KeyboardButton(text='Отправить контактные данные', request_contact=True)]]
    keyboarf = types.ReplyKeyboardMarkup(keyboard=buutton, resize_keyboard=True)
    await message.reply("Теперь пожалуйста, отправьте свои контактные данные", reply_markup=keyboarf) 

@dp.message(F.contact)
async def get_contact(message:Message):
    contact_info = f"Имя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    await message.answer("Спасибо, что заказали наш товар!")
    await message.answer(f"Вы вернулись на главное меню", reply_markup=start_keyboard)

@dp.message(F.text == "Назад")
async def back(message:Message):
    await message.answer("Вы вернулись в главное меню 🔙", reply_markup=start_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())