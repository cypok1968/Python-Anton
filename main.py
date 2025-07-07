#Условные алгоритмы
from random import choice

a = 1
if a == 5:
    print('а равно 5')
    print('условие выполнилось')

elif a == 3:
    print('а равно 3')
    print('условие выполнилось')

else:
        print('а не равно 5')
        print('условие не выполнилось')
print('Витязь на распутье')
print('Налево (L) пойдёшь, вольну-волю обретёшь...')
print('Направо (R) пойдёшь, коня потеряешь...')
print('Прямо (F) пойдёшь, сыт и весел будешь...')
choice = input('Куда идём (L, R или F): ')
if choice == 'L' or choice == 'l':
    print('Вольная воля')
elif choice == 'R'or choice == 'r':
    print('Конь сбежал')
elif choice == 'F'or choice == 'f':
    print('Сыт и весел')
else:
    print('Выбор не ясен')
promt = """Витязь на распутье
Налево (L) пойдёшь, вольну-волю обретёшь...
Направо (R) пойдёшь, коня потеряешь...
Прямо (F) пойдёшь, сыт и весел будешь..."""
print(promt)
choice = input('Куда идём (L, R или F): ')
if choice == 'L' or choice == 'l':
    print('Вольная воля')
elif choice == 'R'or choice == 'r':
    print('Конь сбежал')
elif choice == 'F'or choice == 'f':
    print('Сыт и весел')
else:
    print('Выбор не ясен')


    hour = 13

    if hour > 23:
        hour = 23
    if hour < 0:
        hour = 0
    if hour >= 7 and hour < 12:
        print('Доброе утро!')
    elif hour >= 12 and hour < 17:
        print('Добрый день!')
    elif hour >= 17 and hour < 23:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')
a = 3
b = 5

print('До:')
print('a =', a, 'b=', b)
temp = a
a = b
b = temp
#a, b = b, a # swap меняем значения переменных местами

print('После:')
print('a =', a, 'b=', b)

# Iterable object
# len()
from operator import length_hint

a = 123456

length = len(str(a))

print(length)

word = input ('Введите слово для анализа длины:')
if not word or len(word) < 4:
    print('Вы ничего не ввели или слово слишком короткое')
else:
    print('Длина слова "'+ word +'" =', len(word) )

# Форматы ввода-вывода
# \ - управляющая последовательность: начало escape sequence (+экранирование символов внутри строки)
# \n - перевод строки
# \t - табуляция
# \x - вывод символа по 2 знакоместам в 16-формате (ASCII)
# \u - вывод символа по 4 знакоместам в 16-формате (UNICODE)
# sep=''- сепаратор-разделитель выводимых переменных
# end='' - любой печатный символ конца строки
# Burned Again Shell - BASH (консоль Линокса)
#from tkinter.font import names

word1 = 'пришёл'
word2 = 'увидел'
word3 = 'победил'
word4 = '27\xB0C'

print(word1, word2, word3, sep=', ', end=' -> ')
print(word4, end='\n')

print("Концерт группы \"Кино\"")

# Формат вывода 2
name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32
weight = 92.233654
# 1 способ (плейсхолдеры)
# %s - string
# %d - digit (целое)
# %f - float
print('Имя: %s, E-mail: %s, Возраст %s' % (name, email, age))
# 2 способ
print('Имя: {}, E-mail: {}, Возраст {}' .format(name, email, age))
# самый популярный с версии 3.6 - f-строка
print(f'Имя: {name}, E-mail: {email}, Возраст {age}, Вес: {weight:.3f}')

"""
name: Игорь
email: aaa@bbb.ru
age: 32
weight: 92.233654
"""
#Д/З 25.06.25

promt = """
name: Игорь
weight: 92.24
height: = 180
"""
print (promt)

name = 'Игорь'
weight = 92.23654154623
height = 180

print(f'Имя: {name} \nВес: {weight:.2f} \nРост: {height}')
# решение квадратного уравнения ax**2+bx+c=0
# ввщдим коэффициенты
a = int(input('введите a:'))
b = int(input('введите b:'))
c = int(input('введите c:'))

if a != 0:
    # Дискриминант
    d = b ** 2 - 4 * a * c
    if d < 0:
        print ('Уравнение не имеет корней')
    elif d == 0:
        x = -b / (2 * a)
        print(f'Корень уравнения: {x:.2f}')
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b + d ** 0.5) / 2 * a
        print(f'Корни уравнения: \n\t{x1:.2f}\n\t{x1:.2f}')
else:
    print('По условию квадратного уравнения а не равно нулю!')

# Циклы (Loops):
# while
# while <условие>:
#    команды
# for
counter = 0 # обнуляем счетчик
# цикл из 5 итераций
while counter < 5:
    print(f'Итерация номер: {counter + 1}')
    #counter = counter + 1 # инкремент
    counter +=1 # инкремент (краткая запись)
print(f'Итого в counter уже {counter}')


counter = 5 # обнуляем счетчик
# цикл из 5 итераций
while counter > 0:
    print(f'Итерация номер: {counter}')
    counter = counter - 1 # инкремент
    #counter -=1 # декремент (краткая запись)
print(f'Обратный отсчёт: {counter}')

# Циклы (Loops):
# Цикл до ввода пустой строки
# без := "моржа"
word = input('Введите слово: ')

while word != '':
    print(f'Слово: "{word}"')
    word = input('Введите слово ')

print('Пустая строка введена')

# c := "моржом"
#while (word := input('Введите слово:')) != '':
#    print(f'Слово: "{word}"')
#print('Пустая строка введена')

# := оператор "морж" присваивает значение пременной и возвращает её значение
# только для версии Python 3.8 !!!!
#while len(word := input('Введите слово не короче 3 символов:')) <= 3:
#    print(f'Слово: "{word}" слишком короткое.')
#print(f'Вы ввели слово: "{word}"')

num = 3 # число, которое надо угадать
flag = True # флаг, изменяет значение по событию
var = '3'

print('Я загадал число, угадай!')

while flag:
    var = int(input('Ваше значение: '))
    if var == num:
        print('Ура. Угадал!')
        flag = not flag
    elif var > num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')
    # break, continue
num = 3 # число, которое надо угадать
var = ''

print('Я загадал число, угадай!')

while True:
    var = int(input('Ваше значение: '))
    if var == num:
        print('Ура. Угадал!')
        break
    elif var > num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')

#continue - прервать текущую операцию (проскочить) и начать следующую (не прерывая цикл)
counter = 0 # обнуляем счетчик
# цикл из 5 итераций, но номере 3 пропускаем
while counter < 5:
    counter += 1  # инкремент (краткая запись)
    if counter == 3:
        continue
    print(f'Итерация номер: {counter}')

# вариант 1
height = int(input('Введите, пожалуйста, свой рост в см:'))

while (height < 150) or (height > 180):
    print(f'Увы, Вы не подходите по росту!')
    height = int(input('Введите, пожалуйста, свой рост в см:'))

print('Примите наши поздравления! Ваш рост устраивает!')

# вариант 2

height = int(input('Введите, пожалуйста, свой рост в см:'))

while not (150 <= height <= 180):
    print(f'Увы, Вы не подходите по росту!')
    height = int(input('Введите, пожалуйста, свой рост в см:'))

print('Примите наши поздравления! Ваш рост устраивает!')

# match - case (для версии > 3.10)

# 1 вариант

print('Возможные ходы: \n\tL - влево\n\tR - вправо\n\tF - прямо\n\tQ - выход')
ch = input('Ваш выбор: ')

match ch:
    case 'L' | 'l' | 'д' | 'Д':
        print('Свернули налево')
    case 'R' | 'r' | 'к' | 'К':
        print('Свернули направо')
    case 'F' | 'f' | 'а' | 'А':
        print('Свернули налево')
    case 'Q' | 'q' | 'й' | 'Й':
        print('Свернули налево')
    case _:  # default
        print('Свернули налево')


