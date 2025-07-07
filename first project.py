# Файлы это набор данных, сохраненных на носителе инфо определённой структуры, содержащем имя и расширени
# расширение может ни о чём не говорить, если файл другой структуры
# name.txt (текстовые файлы, читаемые), бинарные (двоичные) в отличие текстовых не читаются (в смысле инфо)
# t - текстовый файл (txt, html, xml)
# b - бинарный файл (jpg, avi, mp3)
# w - write (запись: файл создаётся или если он был, то всё что в нём было стирается)
# a - append (добавление записи в конец файла, сам файл не стирается)
# r - read (чтение: по умолчанию)


# fo = open('info.txt', 'wt', encoding='utf-8') # запись в файл

# fo.write('Хороший текст.')
# print('\nА вот это будет уже с новой строки.', file=fo)
# print('\nА вот ещё одна строка.', file=fo)

fo = open('info.txt', 'rt', encoding='utf-8')

# Построчное чтение № 1
# while text := fo.readline():
#     print(text.rstrip('\n'))

# Построчное чтение № 2
# lst = fo.readlines()
# lst = list(map(lambda x: x.strip('\n'), lst))
# print(lst)

# Построчное чтение № 3
text = fo.read()
lst = text.splitlines()
print(lst)

fo.close()

# text = fo.read(11) # в скобках указывается сколько начальных байт текста читать (для (3)='Это')
# fo.read(6) # СЛЕДУЩЕЕ ЧТЕНИЕ НАЧИНАЕТСЯ С 12 позиции (со следующей)
# text += fo.read(7)
# print('Вот что было в файле', end=': ')
# print(text)

#fo.close() # лучше закрывать файлы в конце их вызова, даже только для чтения

# fo = open('info.txt', 'wt', encoding='utf-8')
# # print(fo.mode)
# # print(fo.name)
# # print(fo.encoding)
#
# count = fo.write('Этот текст будет в файле!')
# print('В файл записано', count, 'байт!')
# fo.close()

# Документы по шаблону (из методичек https://disk.yandex.ru/d/9HNsXg77_qeidg
# Внешние библиотеки
# Создаем и пишем свою библиотеку lib.py в проекте и подключаем её модули
# Установка lib.py - модулей Сложение, Вычитание) - pip install lib
# from . lib import summ - из текущей дирректории
# from .. lib import summ - уровнем выше
# from .lib import summ - относительный импорт (лучше не злоупотреблять)

# from package1 import * # для __all__
# from package1.module import greet
# from package1 import *
#
# print(greet('Мир'))
# print(add(3, 7))
# print('Автор')
# #print(package1.module._hidden_function()) # при попытке вывода результата скрытой функции _hidden_function
#                                           # выдается предупреждение об ограничении её использования
#
#
# import lib
#from lib import diff
#from lib import summ
# print(lib.diff(7, 3))
#
# if __name__ == '__main__': # 1-й способ печати значения функции суммирования для файла, в котором
#                            # работаем (имя рабочего файла (first project), где находимся всегда имя main)
#     print(lib.summ(5, 3))
#
# # print(lib.summ(7, 3))
#
# def main():
#     print(lib.summ(7, 3))
#
#
# if __name__ == '__main__': # 2-й способ печати значения функции (через def) суммирования lib.py для файла,
#                            # в котором работаем (имя рабочего файла (first project), где находимся всегда имя main)
#     main()
