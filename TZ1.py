class Matrix:
    def __init__(self, matr):
        self.data = matr
        width = 0
        for row in matr:
            if len(row) > width:
                width = len(row)

        for row in self.data:
            if len(row) < width:
                for i in range(len(row), width):
                    row.append(0)

    def print_matrix(self):
        for row in self.data:
            s = ''
            for el in row:
                s += f'{el}  '
            print(s)


example = [
    [1, 2, 3],
    [4, 5],
    [7, 8, 9, 8]
]
M = Matrix(example)
M.print_matrix()