# 2 вариант

print('Возможные ходы: \n\tL - влево\n\tR - вправо\n\tF - прямо\n\tQ - выход')
ch = input('Ваш выбор: ')

while flag:
    ch = input('Ваш выбор: ')
    match ch:
    case 'L' | 'l' | 'д' | 'Д':
        print('Свернули налево')
    case 'R' | 'r' | 'к' | 'К':
        print('Свернули направо')
    case 'F' | 'f' | 'а' | 'А':
        print('Свернули налево')
    case 'Q' | 'q' | 'й' | 'Й':
        print('Свернули налево')
        flag = False
    case _:  # default
        print('Свернули налево')

# цикл for
# for <переменная> in ...:
# команды
#word = 'поток'

#for ch in word:
#    print(ch)

# итератор range (start, stop, step)

#for i in range(2, 13, 2):
#    print(i)

# итератор range (0, stop, 1) - по умолчанию если не указаны 1 и 3 позиции

#for i in range(13):
#    print(i)

#for i (или _) in range(10):
#    print('Привет')

for i in range(1, 101):
    if i % 10 == 5:
        if i == 15:
            continue
    print(i)

for i in range(1, 101):
    if i % 10 == 5 and i != 15:
        print(i)

# итератор range (start, stop, step)
# итератор range (0, stop, 1) - по умолчанию если не указаны 1 и 3 позиции


for i in range(5, 96, 5):
    print(i)

# min, max, average, summ. production
N = 5
total = 0
prod = 1
min_val = float('inf') # + бесконечность
max_val = float('-inf') # - бесконечность


for _ in range(N):
    num = int(input('Введите целое число: '))
    if num < min_val:
        min_val = num
    if num < max_val:
        max_val = num
    total += num
    prod *= num
    average = total / N

print(f'Сумма: {total}')
print(f'Произведение: {prod}')
print(f'Ср. арифметическое: {average}')
print(f'Минимум: {min_val}')
print(f'Максимум: {max_val}')

# factorial
# N = 5
# fact = 1
#
# for i in range(1, N + 1):
#     fact = *=

#Вложенные циклы
for i in range (1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end='\t')
    print()

    # Подбор по росту
    # 150 < height < 180
    # Число кандидатов
    # Число, кто прошёл по критерию
    # Среди прошедших min и max
    total = 0
    total_success = 0
    total_unsuccess = 0
    min_val = float('inf')  # - бесконечность
    max_val = float('-inf')  # + бесконечность

    while (num := int(input('Введите рост: '))) != -1:
        if 150 <= num <= 180:
            total_success += 1
            if min_val > num:
                min_val = num
            if num > max_val:
                max_val = num
        total += 1

    print(f'Число кандидатов: {total}')
    print(f'Число прошедших отбор: {total_success}')
    print(f'Минимальный рост: {min_val}')
    print(f'Максимальный рост: {max_val}')

# Д/З 26.06.25 "Hахождение фальшивой монеты методом взвешивания на рычажных весах"
weighta = input ('Введите вес первой монеты: ')
weightb = input ('Введите вес второй монеты: ')
weightc = input ('Введите вес третьей монеты: ')

if weighta == weightb:
    print('Фальшивая третья монета !')
elif weighta > weightb:
    print('Фальшивая вторая монета !')
else:
    print('Фальшивая первая монета !')

# Коллекции (set, list, dict, tuple)
# Множество - набор элементов разного типа,
# при выводе на экран: нет упорядоченности элементов и устраняются все повторы элементов в множестве
s = set () # пустое множество (для будущих объектов)
print(dir(s)) # методы для множества
# s = {'3', '5', 7, '3', '5', 7} # непустое множество из констант
s.add(True) # добавление в множество элементов любого типа, в т.ч. логические
# s.remove('3') # удаление из множества элементов любого типа, в случае наличия (ошибка, если нет)
# s.discard('3') # удаление из множества элементов любого типа, даже если его нет (удаление вслепую)
# temp = s.pop() # удаляет случайный и возвращает его
# s.clear() # очищает множество полностью
print (type(s)) # класс
print(f'Число элементов в s = {len(s)}')
print('Присутствует ли 3')
if '3' in s:
    print('Да')
else:
    print('Нет')
# for item in s:
#     if item == '3': # вывод одного элемента из множества
#         print(item)
print(item)

# Города
s = set()

while (city := input('Назовите город: ')) != '':
    if city in s:
        print('Такой город уже был')
    else:
        s.add(city)
print(f'Итого было названо; {len(s)} городов')
for item in s:
    print('\t', item)

# Сдаем карты
cards = {3, 7, 'туз', 'валет', 'король', 'дама'}

while cards: # сдаем пока карты есть в колоде
    print(cards.pop())

# Сдаем карты кроме туза, оставляем в колоде
cards = {3, 7, 'туз', 'валет', 'король', 'дама'}

# 1 вариант

ace = {'туз'}
result = cards - ace
print(result)

# 2 вариант

t_is = False

while cards:
    card = cards.pop() # удаленный элемент, карта которую случайным образом сдали из колоды cards
    if card == 'туз':
        cards.add(card) # возврат карты в колоду, если это туз
        t_is = True
    else:
        print(card)

    if t_is and len(cards) == 1:
        break

# Операции над множествами
a = {3, 5, 7}
b = {3, 5, 7, 9, 11}

# Объединение множеств
c = a.union(b) # или c = b.union(a)
# c = a / b
print(c)

#PEP8 - правила именования
# недопустимые буквы в именах переменных a, c, l, O, I (т.к. похожи на рус. а, c, 1, 0, 1)
# Операции над множествами
a = {3, 5, 7}
b = {3, 5, 7, 9, 11}

# Объединение множеств (объединение элементов множеств без повторов)
c = a.union(b) # или c = b.union(a)
# c = a / b
print(c)

# Пересечение множеств (элементы, которые в обоих множествах)
c = a.intersection(b)
# с = a & b
print(c)

# Разность множеств (есть в первом множестве, но нет во втором)
c = b.difference(a)
# c = b - a
print(c)

# Симметричная разность множеств (есть только в одном)
c = a.symmetric_difference(b)
# c = b ^ a
print(c)

s = ''
print(id(s))
s += 'Привет' # измененное значение строки записывается в другую ячейку памяти,
# а предыдущее (пустое) значение удаляется мусорщиком в корзину
print(id(s))
print(s)
s += 'Hello' # следующее значение ячейки записывается в следущую ячейку с новым ID
print(id(s))
print(s)

s = 'Python'
print(s)
#s [3] = 'y' error (immutable)
# Индекс может быть отрицательным (с конца)
print(f'Длина слова: {len(s)}')
print(s[1])
print(s[-6])

# Строки (immutable) - неизменяемый, но (переписываемый в другую яч.) тип данных
# номера символов в любой строке 012345...
# Задача: посчитать гласные в слове
s = 'язык Python'

v = 0 # Число гласных

for ch in s: # ch - принято называть символьную переменную
    #if ch in {'а','е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'y', 'o'}: # 1-й вариант
    if ch in 'аеёиоуыэюяyo':
        v += 1

print(f'Число гласных в строке: "{s}" = {v}')

# Перебор строки по числовому признаку
for index in range (len(s)):
    print(s[index]) # обращение к элементу строки ch по его индексу (номеру в строке)

# Задача: исправить букву в слове "сабака"
s = 'сабака'
res = ''

for i in range(len(s)):
    if i == 1: # известно, что по индексу 1 допущена ошибка и надо поменять на "о"
        res += 'о'
    else:
        res += s[i]

print(res)

# Строки (immutable, iterable)
# Таблица символов Unicode

s = '\xB0'
u = ('\u2602')

# две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код в десятичной сист.) - возвращает символа Unicode-коду

