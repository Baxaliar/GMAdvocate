
from Game_engine import *

random_number()
number_check()

print(f'Вы угадали за {moves_count} ходов, желаете повторить?')
decision = input('Да, Нет: ')
if decision.lower() == 'да':
    random_number_list.clear()  # Обязательная очистка загаданного числа
    game()
elif decision.lower() == 'нет':
    print('Спасибо за игру! До свидания!')
    exit()
else:
    print('Ответ неясен, игра завершена')
    exit()
