from nim_engine import put_stones, get_bunches, take_from_bunch, game_over
from termcolor import cprint, colored

put_stones()
user_number = 1
while True:
    cprint('Расположение камней на игровом поле:', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number),  color=user_color)
    pos = input(colored('Выберите кучку камней:', color=user_color))
    qua = input(colored('Укажите, сколько хотите взять:', color=user_color))
    step_successful = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successful:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', color='red')
    if game_over():
        break


cprint('Выиграл игрок номер {}'.format(user_number), color='red')
