# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки
# в числовые параметры используйте генераторное выражение.

from random import randint as rd
import sys


def guess(down=10, up=100, tries=10):
    if down > up:
        down, up = up, down
    aim = rd(down, up)
    count = 0
    while count < tries:
        try:
            temp = int(input('Введите число: '))
        except:
            print('Нужно ввести целое число')
            count += 1
            continue
        if temp < aim:
            print('Число больше')
        elif temp > aim:
            print('Число меньше')
        else:
            return True
        count += 1
    return False


if __name__ == '__main__':
    if len(sys.argv) == 2:
        tries = int(sys.argv[1])
        print(guess(tries=tries)) # python .\Seminar_6\task_3.py 7
    elif len(sys.argv) == 4:
        up, down, tries = (int(i) for i in sys.argv[1:])
        print(guess(up, down, tries)) # python .\Seminar_6\task_3.py 100 10 8
    else:
        print(guess())