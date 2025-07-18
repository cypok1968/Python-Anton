# Введение во Flack
# MVC-(Model View Controller)
# GET - запрашивает данные с сервера (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контекста запроса ("заменить")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных, после отправки данных методом POST
# JINIA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping (объектно-реляционное отображение)

import os.path
from sqlite3 import Error

from forms.loginform import LoginForm
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename
from data import db_session
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html',
                           **params)


@app.route('/about')
def about():
    return render_template('about.html',
                           title='Про нас')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html',
                           title='Свяжитесь с нами')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Форма отправлена'
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/python.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Картинка Питона</title>
            </head>
            <body>
                <img src="{url_for('static', filename='images/python.jpg')}" alt="Python">
            </body>
            </html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()


# Так делать мы не будем
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)

# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - дес. дробь
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате)
@app.route('/greeting/<string:user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'


@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    try:
        # Подключение к базе данных
        con = sqlite3.connect('db/movies.sqlite')
        cur = con.cursor()

        if id_num is None:
            # Получение списка всех пользователей
            query = 'SELECT trip_id, name FROM users'
            response = cur.execute(query)
            result = response.fetchall()
            return render_template('get_user.html', users=result)

        # Получение информации о конкретном пользователе
        query = 'SELECT name, city, date_first FROM users WHERE trip_id=?'
        response = cur.execute(query, (id_num,))
        result = response.fetchone()

        if result:
            name, city, date_first = result
            return render_template('get_user.html',
                                   name=name,
                                   city=city,
                                   start=date_first)
        else:
            return "Пользователь не найден", 404

    except Error as e:
        return f"Произошла ошибка: {str(e)}", 500

    finally:
        # Гарантированное закрытие соединения
        if con:
            cur.close()
            con.close()



@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form)
        return 'Форма успешно отправлена'


@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        # print(request.files)
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран!!!'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} успешно загружен!'
    return "Ошибка загрузки"


@app.route('/numbers/')
@app.route('/numbers/<int:num>')
def odd_even(num=None):
    if num is None:
        return render_template('numbers.html',
                               title='Нет числа', number='')
    return render_template('numbers.html',
                           title='Чет-нечёт', number=num)


@app.route('/deals')
def printlist():
    deal = ['Помыть посуду', 'Выгулять собаку',
            'Снять показания счётчика', 'Сходить в магазин']
    return render_template('printlist.html', deals=deal)


@app.route('/queue')
def queue():
    # loop.index - номер итерации, начиная с 1
    # loop.index0 - номер итерации, начиная с 0
    # loop.first - True, если первая итерация
    # loop.last - True, если последняя итерация
    return render_template('vars.html', title='Стоим в очереди')


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='127.0.0.1', port=5000, debug=debug)


# МОЯ СТРАНИЦА от 17/07/25

