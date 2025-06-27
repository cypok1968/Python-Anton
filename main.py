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
