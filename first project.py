# ООП (polymorphism - свойство кода работать с разными типами данных)
# method override; operator overloadind
# (термины: переопределения метода и переопределения оператора)
# "утиная типизация" - функция-оператор сама различает к какому классу относится операнд

# ООП (magic methods) - специальные методы
# для нужд отладки и визуализации

# __call__ - экземпляр класса становится вызываемым (как функция)
# y = ax^2 + bx + c
class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


s = SquareFunction(1, 2, 3) # вызов экземпляра s (со свойствами функции)
print(s(2))

# class MyTime:
#     def __init__(self, minutes, seconds):
#         if 0 <= minutes < 60:
#             self.minutes = minutes
#         if 0 <= seconds < 60:
#             self.seconds = seconds
#
#     def __add__(self, other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s//60
#         s = s % 60 # сумма не должна выходить за ограничение 60
#         m = m % 60
#         print(m, s)
#         return MyTime(m, s)
#
#         #return f'Сумма минут: {self.minutes + other.minutes}, сумма секунд: {self.seconds + other.seconds}'
#
#     def __str__(self):
#         return f'<Time {self.minutes:02}:{self.seconds:02}>'
#
# t1 = MyTime(13, 5)
# t2 = MyTime(53, 0)
# print(t1 + t2)
# t = MyTime(13, 15)
# print(t)



# from math import hypot
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Point: ({self.x}, {self.y})>'
#
#     def __repr__(self):
#         return f'Points: ({self.x}, {self.y})'
#
#     def __sub__(self, other):
#         #return Point(self.x - other.x, self.y - other.y) # вывод расстояний между 2-мя (.)
#                                                           # на коорд.плоскости с учетом знака
#         return Point(abs(self.x - other.x), abs(self.y - other.y)) # ...абсолютное значение
#
#     # Расчёт расстояния между точками на координатной плоскости
#     def __add__(self, other):
#         return hypot(self.x - other.x, self.y - other.y) # исп. готовую ф-ю из библ.math

# Расчёт расстояния между A(5, 4), B(10, 2) точками на координатной плоскости
# p1 = Point(5, 4) # коордиинаты первой точки на коорд.плоскости
# p2 = Point(10, 2) # коордиинаты второй точки на коорд.плоскости
# print(p1-p2) # вывод значений массива длин катетов
# print(p1+p2) # вывод расчёта гипотенузы
#             # (расстояния между 2-мя точками на координат.плоскости)
# print(29**0.5) # проверка метода расчёта расстояния между 2-мя точками на координат.плоскости
# p = [Point(), Point()]
# p = Point()
# print(p)
#str(a) -> a.__str__ (одинаковый перевод в строку)


# isinstance (объект, тип) -> True
# isinstance (объект, (тип 1, тип 2, ... , тип N) -> True (если список, то действуем по другому сценарию)

# lst = list(range(1, 15))
# lst += ['a'] # добавим элемент списка не явл. целым числом
#
# class Stat:
#         def __init__(self, vals):# класс возвращает мин, макс и среднее арифметическое
#             self.values = vals[:]
#
#         def is_int(self) -> bool:
#             return all(isinstance(item, int) for item in self.values)
#
#         def get_min(self):
#             if self.is_int():
#                 return min(self.values)
#             return None
#
#         def get_max(self):
#             if self.is_int():
#                 return min(self.values)
#             return None
#
#         def get_aver(self):
#             if self.is_int():
#                 return sum(self.values) / len(self.values)
#             return None
#
# s =  Stat(lst)
# print(s.get_min())
# print(s.get_max())
# print(s.get_aver())

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

#from lib import Rectangle, Circle, Square

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
# # # 1-й способ
# # # def shape_info(shape: object):
# # #     print(f'Площадь {shape.get_name()}a: {shape.area()}, Периметр: {shape.perimetr()}')
# # #     # функция shape_info различает обращение к вычисляемым значениям по классу объекта
# #
# # 2-й способ через isinstance
# rect, circ, sqr = ['прямоугольник', 'круг', 'квадрат']
# fig = ''
# def shape_info(shape: object):
#     if isinstance(shape, Circle):
#         fig = circ
#     elif isinstance(shape, Rectangle):
#         fig = rect
#     else:
#         fig = sqr
#
#     print(f'Площадь {fig}a: {shape.area()}, Периметр: {shape.perimetr()}')

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

