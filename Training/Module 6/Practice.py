
def func_3():
    global x
    x = 'LOCO'
    print('x in f1 =', x)


print(globals())
func_3()
print(x)
print(globals())
