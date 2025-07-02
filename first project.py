# ДЗ 02.07.25
# Превратить список nums в строку 123456789:
# сначала с помощью функции map превратить в список строк, а затем использовать.join

def square(num):
    return num ** 2

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(square, nums)
print(list(squares))