print(u)
print('25' + s + 'C')
print(f'Код зонта в Unicode: {ord('☂')}')
print(chr(9730))
print(chr(176)) #ASCII коды от IBM (до 176 символа для всех прочих таблиц символов и для Unicode)

s = set()
word = input('Введите фразу для зашифровки: ')
#
# # Зашифровываем
for ch in word:
    s.add(ord(ch))

print(s)

# Расшифровываем

res = ''
for i in s:
    res += chr(i)

print(res)

# Каждая буква повторяется столько раз,
# какой её номер в строке (считаем с 1)

word = 'статор'
res = ''

# 1 способ
for i in range(len(word)):
     print(word[i] * (i + 1), end='')
# 2 способ
for i in range(len(word) + 1):
    print(word[i-1] * i, end='')

#ДЗ 27/06/25

# Создаем алфавит
alphabet = 'абвгдеёжзийклмнопрстуфхцъыьэюя'

# Получаем входные данные
message = input('Введите строку: ').strip().lower() # убираем пробелы слева и справа, переводим в маленькие буквы
key = int(input('Введите ключ: '))

#Инициализируем пустую строку для результата
encrypted = ''

# Перебираем каждый символ в сообщении
for letter in message:
    # Проверяем, является ли символ буквой из алфавита
    if letter in alphabet:
        # Находим позицию буквы в алфавите
        t = alphabet.index(letter)
        # Вычисляем новую позицию с учетом сдвига
        new_key = (t + key) % len(alphabet) # используем длину алфавита в 33 буквы
        # (для символа ю 31+3=34%33=1 получаем символ б)
        # Добавляем зашифрованный символ
        encrypted += alphabet[new_key]
    else:
        # Если символ не буква, оставляем его без изменений
        encrypted += letter

# Для расшифровки достаточно изменить формулу вычисления новой позиции
# new_key = (t - key) % len(alphabet)
print('Зашифрованное сообщение: ', encrypted)

# Строки (immutable, iterable)
# Начало и окончание строки
# startswith, endswith

s = 'Смотреть'

if s.lower().startswith('смо'):
    print('Да')

if s.endswith('еть'):
    print('Да')

    # 1. replace ('что, 'на что') полная замена
    # 2. replace ('что, 'на что', сколько раз) - число замен

    s = 'тиливизор'

    print(s.replace('и', 'е', 2))

    s = '+7-012-345-67-89'  # +7 (012) 345-6789

    res = s.replace('-', ' (', 1)
    res = res.replace('-', ') ', 1)

    print(res)

# Срез (у строки и у других коллекций, кроме set)
# [начало:окончание:шаг] обращение по срезу не выбрасывает за пределы строки

s = 'добрый день'

print(s[0:6:1])
print(s[7:11:1])
print(s[:6]) # если с начала и до заданного индекса (по умолчанию)
print(s[7:]) # от текущего индекса до конца (по умолчанию)
print(s[3:8]) # от n до m (не включая)
print(s[:-6]) # от начала до m (не включая m)
print(s[::2]) # c начала до конца с шагом 2

s = input('Введите строку: ').strip() # 'потоп'

if s == s[::-1].lower():
    print(f'Строка "{s}" - палиндром!')
else:
    print(f'Строка "{s}" - не палиндром!')

a = 'Python'
print(a[2:522]) # чтобы указать конец слова, можно использовать любое число превышающее количество символов

s = input('Введите строку: ').strip() # 'потоп'

if s == s[::-1].lower():
    print(f'Строка "{s}" - палиндром!')
else:
    print(f'Строка "{s}" - не палиндром!')

a = 'Python'
print(a[2:522]) # чтобы указать конец слова, можно использовать любое число превышающее количество символов

s = 'Дорог Рим город или дорог Миргород' # + u *
# Миргород дорог... дорог...
t = '...'
print(s[26:] + (s[19:25] + t) * 2)

s = 'Дорог Рим' # + u *
# Город Миргород

temp = s.lower()
city = temp[:5][::-1]
res = city + ' ' + temp[6:][::-1] + city

print(res.title())

# lst = [] # создаем пустой список, через l список называть нельзя, запрещенное имя для списков
# lst = list('Python') # каждый символ строки стал элементом списка (теперь строка - итерируемый объект)
# lst = [1,2,3] * 3 # можно использовать при создании повторы элементов списка
# lst = ['s'] * 10
# print(type(lst))
# print(lst[:2]) # срез из списка работает как и срез для строки
# print(lst)
#
# s = 'сабака'
# lst = list(s)
#
# print(lst)

# s1 = [1, 2, 3] + ['f', 89]
# s2 = [4, 5, 6]
#
# s1[0] = 22
#
# s = s1.extend(s2) # изменение величины списка s1, добавление элементов в список
#
# print(s1)

# lst = list (range(10))
# for item in lst:
#     print(item, '-', item ** 2)

# создание списка соответствия квадратов чисел от 0 до 10

# lst = list (range(10))
# del lst[::2] # удаление элемента из списка
# lst.pop() # удаляет элемент по указанному индексу (по умолчанию удаляет последний элемент)
# print(lst)
#
# lst = [1, 2, 2, 3, 4, 5]
# lst.remove(2)

# lst = [1, 7, 3, 5, 6, 4, 2]
# lst.sort() # сортирует список
# lst.reverse()

# for item in range(0, len(lst), 2):
#     print(lst[item], '-', lst[item] ** 2)
#
# lst = list (range(10))
# slice = lst[0:len(lst):2] # срез списка (по умолчанию 0 и длину всего списка можно не указывать)
# print(slice)
# for item in range(0, len(lst), 2):
#     print(lst[item], '-', lst[item] ** 2)

# a = ['a', 'b', 'c']
# b = a # новый список при этом не создается, а создается идентичный список с тем же ID (в отличие от строк)
# c = a.copy() # создаем другой список (с новым ID)
# #b.append('d') # b+= ['d']
# c.append('d') # c+= ['d']
# print(id(a))
# print(id(b))
# print(id(c))
# print(a)
# print(b)
# print(c)

lst = [] # пустой список "окрошка"

while (item := input('Ингредиент: ')) != '': # выбор ингредиентов окрошки
    lst.append(item)

temp = set(lst) # исключение повторов ингредиентов окрошки
lst = list(temp)

print(f'У нас есть {len(lst)} ингредиентов: ')

lst.sort()

for i in range(len(lst)):
    print(f'\t{i+1}. {lst[i]}') # упорядочение вывода списка

    # иммитация стека

    N = 5  # задаем количество элементов стека

    lst = []  # пустой список "стопка книг в виде стека"

    for i in range(N):
        print(f'Кладём {i + 1} в стопку.')
        lst.append(i + 1)

    print('---')

    while lst:
        item = lst.pop()  # по умолчанию получаем стек, если задать начало '0' получаем очередь (не стек)
        # то есть в каком порядке книги положены в стопку, в таком порядке и возвращаются
        print(f'Берём книгу {item} из стопки.')

# Создание аббревиатур

lst = [] # пустой список для создания аббревитуры

while (word := input('Введите слово: ').strip()) !='': # вводим последовательно построчно слова аббревиатуры
    lst.append(word[0].upper()) # выбор в каждом слове первой буквы, делаем заглавную

print('Получилась аббревиатура', end=': ')
print(*lst, sep='') # sep - убираем пробелы между буквами аббр.

# Кортеж (tuple) тот же список, но неизменяемый (отличие от строки)
from main import cards

BLACK = (0, 0, 0) # занимает в памяти меньше места, обращение к кортежу происходит быстрее

empty = () # пустой кортеж
one = (1,) # кортеж получается при проставлении запятой
s = 'Python'
t = tuple(s) # превращение строки в кортеж
t = tuple(s) + ('.',) # кортеж неизменяем, но можно создать (увеличением элементов) на его основе другой кортеж (с др. ID)
print(t)

