# module.py модуль из пакета связанных библиотек package1
# Публичная функция
def greet(name):
    return f'Привет, {name}'

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Скрытая функция (имя с обязательным первым символом "подчёркивания")
def _hidden_function():
    return 'Для внутреннего пользования'
