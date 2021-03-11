
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


res = vector_module(2, y=3, z=4)
print(res)

# some_list = [2, 3, 4]
# res = vector_module(*some_list)
# print(res)

some_list = [2, 3]
some_dict = dict(z=4)
res = vector_module(*some_list, **some_dict)
print(res)
