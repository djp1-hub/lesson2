class Matrix:
    def __init__(self, ar_of_ar):
        len_of_matrix = len(ar_of_ar[0])
        for ar in ar_of_ar:
            if not len(ar) == len_of_matrix:
                print(f'Передан массив массивов разных длин.')
                raise ValueError
        self._data = ar_of_ar

    def __str__(self):
        result = f'Matrix\n(\t' + f'\t)\n(\t'.join(f', '.join(str(x) for x in line) for line in self._data) + f'\t);'
        return result

    def __add__(self, other):
        len_of_matrix = len(self._data[0])
        hig_of_matrix = len(self._data)
        if not (len_of_matrix == len(other._data[0]) and hig_of_matrix == len(other._data)):
            print("К сложению принимаются матрицы одинаковых размеров.")
            raise ValueError
        result = [[self._data[y][x] + other._data[y][x] for x in range(len_of_matrix)]
                  for y in range(hig_of_matrix)]
        return Matrix(result)


if __name__ == '__main__':
    # m = Matrix([[], [1], []])
    m = Matrix([[], [], []])
    m2 = Matrix([[3, 45], [65, 76], [523, 16]])
    m_2 = Matrix([[12, -11], [87, 53], [-54, -16]])

    print(m)
    print(m2)

    m3 = m2 + m_2
    print(m3)