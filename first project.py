# ДЗ 07/07/25
# в Методичка.pdf

from package1 import * # для __all__
# from package1.module import greet
from package1 import module
from package1 import utils
#

print(int(module.factorial(5)))
print(utils.add(50, 80))

print(greet('Мир'))
print(add(3, 7))
print('Автор')
#print(package1.module._hidden_function()) # при попытке вывода результата скрытой функции _hidden_function
                                          # выдается предупреждение об ограничении её использования
#