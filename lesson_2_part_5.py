start = [100, 10, 5, 5, 2]
a=0
while a < 5:
    print('наша последовательность', start)
    i = int(input("Введите число: "))
    if i > max(start):
        start.insert(0,i)
    elif i in start:
        c = start.count(i)
        start.insert(start.index(i)+c, i)
    elif i < min(start):
        start.append(i)
    else:
        for m in start:
            if m < i:
                index = start.index(m) #
                start.insert(index, i)
                break
    a+=1
    print(start)
