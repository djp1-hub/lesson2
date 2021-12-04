my_f = open('test.txt', 'w')
line = input('Введите текст:')
while line:
    my_f.writelines(line + '\n')
    line = input('Введите текст:')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

