# Строки (immutable, iterable)
# Таблица символов Unicode

s = '\xB0'
u = ('\u2602')

# две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код в десятичной сист.) - возвращает символа Unicode-коду

print(u)
print('25' + s + 'C')
print(f'Код зонта в Unicode: {ord('☂')}')
print(chr(9730))
print(chr(176)) #ASCII коды от IBM (до 176 символа для всех прочих таблиц символов и для Unicode)
