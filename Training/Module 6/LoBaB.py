from random import randint

from termcolor import cprint


class Human:

    def __init__(self, name):
        self.house = None
        self.name = name
        self.fullness = 50
        self.alive = True

    def __str__(self):
        return 'Я - {}, сытость {}.'.format(self.name, self.fullness)

    def eat(self):
        if self.house.fridge.food >= 10:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 10
            self.house.fridge.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.nightstand.money += 150
        self.fullness -= 10

    def shuffle_cards(self):
        cprint('{} тасовал карты'.format(self.name), color='cyan')
        self.fullness -= 10

    def shopping(self):
        if self.house.nightstand.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='green')
            self.house.nightstand.money -= 50
            self.house.fridge.food += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='grey')

    def act(self):
        if self.fullness <= 0:
            self.alive = False
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.fridge.food < 10:
            self.shopping()
        elif self.house.nightstand.money < 10:
            self.work()
        elif self.house.cat_food < 10:
            self.shopping_for_cat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.shuffle_cards()

    def get_cat(self, cat):
        self.house.cat = cat
        self.house.cat_bowl = CatBowl()
        self.house.cat_food = 0
        cprint('{} въехал в дом'.format(self.house.cat.name), color='grey')

    def shopping_for_cat(self):
        if self.house.nightstand.money >= 50:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='green')
            self.house.nightstand.money -= 50
            self.house.cat_bowl.food += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20


class Cat:

    def __init__(self, name):
        self.house = None
        self.name = name
        self.fullness = 50
        self.alive = True
        self.food = None

    def __str__(self):
        return 'Я - {}, сытость {}.'.format(self.name, self.fullness)

    def sleep(self):
        self.fullness -= 10

    def fun(self):
        if self.fullness <= 0:
            self.alive = False
            return
        else:
            self.fullness -= 10
            self.house.dirt += 5


class House:

    def __init__(self, cat):
        self.fridge = None
        self.nightstand = None
        self.cat = cat
        self.cat_food = 0
        self.dirt = 0
        self.cat_bowl = None

    def __str__(self):
        return 'В доме - {} еды,  денег - {}, кошачьей еды - {}, грязи - {}'.format(
            self.fridge.food, self.nightstand.money, self.cat_food, self.dirt)


class Fridge:

    def __init__(self):
        self.food = 10


class CatBowl:

    def __init__(self):
        self.cat = None
        self.food = 0


class Nightstand:

    def __init__(self):
        self.money = 50


inhabitants = [
    Human(name='Мэдисон'),
    Human(name='Алан'),
    Human(name='Уильямс'),
    Human(name='Мэган')
]
cats = [

    Cat(name='Тень')
]


def life_of_mad_house():
    mad_house = House(cat=None)
    mad_house.fridge = Fridge()
    mad_house.nightstand = Nightstand()
    print(mad_house)
    for inhabitant in inhabitants:
        inhabitant.go_into_house(mad_house)
    for cat in cats:
        inhabitants[randint(1, len(inhabitants))].get_cat(cat)
    mad_house.cat_bowl = CatBowl()
    print(mad_house)
    for day in range(1, 366):
        total_corpses = 0
        corpses_list = []
        cprint('============== день {} =============='.format(day), color='blue', attrs=['reverse'])
        for inhabitant in inhabitants:
            if inhabitant.alive:
                inhabitant.act()
            elif not inhabitant.alive:
                cprint('======================================', color='yellow')
                total_corpses += 1
                cprint('{} умер'.format(inhabitant.name), color='red')
                if total_corpses == len(inhabitants):
                    print('Не будь как', end=' ')
                    for corpse in inhabitants:
                        corpses_list.append(corpse.name)
                    print(*corpses_list, sep=', ', end='!')
                    exit()
        cprint('=============в конце дня==============', color='yellow')
        for inhabitant in inhabitants:
            if inhabitant.alive:
                print(inhabitant)
        cprint('================в доме================', color='yellow')
        print(mad_house)


life_of_mad_house()
