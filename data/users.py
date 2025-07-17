import datetime
import sqlalchemy
from sqlalchemy import Column

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase): # создаем новую таблицу, указание нового имени обязательно,
                            # чтоб имя не User (user)
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, # создаем колонки новой БД
                             nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String,
                             nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                             index=True,
                             nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String,
                                       nullable=True)
    create_data = sqlalchemy.Column(sqlalchemy.DateTime,
                                       default=datetime.datetime)