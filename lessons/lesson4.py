#что такое декаратор



def my_decorator(func):
    def wrapper():
        print('перед выполнением функции')
        func()#5
        print('после выполнении функции')#6
    return wrapper#3

@my_decorator
def hello():
    print("Привет мир")
hello()#1


#декораторы с аргументами
#n=3
def repeat(func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("привет")



#декораторы для класса
def class_decorator(cls):

    class NewClass(cls):
        def new_method(self):
            return print('new method')
    return NewClass

@class_decorator
class MyClass:
    def old_method(self):
        return print(('старый метод'))

# obj = MyClass()
# obj.old_method()
# obj.new_method()






# def is_admin(func):
#     pass
#
# @is_admin
# def ban(user_sms):
#     pass

class Person:
    #конструктор\ магический метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"бла бла бла"


# obj = Person("pavel", 25)
# print(obj)

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        print(f"{self.amount}-----{other}")
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"{self.amount} som"
    def __len__(self):
        return

m1 = Money(100)
m2 = Money(400)
m3 = m1 + m2
print(m3)
len(m3)


class Math:
    @staticmethod
    def add(self, a, b,):
        return a + b

obj3 = Math()
print(obj3.add(1,2))

class Person:
    count = 0
    password = "def"

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_population(cls):
        return cls.count

    @classmethod
    def create_person(clscls, name):
        return cls(name)

person1= Person("Alice")
person2= Person("bob")
person3= Person("lilo")
print(Person.get_population())
Person4 = Person.create_person("john")
print(person4.name)