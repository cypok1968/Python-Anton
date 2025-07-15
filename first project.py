# База данных (запись)



# База данных (чтение)
"""
1. Импорт библиотеки SQL
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем с БД (запросы и ответы)
5. Подтвердить изменение (commit)
6. Отключаемся от БД
"""
import sqlite3

class Crud: # create, red, update, delite данных в БД
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)
        self._cur = self._conn.cursor()

    def create(self, table_name, name, age):
        self._cur.execute(
            f"""
             INSERT INTO {table_name}(name, age)
             VALUES(?, ?)
             """, (name, int(age))
            )

    def read(self, table_name):
        res = self._cur.execute(
            f'SELECT * FROM {table_name}'
        ).fetchall()
        for num, name, age in res:
            print(num, name, age)

    def update(self, table_name, id_num, name=None, age=None):
        self._cur.execute(
        query = f'UPDATE {table_name} SET name={name}, age={age} WHERE id = {id_num}'
        )
        # print(query)
        self._cur.execute(
            query
        )
        self._conn.commit()

    def delete(self, id_num, table_name):
        self._cur.execute(
            f'DELETE FROM {table_name} WHERE id={id_num}'
        )
        self._conn.commit()

    # method override (переопределяем метод уничтожения объекта,
    # как только закончили работу с объектом удаляется временый объект и закрываются курсор и соединение с БД
    def __del__(self):
        self._cur.close() # сносим сначала курсор
        self._conn.close() # а потом соединение с БД

db = Crud('db/movies.sqlite')
# db.create('users', 'Егор', 25)
# db.delete(6, 'users')
db.update('users', 1, 'Евгений', 27)
db.read('users')

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
