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
