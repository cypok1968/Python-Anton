# Строки (immutable, iterable)
# Списки (lists)

lst = [] # пустой список "окрошка"

while (item := input('Ингредиент: ')) != '': # выбор ингредиентов окрошки
    lst.append(item)

temp = set(lst) # исключение повторов ингредиентов окрошки
lst = list(temp)

print(f'У нас есть {len(lst)} ингредиентов: ')

lst.sort()



for i in range(len(lst)):
    print(f'\t{i+1}. {lst[i]}') # упорядочение вывода списка

