l = []

i = 0;
while True:
    Val = input("Enter value #" + str(i) + ": ")
    i += 1;
    if Val != "":
        l.append(Val)
    else:
        break

print("\nPrinting original list:")
i = 0
for item in l:
    print("Index=", i, "       Value=", item)
    i += 1

for i in range(0, len(l)):
    if (i % 2) == 1:
        x = l[i - 1]
        l[i - 1] = l[i]
        l[i] = x
    else:
        continue

print("\nPrinting processed list:")
i = 0
for item in l:
    print("Index=", i, "       Value=", item)
    i += 1


