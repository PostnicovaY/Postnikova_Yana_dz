class Kletka:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Kletka(self.number + other.number)

    def __sub__(self, other):
        result = self.number - other.number
        if result < 0:
            raise ValueError
        else:
            return Kletka(result)

    def __mul__(self, other):
        return Kletka(self.number * other.number)

    def __floordiv__(self, other):
        return Kletka(self.number // other.number)

    def __truediv__(self, other):
        return Kletka(self.number // other.number)

    def make_order(self,n):
        for j in range(self.number // n):
            print(''.join('*' for i in range(n)))
        print(''.join('*' for i in range(self.number % n)))

k = Kletka(9)
k.make_order(4)