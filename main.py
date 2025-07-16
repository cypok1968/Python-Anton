# Введение во Flack
# MVC-(Model View Controller)
from fileinput import filename

from flask import Flask, url_for

app = Flask(__name__)

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
    lst.append(('Полетели!!!'))
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


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
    # app.run(host='127.0.0.1', port=5000) # вместо имени содержит адрес локального хоста
                                        # localhost:127.0.0.1, тоже будет подключать