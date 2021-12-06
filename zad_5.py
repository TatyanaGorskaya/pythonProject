L = [7, 5, 3, 3, 2]

n = int(input("Введите число: "))

if n <= L[-1]:
    L.append(n)
else:
    for i in range(0, len(L)):
            if n >= L[i]:
                    L.insert(i, n)
                    break

print("\n", L)
