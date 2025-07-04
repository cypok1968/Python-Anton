

lst = [1, 2, 3]

# res = 0
# for x in lst:
#    res += x # суммирование элементов списка через цикл
# print(res)

res = sum(lst)
min_value = min(lst) # - ф-я вычисляет наименьший элемент списка
max_value = max(lst) # ф-я вычисляет наибольший элемент списка
print(res, min_value, max_value) # печать любого резульата




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
