# Подбор по росту
# 150 < height < 180
# Число кандидатов
# Число, кто прошёл по критерию
# Среди прошедших min и max
total = 0
total_success = 0
total_unsuccess = 0
min_val = float('inf') # - бесконечность
max_val = float('-inf') # + бесконечность

while (num := int(input('Введите рост: '))) != -1:
    if 150 <= num <= 180:
        total_success += 1
        if min_val > num:
            min_val = num
        if num > max_val:
            max_val = num
    total += 1

print(f'Число кандидатов: {total}')
print(f'Число прошедших отбор: {total_success}')
print(f'Минимальный рост: {min_val}')
print(f'Максимальный рост: {max_val}')
