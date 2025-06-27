# Строки (immutable, iterable)
# Таблица символов Unicode
# две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код в десятичной сист.) - возвращает символа Unicode-коду
s = set()
word = input('Введите фразу для зашифровки: ')
#
# # Зашифровываем
for ch in word:
    s.add(ord(ch))

print(s)

# Расшифровываем

res = ''
for i in s:
    res += chr(i)

print(res)
