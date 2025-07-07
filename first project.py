# Внешние библиотеки
# Документы по шаблону (из методичек https://disk.yandex.ru/d/9HNsXg77_qeidg
# скачать файл template.docx)
# установка шаблона template.docx (pip install docxtpl)
# установка библиотеки Excel (pip install openpyxl)
# Word - DOCX (pip install python-docx)
# Word - DOCX (pip install docxtpl)
# pip freeze > requirements.txt - создание файла зависимости (замораживаем список библиотеки)
# pip install -r requirements.txt - установка списка библиотек
# RGB - растровое изображение (цвета пикселя)
# thumbnail "большой палец"

# Запись данных в существующий файл
from openpyxl import  load_workbook # импортируем модуль для записи в файл .xlsx
# Открываем (загружаем) рабочую книгу
wb = load_workbook('docs/report.xlsx')

# Активный лист
ws = wb.active
#ws = wb['Отчёт'] # можно присвоить переменному операнду имя

# Создаём Заголовки
ws['A1'] = 'ФИО'
ws['B1'] = 'Должность'
ws['C1'] = 'Отдел'

# создаём Данные
employees = [
    ['Иванов И.И.', 'Менеджер', 'Продажи'],
    ['Петров П.П.', 'Бухгалтер', 'Финансы'],
    ['Сидоров С.С.', 'Аналитик', 'IT']
]

for row, data in enumerate(employees, start=2):
    ws.cell(row=row, column=1, value=data[0])
    ws.cell(row=row, column=2, value=data[1])
    ws.cell(row=row, column=3, value=data[2])

# Способы записи
# ws['F1'] = 'Привет мир' # первый вариант записи (в ячейку с адресом F1)
# ws.cell(1, 3, 'Hello') # второй вариант записи (по номеру строки и столбца ячейки)

wb.save('docs/newtable.xlsx')

# # Пустой файл Exel
# from  openpyxl import Workbook
#
# wb = Workbook() # создаем конструктор
#
# ws = wb.active # создаем пустой документ
# ws.title = 'Отчёт' # присваиваем имя документу
#
# wb.save('docs/report.xlsx')


# from docxtpl import DocxTemplate # извлекаем модуль для загрузки шаблона документа
#
# from main import count
#
# # Загрузка шаблона
# doc = DocxTemplate('docs/template.docx')
#
# # Данные для подстановки в шаблон
# content = {
#     'company': 'ООО "Монолит"',
#     'employee': 'Петров Д.И.',
#     'position': 'Менеджер',
#     'date': '01/01/2025'
# }
#
# count = 1
# for item in content:
#     doc.render(item)
#     doc.save(f' {}')
#
#
# doc.render(content) # шаблон для формирования отчётов
# doc.save('docx/about.docx')

# from docx import Document
# from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_ALIGN_PARAGRAPH
# from docx.shared import Cm, Inches, Mm, Pt # Для размеров
#
# doc = Document() # создание экземпляра документа
#
# # Добавление заголовка
# doc.add_heading('Отчёт за месяц', 1)
# paragraph = doc.add_paragraph() # создаем с нового абзаца (как клавиша "ввод")
# paragraph = doc.add_paragraph('В этом отчёте представлены')
# # add_run прием: внедряет что-то в созданный абзац (может быть не только текст, но и картинка)
# paragraph.add_run(' ключевые показатели').bold = True
# # Новый абзац для списка
# paragraph = doc.add_paragraph()
# paragraph_format = paragraph.paragraph_format # форматирование параграфа
# paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
# #
# paragraph = doc.add_paragraph('Первый пункт', 'List Bullet')
# paragraph = doc.add_paragraph('Второй пункт', 'List Bullet')
# #
# paragraph = doc.add_paragraph('Первый пункт', 'List Number')
# paragraph = doc.add_paragraph('Второй пункт', 'List Number')
#
# paragraph = doc.add_paragraph()
#
# table = doc.add_table(3, cols=3)
#
# for i, row in enumerate(table.rows):
#     for j, cell in enumerate(table.cells):
#         cell.txt = f'Строка {i+1}, Столбец {j+1}'
#
# doc.add_paragraph()
#
# doc.add_picture('image/blue.jpg', width=Mm(10))


# doc.save('docs/report.docx')

# from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
#
# orig = Image.open('images/python.jpg').convert('RGB') # на всякий случай конвертируем в формат RGB
# размытие
# blue_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# blue_image.show()

# Усиление разкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image = enchancer.enchance(4.0)
# sharpened_image.show()



