# Списочные выражения (list comprehension) 01.07.25
# Занести в список каждое третье слово из предложения
text = 'Списочные выражения применяются для эффективности кода'

#res = [a for a in text.split() if (text.index(a) + 1) % 3 == 0]
res = [a for a in text.split()[2::3]] # создание списка
#res = set(a for a in text.split()[2::3]) # создание множества кортеж
print(res)



