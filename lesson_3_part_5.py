def sum_func():
    result=0
    while True:
        list = input("введите числа через пробел, для завершения введите s: ").split()
        for i in list:
            if i != 's':
                result += int(i)
            else:
                break
        print(result)
        if list.count('s') > 0:
            exit()


sum_func()

