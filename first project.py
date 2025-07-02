# Функция, как объект
# Передается в другие функции: функции высшего порядка

# печатник = print # печатник - объект, принявший ссылку на функцию print (не является копией)
# печатник('Привет, мир')

# Функция критерия отбора элементов списка
# Критерий: длина слова
def is_longer_six(word):
    return len(word) > 6 # функция возвращает логическое значение T(F)

# Критерий - первая буква
def is_first_letter_a(word):
    return word[0] == 'а'

fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']
res = list(filter(is_first_letter_a, fruits))
print(res)
words = ['В', 'этом', 'списке', 'останутся', 'слова',
         'длина', 'которых', 'больше', 'шести']
result = list(filter(is_longer_six, words))
print(result)

for word in filter(is_longer_six, words):
    print(word)
