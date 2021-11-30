a = int(input('Введите параметр a: '))
b = int(input('Введите параметр b: '))

day = 1
result = float(a)

while result < b:
    result = result * 1.1
    day += 1

print('')
print('Результат достигнут на:', day, 'день')
