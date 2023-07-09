rows = int(input("Введите количество рядов у ёлки: "))
symbol = 1
while rows > 0:
    print(" " * rows, "*" * symbol)
    rows -= 1
    symbol += 2

