# Черепашья графика в Python grafic
import  turtle as t # - добавляем описание прг turtle
#
# N = 8
t.speed(5) # замедление скорости воспроизведения (0 - мгновенно рисует)
# # черепашка рисует в цвете согласно введенных условий
# colors = ['red','purple','blue','green','yellow','orange']

# t.bgcolor('black')
# angle = 360 // len(colors) - 1
#
# for x in range(200):
#     t.pencolor(colors[x % len(colors)]) # цвет для каждого шага свой
#     t.width(x // 100 + 1) # толщина линии
#     t.forward(x)
#     t.left(angle)



# t.penup() # задаем положение черепашки в любом месте граф.экрана
#                # согласно указанным коорд
# t.goto(100, 200)
# t.pendown()

# for _ in range(4): # черепашка рисует квадрат из центра экрана (по умолчанию
#     t.forward(100)
#     t.right(90)
#
#
# for _ in range(4): # черепашка рисует треугольник
#     t.forward(120)
#     t.right(90)


# for _ in range(N): # черепашка рисует N кругов с центром в заданной области (положение черепашки)
#     t.circle(50)
#     t.right(360 // N)
#
# for _ in range(N): # черепашка рисует N-угольник
#     t.forward(100)
#     t.right(360 // N)

# for _ in range(N):
#     for _ in range(4): # черепашка рисует N-угольник
#                       # указанное количество раз со смещением
#         t.forward(100)
#         t.forward(90)
#     t.right(360 // 5)

# def square(side):
#     for _ in range(4):
#         t.forward(side)
#         t.right(90)
#
#
# def flower():
#     for _ in range(36):
#         t.circle(50)
#         t.right(10)

# for _ in range(N):
#     flower()

def tree(lenght):
    if lenght < 10:
        return
    t.forward(lenght)
    t.left(30)
    tree(lenght * 0.7)
    t.right(60)
    tree(lenght * 0.7)
    t.left(30)
    t.backward(lenght)

t.left(90)
tree(100)
#
t.mainloop()


# Рекурсия - функция вызывает сама себя
# прописываем обязательно условие выхода из рекурсии!
# если можно обойтись без рекурсии, то её не используем!

# 1. программа факториал через внутренний цикл умножения перебираемой последовательности целых чисел
# def factorial(count):# 5! = 1*2*3*4*5 = 120
#     result = 1
#     for i in range(2, count + 1):
#         result *= i
#     return result
#

# 2. программа факториал через рекурсивный цикл
# обращения функции на каждом этапе к самой себе через значение переменной (по числу), помещаемому в стек
# def factorial(x):
#     if x == 1 or x == 0: # базовый вариант, рекурсия прекращается когда х = 1
#         return 1
#     return x * factorial(x - 1) # рекурсивная пружина
#
#
# for x in range(10):
#     print(x, factorial(x))
#      V
#      V
#      V
# factorial <- 1*2
# factorial <- 2*3
# factorial <- 6*4
# factorial <- 24*5
# factorial <- 120 первым приходит в стековую область памяти значений факториала уменьшением аргументов (чисел)




# Анонимные функции (однострочники, безымянные)

# info@inpap.ru по любым вопросам писать для Анны

# lambda-функции
# lambda <аргументы>:<выражение>
# потоковый ввод sys.stdin (система.стандартного потокового ввода) через консоль командной строки:
# потоковый ввод sys.stdin (система.стандартного потокового ввода) через консоль командной строки:
# Ctrl + D в Pycharm, Ctrl + Z в Linox (ключевые клавиши для потокового ввода)

# import sys # подключение системных команд для использования в командной строке консоли


# запуск программы потокового ввода через символ "плэй",
# вводим строку "Фразеологи́зм, фразеологический оборот или фразема"
# за ней ещё строку строку " — свойственное определённому языку устойчивое словосочетание,
# смысл которого не определяется значением отдельно взятых слов, входящих в его состав."
# далее нажимаем Ctrl + D в Pycharm
# вывод потокового ввода в виде списка заданной структуры в описании data
# ['Фразеологи́зм, фразеологический оборот или фразема',
# '— свойственное определённому языку устойчивое словосочетание,
# смысл которого не определяется значением отдельно взятых слов, входящих в его состав.']
# data = sys.stdin.readlines() # запускаем программу работы с потоковым вводом (через командную строку)
# # data = [d.strip('\n') for d in data] # задаем условие вывода данных на экран при потоковом вводе
# # print(data)
# # [(0, 3), (1. 2)]
# data = [d.strip('\n') for d in data] # задаем условие вывода данных на экран при потоковом вводе
# temp = [] # сохраняем сюда индекс строки в data и число строк в виде кортежей
# for i, s in enumerate(data):
#     temp.append((i, len(s.split()))) # строку разбиваем на слова и получаем число слов
#
# temp.sort(key=lambda x:x[1]) # temp отсортирован по условию первая вторая строка
# print(temp)
# print(temp[0])
# index = temp[0][0]
# res = sorted(data[index].split())
#
# print(*res, sep='-')

# раз два три
# елочка гори

# print(data)




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
