# Сдаем карты
cards = {3, 7, 'туз', 'валет', 'король', 'дама'}

# 1 вариант

ace = {'туз'}
result = cards - ace
print(result)

# 2 вариант

t_is = False

while cards:
    card = cards.pop() # удаленный элемент, карта которую случайным образом сдали из колоды cards
    if card == 'туз':
        cards.add(card) # возврат карты в колоду, если это туз
        t_is = True
    else:
        print(card)

    if t_is and len(cards) == 1:
        break



