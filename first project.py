# CSV-файлы
import  csv
from os import write

data = [
    ['name', ' age', ' city'],
    ['Андрей', ' 27', ' Казань'],
    ['Игорь', ' 31', ' Москва'],
    ['Сергей', ' 25', ' Тверь']
]

with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

with open('employee.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerow(data)