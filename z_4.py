def my_func(x, y, mode=0):
    if (mode == 0):
        return x ** y
    else:
        p = 1 / x
        for i in range(y, -1):
            p /= x
        return p


print("Проверка варианта 1. x = 10, y = -3", my_func(10, -3))
print("Проверка варианта 2. x = 10, y = -3", my_func(10, -3, 1))