card = [(7, 'червей'), ('туз', 'пик')] # создание списка с элементами из двух кортежей

print((1, 2) < (2, 1))

a=3
b=4
print((a, b) > (b, a))

channels = ['red', 'green', 'blue']
channels = [128, 200, 155]
r, g, b = channels # распаковка unpack

print(r, g, b)

# Студент и средний балл


N=3
students = []

for st in range(N):
    student, average = input('ФИО: '), float(input('Средний балл: '))
    students.append((student, average)) # создание кортежа из трёх списков со средними баллами (3 студента)
                                        # pack
print(students)

for st in students:
    student, average = st # unpack
    print('Студент: ', student)
    print('Средний балл: ', average)

# Функция sorted() - возвращает сортированный список

# 1 способ с sorted()
s = {'Иванов', 'Петров', 'Сидоров'}
r = False

lst = sorted(s, reverse=r)

print(*lst, sep=', ')

2 способ без sorted()

s = {'Иванов', 'Петров', 'Сидоров'}

lst = list(s)
lst.sort()

print(*lst, sep=', ')

# Функция enumerate () - в цикле for возвращает пару (i, v)

fio = ['Иванов', 'Петров', 'Сидоров']

for item in enumerate(fio): # нумерует элементы списка и выдает результат в виде кортежей
    print(item)

for i, v in enumerate(fio): # нумерует элементы списка и выдает результат построчно с нумерацией строк вывода
    print(f'{i+1}. {v}.')

    text = 'один два       три четыре'

    lst = text.split()  # по умолчанию: все символы пустого пространства исчезают при split-разделении строки
    lst = text.split(' ')

    ip = '192.168.0.1'

    lst = ip.split('.')  # возвращает разделяемые элементы списком из ip-адреса

    print(lst)

    text2 = '-'.join(lst)  # объединяет элементы с помощью заданного соединителя
    print(text2)

    text3 = ' и также '.join(lst)
    print(text3)

    # Методы строки split() и join() - работают только с элементами строк, т.е лишь с символами!!!

    text = ' P y t h o n '
    temp = text.split()
    res = ''.join(text.split())  # операция убрать все пробелы
    print(res)

    # # ДЗ 30.06.25
    #
    # # преобразовать фразу "Полна неожиданностей улица. Под глазом фонарь. К чаю аптека. Аптека. Улица. Фонарь. А.Блок."
    # # в соответствии со стоп листом вывести исходный текст (собрать исходный список), текст без слов из стоп листа, пронумероанные
    # # оставшиеся слова в алфавитном порядке, без повтора и пронумерованные
    #
    # result = [] # создаем пустой список для элементов искомого текста
    #
    # #Вводим фразу: Полна неожиданностей улица. Под глазом фонарь. К чаю аптека. Аптека. Улица. Фонарь. А.Блок.
    # text = input('Введите строку изначальной фразы: ').strip().lower()
    # stop_list = ['полна', 'неожиданностей', 'под', 'глазом', 'к', 'чаю'] # ввод запрещённых слов
    #
    # lst = text.split() # удаление пробелов
    # list = list (set(lst)) # удаление повторов
    #
    # result = [item for item in list if item not in stop_list]
    # # вывод 3 списков со словами в алфавитном порядке, пронумерованными и без повторов
    # print(f'Изначальная фраза содержит список из {len(list)} слов и знаков: ')
    # list.sort()
    # for i in range(len(list)):
    #     print(f'\t{i+1}. {list[i]}')
    # print(f'Запрещённый текст содержит список из {len(stop_list)} слов и знаков: ')
    # list.sort()
    # for i in range(len(stop_list)):
    #     print(f'\t{i+1}. {stop_list[i]}')
    # print(f'Искомый текст содержит список из {len(result)} слов и знаков: ')
    # result.sort()
    # for i in range(len(result)):
    #     print(f'\t{i+1}. {result[i]}')
    # list = set (lst)
    # while (text := input('Введите сообщение: ')) != '':
    #     lst = text.split()
    # for item in list:
    #     if item not in stop_list:
    #         list.append(item)
    # res = sorted(temp)
    # for a, b in enumerate(res, 1):
    #     print(f'{a}. {b}')

    # commas = (',', '!', '.', '?', '-', ':')
    # text = input('Введите строку изначальной фразы: ').strip().lower()
    # stop_list = ['полна', 'неожиданностей', 'под', 'глазом', 'к', 'чаю'] # ввод запрещённых слов
    # for z in commas:
    #     text = text.replace(z, _new:)
    # lst = text.split()
    # result = sorted(set(lst) - stop_list)
    # for a, b in enumerate(result, 1):
    #     print(f'{a}. {b}')

    commas = (',', '!', '.', '?', '-', ':')
    message = input('Введите строку изначальной фразы: ').strip().lower()
    stop_list = ['полна', 'неожиданностей', 'под', 'глазом', 'к', 'чаю']  # ввод запрещённых слов
    for z in commas:
        message = message.replace(z, '')
        lst = message.split()
        res = sorted(set(lst) - stop_list)
        for a, b in enumerate(res, 1):
            print(f'{a}. {b}')

    # список квадратов чисел
    # 1 вариант создания списка
    # squares = [] # пустой список
    #
    # for i in range(10):
    #     squares.append(i ** 2)
    #
    # print(*squares,sep=', ')
    #
    # # 2 вариант создания списка
    # squares = [i ** 2 for i in range(10)] # список: на 1 месте - что попадет, на 2 месте - закономерность попадания
    #
    # print(*squares,sep=', ')

    # список квадратов четных чисел
    squares = [i ** 2 for i in range(10) if i % 2 == 0]  # до пробела 1 часть - что, 2-я - закон, 3-я - условие
    # условие выбора операндов для создания спискаЖ если остаток от деления операнда на 2 равен 0
    print(*squares, sep=', ')

    # произведение i и j
    # тип списочного вычисления списка
    print([i * j for i in range(3) for j in range(3)])
    # вложенный тип создания вычисления списка
    for i in range(3):
        for j in range(3):
            print(i * j)

    n = '500 600 700 800'  # имеется строка
    # создаем список по условию
    # 1 вариант
    a = [int(i) for i in n.split()]
    print(a)
    # 2 вариант сразу выводим список на экран
    print([int(i) for i in n.split()])
    # введем условие для вывода элементов списка на экран после содания списка b
    approved = [500, 800]
    b = [int(i) for i in n.split() if int(i) in approved]
    print(b)

text = 'Списочные выражения применяются для эффективности кода'

#res = [a for a in text.split() if (text.index(a) + 1) % 3 == 0]
res = [a for a in text.split()[2::3]] # создание списка
#res = set(a for a in text.split()[2::3]) # создание множества кортеж
print(res)

# Списочные выражения (list comprehension) 01.07.25
# Вложенные списки - nested lists
a = [1, 38.6, False, 'sfs', (1, 2)] # список может содержать данные любого типа, в том числе списки и выражения
# создание вложенного списка
N = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], # висячая запятая, если вдруг нужно будет добавить ещё один вложенный массив
]
# замена всех элементов списков во вложенном списке на 1
matrix = [[1] * N for _ in range(N)] # преобразование всех элементов вложенного списка размерности N
# вместо i ставим _ потому, что индекс i нигде не используется
print(matrix)

# обход 2-мерного списка (матрицы)
# for row in range(len(matrix)): # сначала выбираем ряд, начиная с 1-го
#     for col in range(len(matrix[row])): # условие вывода каждого элемента очередного ряда, начиная с 1-го
#
# print(matrix[row][col])

# возврат замененных элементов списков во вложенном списке
count = 1
for row in range(len(matrix)): # сначала выбираем ряд, начиная с 1-го
    for col in range(len(matrix[row])): # условие вывода каждого элемента очередного ряда, начиная с 1-го
        matrix[row][col] = count
        count += 1
