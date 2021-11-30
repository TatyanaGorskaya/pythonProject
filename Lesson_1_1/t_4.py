N = int(input('Please enter number = '))

num = N
length = 0
digit = 0
MaxDigit = 0

while num > 0:
    digit = num - (num // 10) * 10
    if digit > MaxDigit:
             MaxDigit = digit
    length += 1
    num = num // 10

print("Number is:", N, "    Length is:", length, "   The largest digit is:", MaxDigit)
