# Регулярные выражения (поиск по патерну)
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от m до n раз (без пробела)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности (32767) {0,}
# + - от 1 до бесконечности (32767) {1,}
# https://regex101.com сайт для работы с квантификаторами

import re
import requests

pattern = r'<img[^>]+src="([^">]+)"'
# Сначала проверили
# test_string = '<img height="50" width="150" src="images/bg.jpg">"'
# html = requests.get('https://skillbox.ru') # метод get качает инфо о сайте
html = requests.get('https://skillbox.ru').text # метод get качает вывод инфо в текстовом формате
result = re.findall(pattern, html) # выбираем на экран терминала пути ко всем картинкам сайта
                                  # копировани и редактирование html картинок с сайта
                                  # является незаконным по отношению к авторским правам правообладателя
print(html)


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
#     return re.sub(r'[^\w\s], ', input_str)

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

# test_string = 'Язык Python, явл?яясь интуи,тивно понятным, прост для изучения'

# result = remove_punctuation(test_string)


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

