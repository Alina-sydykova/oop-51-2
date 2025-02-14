#Магические, статичные, классовые методы в классах, множественное наследование
# Nikita.kg
from abc import  ABC, abstractmethod
class OTPSservice(ABC):
    @abstractmethod
    def sms_send():
        pass

class NikitaOTP(OTPSservice):
    def sms_send():
        phone = input("Введите номер телефона")

class TwilionOTP(OTPSservice):
    def sms_send(self, phone):
        phone = input("Enter your phone")



class Animal(ABC):
    #декоратор
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return print('gaf gaf')

    def move(self):
        return print('run')

dog = Dog()
dog.make_sound()


































