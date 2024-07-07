class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"


class Autobus(Transport):
    def __init__(self):
        super().__init__("Renaul Logan", 180, 12)


def autobus():
    """
    Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
    Ожидаемый результат вывода:
    Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12
    """

    bus = Autobus()

    print(bus)


if __name__ == "__main__":
    autobus()
