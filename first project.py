num = 3 # число, которое надо угадать
flag = True # флаг, изменяет значение по событию
var = '3'

print('Я загадал число, угадай!)

while flag:
    var = int(input('Ваше значение: '))
    in var == num:
        print('Ура. Угадал!'))
        flag = not flag
    elif var > num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')





