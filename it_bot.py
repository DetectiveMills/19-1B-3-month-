from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
import logging, asyncio 
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


start_buttons = [
    [types.KeyboardButton(text='Курсы'), types.KeyboardButton(text='О нас')],
    [types.KeyboardButton(text='Адрес'), types.KeyboardButton(text='Контакты')]
]
start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)



course_button = [
    [types.KeyboardButton(text='Backend'), types.KeyboardButton(text='Frontend')],
    [types.KeyboardButton(text='Android'), types.KeyboardButton(text='UX/UI')],
    [types.KeyboardButton(text='Оставить заявку'), types.KeyboardButton(text='Назад')]
]
course_keyboard = types.ReplyKeyboardMarkup(keyboard=course_button, resize_keyboard=True)

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer(f"Здравстуйте {message.from_user.full_name}",
    reply_markup=start_keyboard)

@dp.message(F.text == 'О нас')
async def about_us(message:Message):
    await message.reply("Geeks - это it курсы в Оше, Кара-Балте, Бишкеке и Ташкенте основанное в 2018г")

@dp.message(F.text == 'Адрес')
async def location(message:Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)

@dp.message(F.text == 'Контакты')
async def contact(message:Message):
    await message.reply_contact(phone_number="+996500182663", first_name="Detective", last_name="Mills")

@dp.message(F.text == 'Курсы')
async def course(message:Message):
    await message.reply("Вот наши курсы:", reply_markup=course_keyboard)

@dp.message(F.text == 'Backend')
async def backend(message:Message):
    await message.reply("Backend — это часть веб-приложения или сайта, которая обрабатывает логику и хранение данных на сервере. Он управляет запросами от клиента, взаимодействует с базой данных и отправляет результаты обратно клиенту. Важно, что пользователи не видят напрямую работу backend, но он обеспечивает функциональность и эффективность веб-приложения.")

@dp.message(F.text == 'Frontend')
async def frontend(message:Message):
    await message.reply("Frontend — это часть веб-приложения или сайта, которая отвечает за визуальное отображение и взаимодействие с пользователем. Он включает в себя всё, что пользователь видит на экране, как элементы дизайна, интерфейсы и анимации. Frontend работает в браузере и взаимодействует с backend, чтобы обеспечить динамическое и удобное пользовательское взаимодействие.")

@dp.message(F.text == 'Android')
async def android(message:Message):
    await message.reply("Android-разработка — это создание мобильных приложений для операционной системы Android. Используются языки Java или Kotlin и среда разработки Android Studio. Основные задачи включают проектирование интерфейсов, интеграцию с API и тестирование приложений.")

@dp.message(F.text == 'UX/UI')
async def ux_ui(message:Message):
    await message.reply("UX/UI — дизайн включает в себя создание удобных и привлекательных интерфейсов для пользователей. UX (User Experience) сосредоточен на улучшении общего пользовательского опыта и взаимодействия с продуктом, тогда как UI (User Interface) фокусируется на визуальном оформлении и дизайне элементов интерфейса. Цель UX/UI-дизайна — сделать использование продукта интуитивным и приятным для пользователей.")

@dp.message(F.text == "Назад")
async def back(message:Message):
    await message.answer("🔙", reply_markup=start_keyboard)

@dp.message(F.text == "Оставить заявку")
async def application(message:Message):
    buutton = [[types.KeyboardButton(text='Отправить заявку', request_contact=True)]]
    keyboarf = types.ReplyKeyboardMarkup(keyboard=buutton, resize_keyboard=True)
    await message.reply("Пожалуйста, отправьте свои контактные данные", reply_markup=keyboarf)

@dp.message(F.contact)
async def get_contact(message:Message):
    contact_info = f"Заявка на курсы \nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}"
    await bot.send_message(chat_id = -4255458461, text = contact_info)
    await message.answer("Спасибо, что оставили заявку")
    await message.answer(f"Вы вернулись на главное меню", reply_markup=start_keyboard)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


