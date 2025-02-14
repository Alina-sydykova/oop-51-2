from faker import Faker

fake = Faker()

class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def introduce(self):
        return f"Hello, my name is {self.name} and I live at {self.address}."

student1 = Student(fake.name(), fake.address())
student2 = Student(fake.name(), fake.address())
student3 = Student(fake.name(), fake.address())

print(student1.introduce())
print(student2.introduce())
print(student3.introduce())


""""Библиотека `Faker` используется для генерации случайных фейковых данных, таких 
как имена, адреса, номера телефонов и многое другое. Она полезна для тестирования, заполнения
 баз данных и обучения. Каждый вызов метода Faker создаёт новые случайные данные."""


