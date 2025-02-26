import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject VARCHAR (50) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
               ''')

connect.commit()


# Create
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


# add_user("Ardager", 23, "плавать")
# add_user("Oleg", 23, "плавать")
# add_user("John", 23, "плавать")
# add_user("Doe", 23, "плавать")
# add_user("Anna", 23, "плавать")


def add_grade(user_id, subject, grade):
    cursor.execute('''
            INSERT INTO grades (user_id, subject, grade) VALUES (?,?,?)
                   ''',
                   (user_id, subject, grade))
    connect.commit()
    print(f"Оценка добавлена для пользователя с ID {user_id}!!!")


# add_grade(4, "Алгебра", 5)
# add_grade(3, "Алгебра", 5)
# add_grade(2, "Алгебра", 5)
# add_grade(1, "Алгебра", 5)
# add_grade(4, "ИЗО", 2)
# add_grade(3, "ИЗО", 2)
# add_grade(2, "ИЗО", 2)
# add_grade(1, "ИЗО", 2)


def get_users_with_grades():
    # Зайди и возьми из таблицы users столб name , из таблицы grades столб subject,
    #  из таблицы grades столб grade
    # ТАМ - ИЗ users
    # Соедени  users с grades в табиле users возьми первое знаяение в сталбце user_id
    # иши записи которые user_id  из users в таблице grades по столбцу user_id

    cursor.execute('''
        SELECT users.name, users.age, grades.subject, grades.grade
        FROM users 
        LEFT JOIN grades ON users.user_id = grades.user_id
                   ''')

    users = cursor.fetchall()
    for i in users:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")


get_users_with_grades()

