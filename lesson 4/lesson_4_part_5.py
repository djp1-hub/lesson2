from functools import reduce
generate_list = [a for a in range(100,1001) if a % 2 == 0]
sum = reduce((lambda x, y: x * y), generate_list)
print(sum)