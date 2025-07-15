


# 
"""
SELECT title, year
FROM films
WHERE year > 2005
AND year < 2010
AND duration < 90
ORDER by year
"""
"""
SELECT title, year
FROM films
WHERE year BETWEEN 2005 AND 2010
AND duration < 90
ORDER by year
"""
# Пример не вполне корректного запроса
"""
SELECT title
"""
# Исправим составной запрос
"""
SELECT title FROM films
WHERE genre = (
SELECT id FROM genres
WHERE title = 'фантастика')
"""
# Выборка по пречню значений
"""
SELECT title, duration FROM films
WHERE duration IN (45, 60, 90)
ORDER BY duration DESC
"""
# по убывваанию длительности фильма

# Выборка с группировкой по ID (по возрастанию)
"""
SELECT * FROM films
WHERE year >= 2001
AND duration BETWEEN 45 and 90
GROUP BY id
"""

# Название фильма на А и содержит любое число букв "к"
### Примечание LIKE:
- % - любое количество символов от 0 до INF
- _ - любой символ
- можно и NOT LIKE
"""
SELECT title FROM films
WHERE title LIKE 'А_к%'
"""
"""
SELECT title FROM films
WHERE title NOT LIKE 'А_к%'
"""

# Выборка без повторов
### Примечание:
- DISTICT
"""
SELECT DISTICT year from films
ORDER by year
"""
# Выборка с объединением 2-х таблиц
# Составляем сводную таблицу с названиями столбцов
# на русском языке (выбираем фильмы и жанры в столбцы)
"""
SELECT
films.title as Фильм,
genres.title as Жанр
FROM films
JOIN genres
WHERE films.genre = genres.id
"""
# Выборка: сколько фильмов каких годов 
"""
SELECT year, count(*) as Кол_во
FROM films
GROUP BY year
ORDER BY Кол_во DESC
"""
# Выборка: сколько фильмов каких годов,
# количество которых более 500
"""
SELECT year, count(*) as Кол_во
FROM films

GROUP BY year
ORDER BY Кол_во DESC
"""
# Добавление в таблицу БД новых пользователей
"""
INSERT INTO
users(name, age)
VALUES('Bill', 21),
('Tom', 20),
('Tim', 41)
"""

# изменение возраста по записи, изменение имени, удаление по условию
"""
UPDATE users
SET age=33
WHERE id=3
"""

"""
UPDATE users
SET age=18, name='Billy'
WHERE id=2
"""

"""
DELETE from users
WHERE age < 19
"""