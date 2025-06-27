# Строки (immutable, iterable)
# Каждая буква повторяется столько раз,
# какой её номер в строке (считаем с 1)

word = 'статор'
res = ''

# 1 способ
for i in range(len(word)):
     print(word[i] * (i + 1), end='')
# 2 способ
for i in range(len(word) + 1):
    print(word[i-1] * i, end='')


#abc = 'абвгдеёжзийклмнопрстуфхцъыьэюя'


