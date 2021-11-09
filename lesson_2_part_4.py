list=input('Введите предложение: ').split()
count=1
for i in list:
    print(f"{count}. {i[0:10]}")
    count=count+1
