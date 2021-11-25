from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    benefit = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Input time work: "))
    rate = int(input("Input rate: "))
    benefit = int(input("Input benefit: "))
    print((time_work * rate) + benefit)