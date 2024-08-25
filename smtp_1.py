import smtplib
from email.message import EmailMessage
from config import smtp_sender, smtp_sender_password

def send_email(to_email, subject, message):
    sender = smtp_sender
    password = smtp_sender_password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to_email

        # if image_path:
        #     with open(image_path, 'rb') as img:
        #         img_d = img.read()
        #         msg.add_attachment(img_d, main_type='image', subtype='jpg', filename=image_path)

        server.send_message(msg)
        return '200 OK'
    
    except Exception as error:
        return f"Error {error}"
    
print(send_email('sfly9512@gmail.com', 'СРОЧНО!', """
Вы зашли на аккаунт, если это не вы то 
немедленно зайтите на свой аккаунт и поменяйте пароль!!!
"""))