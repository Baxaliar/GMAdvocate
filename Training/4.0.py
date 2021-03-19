
# Произвольное число позиционных параметров
def print_them_all_v1(*args):
    print('print_them_all_v1')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)


print_them_all_v1(2, 'привет', 5.6)
