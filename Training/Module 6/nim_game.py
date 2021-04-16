from nim_engine import put_stones, get_bunches, take_from_bunch, gameover


put_stones()
user_number = 1
while True:
    print('Текущая позиция')
    print(get_bunches())
    print('Ход игрока {}'.format(user_number))
    pos = input('Откуда берём?')
    qua = input('Сколько берём?')
    take_from_bunch(position=int(pos), quantity=int(qua))
    if gameover():
        break
    user_number = 2 if user_number == 1 else 1
