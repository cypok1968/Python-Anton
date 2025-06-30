# Кортеж (tuple) тот же список, но неизменяемый (отличие от строки)
# Студент и средний балл


N=3
students = []

for st in range(N):
    student, average = input('ФИО: '), float(input('Средний балл: '))
    students.append((student, average)) # создание кортежа из трёх списков со средними баллами (3 студента)
                                        # pack
print(students)

for st in students:
    student, average = st # unpack
    print('Студент: ', student)
    print('Средний балл: ', average)

