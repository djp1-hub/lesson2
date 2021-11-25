from itertools import count
from math import factorial

a = int(input('input numer: '))

def fact():
    for el in count(1):
        yield factorial(el)

gen = fact()
x = 0
for i in gen:
    if x < a:
        print(i)
        x += 1
    else:
        break