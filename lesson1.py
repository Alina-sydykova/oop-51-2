#class def

# class Person:
#     #это функция является конструктором
#     def __(self, name, age):
#         #атрибуты класса
#         self.name = name
#         self.age = age
#
#     #метод класса
#     def introduce(self,):
#         print(f"hi i'm {self.name}")
# #class obj - экземпляр класса
# ardager = Person("Ardager", 25)
# ardager.introduce()

# print(type(ardager))
# print(type(123))
# print(type("Hello")


#Родительский класс
class Hero:
    def __init__(self, name, hp, lvl):
        self.name_1 = name
        self.hp_1 = hp
        self.lvl_1 = lvl

    def action(self,):
        print(f"{self.name_1} делает действие")
naofume = Hero("Naofume", 100, 3)

#дочерний класс
class ShiledHero(Hero):
    pass
naofume = ShiledHero("NaoFume", 100, 3)
naofume.action()
# CamelCase
# перемменыхб методовб функций -- snek_case
