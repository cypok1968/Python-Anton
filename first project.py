# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>:<выражение>


# def is_longer_six(word):
#     return len(word) > 6
#
#
# is_longer_six = lambda word: len(word) > 6
#
# def is_first_letter_(word):
#     return world[0] == a
#
#
#     return  word[0] ==

fruits = ['арбуз', 'ананас', 'банан', 'малина', 'ежевика']

res = list(filter(lambda x: x[0] == 'a', fruits))
print(res)

res = list(filter(lambda s: 'ан' in s, fruits))
print(res)

# в одну строку вывести список квадратов чисел от 3 до 15
# [9,16,...]
res = list(map(lambda y: y ** 2, range(3, 16)))
print(res)
res = [y ** 2 for y in range(3, 16)]
print(res)

words = ['В', 'этом', 'списке', 'останутся', 'слова',
          'длина', 'которых', 'больше', 'шести']

# result = list(filter(lambda word: len(word) > 6. words))

long_words = [word for word in words if len(word) > 6]
print(long_words)
