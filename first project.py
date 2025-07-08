# Исключения
# try:
#     определяемся, что будем делать с исключением
# except:
#     обрабатываем исключение
# else:
#     если исключения не было
# finally:
#     выполняется в любом случае


# print(name) # выдает ошибку при выводе на печать файла, которого нет
# fo = open('information') # выдает ошибку при открытии файла, которого нет


# try:
#     fo = open('information') # проверка открытия файла для получения инфо о его наличии
# except FileNotFoundError:
#     print('Такого файла нет')
####################################################################################

flag = False

try:
    fo = open('information', encoding='utf-8') # проверка возможности открытия файла
except FileNotFoundError:
    fo = open('information', 'wt', encoding='utf-8')
    flag = True
    print('Файл не обнаружен и создан с параметрами по умолчанию.')

else:
    print('Файл открыт успешно. Читаем его и закрываем.')
    print(fo.read())
    fo.close()
finally:
    if flag: # проверка флага
        fo.write('По умолчанию')
        fo.close()
    print('Продолжаем работать.')

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
