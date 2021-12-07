class Road:
    WEIGHT1M2 = 25  # кг/см - вес одного квадратного метра толщиной в 1 см

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, depth):
        return depth * self.WEIGHT1M2 * self._width * self._length


if __name__ == '__main__':
    road_krasnoyarsk_abakan = Road(400000, 6)
    print(road_krasnoyarsk_abakan.weight(5))
    print(road_krasnoyarsk_abakan._length/1000)
    print(road_krasnoyarsk_abakan._width)