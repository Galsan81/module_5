class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    #def go_to(self, new_floor):
     #   if new_floor < 0 or new_floor > self.number_of_floors:
      #      print(f'В {self.name} Этажа {new_floor} не существует')
       # else:
        #    for i in range(1, new_floor+1):
         #       print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#h1.go_to(5)
#h2.go_to(1)
print(h1)
print(h2)
print(len(h1))
print(len(h2))