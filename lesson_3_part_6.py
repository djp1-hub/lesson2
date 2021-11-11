def int_func(word):
    first = word[0]
    return first.upper() + word[1:]


print(int_func('text'))

user_input = input('input string with spaces: ').split()
result = ''
for i in user_input:
    result += str(int_func(i)) + ' '

print(result)
