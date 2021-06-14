class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def massa(self, mas_per_sm = 25, sm = 5):
        return self._width * self._length * mas_per_sm * sm

r = Road(20, 5000)
print(r.massa())