import sqlite3

def create_database():
    connection = sqlite3.connect('KG_news.db')
    cursor = connection.cursor()
    
    # Создание таблицы, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        news TEXT
    )
    ''')
    
def save_news(news_list):
    connection = sqlite3.connect('KG_news.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO news (news) VALUES (?)", (news_list,))
    
    connection.commit()




            


