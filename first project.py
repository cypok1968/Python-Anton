# Библиотека pymorphy
# pip install pymorphy3  (подключаем библиотеку)
# pip install -U pymorphy3-dicts-ru (подключаем словарь)

import pymorphy3
from pymorphy3 import MorphAnalyzer

morph = pymorphy3.MorphAnalyzer()

form = MorphAnalyzer().parse('бутылка')[0]

for btl in reversed(range(99)): # склоняется слово "бутылки" при переборе количества бутылок от 1 до 99)
    print(f'В холодильнике {btl+1} {form.make_agree_with_number(btl+1).word} пива')
    print('Возьмём одну и выпьем') # вынимаем по одной бутылке из холодильника
                                   # (запуск цикла с правильным склонением слова "бутылки")
    if btl % 10 == 1 and btl != 11:
        remain = 'Осталась '
    else:
        remain = 'Осталось '
    print(f'{remain}{btl} {form.make_agree_with_number(btl).word} пива.')


#print(morph.parse('пила')) # анализирует слово "пила" на предмет двоякости (существительное, глагол)



# Исключения (runtime - время выполнения процедуры (программы))
# try:
#     определяемся, что будем делать с исключением
# except:
#     обрабатываем исключение
# else:
#     если исключения не было
# finally:
#     выполняется в любом случае
# import pickle # процесс с применением т.н. "засолки"

# import pickle
#
# voc = {
#     'стол': 'table',
#     'стул': 'chair'
# }
#
# # функция для распечатки словаря
# def print_voc():
#     print('Сейчас словарь содержит: ')
#     for k, v in voc.items():
#         print(k, '-', v) # Alt + 0151
#
# # загружаем словарь из файла
# try:
#     with open('dict.dat', 'rb') as dump_in:
#         voc = pickle.load(dump_in)
# except FileNotFoundError:
#     with open('dict.dat', 'wb') as dump_out:
#         pickle.dump(voc, dump_out)
#     print('Создан минимальный словарь: ')
#     print_voc()
#
# while True:
#     temp = input('\nВведите слово для перевода или "#" для завершения: ')
#     word = temp.strip().lower()
#     if word == '#' or word == '№':
#         break
#     if word in voc.keys():
#         translate = voc[word]
#         print(f'Слово "{word}" переводится как {translate}.\n')
#     else:
#         print(f'Значение слова {word} отсутсвует в словаре.')
#         newkey = f'А как слово {word} переводится?'
#         newkey += 'Если ничего не вводите нажмите ENTER, \n'
#         newkey  += 'или введите его здесь: '
#         new_word = input(newkey)
#
#         if new_word != '' or len(new_word) > 2:
#             voc[word] = new_word
#             print(f'Слово {word} с переводом {new_word} внесено в словарь.')
#         else:
#             print('Ничего не введено или слишком короткое слово.')
#             continue
#
# # Необходимо сохранить новый словарь
# with open('dict.dat', 'wb') as dump_out:
#     pickle.dump(voc, dump_out)
#
# print('До новых встреч!!!')


# Задача 2 выявление исключений при делении двух чисел

# 2-й способ с использованием цикла try

# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#     try:
#         result = int(a) / int (b)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!!!')
#     except ValueError:
#         print('Нужно вводить числа...')
#         print(f'А введено: {a} и {b} :(')
#     else:
#         print(result)
#         break

# 1-й способ с использованием цикла if
# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#
#     if a.isdigit() and b.isdigit():
#         if int(b) == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(int(a) / int(b))
#             break
#     else:('Вводить надо только числа')

# #Задача 1.
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# try:
#     index = int(input('Введите индекс: '))
#     if -len(lst) < index < len(lst) -1:
#         raise ValueError('Индекс вне диапазона')
#     res = lst[index]
#     print(f'Число по индексу {index}: {lst[index]}')
# except ValueError as exp:
#     mess, val = exp.args
#     if mess[0].startswith('invalid literal'):
#         print(f'Вводить надо числа.')
#     else:
#         print(exp)


# Утверждения (assertions) разработаны для поиска оптимального решения части программы
# (проверка "всегда ли будет так работать")
# try:
#     text = input('Введите текст: ')
#     assert  len(text) > 3 # это утверждение
# except AssertionError:
#     print('Слишком короткий текст')

# "Бросаемся" исключениями - raise

# max_val = 10
# min_val = 1
#
# try:
#     val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
#     if not  min_val < val < max_val:
#         raise  ValueError('введенное число вне диапазона')
#     print(f'Введенное число {val} лежит в заданном диапазоне')
# except ValueError as exp:
#     print('Надо быть внимательнее: ', exp)


