
from random import randint

random_number_list = []
running = True


def random_number():
    number = randint(1000, 9999)
    for digits in str(number):
        random_number_list.append(digits)
    print(*random_number_list)  # для отладки


def number_check():
    print('Введите число, состоящее из 4 цифр')
    while running:
        bulls_count = 0
        cows_count = 0
        usr_digits = []
        usr_number = input()
        if usr_number.isdigit() and len(usr_number) == 4:
            for digits in str(usr_number):
                usr_digits.append(digits)
            for i in range(4):
                if usr_digits[i] in random_number_list:
                    if usr_digits[i] == random_number_list[i]:
                        bulls_count += 1
                        continue
                    cows_count += 1
            print(*usr_digits)  # для отладки
            if bulls_count != 4:
                print(f'Быков: {bulls_count}, Коров: {cows_count}')
            else:
                print('Вы угадали, желаете повторить?')
                decision = input('Да, Нет: ')
                if decision.lower() == 'да':
                    game()
                elif decision.lower() == 'нет':
                    break
                else:
                    print('Ответ неясен, игра завершена')
                    break
        else:
            print('Введите число, состоящее из 4 цифр')


def game():
    random_number()
    number_check()
