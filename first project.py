# ДЗ 07/07/25
# в Модули.pdf
# https://github.com/ipapMaster/Python_Web_2025.git - путь к учителю и его комитам на гитхаб.ком
# https://disk.yandex.ru/d/9HNsXg77_qeidg - путь к методичкам
# https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru - путь к шрифтам .ttf

import pickle # процесс с применением т.н. "засолки"
import pprint

# d = {
#     'стол': 'table',
#     'стул': 'chair'
# }
#
# # сериализация (последовательность элементов файла (словаря) помещают, преобразовывают в компактный файл, набор байт нечитаемый)
# with open('dictfile.dat', 'wb') as p: # открываем бинарный файл
#     pickle.dump(d, p) # d - что сериализуем, p - куда сериализуем

# десериализация (является небезопасной, т.к. возможно проникновение вирусов, действующих на уровне прав ОС)
with open('dictfile.dat', 'rb'):  # открываем файл
    d = pickle.load(p)  # загружаем файл (читаем, как p)

pprint.pprint(d, width=15)



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
