def int_func(string):
    s = string.capitalize()
    return s


S = input("Введите список слов: ")
l = S.split()
Result = ""
for word in l:
    word = int_func(word)
    Result += (word + " ")

print(Result)
