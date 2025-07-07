# __init__.py показывает что работа идёт с пакетом package1
from.module import greet # относительный упрощенный импорт из module
from.utils import add # относительный упрощенный импорт из module

__version__ = '1.0.0' # версия пакета package1
__doc__ = 'Этот пакет содержит...' # документация к пакету, комментарии
__author__ = ('John')
__all__ = ['greet', 'add'] # для импорта со *