# ООП (объектно-ориентировуанное программирование)
# описание объектов реального мира языком прг-я: их свойств и методов (что делать с объектом)
# класс объекта - прототип будущего объекта, который описывает модель объекта, его свойства и поведение,
# т.е. данные и методы работы с ними
# класс - набор аттрибутов объекта
# объект - экземпляр класса объекта (даже пустой объект является экземпляром)
# метод - как на объект можно воздействовать, организовать использование его свойств
# encapsulation - инкапсуляция, то есть сокрытие внутри капсулы данных объекта прг
# (дополнительно на тему исп-я скрытых программ: mypy - агрессивный литерн, встроенный
# для проверки хороших практик в PyCharm, выявляет непонятные ему вызовы скрытых объектов)

# a = 3 # св-ва объекта 3 ( а также 3, None)
# print(a.__class__.__name__) # a. - метод определения свойств объекта (класс и имя)

# Методы классов и анализ предыдущих вызовов
# Конструктор - метод, называющийся как и класс но с 2-мя скобками Констр. = Класс К() (в прг __init__)
# Имя Класса всегда начинается с большой Буквы
# Статичные члены класса
# ДЗ+ 09/07/25 - добавить в lib геттеры и сеттеры для Car брэнда, модели и цвета

from lib import Balance

b = Balance(),

b.add_left(5)
b.add_right(4)
b.add_left(3)
b.add_right(5)
b.add_left(6)
b.add_right(7)
b.add_left(2)
b.add_right(4)

print(b.result())

# from  lib import Sorter
#
# s = Sorter()
#
# s.add_word('Привет')
# s.add_word('пока')
# s.add_word('здорово')
#
# print(s.result())


# from  lib import Separator
#
# s = Separator()
#
# for i in range(20):
#     s.add_num(i)
#
# print(s.get_odd())

# from lib import Clicker
#
# cl = Clicker()
#
# cl.click()
# cl.click()
# cl.click()
#
# print(cl.get_counter())
# cl.reset()
# print(cl.get_counter())

# from lib import  Car
#
# car = Car()
#
# print(dir(car)) # вызов на экран переменных и методов (свойств) Класса

# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# print('В парке машин: ', Car.get_counter())

# Геттеры и сеттеры

# если этот метод класса добавить в lib, то вызов метода класса через from lib import Person
# class Person:
#     def __init__(self, name='Bill', age=1):
#         # свойства (поля) класса
#         self._name = name
#         self._age = age
#
#     def person_info(self):
#         print(f'Человек с именем {self._name}. Возраст: {self._age}.')
#
#     # setter - атрибут класса: устанавливает значение поля
#     def set_name(self, new_name):
#         if new_name:
#             self._name = new_name
#
#     def set_age(self, new_age): # прошло несколько лет, человек вырос
#         if 0 < new_age < 150:
#             self._age = new_age
#         else:
#             print('Некорректный возраст - ', new_age)
#
#     # getters
#
#     def get_name(self):
#         return self._name
#
#
#     def get_age(self):
#         return self._age
#
#     def person_info(self):
#         print(f'{self._name}.{self._age}')
#
# p = Person()
# p.set_age(89)
# print(p.get_name())
# p.person_info()
# print(p._age) # нельзя к члену класса обращаться напрямую p.age, то есть и в поле класса
# print(p._name)


# from lib import Car (можно выгрузить, если метод класса занесён в нашу библиотеку lib)
# class Car:
#     def __init__(self, brand='Nonamt', model='Nomodel', color='Nocolor'):
#         self.brand = brand #'Skoda'
#         self.model = model #'Octavia'
#         self.color = color # 'red'
#         self.engine_on = False
#         #print('Конструктор вызван') # сначала просто заглушка, изменения см. ниже
#
#     def start_engine(self):
#         self.engine_on = True # через self.* фиксируем локальную переменную * метода, как внешнюю
#                               # (сохраняемая после исп-я метода ячейка памяти)
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place} на {self.brand}', {self.model}, {self.color})
#         else:
#             print('Двигатель не заведён, не едем')
#
# car = Car('Skoda', 'Octavia', 'red') # () - вызывает сразу метод Конструктора (__init__)
# car.start_engine()
# car.drive_to('город')


# Этот Метод для Класса не работает, требует доработки (см.выше)
# class Car:
#     def start_engine(self):
#         self.engine_on = True  # через self.* фиксируем локальную переменную * метода, как внешнюю
#         # (сохраняемая после исп-я метода ячейка памяти)
#
#     def drive_to(self, place):
#         if self.engine_on:
#             print(f'Едем в {place}')
#         else:
#             print('Двигатель не заведён, не едем')
#
#
# car = Car()
# car.start_engine()
# car.drive_to('город')


# Методы классов
# class Greater: # вызов свойства любого объекта класса Greater
#     def hello(self): # self при вызове не пишется но подразумевается для любого объекта класса
#         print('Привет, мир!') # self это контекстный объект, через который передается вызванный метод класса
#                               # через него интерпретатор понимает какой объект вызвал метод (функция)
#                               # self определяет ссылку, которая ведёт на опредённый адрес памяти
#                               # ячейка памяти переменной с именем g, g2 и т.п.
#
#     def goodbye(self, name='Noname') -> None:
#         print('Пока,', name)


