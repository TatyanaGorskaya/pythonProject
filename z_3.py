def my_func(a, b, c):
    if(a > b):
            if(b > c):
                    return a + b
            else:
                    return a + c
    else:
            return b + c

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

print("\nСумма двух максимальных чисел=", my_func(a, b, c))
