class Palto:
    def __init__(self, v):
        self.v = v

    def rashod(self):
        return self.v / 6.5 + 0.5


class Costume:
    def __init__(self, h):
        self.h = h

    def rashod(self):
        return self.h * 2 + 0.3