print(matrix)

matrix = []

start = 1
N = 4

for i in range(N):
    table = []
    for j in range(start, start + N):
        table.append(j)
        matrix.append(table)
        start += N
print(matrix)

N = 3
matrix = [[i+j for j in range(N)]for i in range(1, 10, 3)]
print(matrix)

# Пустой словарь
# 1. d = {}
# 2. d = dict{}
# Предзаполненный словарь
d = {
    'table': ['таблица', 'стол'],
    'well': ['хорошо', 'колодец'], # в каждом элементе словаря могут быть списки синонимов, описаний для данного ключа
    'chair': 'стул',
    'apple': 'яблоко',
    1: 'один', # ключ в словаре может быть разным по типу данных
    (22.75, 37.5): 'Город', # элемент словаря Город и его координаты = ключ для Город
}

print(d[(22.75, 37.5)]) # печатаем значение по ключу-кортежу
print(d['table']) # печатаем значение по ключу table
print(d[1])
print(d['well'][0])
d['well'].append('скважина')
d['plum'] = 'слива' # добавление в словарь элемента 'слива'
print(d['plum']) # добавленный элемент существует при работе со словарём, затем он исчезает
del d['chair'] # удаление элемента словаря по заданному ключу, если такого ключа нет - то error
print(d) # печать словаря целиком по принципу как есть в одну строку

deleted_item = d.pop('apple')
print('Удалился элемент: ', deleted_item)

print('Есть ли "стол" в словаре')
if 'table' in d:
    print('Да, "стол" есть в словаре.')
# мягкий метод обращения к несуществующему элементу словаря
print('Доступ к несуществующему ключу без "исключений"')
pear = d.get('pear', 'Груши нет') # 2-й элемент - значение по дефолту (по умолчанию: None, или: назначенное)
print('Где груша: ', pear)

# перебор по умолчанию ключей и элементов словаря
for key in d: # d подразумевает d.keys()
    print(key, '->', d[key]) # наглядный вывод словаря со стрелочкой (можно с любым: = или др.)

for value in d.values(): # вывод значений (элементов) словаря
    print(value, '->', d.values())

print(d.keys()) # список всех ключей (list)
print(d.values()) # список значений (list)

# Частотный анализ

res = {} # пустой словарь для последующего ввода частотного анализа

text = """Планируют перенести выходной на 9 января,
чтобы в связи с новогодними каникулами отдыхать 12 дней подряд.
Хотят также сделать днем отдыха 31 декабря 2026 года (четверг).
Это возможно благодаря переносу выходных с 3 и 4 января (суббота и воскресенье).
"""

commas = (',', '(', '.', ')')
for x in commas:
    text = text.replace(x, '')

lst = sorted(text.strip().lower().split())

for item in lst:
    if item in res.keys():
        res[item] += 1
    else:
        res[item] = 1

print('Частотный анализ текста')
for k, v in res.items():
    print(f'\t{k}: {v}')

# """ Методы словаря
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# """

# Функции (Do not Repeat Yourself - не повторяй себя: один раз определение, а затем ссылка на него)
# Scope (local or global) - переменные локальные (только внутри ф) и глобальные (внутри всей прг)
# имя функции не должно совпадать с ключевыми словами и со встроенными функциями!!!
# функция не возвращающая результат - ПРОЦЕДУРА (но при этом параметры её меняются!)
# при вызове функции задаются аргументы (при определении функции - параметры)
# Синтаксис:
# def <имя функции>([параметры]):
#     команды (на уровне отступа)
from traceback import print_list

person = 'Пётр' # глобальная переменная определяемая вне функции
count = 0

def greet(name):
    print('Привет,', name) # определение функции "вывод строки", в первой строке  - число использования f
    print(count)

def increment():
    global count # разрешение на изменение функцией значения глобальной переменной (в искл. случае!)
    count += 1

def print_list(array=None):
    if array is None:
        array = []
    for item in array:
        print(item)


# def print_list(name):
#     print(name) # определение функции "вывод строки", в первой строке  - число использования f

# increment()
greet('Дмитрий') # задание аргумента
greet(person) # при вызове функции , берётся копия глобальной переменной
print_list()

# Функции (Do not Repeat Yourself - не повторяй себя: один раз определение, а затем ссылка на него)
# Scope (local or global) - переменные локальные (только внутри ф) и глобальные (внутри всей прг)
# имя функции не должно совпадать с ключевыми словами и со встроенными функциями!!!
# функция не возвращающая результат - ПРОЦЕДУРА (но при этом параметры её меняются!)
# при вызове функции задаются аргументы (при определении функции - параметры)
# Синтаксис:
# def <имя функции>([параметры]):
#     команды (на уровне отступа)
# Чистая функция не меняет после использования глобальные переменные (внешние данные вне функции)
# Return value
def square(num):
    return num ** 2

def even_odd(num):
    if num % 2 == 0:
        return 'Чётное' # завершение работы функции по условию
    return 'Нечётное' # завершение работы функции при невыполнении условия
    print('Привет') # до этой строки выполнение функции не дойдёт, т.к. цикл завершен

def print_string(s=None):
    if s is None:
        return
    print(s)




t = square(5)
t = square(t) # функция не является чистой т.к. меняет глобальную t
print(even_odd(5))
print_string()
print(t)

# ДЗ: число словами 56 -> пятьдесят шесть

d = {
    1: 'один', # задаем буквенные значения чисел
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
}

"""
Функция, принимающая число и возвращающая его словами
: param n: двузначное число 
: return: число словами
"""


# def num_to_word(n):
#     if len(str(n)) > 2:
#         return 'Введите двузначное число'
#     if len(str(n)) == 1 or n in d:
#         return d[int()]
#     return d[int(str(n)[0] + '0')] + ' ' + d[int(str(n)[1])]
#
# print(num_to_word(56))


def num_to_word(n: int) -> str:
    """
    Функция, принимающая число и возвращающая его словами
    : param n: двузначное число
    : return: число словами
    """
    if len(str(n)) > 2:
        return 'Введите двузначное число'
    if len(str(n)) == 1 or n in d:
        return d[int()]
    return d[int(str(n)[0] + '0')] + ' ' + d[int(str(n)[1])]

print(num_to_word(16))

# PI = 3.1415 # необходимо в любой программе написать "блок констант
# # Shadows name 'square' from outer scope - использование глобальной переменной
#
# def greet(name):
#     print('Привет,', name)
#     name = 'друг'
#     print('Здравствуй,', name) # изменение внешнего аргумента-константы только внутри функции
#
# square = 'Дворцовая площадь' # оставляем одну глобальную переменную (подвержена риску изменения!!!)
#
# def square_area(length: int, width: int) -> None:
#     """
#     Функция вычисления площади
#     :param length: (int - задаем сразу тип переменной)
#     :param width:
#     :return: None
#     """
#     area = length * width
#     print(f'Площадь площади "{square}" = {area}')
#
#
# # def square_area(length, width):
# #     square = length * width # пример перекрывания (приоритета) внутренней переменной над глобальной
# #     # так делать нельзя!
# #     print(f'Площадь площади "{square}" = {square}')
#
#
# def circle_length(radius):
#     perimetr = 2 * PI * radius
#     print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')
#
#
# def print_array(array: list) -> None:
#     for item in array: # используем локальную (внутреннюю) переменную
#         print(item)
# # Главная функция для определения локальных переменных, не являющихся видимыми глобальными
# def main():
#     words = ['Привет', 'мир']
#     greet('Пётр')
#     circle_length(5)
#     print_array(words)
#     print_array(['a', 'b', 'c'])
#     print('Давай встретимся, где', square)
#     square_area(320, 240)
#
# main() # подход через Главную фукцию задающую внешние действия при обращении к внутренним функциям


