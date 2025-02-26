import sqlite3

connect = sqlite3.connect('User.db')
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


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


def add_grade(user_id, subject, grade):
    cursor.execute('''
        INSERT INTO grades (user_id, subject, grade) VALUES (?,?,?)
    ''', (user_id, subject, grade))
    connect.commit()
    print(f"Оценка добавлена для пользователя с ID {user_id}!!!")


def get_users_with_grades():
    cursor.execute('''
        SELECT users.name, users.age, grades.subject, grades.grade
        FROM users 
        LEFT JOIN grades ON users.user_id = grades.user_id
    ''')
    users = cursor.fetchall()

    if users:
        for i in users:
            grade = i[3] if i[3] is not None else "No grade"
            print(f"NAME: {i[0]}, AGE: {i[1]}, SUBJECT: {i[2]}, GRADE: {grade}")
    else:
        print("Нет пользователей с оценками.")


def update_grade(grade_id):
    new_grade = input("Введите новую оценку: ").strip()

    if not new_grade.isdigit():
        print("Ошибка: оценка должна быть числом.")
        return

    new_grade = int(new_grade)

    cursor.execute('UPDATE grades SET grade = ? WHERE grade_id = ?', (new_grade, grade_id))
    connect.commit()

    if cursor.rowcount > 0:
        print("subject id updated !!")
    else:
        print("Ошибка: урок с таким ID не найден.")


add_user("Ardager", 23, "плавать")
add_user("Oleg", 23, "плавать")

add_grade(1, "Алгебра", 5)
add_grade(2, "ИЗО", 2)

get_users_with_grades()

lesson_id = int(input("Введите ID оценки для обновления: ").strip())
update_grade(lesson_id)
