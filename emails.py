import sqlite3

def create_database():
    connection = sqlite3.connect('email_letters.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS letters (
        email VARCHAR (100),
        subject VARCHAR (100),
        message TEXT
    )
    ''')
    
def save_emails(to_email, subject, body):
    connection = sqlite3.connect('email_letters.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO letters (email, subject, message) VALUES (?, ?, ?)", (to_email, subject, body))
    
    connection.commit()




            


