from random import randint


class House:
    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 0 or new_floor > self.number_of_floors:
            print(f'В {self.name} Этажа {new_floor} не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, others):
        return self.number_of_floors > others.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, (int, House)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        value = value if isinstance(value, int) else self.number_of_floors

        return self.number_of_floors + value

    def __radd__(self, value):
        if not isinstance(value, (int, House)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        value = value if isinstance(value, int) else self.number_of_floors

        return value + self.number_of_floors

    def __iadd__(self, value):
        if not isinstance(value, (int, House)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом House")

        value = value if isinstance(value, int) else self.number_of_floors
        self.number_of_floors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)
# h2.go_to(1)
value = randint(1, 45)

print(value)  # просто посмотреть чему равен value
print(h1 + value) # для add
print(h2 + value) # для __add__
print(value + h1) # __radd__
print(value + h2) # __radd__
h1 += value
h3 = h1
print(h3, 'yj') #iadd
h2 += value
print(h2)# __iadd__
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
print(h1)
print(h2)
# print(len(h1))
# print(len(h2))
