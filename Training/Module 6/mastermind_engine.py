from random import randint


_bulls_cow = {}
user_number = 6686
count = 0


def random_number():
    number = randint(1000, 9999)
    global res
    res = [int(x) for x in str(number)]
    return res


number = random_number()
print(number)


def number_check(usr_number):
    count_cows = 0
    count_bulls = 0
    list_user_number = [int(i) for i in str(usr_number)]

    # print("secret number : " + str(number))
    print("current try: " + str(list_user_number))

    for idx, item in enumerate(number):
        if item in list_user_number:
            if list_user_number.index(item) == idx:
                count_bulls += 1
            else:
                count_cows += 1
    _bulls_cow['cows'] = count_cows
    _bulls_cow['bulls'] = count_bulls
    return _bulls_cow

    print(_bulls_cow)