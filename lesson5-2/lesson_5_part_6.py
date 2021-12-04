filename = "task6.txt"

subjects = {}

try:
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print(subjects)
