class Car:
    ''' автомобиль '''
    _speed = None
    _color = None
    _name = None
    _is_polis = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'Новая машина: {self.name} (цвет {self.color}) {type(self)}')

    def go(self):
        print(f'{self.name}: машина поехала.')

    def stop(self):
        print(f'{self.name}: машина остановилась.')
    
    def turn(self, diretion):
        print(f'{self.name}: машина повернула - {"налево" if diretion == 0 else "направо"}')
    
    def show_speed(self, speed):
        print(f'{self.name}: скрость: {speed}')

class TownCar(Car):
    '''городской автомобиль'''
    def show_speed(self, speed):
        if speed > 60:
            print(f'{self.name}: скорость автомобиля: {speed}. превышение')
        else:
            super().show_speed(speed)

class WorkCar(Car):
    '''Грузовой автомобиль'''
    def show_speed(self, speed):
        if speed > 40:
            print(f'{self.name}: скорость автомобиля: {speed}. превышение')
        else:
            super().show_speed(speed)

class SportCar(Car):
    '''спортивный автомобиль'''
    def show_speed(self, speed):
        if speed > 120:
            print(f'{self.name}: скорость автомобиля: {speed}. превышение')
        else:
            super().show_speed(speed)

class PolisCar(Car):
    '''Полицейский автомобиль'''
    def __init__(self, name, color):
        super().__init__(name, color)
        self._is_polis = True

police_car = PolisCar("Полицейский", "белый")
police_car.go()
police_car.show_speed(80)
police_car.turn(0)
police_car.stop
print()


worc_car = WorkCar("грузовик", "черный")
worc_car.go()
worc_car.turn(1)
worc_car.show_speed(40)
worc_car.turn(0)
worc_car.show_speed(60)
worc_car.stop()
print()

sport_car = SportCar("спртивная", "красный")
sport_car.go()
sport_car.turn(0)
sport_car.show_speed(120)
sport_car.stop()
print()

town_car = TownCar("маленькая", "синяя")
town_car.go()
town_car.show_speed(50)
town_car.turn(1)
town_car.turn(0)
town_car.show_speed(70)
town_car.stop()
print()

print(f'машина {town_car.name} (цвет {town_car.color})')
print(f'машина {sport_car.name} (цвет {sport_car.color})')