# Встроенные библиотеки (надо иметь ввиду, что в новой версии Python
# могут не сохраняться не переписываться старые библиотеки)
# заходим в хранилище библиотек (репозиторий) Python в инете на сайт
# PyPI - Python Package Index (pypi.org)


from math import pi, sqrt, sin, radians, hypot

# import math as m
#
# print(dir(m)) # вывод на экран всех функций библиотеки math Python
# print(help(m.cos))

# 3-й способ подключения функции из библиотеки (не для всего множества элементов библиотеки)
#from math import * # сначала загружаем в оперативную память все имена функций, а далее смотрим,
# что используем и выводим только необходимые функции или константы
# from math import pi # достаем через (модуль библиотек PyPI) math только число ПИ
# from math import sqrt # достаем через (модуль библиотек PyPI) math только функцию квадратного корня


print('Число Пи', pi)
print('Квадратный корень 4', sqrt(4))
print('Синус 30:', round(sin(radians(30)), 2)) # округляем значение функции до 2 знаков (для краткости)
print('Гипотенуза для 3 и 2', hypot(3, 2))

# 2-й способ подключения функции из библиотеки, m - используем для краткости записей
# import math as m
#
# print('Число Пи', m.pi) # достаем через оператор библиотеки PyPI math число ПИ

# 1-й способ подключения функции из библиотеки
# import math
#
# print('Число Пи', math.pi) # достаем через оператор библиотеки PyPI math число ПИ

# lst = [1, 1, 2, 3, 5]
#
# # res = 0
# # for x in lst:
# #    res += x # суммирование элементов списка через цикл
# # print(res)
#
# res = sum(lst)
# min_value = min(lst) # - ф-я вычисляет наименьший элемент списка
# max_value = max(lst) # ф-я вычисляет наибольший элемент списка
# print(res, min_value, max_value) # печать любого резульата


# ДЗ 03/07/25 в Телеграм

# import sys # подключение системных команд для использования в командной строке консоли
# strings = [d.strip('\n') for d in sys.stdin.readlines()] # задаем условие вывода данных на экран при потоковом вводе
# lenght = len(strings) # сколько строк
# rem = lenght % 3
#
# if rem:
#     strings = strings[:lenght - rem]
#
# for x in range(0, lenght - rem, 3):
#     summ = sum(len(a) for a in strings[x:x + 3] ) # sum оператор вычисляющий сумму элементов списка
#     # считаем сумму каждой тройки строк
#     result = []
#     for s in strings[x:x +3]:
#         temp = s.lower().split()
#         result += filter(lambda  a: len(a) % 2 == summ % 2, temp)
#     result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]
#     print(*result, sep='. ')
