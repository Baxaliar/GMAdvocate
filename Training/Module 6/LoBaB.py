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
            print('{} нет еды'.format(self.name))

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += 50
        self.fullness -= 10

    def play_dota(self):
        cprint('{} играл в доту целый день'.format(self.name), color='cyan')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='green')
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги кончились'.format(self.name))

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='grey')

    def act(self):
        if self.fullness <= 0:
            print('{} умер'.format(self.name))
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
            self.play_dota()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме - {} еды,  денег - {}.'.format(self.food, self.money)


def life_of_beavis_and_butthead():
    beavis = Man(name='Бивис')
    butthead = Man(name='Баттхед')
    mad_house = House()
    beavis.go_into_house(mad_house)
    butthead.go_into_house(mad_house)
    for day in range(1, 366):
        if beavis.alive and butthead.alive:
            cprint('============== день {} =============='.format(day), color='yellow')
            beavis.act()
            butthead.act()
            print(beavis, butthead, mad_house, sep='\n')
        elif beavis.alive:
            cprint('============== день {} =============='.format(day), color='yellow')
            beavis.act()
            print(beavis, '{} умер!'.format(butthead.name), mad_house, sep='\n')
        elif butthead.alive:
            cprint('============== день {} =============='.format(day), color='yellow')
            beavis.act()
            cprint(butthead, '{} умер!'.format(beavis.name), mad_house, sep='\n', color='red')
        else:
            cprint('Не будь как {} и {}!'.format(beavis.name, butthead.name), color='red')
            break


life_of_beavis_and_butthead()
