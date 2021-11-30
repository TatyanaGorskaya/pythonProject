Revenue = int(input('Выручка = '))
Costs = int(input('Издержки = '))
print('')

Profit = Revenue - Costs

if Profit >= 0:
    print('Ура! Прибыль!')
else:
    print('Печаль, убыток...')
