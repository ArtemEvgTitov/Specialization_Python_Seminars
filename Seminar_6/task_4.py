# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def riddle_game(quest, answers: list, attemps):
    print(f'Загадка: {quest}')
    count = 0
    while count < attemps:
        answer = input('Введите свой ответ: ')
        if answer.lower() in map(str.lower, answers):
            return count + 1
        count += 1
    return 0


if __name__ == '__main__':
    question = 'Сидит дед во сто шуб одет, кто его раздевает, тот слёзы проливает'
    answers_ = ['лук', 'onion']
    result = riddle_game(question, answers_, 3)
    print(f'Вы угадали с {result} попытки' if result != 0 else 'Вы не угадали')