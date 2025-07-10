# ООП (polymorphism - свойство кода работать с разными типами данных)
# method override; operator overloadind
# (термины: переопределения метода и переопределения оператора)
# "утиная типизация" - функция-оператор сама различает к какому классу относится операнд
# isinstance (объект, тип) -> True
# isinstance (объект, (тип 1, тип 2, ... , тип N) -> True (если список, то действуем по другому сценарию)

lst = list(range(1, 15))
lst += ['a'] # добавим элемент списка не явл. целым числом

class Stat:
        def __init__(self, vals):# класс возвращает мин, макс и среднее арифметическое
            self.values = vals[:]

        def is_int(self) -> bool:
            return all(isinstance(item, int) for item in self.values)

        def get_min(self):
            if self.is_int():
                return min(self.values)
            return None

        def get_max(self):
            if self.is_int():
                return min(self.values)
            return None

        def get_aver(self):
            if self.is_int():
                return sum(self.values) / len(self.values)
            return None

s =  Stat(lst)
print(s.get_min())
print(s.get_max())
print(s.get_aver())

# class Selector():
#     def __init__(self, vals):
#         self.values = vals[:] # делаем копию списочного выражения, чтобы не изм. начальный список
#
#     def get_odd(self):
#         return [x for x in self.values if x % 2] # остаток от деления не пустое значение (можно ==1)
#
#     def get_even(self):
#         return [x for x in self.values if x % 2 ==0]
#
# s =  Selector(lst)
# print(s.get_odd())
# print(s.get_even())
# print(lst)

# from lib import Student, Employee, Person
#
# people = [
#     Person('Александр', 27),
#     Student('Дмитрий', "ГУАП"),
#     Employee('Владимир', 'Авангард')
# ]
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_univ())
#     elif isinstance(person, Employee):
#         print(person.get_comp())
#     else:
#         print(person.get_name(), person.get_age())

from lib import Rectangle, Circle, Square, Employee

# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.name = 'круг'
#
#     def perimetr(self):
#         return 2 * pi * self.radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def get_name(self):
#         return self.name
#
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#         self.name = 'квадрат'
#
#     def perimetr(self):
#         return 4 * self.side
#
#     def area(self):
#         return self.side ** 2
#
#     def get_name(self):
#         return self.name
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
# # 1-й способ
# # def shape_info(shape: object):
# #     print(f'Площадь {shape.get_name()}a: {shape.area()}, Периметр: {shape.perimetr()}')
# #     # функция shape_info различает обращение к вычисляемым значениям по классу объекта
#
# # 2-й способ через isinstance
# rect, circ, sqr = ['прямоугольник', 'круг', 'квадрат']
# fig = ''
# def shape_info(shape: object):
#     if isinstance(shape, Circle):
#         fig = circ
#     elif isinstance(shape, Rectangle):
#         fig = rect
#     elif isinstance(shape, Square):
#         fig = sqr
#         print(f'Площадь {fig}a: {shape.area()}, Периметр: {shape.perimetr()}')

# s = Square(10)
# shape_info(s)
#
# cr = Circle(10)
# shape_info(cr)
#
# r = Rectangle(5, 2)
# shape_info(r)
#
# print(dir(s))
# print(dir(cr))

# class Book:
#     def __init__(self, title, author):
#         self._title = title
#         self._author = author
#
#     def get_title(self):
#         return self._title
#
#     def get_author(self):
#         return self._author
#
# book = Book('Язык С++', 'Бьярн Страупструп')
#
# print(f'{book.get_title(), book.get_title()}')


# print(1 + 2)
# print(1 + 2.0)
# print('abc' + 'def')
# print([1, 2] + [3, 4])
#
# def func(x, y):
#     return x + y
#
# print(func(2, 3.0))

