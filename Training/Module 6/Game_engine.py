
from random import randint

random_number_list = []
bulls_count = 0
cows_count = 0


def random_number():
    number = randint(1000, 9999)
    for digits in str(number):
        random_number_list.append(digits)


def number_check(usr_number):
    usr_number = input()
    pass
