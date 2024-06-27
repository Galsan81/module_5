class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 0 or new_floor > self.number_of_floors:
            print(f'В {self.name} Этажа {new_floor} не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)
            #if new_floor <
        #new_floor

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)