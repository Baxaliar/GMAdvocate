
def add_element_to_list(element, list_to_add=None):
    """добавляем элемент к списку"""
    if list_to_add is None:
        list_to_add = []
    list_to_add.append(element)
    return list_to_add


# my_list = [3, 4, 5]
# add_element_to_list(element=1, list_to_add=my_list)
# print(my_list)

new_list = add_element_to_list(element=1)
print(new_list)
add_element_to_list(element=7, list_to_add=new_list)
print(new_list)

other_new_list = add_element_to_list(element=2)
print(other_new_list)
print(new_list)
print(other_new_list is new_list)
