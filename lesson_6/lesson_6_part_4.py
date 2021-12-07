class Car:
    __speed = 0
    __direction = None

    def __init__(self, speed, color, name, is_police):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = self.__speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        pass

    def show_speed(self):
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class TownCar(Car):
    WARN_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.WARN_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    WARN_SPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.WARN_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    pc = PoliceCar(33, 'yellow', 'e847ae')
    wc1 = WorkCar(60, 'silver', 'k001rk')
    wc2 = WorkCar(66, 'blue', 't333tt')
    sc = SportCar(111, 'white', 'k333kk')
    tc1 = TownCar(43, 'magenta', 'x700oh')
    tc2 = TownCar(61, 'black', 'm791ac')
    pc.show_speed()
    pc.go()
    pc.show_speed()
    pc.stop()
    print(pc.color)
    pc.go()
    print(pc.name)
    wc1.go()
    wc2.go()
    sc.go()
    tc1.go()
    tc2.go()
    wc1.show_speed()
    wc2.show_speed()
    sc.show_speed()
    tc1.show_speed()
    tc2.show_speed()
