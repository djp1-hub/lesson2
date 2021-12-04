origin_list = [3, 4,4, 7, 21, 1, 11, 11, 33, 12, 11, 70, 70, 11]
my_list = [a for a in origin_list if origin_list.count(a) == 1]
print(my_list)