# Iterable object
# len()
from operator import length_hint

a = 123456

length = len(str(a))

print(length)

word = input ('Введите слово для анализа длины:')
if not word or len(word) > 3:
    print('Вы ничего не ввели или слово слишком короткое')

if len(word) > 3:
    print('Длина слова "'+ word + '" =', len(word) )
