from random import randint


class House:
    history_house = []
    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
    def __new__(cls, *args, **kwargs):
        name = args[0]
        cls.history_house.append(name)
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'



h1 = House('ЖК Эльбрус', 10)
print(House.history_house)
h2 = House('ЖК Акация', 20)
print(House.history_house)
h3 = House('ЖК Матрёшки', 20)
print(House.history_house)

del h2
del h3

print(House.history_house)
