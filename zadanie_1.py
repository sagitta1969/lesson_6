from time import sleep
from itertools import cycle

class TrafficLight:
    __color = [['red',7], ['yellow', 2], ['green', 7], ['yellow', 7]]
    
    def running(self):
        for el in cycle(self.__color):
            for i, val in enumerate(self.__color):
                print(self.__color[i][0])
                sleep(self.__color[i][1])
        
        
        def running_1(self):
            while True:
                print("red")
                sleep(7)
                print("yellow")
                sleep(2)
                print("green")
                sleep(7)
                print("yellow")
                sleep(2)


color_1 = TrafficLight()
color_1.running() 



trafficLight = TrafficLight()
trafficLight.running_1()