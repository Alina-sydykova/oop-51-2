import sqlite3

def get_connection():
    return sqlite3.connect('User.db')

def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR (40) NOT NULL,
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')
        conn.commit()

def add_user(name, age, hobby):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
            (name, age, hobby)
        )
        conn.commit()
        print(f"Пользователь {name} добавлен")

def get_all_by_name(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name, age, hobby FROM users WHERE name =?', (name,))
        users = cursor.fetchall()

    if users:
        print('Список найденных пользователей:')
        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print(f"Пользователь с именем {name} не найден")

create_table()
add_user("Алина", 16, "Чтение")
get_all_by_name("Алина")
