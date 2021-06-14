class Stationery:
    def __init__(self, title="Воллшебный палочка"):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Маркером')

a = [
    Stationery(),
    Pen(),
    Pencil(),
    Handle()
]

for el in a:
    el.draw()