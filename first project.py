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