# from jinja2.ext import loopcontrols
#
# print('Остаток от деления:')
#
# loop = True
#
# while loop: # потоковый ввод чисел для деления 10 c выводом рез-та
#     try:
#         value = int(input('На что делим число 10:')) # возможны исключения: деление ноль,
#                                                  # деление не на целое число
#         res = 10 % value
#         print(f'Остаток от деления на {value} = {res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#     except  ValueError:
#         print('Надо вводить только целые числа')
#     except Exception as exp:
#         print('Произошло исключение:',
#           exp.__class__.__name__,
#           exp)
# else:
#     loop = False

# print('Остаток от деления:')
#
# try:
#     value = int(input('На что делим число 10:')) # возможны исключения: деление ноль,
#                                                  # деление не на целое число
#     res = 10 % value
#     print(f'Остаток от деления на {value} = {res}')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except  ValueError:
#     print('Надо вводить только целые числа')
# except Exception as exp:
#     print('Произошло исключение:',
#           exp.__class__.__name__,
#           exp)

# print(name) # выдает ошибку при выводе на печать файла, которого нет
# fo = open('information') # выдает ошибку при открытии файла, которого нет


# try:
#     fo = open('information') # проверка открытия файла для получения инфо о его наличии
# except FileNotFoundError:
#     print('Такого файла нет')
####################################################################################

# flag = False
#
# try:
#     fo = open('information', encoding='utf-8') # проверка возможности открытия файла
# except FileNotFoundError:
#     fo = open('information', 'wt', encoding='utf-8')
#     flag = True
#     print('Файл не обнаружен и создан с параметрами по умолчанию.')
#
# else:
#     print('Файл открыт успешно. Читаем его и закрываем.')
#     print(fo.read())
#     fo.close()
# finally:
#     if flag: # проверка флага
#         fo.write('По умолчанию')
#         fo.close()
#     print('Продолжаем работать.')

# try:
#     fo = open('information')
#     print(fo.read())
#     fo.close()
# except FileNotFoundError: # без FileNotFoundError не использовать, т.к. слишком много исключений
#     print('Файл не обнаружен и создан с параметрами по умолчанию.')
#     with open('information', 'wt', encoding='utf-8') as fo:
#         fo.write('По умолчанию')
# else:
#     print('Файл открыт успешно. Читаем его и закрываем.')
#     print(fo.read())
#     fo.close()
# finally:
#     print('Продолжаем работать.')

# Файлы это набор данных, сохраненных на носителе инфо определённой структуры, содержащем имя и расширени
# расширение может ни о чём не говорить, если файл другой структуры
# name.txt (текстовые файлы, читаемые), бинарные (двоичные) в отличие текстовых не читаются (в смысле инфо)
# t - текстовый файл (txt, html, xml)
# b - бинарный файл (jpg, avi, mp3)
# w - write (запись: файл создаётся или если он был, то всё что в нём было стирается)
# a - append (добавление записи в конец файла, сам файл не стирается)
# r - read (чтение: по умолчанию)
# print(*args, sep'', end='\n', file=None, flush=False) аргументы для печати

# from path_lib import *
#
# print(img_dir)
# print(font_dir)

# import pickle # процесс с применением т.н. "засолки"
# import pprint

# d = {
#     'стол': 'table',
#     'стул': 'chair'
# }
#
# # сериализация (последовательность элементов файла (словаря) помещают, преобразовывают в компактный файл, набор байт нечитаемый)
# with open('dictfile.dat', 'wb') as p: # открываем бинарный файл
#     pickle.dump(d, p) # d - что сериализуем, p - куда сериализуем

# десериализация (является небезопасной, т.к. возможно проникновение вирусов, действующих на уровне прав ОС)
# with open('dictfile.dat', 'rb'):  # открываем файл
#     d = pickle.load(p)  # загружаем файл (читаем, как p)
#
# pprint.pprint(d, width=15)



# res = [] # создаем пустой список
#
# with open('info.txt', 'rt') as f: # переписываем все элементы строк
#     while temp := f.readline(): # читаем строку из файла
#         res += temp.split(', ')
#
#
# # res = list(map(lambda  x: x.rstip('\n'), res)) # отбрасываем ненужные символы
# # res = set(res) # превращаем в множество
#
# res = set(list(map(lambda  x: x.rstip('\n'), res))) # упрощаем 2-е записи
#
# res = sorted((int(x) for x in res)) # формируем новый список переведенный в числа
#
# res = [int(x) for x in set(res)]
#
# print(res)

# res = [] # создаем пустой список
#
# with open('info.txt', 'rt') as f: # переписываем все элементы строк
#     while temp := f.readline().rstip('\n'): # читаем строки из файла
#         res += temp.split(', ')
#
# # res = list(map(lambda  x: x.rstip('\n'), res)) # отбрасываем ненужные символы
# # res = set(res) # превращаем в множество
# # res = set(list(map(lambda  x: x.rstip('\n'), res))) # упрощаем 2-е записи
#
# res = sorted((int(x) for x in res)) # формируем новый список переведенный в числа
#
# print(res)
