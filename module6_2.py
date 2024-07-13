from colorama import Fore

#print(Fore.BLUE + 'This text is red in color')

#print(colored('Привет мир!', 'red', attrs=['underline']))
#print('Привет, я люблю тебя!')
#cprint('Вывод с помощью cprint', 'green', 'on_blue')
#cprint('Hello, world!', 'red')
#cprint('Hello, world!', 'blue')
#cprint('Hello, world!', 'yellow')
#cprint('Hello, world!', 'magenta')
#cprint('Hello, world!', 'cyan')
class Vehicle:
    __COLOR_VARIANTS = ['RED', 'GREEN', 'BLUE', 'BLACK', 'YELLOW']
    def __init__(self, owner: str, __model: str,__color: str, __engine_power: int ):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self):
        return f' {Fore.RED}Модель: {Fore.BLUE+self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {Fore.CYAN+self.__color}'
    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep='\n', end='\n\n')
    def set_color(self, new_color: str):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(Fore.YELLOW+f'Нельзя менять цвет на {new_color}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()