# ДЗ 600*400 голубой прямоугольник в правом верхнем углу солнце (четверть)
# по центру надпись увеличенным шрифтом "СОЛНЕЧНЫЙ ДЕНЬ"

from PIL import Image, ImageFont, ImageDraw  # функция Image, ImageDraw из PIL отвечает за рисование нового изображения

YELLOW = (255, 255, 0)

image = Image.new('RGB',
                  (600, 400),
                  (0, 0, 255)) # создаем одноцветный прямоугольник с заданными параметрами

draw = ImageDraw.Draw(image) # создаем объект для рисования (прозрачный холст, на котором будем рисовать)

draw.ellipse((-100, -100, 100, 100), 'YELLOW', 'YELLOW', 1)

image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip.save('images/blue.jpg')

image = Image.open('images/blue.jpg')
draw = ImageDraw.Draw(image)

fnt = ImageFont.truetype('FreeMono.ttf', 50) # выбор шрифта и размера
draw.text((100, 100), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW, font=fnt)

image.save('images/blue&sun&text.jpg')
