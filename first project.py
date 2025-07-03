# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>:<выражение>
# словарные выражения

# numbers = [1, 2, 3, 4, 5] # или list(range(1, 6))
# squares = {n: n ** 2 for n in numbers}
# print(squares)
#
# numbers = range (1, 11) - можно перенести внутрь словарного выражения для краткости записи
# squares = {n: n ** 2 for n in range (1, 10) if n % 2 == 0}
# print(squares)
#
# source_dict = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# dest_dict = {k: v * 2 for k, v in source_dict.items()}
# print(dest_dict)

fruits = ['арбуз', 'ананас', 'банан', 'малина', 'ежевика']

print(sorted(fruits, key=lambda ch: len(ch))) # ключ сортировки key - критерий по которому будет сортировка

# fruits.sort()
# print(fruits)

# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^ set([x.upper() for x in RUSSIAN_ABC]) ^ set([x.upper() for x in RUSSIAN_ABC]))
# print(ABC)
# print(ENGLISH_ABC)
# print(RUSSIAN_ABC)


# text = 'Однажды, теперь и потом.'.lower()

txt = ['', '']

def remove_punctuation(text):
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text)) # убираем знаки из текста


def get_word(text: str) -> list:
    return remove_punctuation(text).split() # вывод текста в виде списка


def long_words(text, length=4) -> list:
    return filter(lambda word: len(word) >= length, get_word(text))

words = get_word(txt.lower())

Считаем частоту слов:
for word in words:
    if word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

res = {k: v for k, v in sorted(d.item(), key=lambda item: item[1], reverse=True)}

for k, v in res.items():
    print(k, v)

# print(long_words(text))
# text = ''.join(filter(lambda x: x in ABC ^ {' '}, text))
# print(text)

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

#fruits = ['арбуз', 'ананас', 'банан', 'малина', 'ежевика']
#
# res = list(filter(lambda x: x[0] == 'a', fruits))
# print(res)
#
# res = list(filter(lambda s: 'ан' in s, fruits))
# print(res)
#
# # в одну строку вывести список квадратов чисел от 3 до 15
# # [9,16,...]
# res = list(map(lambda y: y ** 2, range(3, 16)))
# print(res)
# res = [y ** 2 for y in range(3, 16)]
# print(res)
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#           'длина', 'которых', 'больше', 'шести']

# result = list(filter(lambda word: len(word) > 6. words))

# long_words = [word for word in words if len(word) > 6]
# print(long_words)
