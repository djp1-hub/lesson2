my_list = [30, 22, 19, 35, 1, 1, 33, 44, 15]
new = [element for element in my_list if element > my_list[my_list.index(element)-1]]
print(new)