# words = ['Привет', 'мир']
# PI = 3.14
# greet('Пётр')
# square = 'Дворцовая площадь'
# print('Давай встретимся, где', square)
# square_area(320, 240)
# circle_length(5)
# print_array(words)
# print_array(['a', 'b', 'c'])

# def print_array(array: list) -> None:
#     for item in words: # array: поменяли на глобальную (внешнюю) переменную (список words)
#         # так делать нельзя, т.к. аргумент задан внутри функции и переменная становится неизменной
#         print(item)
#
# words = ['Привет', 'мир']
# print_array(words)
# print_array(['a', 'b', 'c'])

# def generate_list():
#     for i in range(5):
#         yield i # данный оператор (создает генератор), возвращает значения переменной,
#         # но не завершает работу
#
# array = tuple(generate_list())
#
# print(array)

# return vs yield - оба оператора возвращают значения переменных,


# def print_goodbye(arg):
#     print('goodbye', end='')
#
#
# def print_cruel(arg):
#     print('cruel', end='')
#
#
# def print_world(arg):
#     print('world', end='')
#
#
# def main():
#     print_goodbye(1)
#     print_cruel(1)
#     print_world(1)
#
# main ()

# Возврат нескольких значений из функции при помощи return

# is на практике
# def print_array(array: list, start: int = None):
#     if start is not None and start > len(array):
#         return
#     if start is None:
#         start = 0
#     for i in range(start, len(array)):
#             print(array[i])
#
#
# a = [1, 2, 3]
# print_array(a, 1) # ,без start: n распечатывается весь список

# Оператор is: a is b -> когда a и b - один и тот же объект
# my_refregirator = ['колбаса', 'масло', 'сыр']
# # his_refregirator = ['колбаса', 'масло', 'сыр']
# #his_refregirator = my_refregirator # не создает новый объект, а только ссылку на тот же id-объект
# his_refregirator = my_refregirator.copy() # или [:] - создание копии с другим ID
# my_refregirator += ['мясо']
# print(his_refregirator)
# print(my_refregirator is his_refregirator)
# print(my_refregirator == his_refregirator)
# print(id(my_refregirator) == id(his_refregirator))
#
# temp = None
# print(type(temp))
# print(temp is None) # print(temp == None) - запись сравнения не корректна, но работает
# temp = 1
# print(type(temp))
# print(temp == 1)

# d = {'a': 1}
# print(id(d))
# d['a'] += 1 # меняем изменяемый объект (словарь), при этом индекс не меняется
# print(id(d))
#
# a = [0]
# print(id(a))
# a[0] += 1 # меняем изменяемый объект (список), при этом индекс не меняется
# print(id(a))

print(calc(1,2,3, operator='*'))

# def multy(*args, first):
#     # print(len(args)) # подсчет числа аргументов
#     # print(args) # возможность обращаться к каждому аргументу по индексу или перебором в цикле
#     # if len(args) == 0:
#     #     return 0
#     if not args:
#         return 0
#     result = 1
#     for arg in args:
#         result *= arg # возвращает произведение неограниченное (неопределено) кол-во аргументов
#     return result
#
# print(multy(2, 2, 3, 4, first=0)) # любое количество аргументов + именной второй аргумент

# def multy(first, *args):
#     # print(len(args)) # подсчет числа аргументов
#     # print(args) # возможность обращаться к каждому аргументу по индексу или перебором в цикле
#     # if len(args) == 0:
#     #     return 0
#     if not args:
#         return 0
#     result = 1
#     for arg in args:
#         result *= arg # возвращает неограниченное (изначально неизвестное) кол-во аргументов
#     return result
#
# print(multy(2, 2, 3, 4)) # первый именной + задаем любое количество аргументов

# def fio(name, surname):
#     return f'{name} {surname}' # возвращает именованные аргументы
#
#
# #print(fio(name='Остап', surname='Бендер'))
# # или
# print(fio(surname='Бендер', name='Остап'))

# def multy(*args):
#     # print(len(args)) # подсчет числа аргументов
#     # print(args) # возможность обращаться к каждому аргументу по индексу или перебором в цикле
#     # if len(args) == 0:
#     #     return 0
#     if not args:
#         return 0
#     result = 1
#     for arg in args:
#         result *= arg # возвращает неограниченное (изначально неизвестное) кол-во аргументов
#     return result
#
# print(multy(1, 2, 3, 4)) # выводим любое количество заданных аргументов



# Unpack и *
# При распаковке * может быть только у одного аргумента, который выводит множество оставшихся элем.
# def coordinates() -> tuple:
#     return 5.4, 3.2, 3.8, 7.2, 4.6
#
# x, y, *rest = coordinates()
# # распаковка если мы не знаем количество элементов выводимых из функции
#             # точно знаем, что не меньше 2-х, остальные (возможно добавленные позже) через *rest
#             # выводим через множество (по остаточному принципу с символом *)
# print(f'x = {x}, y = {y}, rest = {rest}')
#
# *names, surname = 'Остап Сулейман Бендер'.split() # где символ *, там выводим списком (множеством)
# print(names, surname)

#def calc(*args: tuple, operator: str = '+') -> any:
#     match operator:
#         case '+':
#             result = 0
#             for i in args:
#                 result += i
#         case '*':
#             result = 1
#             for i in args:
#                 result *= i
#         case _: # аналог else - все остальные значения operator (по default)
#             return 'Так нельзя'
#     return result
#
#
# print(calc(2,2,3, operator='*'))

#Функция с переменным числом аргументов, изменяется с помощью оператора ввода *args
# эта функция позволяет ввести сначала именной аргумент first и переменное число арг. (за ним!)


# def calc(*args: tuple, operator: str = '+') -> any:
#     match operator:
#         case '+':
#             result = 0
#             for i in args:
#                 result += i
#         case '*':
#             result = 1
#             for i in args:
#                 result *= i
#         case _: # аналог else - все остальные значения operator (по default)
#             return 'Так нельзя'
#     return result
#
#
# print(calc(1,2,3, operator='*'))

# def sandwich(type_of_meal, with_onion=False, with_tomato=False):
#     print('Булочка')
#     if with_onion:
#         print('Лук')
#     print(type_of_meal)
#     if with_tomato:
#         print('Помидоры')
#     print('Булочка')
#
#
#
#
# def print_any(*args, **kwarg):
#     for i in args:
#       print(i)
#     for k, v in kwarg.items():
#         print(k, '=', v) # создание словаря
# # **additional - Kwargs для резервирования дополнительной (неизвестной заранее) позиции для инфо
# def profile(name, surname, city, *children, **additional):
#     print(f'Имя: {name}')
#     print(f'Фамилия: {surname}')
#     print(f'Из города: {city}')
#     if len(children) > 0:
#         print('Дети:', ', '.join(children) )
#     print('Хобби:', ', '.join(additional['hobbies']))
#     # print(additional)
#
# profile('Дмитрий', 'Колесов', 'Волгоград',
#         'Мария', 'Пётр', 'Василий', hobbies=['Филателия', 'Шахматы'])

# print_any('Дмитрий', 'Колесов', citi='Москва', age=27)
# sandwich(type_of_meal='котлета', with_onion=True)

# Функция, как объект
# Передается в другие функции: функции высшего порядка

# печатник = print # печатник - объект, принявший ссылку на функцию print (не является копией)
# печатник('Привет, мир')

# Функция критерия отбора элементов списка
# Критерий: длина слова
# def is_longer_six(word):
#     return len(word) > 6 # функция возвращает логическое значение T(F)

# Критерий - первая буква
# def is_first_letter_a(word):
#     return word[0] == 'а'
#
# fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']
# res = list(filter(is_first_letter_a, fruits))
# print(res)
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#          'длина', 'которых', 'больше', 'шести']
# result = list(filter(is_longer_six, words))
# print(result)
#
# for word in filter(is_longer_six, words):
#     print(word)

