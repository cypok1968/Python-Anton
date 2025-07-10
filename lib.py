def summ(a, b):
    return a + b


def diff(a, b):
    return a - b

# Фигуры, периметр и площадь
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'круг'

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def get_name(self):
        return self.name


class Square:
    def __init__(self, side):
        self.side = side
        self.name = 'квадрат'

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def get_name(self):
        return self.name

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = 'прямоугольник'

    def perimetr(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def get_name(self):
        return self.name
# # 1-й способ
# # def shape_info(shape: object):
# #     print(f'Площадь {shape.get_name()}a: {shape.area()}, Периметр: {shape.perimetr()}')
# #     # функция shape_info различает обращение к вычисляемым значениям по классу объекта
#
# 2-й способ через isinstance
rect, circ, sqr = ['прямоугольник', 'круг', 'квадрат']
fig = ''
def shape_info(shape: object):
    if isinstance(shape, Circle):
        fig = circ
    elif isinstance(shape, Rectangle):
        fig = rect
    else:
        fig = sqr

    print(f'Площадь {fig}a: {shape.area()}, Периметр: {shape.perimetr()}')

# Class Methods

# class Balance:
#     def __init__(self):
#         self._right = []
#         self._left = []
#
#      __name__
#
#     def add_left(self, weight):
#         pass
#
#     def add_right(self, weight: int): -> None:
#         """"
#         Добавляет вес в левую чашу
#         :param weight: вес, размещаемый в правую чашу
#         :raises ValueError: если вес отрицательный
#         """"
#         if weight < 0:
#             raise ValueError('Снятие веса не поддерживается в текущей версии'
#         self._right += weight
#
#     def result(selfs):
#
#
#     def result(self) -> str:
#         return # состояние (левая перевесила, уравновешена)
#
#
#
# class Sorter:
#     def __init__(self):
#         self.words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def result(self):
#         return sorted(self.words, key=lambda x: len(x), reverse=True)# список слов отсортированный по длине


class Separator:
    def __init__(self):
        self.odd = []
        self.even = [] # чётные

    def add_num(self, num):
        if num % 2:
            self.odd.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even

class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter +=1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0





class Car:
    counter = 0 # статичное свойство класса (счётчик машин)
    def __init__(self, brand='Noname', model='Nomodel', color='Nocolor'):
        self.brand = brand # 'Skoda'
        self.model = model # 'Octavia'
        self.color = color # 'red'
        self.engine_on = False
        Car.counter += 1

    def start_engine(self):
        self.engine_on = True # через self.* фиксируем локальную переменную * метода, как внешнюю
                              # (сохраняемая после исп-я метода ячейка памяти)

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand}', {self.model}, {self.color})
        else:
            print('Двигатель не заведён, не едем')
    # статичные члены класса
    @staticmethod # метод обращается только к данному классу (он статичный)
    def get_counter():
        return Car.counter
    # # setters - аттрибут класса: устанавливает значение поля
    # def set_brand(self, new_brand):
    #     if new_brand:
    #         self.brand = new_brand
    #
    # def set_model(self, new_model):  # прошло несколько лет, человек вырос
    #     if new_model:
    #         self.model = new_model
    #
    # else:
    #         print('Старая модель - ', new_age)
    #
    # # getters
    #
    # def get_brand(self):
    #     return self.brand
    #
    # def get_model(self):
    #     return self.model

# Списки лиц и организаций
class Student:
    def __init__(self, name='', univ=''):
        # свойства (поля) класса
        self._name = name
        self._univ = univ

    def get_univ(self):
        return self._name, self._univ

class Employee:
    def __init__(self, name='', comp=''):
        # свойства (поля) класса
        self._name = name
        self._comp = comp

    def get_comp(self):
        return self._name, self._comp

class Person:
    def __init__(self, name='Bill', age= 21):
        # свойства (поля) класса
        self._name = name
        self._age = age

    def person_info(self):
        print(f'Человек с именем {self._name}. Возраст: {self._age}.')

    # setters - атрибут класса: устанавливает значение поля
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age): # прошло несколько лет, человек вырос
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст - ', new_age)

    # getters

    def get_name(self):
        return self._name


    def get_age(self):
        return self._age

    def person_info(self):
        print(f'{self._name}.{self._age}')


if __name__ == '__main__':
    print('Это библиотека, а исполняемый - first project')