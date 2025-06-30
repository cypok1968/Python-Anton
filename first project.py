# Строки (immutable, iterable)
# Начало и окончание строки
# 1. find('подстрока) с нулевого индекса поиск
# 2. find('подстрока, start) - с какого места искать
# 2. find('подстрока, start, end) - с какого по какое искать

# s = 'Смотреть, вертеть, видеть'
#
# index = s.find('еть') # с начала строки s
# print(index)
#
# index = s.find(_sub: 'еть', _start:10) # с позиции start
# print(index)
#
# index = s.find(_sub: 'ер', _start:10, _end:15) # с позиции start по позицию end
# print(index)

s = 'синхрофазотрон' # ищем 'о': сколько их и где находятся
ch = 'о'

if ch in s:
    count = s.count(ch)
    print(f'Буква {ch} встречается в слове "{s}" {count} раз.')
    print('Её позиция/позиции:', end=' ')
    start = 0
    for i in range(count):
        pos = s.find(ch, start)
        start = pos + 1
        print(pos, end='')
else:
    print(f'Буквы \'{ch}\' нет в слове "{s}".')






