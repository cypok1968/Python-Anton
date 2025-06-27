# Строки (immutable, iterable)
# Таблица символов Unicode
# две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код в десятичной сист.) - возвращает символа Unicode-коду

#abc = 'абвгдеёжзийклмнопрстуфхцъыьэюя'
phrase = 'Язык Phyton'

print(phrase.lower()) # все маленькие
print(phrase.upper()) # dct ,jkmibt
print(phrase.capitalize()) # только первая буква заглавная
print(phrase.title()) # все слова с заглавной
print('Ура! ' * 3) # повторение строки
print('Телевизор'.count('e')) # количество вхождений подстроки (число повторений символа)
print('Python'.index('h')) # индекс символа, его номер в строке (012345...)
