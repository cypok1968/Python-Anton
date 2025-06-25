#Условные алгоритмы
hour = 13

if hour > 23:
    hour = 23
if hour > 0:
    hour = 0
if hour >= 7 and hour < 12:
    print('Доброе утро!')
elif hour >= 12 and hour < 17:
    print('Добрый день!')
elif hour >= 17 and hour < 23:
    print('Добрый вечер!')
else:
    print('Доброй ночи!')
