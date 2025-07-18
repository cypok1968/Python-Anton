from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Введите корректный Email')])
    password = PasswordField('Пароль', validators=[DataRequired('Пароль обязателен')])
    password_again = PasswordField('Подтвердите пароль', validators=[DataRequired('Пароли должны совпадать')])
    name = StringField('Ваше имя', validators=[DataRequired('Введите Ваше имя')])
    about = TextAreaField('Расскажите немного о себе')
    submit = SubmitField('Регистрация')