# ДЗ 02.07.25
# Превратить список nums в строку 123456789:
# сначала с помощью функции map превратить список в строку,
# а затем использовать оператор .join для удаления разделителей , и _
#
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9) # задаем кортеж (или список [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # 1 вариант
# res = ' '.join(map(str, nums))
# print(res) # печатаем кортеж (список)

# 2 вариант
# def list_str(num):
#     strs = ''.join(map(str, nums)) # преобразование элементов списка в элементы строки и удаление разделителей
#     return strs # возвращает список в элементы строки
#
# print(list_str(nums)) # печать элементов списка в виде строки

# Встроенные библиотеки (надо иметь ввиду, что в новой версии Python
# могут не сохраняться не переписываться старые библиотеки)
# заходим в хранилище библиотек (репозиторий) Python в инете на сайте
# PyPI - Python Package Index (pypi.org)
# from pprint import pprint
# PIL - Python Imagine Library, векторное изображение
# (пакет для установки доп.библиотек: в командной строке pip install pillow))
# для удаления доп.библиотек: в командной строке pip uninstall pillow
# python3 -m (только для Линокс) pip install --upgrade pip - обновление установщика библиотек для инсталяции
# python3 -m (только для Линокс) pip install --upgrade pillow
# pip freeze > requirements.txt - создание файла зависимости (замораживаем список библиотеки)
# pip install -r requirements.txt - установка списка библиотек
# RGB - растровое изображение (цвета пикселя)
# thumbnail "большой палец"

#from PIL import Image # - объект Image из PIL отвечает за информацию об изображении, копирование,
# from PIL import Image, ImageDraw
#
# RED = (255, 0, 0)
# POLY = [(100, 50), (150, 50), (180, 120)]
#
# # создание таблицы пикселей,
#
# image = Image.new('RGB',
#                   (600, 400),
#                   (0, 0, 255)) # создаем одноцветный прямоугольник с заданными параметрами
#
# draw = ImageDraw.Draw(image) # создаем прозрачный холст на котором будем рисовать
#
#
# draw.line((0, 0, 600, 400),
#           fill=RED, width=5)
# draw.line((0, 0, 600, 400),
#           fill=RED, width=5)
# draw.rectangle((10, 10, 590, 390),
#                outline=RED, width=10)
#
# draw.ellipse((10, 10, 590, 390),
#              outline=RED, width=10)
#
# draw.polygon(POLY, outline='green', width=15)
# draw.text((100, 100), 'Текст', fill=RED)
#
#
#
#
#
#
#
# image.save('images/blue.jpg')


# изменение изображения

# image = Image.open('images/python.jpg')
# print(image.size)
#
# x, y = image.size
# mode = image.mode
#
# pixels = image.load() # загрузить таблицу пикселей (чистый массив пикселей) объект получил доступ ко всему в изображении
#
# print(f'Ширина = {x},высота = {y}')
# print(f'Цветовая схема = {mode}')

#image_rotate = image.rotate(90) # поворот на 90 град
# image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) # смотрит в другую сторону
# cropped = image.crop((250, 0, 550, 300))
# resized = image.resize((400, 300))


# Негатив
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = 255-r, 255-g, 255-b

# Grayscale
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         average = (r + g + b) // 3
#         pixels[i, j] = average, average, average

# Инверсия перестановкой основных цветов в схеме
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = g, b, r


#image.save('images/python2.jpg') # сохраняем все текущие изменения файла в новое изображение (*2.*)
# image.rotate.save('images/python2.jpg')
# image.transpose.save('images/python2.jpg')
# image.cropped.save('images/python2.jpg')

#image.save('images/python2.jpg')

#import pprint

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# print(matrix)
# pprint.pprint(matrix)
# Модуль datetime: берёт данные по времени из системных часов компьютера
#
# import datetime as dt
#
# my_time = dt.time (15, 27, 32) # вывод времени моего часового пояса
# print(my_time)
# my_day = dt.date(2025, 7, 3) # вывод даты моего часового пояса
# print(my_day)
# my_day_time = dt.datetime.combine(my_day, my_time) # вывод полного формата времени часового пояса
# print(my_day_time)
#
# date1 = dt.date(2025, 6, 15)
# date2 = dt.date(2025, 7, 15)
# delta = date2 - date1 # считаем число дней между датами (сколько дней в командировке)
# print(delta)
#
#
# time = dt.datetime.now()
#
# ftime = time.strftime('%d-%m-%Y') # создаем строку форматированного времени для даты
#                                   # задаём порядок следования позиций, разделитель "-"
# print('Сегодня: ', ftime)
#
# ftime = time.strftime('%H:%M') # создаем строку форматированного времени для часов и минут
#                                # задаём порядок следования позиций, разделитель ":"
# print('Время: ', ftime)

# print(dt.datetime.now()) # вывод полного формата времени, вплоть до 6 знаков после , для сек
# print(dt.datetime.now().date()) # вывод только даты
# print(dt.datetime.now().time()) # вывод времени

# import random as r
# r.seed()
# print(r.random()) # получение случайного значения числа
#
# # программа генерации случайного пароля из подстрок 3-х строк
# N = 8
#
# abc = 'qwertyuiopasdfghjklzxcvbnm'
# num = '1234567890'
# spec = '@#$&'
# abc = list(abc)
# num = list(num)
# spec = list(spec)
#
# r.shuffle(abc)
#
# temp = abc[:N - 3]
# temp.append(r.choice(abc).upper())
# temp.append(r.choice(num))
# temp.append(r.choice(spec))
# r.shuffle(temp)
# res = ''.join(temp)
#
# print(res)


# abc = ('qwertyuiopasdfghjklzxcvbnm')
# lst = list(abc) + ['1', '2'] + ['#', 'S'] # перевод строки в список и добавление элементов в список
# r.shuffle(lst) # выбор случайной последовательности всех элементов нового списка
# res = ''.join(lst[:8]) # вывод на экран первых 8 элементов последовательности
#
# print(res)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for _ in range(10):
#     print(r.sample(lst, k=5)) # цикл выборки (10 шагов) любых пяти элементов списка, без повторов

# res = r.sample(lst, k=5) # выборка случайных пяти элементов списка
# print(res)

# zara = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
#
# for _ in range(10):
#     print(r.choice(zara), r.choice(zara)) # иммитация бросания игральных "костей"
#     # бросаем (циклом) в 10 раз

# d = {
#     'а': 1,
#     'b': 2,
#     'c': 3,
# }
#
# keys = list(d.keys())
#
# key = r.choice(keys) # выбор случайного индекса (элемента) из словаря d
# print(d[key])

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = r.choice(lst) # выбор из списка случайного элемента
# print(res)

#print(r.choice(['орёл', 'решка'])) # орёл или решка (случайный выбор)
# print(r.choice('орёл')) # выбор случайной буквы из строки орёл

# num = r.randint(0, 10) # выбирает случайное значение числа от 0 до 10
# print(num)

# for _ in range(10):
#     #print(r.randint(0, 10))
#     print(r.randrange(0, 10, 2)) # выбирает случайное значение числа от 0 до 10 (шаг 2)

# import math as m
#
# print(dir(m)) # вывод на экран всех функций библиотеки math Python
# print(help(m.cos))

#from math import pi, sqrt, sin, radians, hypot

# 3-й способ подключения функции из библиотеки (не для всего множества элементов библиотеки)
#from math import * # сначала загружаем в оперативную память все имена функций, а далее смотрим,
# что используем и выводим только необходимые функции или константы
# from math import pi # достаем через (модуль библиотек PyPI) math только число ПИ
# from math import sqrt # достаем через (модуль библиотек PyPI) math только функцию квадратного корня


# print('Число Пи', pi)
# print('Квадратный корень 4', sqrt(4))
# print('Синус 30:', round(sin(radians(30)), 2)) # округляем значение функции до 2 знаков (для краткости)
# print('Гипотенуза для 3 и 2', hypot(3, 2))

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

