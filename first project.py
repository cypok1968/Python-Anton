# JSON - (Java Script Object Notation) - не родной формат Питона, а формат Java Script (преобразуется в Питон)
# load () - метод для чтения из файла JSON
# loads () - метод для чтения строкового представления
# зарегистрироваться на сайте openweathermap.org, взять после регистрации ключ для обращения к серверу !!!
# import json
#
# d = {
#     'ананас': 300,
#     'банан': 400,
#     'яблоко': 120,
#     'груша': 280,
# }
# # # запись напрямую в файл
# with open('fruits.json', 'w', encoding='utf-8') as f:
#     json.dump(d, f, indent=4)
# print()
# вывод в виде строки
# print(json.dumps(d, indent=4))
# print(data)





# with open('dogs.json', 'rt') as d:
#     # data = json.load(d) # для последующего чтения напрямую из файла
# # print(data) # простой вывод инфо из словаря
#     temp = d.read() # читаем файл как строку
#     data = json.loads(temp) # строковое представление JSON
#
# for i in range(len(data)):
#     print(f'Питомец: {i+1}')
#     for k, v in data[i].items():
#         if type(v) == list:
#             print(f'{k}: {', '.join(v)}')
#         else:
#             print(f'\t{k}: {v}')

# for k, v in data.items():
#     if type(v) == list:
#         print(f'{k}: {', '.join(v)}')
#     else:
#         print(f'{k}: {v}')


# ZIP
from zipfile import is_zipfile, ZipFile
import os

# csv_files = [f for f in os.listdir() if f.endswith('csv')] # вывод списка файлов
# # print(csv_files)
# with ZipFile('archive.zip', 'w') as myzip: # упаковка в архив с последующим удалением самих файлов
#     for file in csv_files:
#         myzip.write(file)
#         os.remove(file)

# files_to_extract = ['people.csv', 'files.csv']
#
# # Распаковать
# with ZipFile('archive.zip', 'w') as zip_obj: # распаковка из архива
#     #zip_obj.extractall() # распаковка всех файлов
#     zip_obj.extractall(members=files_to_extract) # выборочная распаковка


# CSV-файлы (strptime)
# import  csv
# from os import write

# data = [
#     ['name', ' age', ' city'],
#     ['Андрей', ' 27', ' Казань'],
#     ['Игорь', ' 31', ' Москва'],
#     ['Сергей', ' 25', ' Тверь']
# ]
#
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         print(row)
#
# with open('employee.csv', 'w', encoding='utf-8') as f:
#     write = csv.writer(f)
#     write.writerow(data)
#
# with open('people.csv', 'r', encoding='utf-8') as f:
#     dict_reader = csv.DictReader(f)
#     for row in dict_reader:
#         print(f'{row['name']} живёт в городе {row['city']}')

# field_names = ['name', ' age', ' city']
# data = {
#     'name', 'Андрей',
#     'age', 27,
#     'city', 'Москва',
# }
#
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=field_names)
#     writer.writerow(data)

# Режимы квотирования
# data = ['name', 25, 'town']
# with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)

