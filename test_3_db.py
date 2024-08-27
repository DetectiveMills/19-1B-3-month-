import sqlite3

def create_database():
    connection = sqlite3.connect('users_chine.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name VARCHAR (100),
        surname VARCHAR (100),
        phone_number INTEGER,
        code TEXT
        )
    ''')
    
def save_emails(name, surname, phone_number, cod):
    connection = sqlite3.connect('users_chine.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users (name, surname, phone_number, code) VALUES (?, ?, ?, ?)", (name, surname, phone_number, cod))
    
    connection.commit()