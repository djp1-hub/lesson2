from typing import List

digits_list=input("введите список цифр разделяя пробелами: ").split()
count=len(digits_list) #вычисляем длину
print(digits_list)
print(count, type(count))
if count > 2:
     for i in range(0, count-1, 2):
        digits_list[i], digits_list[i+1] = digits_list[i+1] ,digits_list[i]
print(digits_list)
