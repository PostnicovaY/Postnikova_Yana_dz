import re


class Complex:
    def __init__(self, a, b):
        self.re = float(a)
        self.im = float(b)

    def __str__(self):
        return f'{self.re}{("+", "")[self.im < 0]}{self.im}i'

    def __add__(self, other):
        repart = self.re + other.re
        impart = self.im + other.im
        return Complex(repart, impart)

    def __mul__(self, other):
        repart = self.re * other.re - self.im * other.im
        impart = self.re * other.im + self.im * other.re
        return Complex(repart, impart)


c1 = Complex(1,1)
c2 = Complex(1,-1)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)