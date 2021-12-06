def Div(a, b):
    if (b != 0):
        return a / b
    else:
        return "ERROR"


a = float(input("Введите число: "))
b = float(input("Введите делитель: "))

print("\nРезультат деления: ", Div(a, b))
