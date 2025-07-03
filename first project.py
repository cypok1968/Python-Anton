# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>:<выражение>
# потоковый ввод sys.stdin (система.стандартного потокового ввода) через консоль командной строки:
# потоковый ввод sys.stdin (система.стандартного потокового ввода) через консоль командной строки:
# Ctrl + D в Pycharm, Ctrl + Z в Linox (ключевые клавиши для потокового ввода)

import sys # подключение системных команд для использования в командной строке консоли

# запуск программы потокового ввода через символ "плэй",
# вводим строку "Фразеологи́зм, фразеологический оборот или фразема"
# за ней ещё строку строку " — свойственное определённому языку устойчивое словосочетание,
# смысл которого не определяется значением отдельно взятых слов, входящих в его состав."
# далее нажимаем Ctrl + D в Pycharm
# вывод потокового ввода в виде списка заданной структуры в описании data
# ['Фразеологи́зм, фразеологический оборот или фразема',
# '— свойственное определённому языку устойчивое словосочетание,
# смысл которого не определяется значением отдельно взятых слов, входящих в его состав.']
data = sys.stdin.readlines() # запускаем программу работы с потоковым вводом (через командную строку)
data = [d.strip('\n') for d in data] # задаем условие вывода данных на экран при потоковом вводе
print(data)






# проверка коллекций: any(), all()
# any - хотя бы один (любой) элемент коллекции вернул True
# all - се элементы коллекции вернули True

# print(all([1, 2, 3])) # все элементы ненулевые
# print(all([1, 2, 0])) # один элемент нулевой
# print(all([])) # пустой список возвращает True (видимо есть элемент и расценивается как "пробел")
#
# words = 'один два три'.split()

# list_for_analize = list(map(lambda x: len(x) > 3, words)) # все ли элементы списка > 3
# print(all(list_for_analize))
# print(any(list(map(lambda x: len(x) > 3, words)))) # есть ли хотя бы один элемент > 3

# numbers = [1, 2, 3, 4, 5] # или list(range(1, 6))
# squares = {n: n ** 2 for n in numbers}
# print(squares)
#
# numbers = range (1, 11) - можно перенести внутрь словарного выражения для краткости записи
# squares = {n: n ** 2 for n in range (1, 10) if n % 2 == 0}
# print(squares)
#
# source_dict = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# dest_dict = {k: v * 2 for k, v in source_dict.items()}
# print(dest_dict)

# fruits = ['арбуз', 'ананас', 'ежевика', 'арбуз', 'малина']
#
# print(sorted(fruits, key=lambda s: (len(s), s[-1]))) # сначала сортировка по длине слов, затем по последней букве

# goods = [
#     ['Утюг', 1500, 2],
#     ['Фен', 1000, 5],
#     ['Телевизор', 8000, 3]
# ]

# print(sorted(goods)) # по умолчанию сортировка по первому символу строки (по алфавиту) в списках
# print(sorted(goods, key=lambda s: s[1])) # сортировка по возрастанию второго элемента (числа) в списках
# print(sorted(goods, key=lambda s: (s[1], s[2], s[0]))) # последовательная сортировка по 3 ключам сортировки

#print(sorted(fruits, key=lambda ch: len(ch))) # ключ сортировки key - критерий по которому будет сортировка

# fruits.sort()
# print(fruits)

# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^ set([x.upper() for x in RUSSIAN_ABC]) ^ set([x.upper() for x in RUSSIAN_ABC]))
# print(ABC)
# print(ENGLISH_ABC)
# print(RUSSIAN_ABC)


# text = 'Однажды, теперь и потом.'.lower()

# txt = ['', '']
#
# def remove_punctuation(text):
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, text)) # убираем знаки из текста
#
#
# def get_word(text: str) -> list:
#     return remove_punctuation(text).split() # вывод текста в виде списка
#
#
# def long_words(text, length=4) -> list:
#     return filter(lambda word: len(word) >= length, get_word(text))
#
# words = get_word(txt.lower())
#
# Считаем частоту слов:
# for word in words:
#     if word in words:
#         if word in d:
#             d[word] += 1
#         else:
#             d[word] = 1
#
# res = {k: v for k, v in sorted(d.item(), key=lambda item: item[1], reverse=True)}
#
# for k, v in res.items():
#     print(k, v)

# print(long_words(text))
# text = ''.join(filter(lambda x: x in ABC ^ {' '}, text))
# print(text)

# def is_longer_six(word):
#     return len(word) > 6
#
#
# is_longer_six = lambda word: len(word) > 6
#
# def is_first_letter_(word):
#     return world[0] == a
#
#
#     return  word[0] ==

#fruits = ['арбуз', 'ананас', 'банан', 'малина', 'ежевика']
#
# res = list(filter(lambda x: x[0] == 'a', fruits))
# print(res)
#
# res = list(filter(lambda s: 'ан' in s, fruits))
# print(res)
#
# # в одну строку вывести список квадратов чисел от 3 до 15
# # [9,16,...]
# res = list(map(lambda y: y ** 2, range(3, 16)))
# print(res)
# res = [y ** 2 for y in range(3, 16)]
# print(res)
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#           'длина', 'которых', 'больше', 'шести']

# result = list(filter(lambda word: len(word) > 6. words))

# long_words = [word for word in words if len(word) > 6]
# print(long_words)
