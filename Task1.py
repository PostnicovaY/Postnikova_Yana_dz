import time

class TrafficLight:
    def running(self, green_time = 5):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(green_time)

t = TrafficLight()
t.running(3)