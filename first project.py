# Документы по шаблону (из методичек https://disk.yandex.ru/d/9HNsXg77_qeidg
# Внешние библиотеки
# Создаем и пишем свою библиотеку lib.py в проекте и подключаем её модули
# Установка lib.py - модулей Сложение, Вычитание) - pip install lib
# from . lib import summ - из текущей дирректории
# from .. lib import summ - уровнем выше
# from .lib import summ - относительный импорт (лучше не злоупотреблять)

# from package1 import * # для __all__
# from package1.module import greet
from package1 import *



print(greet('Мир'))
print(add(3, 7))
print('Автор')
#print(package1.module._hidden_function()) # при попытке вывода результата скрытой функции _hidden_function
                                          # выдается предупреждение об ограничении её использования


import lib
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
