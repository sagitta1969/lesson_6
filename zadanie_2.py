class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def calc(self):
        print(f"масса асфальта дороги: {self._lenght * self._width * 5 * 0.025} тн")


def main():
    while True:
        try:
            new_road = Road(int(input("введите ширину дороги в метрах: ")),\
                            int(input("введите длину дороги в метрах: ")))
            new_road.calc()
            break
        except ValueError:
            print("вводить только цифры")

main()
