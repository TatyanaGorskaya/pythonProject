MonthsList = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
MonthsDic = {12 : "Зима", 1 : "Зима", 2 : "Зима", 3 : "Весна", 4 : "Весна", 5 : "Весна", 6 : "Лето", 7 : "Лето", 8 : "Лето", 9 : "Осень", 10 : "Осень", 11 : "Осень"}

month = int(input("Введите месяц (от 1 до 12): "))

if(month >= 1 and month <= 12):
    print("\nВремя года:", MonthsList[month-1])
    print("Время года:", MonthsDic[month])
else:
    print("\nОшибка ввода!")
    
