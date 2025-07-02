# Области видимости
PI = 3.1415 # необходимо в любой программе написать "блок констант
# Shadows name 'square' from outer scope - использование глобальной переменной

def greet(name):
    print('Привет,', name)
    name = 'друг'
    print('Здравствуй,', name) # изменение внешнего аргумента-константы только внутри функции

square = 'Дворцовая площадь' # оставляем одну глобальную переменную (подвержена риску изменения!!!)

def square_area(length: int, width: int) -> None:
    """
    Функция вычисления площади
    :param length: (int - задаем сразу тип переменной)
    :param width:
    :return: None
    """
    area = length * width
    print(f'Площадь площади "{square}" = {area}')


# def square_area(length, width):
#     square = length * width # пример перекрывания (приоритета) внутренней переменной над глобальной
#     # так делать нельзя!
#     print(f'Площадь площади "{square}" = {square}')


def circle_length(radius):
    perimetr = 2 * PI * radius
    print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')


def print_array(array: list) -> None:
    for item in array: # используем локальную (внутреннюю) переменную
        print(item)
# Главная функция для определения локальных переменных, не являющихся видимыми глобальными
def main():
    words = ['Привет', 'мир']
    greet('Пётр')
    circle_length(5)
    print_array(words)
    print_array(['a', 'b', 'c'])
    print('Давай встретимся, где', square)
    square_area(320, 240)

main() # подход через Главную фукцию задающую внешние действия при обращении к внутренним функциям


# words = ['Привет', 'мир']
# PI = 3.14
# greet('Пётр')
# square = 'Дворцовая площадь'
# print('Давай встретимся, где', square)
# square_area(320, 240)
# circle_length(5)
# print_array(words)
# print_array(['a', 'b', 'c'])

# def print_array(array: list) -> None:
#     for item in words: # array: поменяли на глобальную (внешнюю) переменную (список words)
#         # так делать нельзя, т.к. аргумент задан внутри функции и переменная становится неизменной
#         print(item)
#
# words = ['Привет', 'мир']
# print_array(words)
# print_array(['a', 'b', 'c'])