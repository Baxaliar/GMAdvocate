
from random import randint

random_number_list = []


def random_number():
    number = str(randint(1000, 9999))
    for digits in number:
        random_number_list.append(digits)
    a, b, c, d = number[0], number[1], number[2], number[3]
    if a == b or a == c or a == d or b == c or b == d or c == d:
        random_number()
    # print(*random_number_list)  # для упрощения отладки


def number_check():
    print('Компьютер загадал число', 'Введите число, состоящее из 4 различных цифр', sep='\n')
    while True:
        bulls_count = 0
        cows_count = 0
        usr_digits = []
        usr_number = input()
        a, b, c, d = usr_number[0], usr_number[1], usr_number[2], usr_number[3]
        if a == b or a == c or a == d or b == c or b == d or c == d:
            number_check()
        if usr_number.isdigit() and len(usr_number) == 4:
            for digits in str(usr_number):
                usr_digits.append(digits)
            for i in range(4):
                if usr_digits[i] in random_number_list:
                    if usr_digits[i] == random_number_list[i]:
                        bulls_count += 1
                        continue
                    cows_count += 1
            # print(*usr_digits)  # для упрощения отладки
            if bulls_count != 4:
                print(f'Быков: {bulls_count}, Коров: {cows_count}', 'Введите новое число: ', sep='\n')
            else:
                print('Вы угадали, желаете повторить?')
                decision = input('Да, Нет: ')
                if decision.lower() == 'да':
                    game()
                elif decision.lower() == 'нет':
                    print('Спасибо за игру! До свидания!')
                    break
                else:
                    print('Ответ неясен, игра завершена')
                    break
        else:
            print('Введите число, состоящее из 4 различных цифр')


def game():
    random_number()
    number_check()