# g = Greater() # создали объект
# g.hello() # создали и вызвали метод (функцию объекта), привязанный к любому экземпляру класса Greater
# g.goodbye()
# g = Greater() # создали второй объект
# g.hello() # создали и вызвали метод (функцию объекта), привязанный к любому экземпляру класса Greater
# g.goodbye()
# g.hello('Ольга') # присваиваем переменной внутри метода класса и задаем аргумент для вывода метода
# Свойства классов
# class Fruit:# создание пустого класса Fruit:
#     pass
#
#
# a = Fruit()
# b = Fruit()
# c = Fruit()
#
#
#
# # присваиваем свойства элементу созданного класса
# a.name = 'Яблоко' # даём имя переменному элементу
# a.weight = 120 # задаём вес нового элемента
# b.name = 'Груша'
# b.weight = 150
#
# print(a.name)
# print(b.weight)
# print(c.weight) # если с не присвоили аттрибут "вес",
#                 # то при выводе ошибка что этот аттрибут с не существует
# print(a.__class__)

# Регулярные выражения (поиск по патерну)
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от n до m раз (без пробела)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности (32767) {0,}
# + - от 1 до бесконечности (32767) {1,}
# https://regex101.com сайт для работы с квантификаторами

# import re
# from re import sub

# pattern = r'<img[^>]+src="([^">]+)"'
# # Сначала проверили
# test_string = '<img height="50" width="150" src="images/bg.jpg">"'
# html = requests.get('https://skillbox.ru') # метод get качает инфо о сайте
# html = requests.get('https://skillbox.ru').text # метод get качает вывод инфо в текстовом формате
# result = re.findall(pattern, html) # выбираем на экран терминала пути ко всем картинкам сайта
#                                   # копировани и редактирование html картинок с сайта
#                                   # является незаконным по отношению к авторским правам правообладателя
# print(html)
#
# result = re.findall(pattern, test_string)
# print(result)



# pattern = r'\b\w{4}\b' # все слова из 4 символов СИМВОЛ "r" используем только
#                        #  когда в строка выбора есть метасимволы
#                        через символ "\"(в обычных скобках группа захвата метасимволов)
# pattern = r'\d' # все цифры от 0 до 9
# pattern = r'\d{3}' # три цифры подряд
# pattern = r'начало!\Z' # на что заканчивается
# test_string = 'Главное - начало!'
# pattern = '[0-5] [0-9]' # две идущие подряд
# pattern = '[а-яА-Я]' # все буквы от а до я и от А до Я
# pattern = '[^ерм]' # исключить из вывода символы (вывод всех символов, кроме исключенных)
# test_string = 'Время - 07:55'
# pattern = r'\((.+?)\)' # извлечение текста из скобок по образцу
#                        # (ищет в отдельном выражении повторение символа один и более раз)
# test_string = 'Поиск по образцу (pattern)'

# pattern = 'o{2, 5}' # извлечение текста из скобок по образцу
#                        # (ищет в отдельном выражении повторение сивола "o" от 2 до 5 раз)
# pattern = 'Go{2,}gle' # ищет в отдельном выражении повторение сивола "o" от 2 и более раз
# pattern = r'стеклянн?ый' # 2-я "n" может присутствовать, но не обязательно
# "жадный" (без ?) и "ленивый" (с ?) квантификатор (greedy quantifitr)
# pattern = r'<img*>' # жадный квантификатор
# pattern = r'<img*?>' # ленивый (lazy, non-greedy) квантификатор
# test_string = 'Картинка <img src="bg.jpg"> в тексте <\p>'
# pattern = r'<img[^>]+src="([^">]+)"' # только путь к картинке
                                     # можно найти на любом сайте и использовать
                                     # (нарушает авторские права обладателя)
# pattern = '<p>(.*?)</p>' # содержимое абзаца html
# pattern = r'<p[^>]*>(.*)</p>'# содержимое абзаца html с атрибутами



# def remove_punctuation(input_str: str) -> str:
#     """"
#     Методом sub()  заменяем все найденные совпадения
#     пустой строкой и возвращаем "очищенную
#     :param input_str: строка со знаками препинания
#     :return: строку очищенную от зн. преп.
#     """
#     return re.sub(r'[^\w\s]', '', input_str)
#
# test_string = 'Язык Python! явл?яется интуи,тивно понят.ным для; изучения'
#
# result = remove_punctuation(test_string)
# print(result)

# pattern = r'[,.:;!]'
# test_string = 'яблоко,груша.банан;слива!абрикос'
# test_string =''.join(test_string.split()) # убираем все пробелы
# result = re.split(pattern, test_string)
# через map
# result = list(map(lambda x: x.strip(), result))
# через list comprehension
# result = [x.strip() for x in result]
# result = sorted(x.strip() for x in result) # с сортировкой, если нужно
# print(result)




# test_string = '<b>Центрируем</b><p></b><p align="center">Содержимое</p>'
# test_string = '<b>Вот начало: </b><p>Содержимое</p><i>и т.д.</i>'
# test_string = 'стеклянный, стекляный, оловянный, серебряный'

# test_string = 'Google, Goooogle, Goooooooogle'
# test_string = 'телефон 112'
# result = re.findall(pattern, test_string)
# print(result)
# Ternary If (тернарный условный оператор)
# print('Цифры есть') if result else print('Цифры есть')

# # pattern = '20' # задаем символ поиска в строке
# pattern = r'\b\w{4}\b' # сырая строка выявляет четыре подряд идущих символа (без пробелов)
# #test_string = '10 плюс 20 будет 30' # создаем анализируемую строку
# test_string = 'дома было холодно' # создаем анализируемую строку
#
# #result = re.search(pattern, test_string)
# result = re.findall(pattern, test_string) # ищет все повторения 4-х символов подряд в строке
# print(result)

