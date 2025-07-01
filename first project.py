# Списочные выражения (list comprehension) 01.07.25
# Вложенные списки - nested lists
a = [1, 38.6, False, 'sfs', (1, 2)] # список может содержать данные любого типа, в том числе списки и выражения
# создание вложенного списка
N = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], # висячая запятая, если вдруг нужно будет добавить ещё один вложенный массив
]
# замена всех элементов списков во вложенном списке на 1
matrix = [[1] * N for _ in range(N)] # преобразование всех элементов вложенного списка размерности N
# вместо i ставим _ потому, что индекс i нигде не используется
print(matrix)

# обход 2-мерного списка (матрицы)
# for row in range(len(matrix)): # сначала выбираем ряд, начиная с 1-го
#     for col in range(len(matrix[row])): # условие вывода каждого элемента очередного ряда, начиная с 1-го
#
# print(matrix[row][col])

# возврат замененных элементов списков во вложенном списке
count = 1
for row in range(len(matrix)): # сначала выбираем ряд, начиная с 1-го
    for col in range(len(matrix[row])): # условие вывода каждого элемента очередного ряда, начиная с 1-го
        matrix[row][col] = count
        count += 1
print(matrix)

matrix = []

start = 1
N = 4

for i in range(N):
    table = []
    for j in range(start, start + N):
        table.append(j)
        matrix.append(table)
        start += N
print(matrix)

N = 3
matrix = [[i+j for j in range(N)]for i in range(1, 10, 3)]
print(matrix)



