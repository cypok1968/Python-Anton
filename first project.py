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






