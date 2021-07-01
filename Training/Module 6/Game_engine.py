
from random import randint

res, moves_count, number, bulls_cow = 0, 0, 0, {}
random_number_list = []
res = 0


def random_number():  # Генератор случайного хххх числа с неповторяющимися цифрами
    global number
    number = str(randint(1000, 9999))
    a, b, c, d = number[0], number[1], number[2], number[3]  # Проверка не повторяются ли цифры в числе
    if a == b or a == c or a == d or b == c or b == d or c == d:
        random_number()
    else:
        for digits in number:
            random_number_list.append(digits)
        print(*random_number_list)  # для упрощения отладки


def number_check():  # Проверка числа, введённого игроком и подсчёт Быков/Коров
    global bulls_cow
    print('Компьютер загадал число', 'Введите число, состоящее из 4 различных цифр', sep='\n')
    while True:
        bulls_count = 0
        cows_count = 0
        usr_digits = []
        usr_number = input()
        if usr_number.isdigit() and len(usr_number) == 4:
            a, b, c, d = usr_number[0], usr_number[1],\
                         usr_number[2], usr_number[3]  # Проверка наличия повторяющихся цифр
            if a == b or a == c or a == d or b == c or b == d or c == d:
                number_check()
            for digits in str(usr_number):
                usr_digits.append(digits)
            for i in range(4):
                if usr_digits[i] in random_number_list:
                    if usr_digits[i] == random_number_list[i]:
                        bulls_count += 1
                        bulls_cow = {'Быков': bulls_count, 'Коров': cows_count}
                        continue
                    cows_count += 1
                    global moves_count
                    moves_count += 1
                    bulls_cow = {'Быков': bulls_count, 'Коров': cows_count}
                    global res
                    res = moves_count
            # print(*usr_digits)  # для упрощения отладки
            if bulls_count != 4:
                # print(f'Быков: {bulls_count}, Коров: {cows_count}', 'Введите новое число: ', sep='\n')  # Для
                # десктопной версии программы
                print(bulls_cow)
            else:
                break
        else:
            print('Введите число, состоящее из 4 различных цифр')
