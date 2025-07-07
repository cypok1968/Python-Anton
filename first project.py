# ДЗ 600*400 голубой прямоугольник в правом верхнем углу солнце (четверть)
# по центру надпись увеличенным шрифтом "СОЛНЕЧНЫЙ ДЕНЬ"

from PIL import Image, ImageFont, ImageDraw

# Мои варианты

YELLOW = (255, 255, 0)

image = Image.new('RGB',
                  (600, 400),
                  (0, 163, 232))

draw = ImageDraw.Draw(image)

draw.circle((600, 0), 70, 'YELLOW', 'YELLOW', 1)

#  0-вой вариант без изменения высоты стандартного шрифта
# draw.text((100, 100), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW)

# 1-й вариант
# fnt = ImageFont.truetype(font='arial.ttf', size=50) # для встроенного шрифта  arial.ttf

# 2-й вариант с загрузкой шрифтов в fonts/...
font = ImageFont.truetype(font='fonts/ofont.ru_Propaniac.ttf', size=45) # для загруженного шрифта ofont.ru_Propaniacl.ttf
draw.text((180, 170), 'СОЛНЕЧНЫЙ ДЕНЬ', fill=YELLOW, font=font)

image.save('images/blue&sun&text.jpg')

# Вариант Мастера (Учителя)

# H = 400
#
# image = Image.new('RGB',
#                   (W, H),
#                   (0, 163, 232))
#
# draw = ImageDraw.Draw(image)
#
# text = 'Солнечный день'
# # draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
# draw.circle((600, 0), 100, fill='yellow')
# font = ImageFont.truetype(
#     # font='arial.ttf',  # можно использовать любой установленный шрифт
#     font='fonts/Geisha.ttf',
#     size=50
# )
# # Получаем размеры текста
# _, _, w, h = draw.textbbox((0, 0), text, font=font)
#
# # Рассчитываем позицию для центрирования
# x = (W - w) // 2
# y = (H - h) // 2
#
# draw.text((x, y), text, fill=(255, 255, 0), font=font)
#
# # image.save('images/sunny_day.jpg')
# image.show()
