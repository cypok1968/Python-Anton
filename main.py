# Введение во Flask
# MVC-(Model View Controller)
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - заменяет всё на сервере из контекста запроса ("заменить")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных
# JINJA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping
# DBeaver - универсальный софт для работы с БД
import os.path
import sqlite3
from sqlite3 import Error

from flask import Flask, url_for, request, render_template, redirect
from werkzeug.utils import secure_filename

from data import db_session
from data.news import News
from data.users import User
from forms.loginform import LoginForm
from forms.user import Register
from flask_login import LoginManager, login_user, logout_user
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.errorhandler(404)
@@ -49,27 +49,32 @@
    return render_template('404.html', title='Не найдено')


@app.errorhandler(401)
def not_authorized(_):
    return redirect('/login')


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
@@ -89,27 +94,28 @@


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = Register()
    if form.validate_on_submit():  # тоже самое, что и request.method == 'POST'
        # если пароли не совпали
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Регистрация',
                                   message='Пароли не совпадают',
                                   form=form)

        db_sess = db_session.create_session()

        # Если пользователь с таким E-mail в базе уже есть
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Регистрация',
                                   message='Такой пользователь уже есть',
                                   form=form)
@@ -257,57 +263,61 @@
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


# Вывод всех публичных новостей (is_private == False)
@app.route('/news')
def news():
    db_sess = db_session.create_session()
    all_news = db_sess.query(News).filter(News.is_private != True).all()
    if current_user.is_authenticated:
        all_news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True)).all()
    else:
        all_news = db_sess.query(News).filter(News.is_private != True).all()
    # print(all_news)
    return render_template('news.html',
                           title='Новости', news=all_news)


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='127.0.0.1', port=5000, debug=debug)

    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # for news in user.news:
    #     print(news)
    # print(user.id)
    # news = News(title='Third News', content='Third Content',
    #              is_private=False)
    # user.news.append(news)
    # # db_sess.add(news)
    # db_sess.commit()
    # user = User()
    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # print(user)
    # db_sess.delete(user)
    # # user.set_username('John')
    # db_sess.commit()
    # user.name = 'User2'
    # user.about = 'Данные про User2'
    # user.email = 'b@c.ru'
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()


# МОЯ СТРАНИЦА от 17/07/25 для чтения комментов (замещена)



