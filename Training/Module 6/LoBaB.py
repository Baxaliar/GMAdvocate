from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.house = None
        self.name = name
        self.fullness = 50
        self.alive = True

    def __str__(self):
        return 'Я - {}, сытость {}.'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += 50
        self.fullness -= 10

    def shuffle_cards(self):
        cprint('{} тасовал карты'.format(self.name), color='cyan')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='green')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='grey')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер'.format(self.name), color='red')
            self.alive = False
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 10:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.shuffle_cards()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме - {} еды,  денег - {}.'.format(self.food, self.money)


def life_of_madison_and_holmes():
    daniel_madison = Man(name='Мэдисон')
    alan_tcb = Man(name='Алан')
    mad_house = House()
    print(daniel_madison, alan_tcb, mad_house, sep='\n')
    daniel_madison.go_into_house(mad_house)
    alan_tcb.go_into_house(mad_house)
    for day in range(1, 366):
        cprint('============== день {} =============='.format(day), color='yellow')
        if daniel_madison.alive and alan_tcb.alive:
            daniel_madison.act()
            alan_tcb.act()
            cprint('======================================', color='yellow')
            print(daniel_madison, alan_tcb, mad_house, sep='\n')
        elif daniel_madison.alive:
            daniel_madison.act()
            cprint('======================================', color='yellow')
            print(daniel_madison, '{} умер!'.format(alan_tcb.name), mad_house, sep='\n')
        elif alan_tcb.alive:
            daniel_madison.act()
            cprint('======================================', color='yellow')
            cprint(alan_tcb, '{} умер!'.format(daniel_madison.name), mad_house, sep='\n', color='red')
        else:
            cprint('Не будь как {} и {}!'.format(daniel_madison.name, alan_tcb.name), color='red')
            break


life_of_madison_and_holmes()
