import smtplib, logging, asyncio
from email.message import EmailMessage
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command, CommandStart
from config import TOKEN, smtp_sender, smtp_sender_password

logging.basicConfig(level=logging.INFO)

SMTP = 'smtp.gmail.com'
SMTP_PORT = 578
SMTP_SENDER_EMAIL = smtp_sender
SMTP_SENDER_PASSWORD = smtp_sender_password

bot = Bot(token=TOKEN)
dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def send_welcom(message:Message):
    await message.answer(f"Привет! Отправь команду /send_email, чтобы я отправил письмо")

@router.message(Command('send_email'))
async def send_email(message:Message):
    to_email = "recipient@example.com"
    subject = "Тестовое письмо"
    body = "Это тестовое письмо"

    try:
        server = smtplib.SMTP(SMTP, SMTP_PORT)
        server.starttls()

        server.login(SMTP_SENDER_EMAIL, SMTP_SENDER_PASSWORD)
        msg = EmailMessage()
        msg['From'] = SMTP_SENDER_EMAIL
        msg['Subject'] = subject
        msg['To'] = to_email
        msg.send_content(body)

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