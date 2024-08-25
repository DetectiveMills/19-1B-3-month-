from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from email.message import EmailMessage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from emails import create_database, save_emails
from config import TOKEN, smtp_sender, smtp_sender_password
import smtplib, logging, asyncio, sqlite3

SMTP = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_SENDER_EMAIL = smtp_sender
SMTP_SENDER_PASSWORD = smtp_sender_password

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

logging.basicConfig(level=logging.INFO)

create_database()

class EmailForm(StatesGroup):
    email = State()
    subject_email = State()
    message_email = State()

async def cancel_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Процесс отменен. Если хочешь заново начать нажми на /start")

router.message.register(cancel_command, Command(commands="cancel"))

@router.message(Command("start"))
async def send_welcom(message:Message):
    await message.answer(f"Привет! Я могу отправить письмо любому от своего имени!\n/send_email - начать отправление письма\n/cancel - сбросить все данные.")

@router.message(Command('send_email'))
async def send_email(message:Message, state : FSMContext):
    await state.set_state(EmailForm.email)
    await message.reply("Введите email того, кому нужно отправить письмо\nПример отправки: example@gmail.com")

@router.message(EmailForm.email)
async def email(message : Message, state : FSMContext):
    await state.update_data(email = message.text)
    await state.set_state(EmailForm.subject_email)
    data = await state.get_data()
    email = data.get('email')
    await message.answer(f"Проверьте, правильно ли вы написали email - {email}\nЕсли вы допустили ошибку при написании email, то вы можете воспользоваться командой /cancel, тем самым сбросив данные.\nЕсли все правильно, введите заголовок/тему вашего письма:")

@router.message(EmailForm.subject_email)
async def age(message : Message, state : FSMContext):
    await state.update_data(subject_email = message.text)
    await state.set_state(EmailForm.message_email)
    await message.answer("Введите содержание/текст вашего письма:")

@router.message(EmailForm.message_email)
async def message(message:Message, state:FSMContext):
    await message.answer("Загрузка...")
    data = await state.get_data()
    email = data.get('email') 
    subject_email = data.get('subject_email')
    message_email = message.text

    to_email = email
    subject = subject_email
    body = message_email
    save_emails(to_email, subject, body)

    try:
        server = smtplib.SMTP(SMTP, SMTP_PORT)
        server.starttls()

        server.login(SMTP_SENDER_EMAIL, SMTP_SENDER_PASSWORD)
        msg = EmailMessage()
        msg['From'] = SMTP_SENDER_EMAIL
        msg['Subject'] = subject
        msg['To'] = to_email
        msg.set_content(body)

        server.send_message(msg)
        server.quit
        return await message.answer("Письмо успешно отправлена!")
 
    except Exception as error:
        return await message.answer(f"Error {error}")  

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  