# Оператор is: a is b -> когда a и b - один и тот же объект
my_refregirator = ['колбаса', 'масло', 'сыр']
# his_refregirator = ['колбаса', 'масло', 'сыр']
#his_refregirator = my_refregirator # не создает новый объект, а только ссылку на тот же id-объект
his_refregirator = my_refregirator.copy() # или [:] - создание копии с другим ID
my_refregirator += ['мясо']
print(his_refregirator)
print(my_refregirator is his_refregirator)
print(my_refregirator == his_refregirator)
print(id(my_refregirator) == id(his_refregirator))

temp = None
print(type(temp))
print(temp is None) # print(temp == None) - запись сравнения не корректна, но работает
temp = 1
print(type(temp))
print(temp == 1)

# d = {'a': 1}
# print(id(d))
# d['a'] += 1 # меняем изменяемый объект (словарь), при этом индекс не меняется
# print(id(d))
#
# a = [0]
# print(id(a))
# a[0] += 1 # меняем изменяемый объект (список), при этом индекс не меняется
# print(id(a))



