#Функция с переменным числом аргументов, изменяется с помощью оператора ввода *args
# эта функция позволяет ввести сначала именной аргумент first и переменное число арг. (за ним!)


# def calc(*args: tuple, operator: str = '+') -> any:
#     match operator:
#         case '+':
#             result = 0
#             for i in args:
#                 result += i
#         case '*':
#             result = 1
#             for i in args:
#                 result *= i
#         case _: # аналог else - все остальные значения operator (по default)
#             return 'Так нельзя'
#     return result
#
#
# print(calc(1,2,3, operator='*'))

def sandwich(type_of_meal, with_onion=False, with_tomato=False):
    print('Булочка')
    if with_onion:
        print('Лук')
    print(type_of_meal)
    if with_tomato:
        print('Помидоры')
    print('Булочка')




def print_any(*args, **kwarg):
    for i in args:
      print(i)
    for k, v in kwarg.items():
        print(k, '=', v) # создание словаря
# **additional - Kwargs для резервирования дополнительной (неизвестной заранее) позиции для инфо
def profile(name, surname, city, *children, **additional):
    print(f'Имя: {name}')
    print(f'Фамилия: {surname}')
    print(f'Из города: {city}')
    if len(children) > 0:
        print('Дети:', ', '.join(children) )
    print('Хобби:', ', '.join(additional['hobbies']))
    # print(additional)

profile('Дмитрий', 'Колесов', 'Волгоград',
        'Мария', 'Пётр', 'Василий', hobbies=['Филателия', 'Шахматы'])

# print_any('Дмитрий', 'Колесов', citi='Москва', age=27)
# sandwich(type_of_meal='котлета', with_onion=True)
