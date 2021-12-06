def MySum(text):
    S = 0
    ErrorCode = 0
    l = text.split()
    for word in l:
            if(word.isdigit()):
                    S += int(word)
            else:
                    ErrorCode = 1
                    break;
    return (S, ErrorCode);

S = 0

while True:
    MS = MySum(input("Введите числа, разделенные пробелами: "))
    S += MS[0]
    print("Сумма чисел равна: ", S)
    if MS[1] != 0:
            print("Завершение программы...")
            break;
