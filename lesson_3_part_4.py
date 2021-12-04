def degree(a, b):
    result = 1
    if b < 0:  # через цикл
        while b < 0:
            result = result * a
            b += 1
        print(1 / result)
    elif b > 0:  # через присвоение степени
        a **= b
        print(a)


degree(4, -2)
