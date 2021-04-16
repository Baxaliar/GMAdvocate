from nim_engine import put_stones, get_bunches, take_from_bunch, gameover


put_stones()
while True:
    print('Текущая позиция')
    print(get_bunches())
    pos = input('Откуда берём?')
    qua = input('Сколько берём?')
    take_from_bunch(position=int(pos), quantity=int(qua))
    if gameover():
        break