# orig = Image.open('images/sunny_day.jpg').convert('RGB')
#
# up = orig.crop((0, 0, 600, 200))
# down = orig.crop((0, 200, 600, 400))
#
# new = Image.new('RGB', (600, 400))
#
# new.paste(down, )
# new.paste(down, )
# show()



# ДЗ 600*400 голубой прямоугольник в правом верхнем углу солнце (четверть)
# по центру надпись увеличенным шрифтом "СОЛНЕЧНЫЙ ДЕНЬ"

# 1 вариант (мой, выдает ошибку
# from PIL import Image, ImageFont, ImageDraw  # функция Image, ImageDraw из PIL отвечает за рисование нового изображения
#
# YELLOW = (255, 255, 0)
#
# image = Image.new('RGB',
#                   (600, 400),
#                   (0, 0, 255)) # создаем одноцветный прямоугольник с заданными параметрами
#
# draw = ImageDraw.Draw(image) # создаем объект для рисования (прозрачный холст, на котором будем рисовать)
#
# draw.ellipse((-100, -100, 100, 100), 'YELLOW', 'YELLOW', 1)
#
# image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# image_flip.save('images/blue.jpg')
#
# image = Image.open('images/blue.jpg')
# draw = ImageDraw.Draw(image)
#
# draw.text((100, 100), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW) # без выбора шрифта и размера
# # fnt = ImageFont.truetype('FreeMono.ttf', 50) # выбор шрифта и размера
# # draw.text((100, 100), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW, font=fnt)
#
# image.save('images/blue&sun&text.jpg')

# 2 вариант


# https://fontsforyou.com/ru/specific-fonts/ttf-

# W = 600
# H = 400
#
# image

# расчитываем позицию для центрирования


# image save (

# Документы по шаблону (из методичек https://disk.yandex.ru/d/9HNsXg77_qeidg
# скачать файл template.docx)
# установка шаблона template.docx (pip install docxtpl)
# установка библиотеки Excel (pip install openpyxl)
# Word - DOCX (pip install python-docx)
# Word - DOCX (pip install docxtpl)
# pip freeze > requirements.txt - создание файла зависимости (замораживаем список библиотеки)
# pip install -r requirements.txt - установка списка библиотек


# Работа с формулами:
# ...
# ws['A1'] = "=SUM(A1:A10)" - работа с формулами
# Формат:
# from openpyxl.styles import  Font, Alignment
# # Чтение данных
# from openpyxl import  load_workbook # импортируем модуль для чтения .xlsx
#
# wb = load_workbook('docs/newtable.xlsx')
# ws = wb.active
# ws['A1'].font = Font(bold=True, size=14) # форматирование данных в таблице
# ws['A1'].alignment = Alignment(horizontal="center")
#
# row_count = ws.max_row # выводим число заполненных строк
#
# for row in ws.iter_rows(values_only=True):
#     fio, pos, dept = row
#     print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dept}') # более удобный формат вывода
#     # print(row)

# Запись данных в существующий файл

from openpyxl import  load_workbook # импортируем модуль для записи в файл .xlsx

# # Открываем (загружаем) рабочую книгу
# wb = load_workbook('docs/report.xlsx')
#
# # Активный лист
# ws = wb.active
# #ws = wb['Отчёт'] # можно присвоить переменному операнду имя
#
# # Создаём Заголовки
# ws['A1'] = 'ФИО'
# ws['B1'] = 'Должность'
# ws['C1'] = 'Отдел'
#
# # создаём Данные
# employees = [
#     ['Иванов И.И.', 'Менеджер', 'Продажи'],
#     ['Петров П.П.', 'Бухгалтер', 'Финансы'],
#     ['Сидоров С.С.', 'Аналитик', 'IT']
# ]
#
# for row, data in enumerate(employees, start=2):
#     ws.cell(row=row, column=1, value=data[0])
#     ws.cell(row=row, column=2, value=data[1])
#     ws.cell(row=row, column=3, value=data[2])
#
# # Способы записи
# # ws['F1'] = 'Привет мир' # первый вариант записи (в ячейку с адресом F1)
# # ws.cell(1, 3, 'Hello') # второй вариант записи (по номеру строки и столбца ячейки)
#
# wb.save('docs/newtable.xlsx')

# # Пустой файл Exel
# from  openpyxl import Workbook
#
# wb = Workbook() # создаем конструктор
#
# ws = wb.active # создаем пустой документ
# ws.title = 'Отчёт' # присваиваем имя документу
#
# wb.save('docs/report.xlsx')


# from docxtpl import DocxTemplate # извлекаем модуль для загрузки шаблона документа
#
# from main import count
#
# # Загрузка шаблона
# doc = DocxTemplate('docs/template.docx')
#
# # Данные для подстановки в шаблон
# content = {
#     'company': 'ООО "Монолит"',
#     'employee': 'Петров Д.И.',
#     'position': 'Менеджер',
#     'date': '01/01/2025'
# }
#
# count = 1
# for item in content:
#     doc.render(item)
#     doc.save(f' {}')
#
#
# doc.render(content) # шаблон для формирования отчётов
# doc.save('docx/about.docx')

# from docx import Document
# from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_ALIGN_PARAGRAPH
# from docx.shared import Cm, Inches, Mm, Pt # Для размеров
#
# doc = Document() # создание экземпляра документа
#
# # Добавление заголовка
# doc.add_heading('Отчёт за месяц', 1)
# paragraph = doc.add_paragraph() # создаем с нового абзаца (как клавиша "ввод")
# paragraph = doc.add_paragraph('В этом отчёте представлены')
# # add_run прием: внедряет что-то в созданный абзац (может быть не только текст, но и картинка)
# paragraph.add_run(' ключевые показатели').bold = True
# # Новый абзац для списка
# paragraph = doc.add_paragraph()
# paragraph_format = paragraph.paragraph_format # форматирование параграфа
# paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
# #
# paragraph = doc.add_paragraph('Первый пункт', 'List Bullet')
# paragraph = doc.add_paragraph('Второй пункт', 'List Bullet')
# #
# paragraph = doc.add_paragraph('Первый пункт', 'List Number')
# paragraph = doc.add_paragraph('Второй пункт', 'List Number')
#
# paragraph = doc.add_paragraph()
#
# table = doc.add_table(3, cols=3)
#
# for i, row in enumerate(table.rows):
#     for j, cell in enumerate(table.cells):
#         cell.txt = f'Строка {i+1}, Столбец {j+1}'
#
# doc.add_paragraph()
#
# doc.add_picture('image/blue.jpg', width=Mm(10))


# doc.save('docs/report.docx')

# from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
#
# orig = Image.open('images/python.jpg').convert('RGB') # на всякий случай конвертируем в формат RGB
# размытие
# blue_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# blue_image.show()

# Усиление разкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image = enchancer.enchance(4.0)
# sharpened_image.show()

# Открытие с менеджером контектса
# with open('info.txt', 'rt', encoding='utf-8') as fo:
#     text = fo.read()
#     lst = text.splitlines()
#     print(lst)
 # Проследит, чтобы файл закрылся

# fo = open('info.txt', 'wt', encoding='utf-8') # запись в файл

# fo.write('Хороший текст.')
# print('\nА вот это будет уже с новой строки.', file=fo)
# print('\nА вот ещё одна строка.', file=fo)

# fo = open('info.txt', 'rt', encoding='utf-8')

# Построчное чтение № 1
# while text := fo.readline():
#     print(text.rstrip('\n'))

# Построчное чтение № 2
# lst = fo.readlines()
# lst = list(map(lambda x: x.strip('\n'), lst))
# print(lst)

# Построчное чтение № 3
# text = fo.read()
# lst = text.splitlines()
# print(lst)
#
# fo.close()

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
