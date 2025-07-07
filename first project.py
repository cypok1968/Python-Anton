# Встроенные библиотеки (надо иметь ввиду, что в новой версии Python
# могут не сохраняться не переписываться старые библиотеки)
# заходим в хранилище библиотек (репозиторий) Python в инете на сайте
# PyPI - Python Package Index (pypi.org)
# from pprint import pprint
# PIL - Python Imagine Library, векторное изображение
# (пакет для установки доп.библиотек: в командной строке pip install pillow))
# для удаления доп.библиотек: в командной строке pip uninstall pillow
# python3 -m (только для Линокс) pip install --upgrade pip - обновление установщика библиотек для инсталяции
# python3 -m (только для Линокс) pip install --upgrade pillow
# pip freeze > requirements.txt - создание файла зависимости (замораживаем список библиотеки)
# pip install -r requirements.txt - установка списка библиотек
# RGB - растровое изображение (цвета пикселя)
# thumbnail "большой палец"

from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw

orig = Image.open('images/python.jpg').convert('RGB') # на всякий случай конвертируем в формат RGB
# размытие
# blue_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# blue_image.show()

# Усиление разкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image = enchancer.enchance(4.0)
# sharpened_image.show()


# orig = Image.open('images/sunny_day.jpg').convert('RGB')
#
# up = orig.crop((0, 0, 600, 200))
# down = orig.crop((0, 200, 600, 400))
#
# new = Image.new('RGB', (600, 400))
#
# new.paste(down, )
# new.paste(down, )
# show()



# ДЗ 600*400 голубой прямоугольник в правом верхнем углу солнце (четверть)
# по центру надпись увеличенным шрифтом "СОЛНЕЧНЫЙ ДЕНЬ"

# 1 вариант (мой, выдает ошибку
# from PIL import Image, ImageFont, ImageDraw  # функция Image, ImageDraw из PIL отвечает за рисование нового изображения
#
# YELLOW = (255, 255, 0)
#
# image = Image.new('RGB',
#                   (600, 400),
#                   (0, 0, 255)) # создаем одноцветный прямоугольник с заданными параметрами
#
# draw = ImageDraw.Draw(image) # создаем объект для рисования (прозрачный холст, на котором будем рисовать)
#
# draw.ellipse((-100, -100, 100, 100), 'YELLOW', 'YELLOW', 1)
#
# image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# image_flip.save('images/blue.jpg')
#
# image = Image.open('images/blue.jpg')
# draw = ImageDraw.Draw(image)
#
# draw.text((100, 100), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW) # без выбора шрифта и размера
# # fnt = ImageFont.truetype('FreeMono.ttf', 50) # выбор шрифта и размера
# # draw.text((100, 100), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW, font=fnt)
#
# image.save('images/blue&sun&text.jpg')

# 2 вариант


# https://fontsforyou.com/ru/specific-fonts/ttf-

# W = 600
# H = 400
#
# image

# расчитываем позицию для центрирования


# image save (
