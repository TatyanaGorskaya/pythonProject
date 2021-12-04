S = input("Введите строку из слов с пробелами: ")

Words = list()
Words = S.split()

print("")
i = 1;
for Word in Words:
    print(i, "   ", Word[0:10])
    i += 1
    
