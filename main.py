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
