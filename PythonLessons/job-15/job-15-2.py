class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus(Transport):
    def __init__(self):
        super().__init__("Renaul Logan", 180, 12)

    def seating_capacity(self, capacity: int = 50):
        return super().seating_capacity(capacity)


def autobus():
    """
    Создайте класс Autobus, который наследуется от класса Transport.
    Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
    И спользуйте переопределение метода.
    Ожидаемый результат вывода:
    Вместимость одного автобуса Renaul Logan: 50 пассажиров
    """

    bus = Autobus()

    print(bus.seating_capacity())


if __name__ == "__main__":
    autobus()
