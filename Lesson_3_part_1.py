def my_div(arg_1, arg_2):
    if arg_2 == 0:
        return 'Деление на ноль невозможно'
    result = arg_1 / arg_2
    return result


print(my_div(1, 0))
print(my_div(10, 3))

a = float(input('first number: '))
b = float(input('second number: '))
print(my_div(a, b))
