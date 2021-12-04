from itertools import cycle, count

def my_count_func(first, last):
    for element in count(first):
        if element > last:
            break
        else:
            print(element)
def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_count_func(first = int(input("enter first number: ")), last = int(input("enter lastr number: ")))
my_cycle_func(my_list = ['конь', 'пес'], iteration = int(input("enter iteration: ")))