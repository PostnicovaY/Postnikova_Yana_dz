class Car:
    def init_default(self, speed, color, name):
        self.name = name
        self.color = color
        self.speed = speed

    def __init__(self, speed = 0, color = "black", name = "Drandulet"):
        self.init_default(speed, color, name)
        self.is_police = False

    def output_all(self):
        print(self.name)
        print(self.color)
        print(self.speed)
        print(self.is_police)

    def go(self):
        self.speed = 30
        print("Машина поехала")

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed=0):
        self.init_default(speed, "Черно-белая", "Nissan")
        self.is_police = True

class SportCar(Car):
    pass

car1 = TownCar()
car2 = SportCar()
car3 = WorkCar()
car4 = PoliceCar()

car4.output_all()
car3.go()
car2.stop()
car1.speed = 80
car1.show_speed()