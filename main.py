# Введение во Flack
# MVC-(Model View Controller)
# GET - запрашивает данные с сервера (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контекста запроса ("заменить")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных, после отправки данных методом POST
import os.path

from flask import Flask, url_for, request # не путать с import request
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/' # подключаем оператор выгрузки в дир. uploads/
ALLOWED_EXTENSION = ['txt', 'pdf', 'zip', 'jpg', 'png'] # разрешаем выгрузку типов файлов
debug = False

def allowed_file(filename):
    return ('.' in filename and # разделение записи из-за лимита длины,
                                # скобка для восприятия как единого целого
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION)

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
    </table>'''

@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form)
        # print(request.form['gender'])
        # print(request.form['about'])
        # print(request.form['email'])
        # print(request.form['accept'])
        #request.form['gender']
        return 'Форма успешно отправлена'

@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл не был выбран!!!' # если файл не попадает своим расширением в разрешенный список для выгрузки

        file = request.files['file']

        if file.filename =='':
            return 'Файл не был выбран!!!' # в случае если указанный файл не имеет расширения
                                           # или без имени (имя на русском), то есть не опознан прг

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name)) # выбираем файл и загружаем
            return f'Файл{new_name} успешно загружен!'
    return "Ошибка загрузки"





if __name__ == '__main__': # запуск приложения веб-сайта на браузере
                           # только после ввода всех функций и запросов!!!
    app.run(host='localhost', port=5000, debug=debug)
    # app.run(host='127.0.0.1', port=5000) # вместо имени содержит адрес локального хоста
                                        # localhost:127.0.0.1, тоже будет подключать
