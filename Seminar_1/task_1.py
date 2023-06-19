num = int(input("Введите год: "))

if num < 1582:
    res = "Нет календаря"
elif num % 4 != 0 or num % 100 == 0 and num % 400 != 0:
    res = "Обычный"
else:
    res = "Високосный"

print(res)