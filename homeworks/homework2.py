import random
class Hero:
    def __init__(self,name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"base action")

    def attack(self):
        print(f"kill")

class Archer(Hero):
    def __init__(self, name, hp, arrows=6, precision=0.7):
        super().__init__( name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self, target="зомби"):
        if self.arrows > 0:
            self.arrows -=1
            hit_chance = random.random()
            if hit_chance <= self.precision:
                print(f"{self.name} атаковал {target}. Атака успешна! Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} промахнулся по {target}. Осталось стрел: {self.arrows}")
        else:
             print(f"{self.name} попытался атаковать {target}, но стрелы закончились. Атака неуспешна!")

    def rest(self):
        self.arrows +=5
        print(f"Добавлено 5 стрел. Теперь у вас {self.arrows} стрел.")

    def status(self):
        print(f"информация о текущем состоянии персонажа: {self.name}, {self.hp}")

archer = Archer('Argen', 100, 10)
archer.status()
archer.attack("скелет")
archer.attack("зомби")
archer.attack("вампир")
archer.rest()
archer.status()