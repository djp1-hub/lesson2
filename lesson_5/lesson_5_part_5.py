filename = "task5.txt"

dig_string = "1.2 8.6 34.65 456 67 4574578"

summ = 0

try:
    with open(filename, 'w') as fhs:
        fhs.write(dig_string)

    with open(filename, 'r') as fhd:
        data = fhd.read()

    for item in data.split():
        summ += float(item)
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print(summ)
