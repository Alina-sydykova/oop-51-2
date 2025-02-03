class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

hero1 = Hero("Артур", 5, 100)
hero2 = Hero("Ланселот", 12, 150)
hero3 = Hero("Гвен", 10, 120)

print(f"{hero1.name} взрослый? {hero1.is_adult()}")
print(f"{hero2.name} взрослый? {hero2.is_adult()}")
print(f"{hero3.name} взрослый? {hero3.is_adult()}")
