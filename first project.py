# Декораторы (определение функции внутри другой функции)
# Nonlocal использум когда хотим обратиться из внутренней функции к внешней
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Функция исполнялась:{finish - start:.4f} сек.')
        return  result
    return wrapper

@timeit
def test():
    time.sleep(0.8)


test()

# def logger(func):
#     counter = 0
#     def decorated_func(*args, **kwargs):
#         nonlocal counter
#         counter += 1
#         print(counter, '->', 'Аргументы', args,
#               'Именованные аргументы:', kwargs)
#         result = func(*args, **kwargs)
#         print('____', 'Результат:', result)
#         return (result)
#     return decorated_func
#
# @logger # декорирует имеющуюся функцию (ниже)
# def make_burger(meal='говядиной', onion=False, tomato=False):
#     print('Булочка')
#     if onion:
#         print('Луковые кольца')
#     print('Котлета с', meal)
#     if tomato:
#         print('Помидоры')
#     print('Булочка')
#
# make_burger('бараниной', onion=True)


# def outer():
#     x=5
#
#
#     def inner():
#         nonlocal x
#         print('Nonlocal x=', x)
#         x = 10
#
# inner()
# print('New x=', x)

# def upper_case_print(old_func):
#     def new_func(*args, **kwargs):
#         case = kwargs.pop('case', None)
#         if case =='U':
#             args_up_case = [str(arg).upper() for arg in args]  # декорируем чужую функцию верхним регистром вывода текста
#         elif case =='L':                                      # ИЛИ
#             args_up_case = [str(arg).lower() for arg in args] # декорируем чужую функцию нижним регистром вывода текста
#         return old_func(*args, **kwargs)
#     return  new_func
# new_print = upper_case_print(print)
# new_print('приветствую') # получаем верхний регистр ПРИВЕТСТВУЮ
# new_print('Привет', case='U')
# new_print('Привет', case='L')

# def upper_case_print(old_func):
#     def new_func(*args, **kwargs):
#         args_up_case = [str(arg).upper() for arg in args]  # декорируем чужую функцию верхним регистром вывода текста
#         old_func(*args_up_case, **kwargs)
#     return  new_func
# new_print = upper_case_print(print)
# new_print('приветствую') # получаем верхний регистр ПРИВЕТСТВУЮ

# def answer(question): # функция с небогатым функционалом (не имеем права переделывать)
#     return 'думайте сами'
#
# def dialog():
#     def answer(question): # переопределяем (расширяем) функционал чужой функции
#                        # внутри своей функции (с необходимые нам свойствами)
#         if question.lower().startswith('когда'):
#             return 'Никогда'
#         else:
#             return 'Уппппс'
#     question = input()
#     while question != '':
#         print(answer(question))
#         question = input()
#
# dialog()

# Погода через API

# from http.client import responses
# import requests
# from PIL import Image
# import io
#
# API_KEY = '59c82cd885057e420a60002ceb04e81e'
# URL = 'http://api.openweathermap.org/data/2.5/weather'
# CITY = 'Лондон'
#
# params = {
#     'q': CITY,
#     'appid': API_KEY,
#     'units': 'metric',
#     'lang': 'ru'
# }
#
# response = requests.get(URL, params=params)
# result = response.json()
# # print(result)
#
# weather = result['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
# data = result['coord']
# ll = f'{data['lon']},{data['lat']}'
# # print(ll)
#
#
# print(f'Сегодня в городе {CITY}: {weather}')
# print(f'Температура: {temperature:.1f}\xB0C')
# print(f'Влажность: {humidity}%')
# print(f'Скорость ветра: {wind} м/с')
# link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&map=0.005,0.005&l=sat&pt={ll},pm2dgl'
# # link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
# image = requests.get(link).content
# if image:
#     im = Image.open(io.BytesIO(image)).convert('RGB')
#     im.save('map.jpg')

