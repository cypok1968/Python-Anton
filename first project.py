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
import csv



# Подключаемся
connection = sqlite3.connect('db/movies.sqlite')

# Курсор
cursor = connection.cursor()

# Запрос (с помощью курсора)
with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # пропускаем первую строку т.к. заголовки столбцов в таблице БД
    for name, age in reader:
        cursor.execute(
            """
            INSERT INTO
            users(name, age)
            VALUES(?, ?)
            """,(name, int(age))
        )

connection.commit() # Подтверждение
connection.close() # Закрываем подключение

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
