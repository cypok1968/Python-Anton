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






