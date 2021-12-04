Revenue = int(input('Выручка = '))
Costs = int(input('Издержки = '))
print('')

Profit = Revenue - Costs

if Profit >= 0:
    print('Ура! Прибыль!')
    Profitability = Profit / Revenue
    Employees = int(input('Введите количество сотрудников: '))
    ProfitPerHead = Profit / Employees
    print('Рентабельность выручки=', Profitability, '    Прибыль на сотрудника=', ProfitPerHead)

else:
    print('Печаль, убыток...')
