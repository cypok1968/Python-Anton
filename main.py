# Введение во Flack
# MVC-(Model View Controller)
from flask import Flask, url_for

app = Flask(__name__)
debug = False

@app.route('/') # отклик на вызов декоратора
@app.route('/index') # тот же отклик на вызов другого декоратора
def index():
    return 'Привет, Flask'


@app.route('/about')
def about(): # можно задавать ту же функцию, но с другим имененем
             # для каждого декоратора, т.е. нельзя использовать снова имя index
    print('Вызвана функция about')
    return 'O нас'


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))] # return только!!! строковое представление (str)
                                                # в т.ч. для *.html
    lst.append('Полетели!!!')
    #return '\n'.join(lst) # вывод ответа браузера списком в строку
    return '<br>'.join(lst) # вывод ответа браузера списком в столбец

@app.route('/image') # при отображении специальных шрифтов java scr и т.д.
                    # данные в папке static (корневой каталог для таких файлов + подкаталоги)
def show_image():
    return '<img src ="./static/images/python.jpg">' # без url for см. в подключениях импорта
    # return f'<img src="{url_for('static', filename='/images/python.jpg')}">'

@app.route('/sample-page') # app использует -
def sample_page():
    return f"""<!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Питон(картинка)</title>
        </head>
        <body>
            <img src="f{url_for('static', filename='images/python.jpg')}" alt="Python">
        </body>
        </html>
    """


@app.route('/sample-page2') # app использует -
def sample_page2():
    with open ('temp.html', 'r', encoding='UTF-8') as html:
        return html.read()

# Так делать не будем
# x=5
#
# @app.route('/1') # app использует -
# def show_num():
#     global x
#     x += 1
#     return str(x)

# <string> - по умолчанию строчное представление
# для отображения записи целого числа <int:number>
# для записи дес. числа <float:number>
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате, в 16-ном формате)
# <user> - пишем в пути для сайта на браузере и появляется на экране Привет...
# @app.route('/greeting/<user>')
# def greeting(user):
#     return f'Привет, {user}'


@app.route('/greeting/<string:user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'

import sqlite3

# Подключаемся вверху к БД SQL и
# делаем запрос с отображением в адресной строке браузера ид-номера пользователя
# для вывода имени и города
@app.route('/get-user')
@app.route('/get-user/<int:id_num>')
# def get_user(id_num):
def get_user(id_num=None): # если запись вводится без номера id,
                          # то вывод не инфо, а соотв. сообщения
    if id_num is None:
        return 'Нет номера записи'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    print(result) # промежуточная проверка вывода на экран в Пайчарм
    name, city = result
    cur.close()
    con.close()
    # return str(result[0]) - вывод строкой
    return f'''<table border=1>
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>
'''

if __name__ == '__main__': # запуск приложения веб-сайта на браузере
                           # только после ввода всех функций и запросов!!!
    app.run(host='localhost', port=5000, debug=debug)
    # app.run(host='127.0.0.1', port=5000) # вместо имени содержит адрес локального хоста
                                        # localhost:127.0.0.1, тоже будет подключать