# мой вариант, не работает !!!
# URL ='http:///api.openweathermap.org/data/2.5/weather'
# CITY = 'Санкт-Петербург' # ввод города для метеоинформации
#
# params = {
#     'q': CITY, # указываем по этому ключу Город
#     'appid': API_KEY, # указываю свой ключ
#     'units': 'metric', # указываем систему мер
#     'lang': 'ru'
# }
#
# response = requests.get(URL, params=params)
# # print(response)
# result = response.json()
# # print(result)
# weather = ['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
#
# print(f'Сегодня в городе {CITY}: {weather}')
# print(f'Температура: {temperature:.1f}\xB0C')
# print(f'Влажность: {humidity}%')
# print(f'Скорость ветра: {wind} м/с')
# data = result['coords']
# ll = f'{data['lon']},{data['lat']}'
# print(ll)
# link = f'https://static-maps.yandex.ru/1.x/?ll=30.325498,59.918305&spn=0.0025,0.0025&l=map&pt=30.325498,59.918305,pm2dgl'
# # link = f'https://static-maps.yandex.ru/1.x/?ll=30.325498,59.918305&spn=0.0025,0.0025&l=spn&pt=30.325498,59.918305,pm2dgl'
# # спутниковый снимок
# image = requests.get(link).content
# if image:
#     # Image.open(io.BytesIO(image)).show() # если просто показать на экране
#     im = Image.open(io.BytesIO(image)).convert('RGB')
#     im.save('map.jpg')

# конец моего (не рабочего) варианта

# # База данных (запись)
# # База данных (чтение)
# """
# 1. Импорт библиотеки SQL
# 2. Подключаемся к БД
# 3. Назначить "курсор"
# 4. Работаем с БД (запросы и ответы)
# 5. Подтвердить изменение (commit)
# 6. Отключаемся от БД
# """
# import sqlite3
#
# class Crud: # create, red, update, delite данных в БД
#     def __init__(self, db_path):
#         self._conn = sqlite3.connect(db_path)
#         self._cur = self._conn.cursor()
#
#     def create(self, table_name, name, age):
#         self._cur.execute(
#             f"""
#              INSERT INTO {table_name}(name, age)
#              VALUES(?, ?)
#              """, (name, int(age))
#             )
#
#     def read(self, table_name):
#         res = self._cur.execute(
#             f'SELECT * FROM {table_name}'
#         ).fetchall()
#         for num, name, age in res:
#             print(num, name, age)
#
#     def update(self, table_name, id_num, name=None, age=None):
#         self._cur.execute(
#         query = f'UPDATE {table_name} SET name={name}, age={age} WHERE id = {id_num}'
#         )
#         # print(query)
#         self._cur.execute(
#             query
#         )
#         self._conn.commit()
#
#     def delete(self, id_num, table_name):
#         self._cur.execute(
#             f'DELETE FROM {table_name} WHERE id={id_num}'
#         )
#         self._conn.commit()
#
#     # method override (переопределяем метод уничтожения объекта,
#     # как только закончили работу с объектом удаляется временый объект и закрываются курсор и соединение с БД
#     def __del__(self):
#         self._cur.close() # сносим сначала курсор
#         self._conn.close() # а потом соединение с БД
#
# db = Crud('db/movies.sqlite')
# # db.create('users', 'Егор', 25)
# # db.delete(6, 'users')
# db.update('users', 1, 'Евгений', 27)
# db.read('users')

# import csv
#
# # Подключаемся
# connection = sqlite3.connect('db/movies.sqlite')
#
# # Курсор
# cursor = connection.cursor()
#
# # Запрос (с помощью курсора)
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',')
#     next(reader) # пропускаем первую строку т.к. заголовки столбцов в таблице БД
#     for name, age in reader:
#         cursor.execute(
#             """
#             INSERT INTO
#             users(name, age)
#             VALUES(?, ?)
#             """,(name, int(age))
#         )
#
# connection.commit() # Подтверждение
# connection.close() # Закрываем подключение

# result = cursor.execute(
#     """
#     UPDATE users
#     SET age=33
#     WHERE id=3
#     """
# )



# print(result)

# fetchall - всё
# fetchone - только первое соответствие
# fetchmany(N) - N - соответствий

# array = result.fetchall()
#
# for title, year in array:
#     print(title, year)

# connection.commit() # Подтверждение
# connection.close() # Закрываем подключение
