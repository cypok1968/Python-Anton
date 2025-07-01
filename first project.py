# # ДЗ 30.06.25
#
# # преобразовать фразу "Полна неожиданностей улица. Под глазом фонарь. К чаю аптека. Аптека. Улица. Фонарь. А.Блок."
# # в соответствии со стоп листом вывести исходный текст (собрать исходный список), текст без слов из стоп листа, пронумероанные
# # оставшиеся слова в алфавитном порядке, без повтора и пронумерованные
#
# result = [] # создаем пустой список для элементов искомого текста
#
# #Вводим фразу: Полна неожиданностей улица. Под глазом фонарь. К чаю аптека. Аптека. Улица. Фонарь. А.Блок.
# text = input('Введите строку изначальной фразы: ').strip().lower()
# stop_list = ['полна', 'неожиданностей', 'под', 'глазом', 'к', 'чаю'] # ввод запрещённых слов
#
# lst = text.split() # удаление пробелов
# list = list (set(lst)) # удаление повторов
#
# result = [item for item in list if item not in stop_list]
# # вывод 3 списков со словами в алфавитном порядке, пронумерованными и без повторов
# print(f'Изначальная фраза содержит список из {len(list)} слов и знаков: ')
# list.sort()
# for i in range(len(list)):
#     print(f'\t{i+1}. {list[i]}')
# print(f'Запрещённый текст содержит список из {len(stop_list)} слов и знаков: ')
# list.sort()
# for i in range(len(stop_list)):
#     print(f'\t{i+1}. {stop_list[i]}')
# print(f'Исходный текст содержит список из {len(result)} слов и знаков: ')
# result.sort()
# for i in range(len(result)):
#     print(f'\t{i+1}. {result[i]}')
from main import message

# list = set (lst)
# while (text := input('Введите сообщение: ')) != '':
#     lst = text.split()
# for item in list:
#     if item not in stop_list:
#         list.append(item)
# res = sorted(temp)
# for a, b in enumerate(res, 1):
#     print(f'{a}. {b}')
# commas = (',', '!', '.', '?', '-', ':')
# text = input('Введите строку изначальной фразы: ').strip().lower()
# stop_list = ['полна', 'неожиданностей', 'под', 'глазом', 'к', 'чаю'] # ввод запрещённых слов
# for z in commas:
#     text = text.replace(z, _new:)
# lst = text.split()
# result = sorted(set(lst) - stop_list)
# for a, b in enumerate(result, 1):
#     print(f'{a}. {b}')