# import os.path
# from forms.loginform import LoginForm
# from flask import Flask, url_for, request, render_template # не путать с import request
# from werkzeug.utils import secure_filename
# from data import db_session
# import sqlite3
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/' # подключаем оператор выгрузки в дир. uploads/
# app.config['SECRET_KEY'] = 'just_secret_key' # генерируем секретный ключ 'just_secren_key'  , чтобы у других не было доступа
# ALLOWED_EXTENSION = ['txt', 'pdf', 'zip', 'jpg', 'png'] # разрешаем выгрузку типов файлов
# debug = False
#
# def allowed_file(filename):
#     return ('.' in filename and # разделение записи из-за лимита длины,
#                                 # скобка для восприятия как единого целого
#             filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION)
#
# @app.route('/') # отклик на вызов декоратора
# @app.route('/index') # тот же отклик на вызов другого декоратора
# def index():
#     params = {}
#     params['user'] = 'слушатель'
#     params['weather'] = 'Хорошая погода'
#     params ['title'] = 'Приветствую'
#     username = 'слушатель'
#     return render_template('index.html',
#                            **params)
#
# @app.route('/about') # тот же отклик на вызов другого декоратора
# def about():
#       return render_template('about.html',
#                            title='О компании')
#
#
# @app.route('/contacts') # тот же отклик на вызов другого декоратора
# def contacts():
#       return render_template('/contacts.html',
#                            title='Наши контакты')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return 'Форма отправлена'
#     return render_template('login.html', title='Авторизация', form=form)
#
# # @app.route('/about')
# # def about(): # можно задавать ту же функцию, но с другим имененем
# #              # для каждого декоратора, т.е. нельзя использовать снова имя index
# #     print('Вызвана функция about')
# #     return 'O нас'
# #
# # @app.route('/contacts')
# # def contacts():
# #     print('Вызвана функция contacts')
# #     return 'Наши контакты'
#
#
# @app.route('/countdown')
# def cd():
#     lst = [str(x) for x in reversed(range(10))] # return только!!! строковое представление (str)
#                                                 # в т.ч. для *.html
#     lst.append('Полетели!!!')
#     #return '\n'.join(lst) # вывод ответа браузера списком в строку
#     return '<br>'.join(lst) # вывод ответа браузера списком в столбец
#
# @app.route('/image') # при отображении специальных шрифтов java scr и т.д.
#                     # данные в папке static (корневой каталог для таких файлов + подкаталоги)
# def show_image():
#     return '<img src ="./static/images/python.jpg">' # без url for см. в подключениях импорта
#     # return f'<img src="{url_for('static', filename='/images/python.jpg')}">'
#
# @app.route('/sample-page') # app использует -
# def sample_page():
#     return f"""<!DOCTYPE html>
#         <html lang="ru">
#         <head>
#             <meta charset="UTF-8">
#             <title>Питон(картинка)</title>
#         </head>
#         <body>
#             <img src="f{url_for('static', filename='images/python.jpg')}" alt="Python">
#         </body>
#         </html>
#     """
#
#
# @app.route('/sample-page2') # app использует -
# def sample_page2():
#     with open ('temp.html', 'r', encoding='UTF-8') as html:
#         return html.read()
#
# # Так делать не будем
# # x=5
# #
# # @app.route('/1') # app использует -
# # def show_num():
# #     global x
# #     x += 1
# #     return str(x)
#
# # <string> - по умолчанию строчное представление
# # для отображения записи целого числа <int:number>
# # для записи дес. числа <float:number>
# # <path:p> - может содержать слэши для указания пути
# # <uuid:id> - строка-идентификатор (16-байт в HEX-формате, в 16-ном формате)
# # <user> - пишем в пути для сайта на браузере и появляется на экране Привет...
# # @app.route('/greeting/<user>')
# # def greeting(user):
# #     return f'Привет, {user}'
#
#
# @app.route('/greeting/<string:user>/<int:id_num>')
# def greeting(user, id_num):
#     return f'Привет, {user} c id={id_num}'
#
#
#
# # Подключаемся вверху к БД SQL и
# # делаем запрос с отображением в адресной строке браузера ид-номера пользователя
# # для вывода имени и города
# @app.route('/get-user')
# @app.route('/get-user/<int:id_num>')
# # def get_user(id_num):
# def get_user(id_num=None): # если запись вводится без номера id,
#                           # то вывод не инфо, а соотв. сообщения
#     if id_num is None:
#         return 'Нет номера записи'
#     con = sqlite3.connect('db/movies.sqlite')
#     cur = con.cursor()
#     query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
#     response = cur.execute(query)
#     result = response.fetchone()
#     print(result) # промежуточная проверка вывода на экран в Пайчарм
#     name, city = result
#     cur.close()
#     con.close()
#     # return str(result[0]) - вывод строкой
#     return f'''<table border=1>
#     <tr>
#     <td>ФИО</td>
#     <td>Город</td>
#     </tr>
#     <tr>
#     <td>{name}</td>
#     <td>{city}</td>
#     </tr>
#     </table>'''
#
#
# @app.route('/form-test', methods=['POST', 'GET'])
# def form_test():
#     if request.method == 'GET':
#         with open('form.html', 'r', encoding='utf-8') as html:
#             return html.read()
#     elif request.method == 'POST':
#         print(request.form)
#         # print(request.form['gender'])
#         # print(request.form['about'])
#         # print(request.form['email'])
#         # print(request.form['accept'])
#         #request.form['gender']
#         return 'Форма успешно отправлена'
#
# @app.route('/upload', methods=['POST', 'GET'])
# def file_upload():
#     if request.method == 'GET':
#         with open('upload.html', 'r', encoding='utf-8') as html:
#             return html.read()
#     elif request.method == 'POST':
#         if 'file' not in request.files:
#             return 'Файл не был выбран!!!' # если файл не попадает своим расширением в разрешенный список для выгрузки
#
#         file = request.files['file']
#
#         if file.filename =='':
#             return 'Файл не был выбран!!!' # в случае если указанный файл не имеет расширения
#                                            # или без имени (имя на русском), то есть не опознан прг
#
#         if file and allowed_file(file.filename):
#             new_name = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name)) # выбираем файл и загружаем
#             return f'Файл{new_name} успешно загружен!'
#     return "Ошибка загрузки"
#
#
# @app.route('/numbers')
# @app.route('/numbers/<int:num>')
# def odd_even(num=None):
#     if num is None:
#         return render_template('numbers.html',
#                                title='Нет числа', number='')
#     return render_template('numbers.html',
#                            title='Чёт-нечёт', number=num)
#
# # @app.route('/numbers')
# # def odd_even():
# #     return render_template('numbers.html',
# #                            title='Чёт-нечёт', number=2)
#
#
# app.route('/deals')
# def printlist():
#     deal = ['Помыть посуду', 'Выгулять собаку',
#             'Снять показания счётчика воды' 'Сходить в магазин']
#     return render_template('printlist.html',
#                            deals=deal)
#
# app.route('/queue')
# def queue():
#     # loop.index - номер иттерации начиная с первой иттерации
#     # loop.index0 - номер иттерации начиная с нуля
#     # loop.first - номер первой иттерации
#     # loop.last - номер последней иттерации
#     return render_template('vars.html',
#                            title='Стоим в очереди')
#
#
#
#
# # if __name__ == '__main__': # запуск приложения веб-сайта на браузере
# #                            # только после ввода всех функций и запросов!!!
# #     # app.run(host='localhost', port=5000, debug=debug)
# #     app.run(host='127.0.0.1', port=5000) # вместо имени содержит адрес локального хоста
# #                                         # localhost:127.0.0.1, тоже будет подключать
#
# if __name__ == '__main__': # запуск приложения веб-сайта на браузере
#                            # только после ввода всех функций и запросов!!!
#     # app.run(host='localhost', port=5000, debug=debug)
#     db_session.global_init('db/news.sqlite')
#     app.run(host='127.0.0.1', port=5000) # вместо имени содержит адрес локального хоста
#                                         # localhost:127.0.0.1, тоже будет подключать


