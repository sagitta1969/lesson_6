from time import sleep
from itertools import cycle

class TrafficLight:
    __color = [['red',7], ['yellow', 2], ['green', 7], ['yellow', 7]]     
        
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


trafficLight = TrafficLight()
trafficLight.running_1()
