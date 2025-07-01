# Словари
# Частотный анализ

res = {} # пустой словарь для последующего ввода частотного анализа

text = """Планируют перенести выходной на 9 января,
чтобы в связи с новогодними каникулами отдыхать 12 дней подряд.
Хотят также сделать днем отдыха 31 декабря 2026 года (четверг).
Это возможно благодаря переносу выходных с 3 и 4 января (суббота и воскресенье).
"""

commas = (',', '(', '.', ')')
for x in commas:
    text = text.replace(x, '')

lst = sorted(text.strip().lower().split())

for item in lst:
    if item in res.keys():
        res[item] += 1
    else:
        res[item] = 1

print('Частотный анализ текста')
for k, v in res.items():
    print(f'\t{k}: {v}')




# """ Методы словаря
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# """


