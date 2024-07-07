class Turtle:
    def __init__(self):
        self.speed = 1
        self.x = 0
        self.y = 0

    def go_up(self):
        self.y = self.y + self.speed
        self.print_pos()

    def go_down(self):
        self.y = self.y - self.speed
        self.print_pos()

    def go_left(self):
        self.x = self.x - self.speed
        self.print_pos()

    def go_right(self):
        self.x = self.x + self.speed
        self.print_pos()

    def evolve(self):
        self.speed = self.speed + 1

    def degrade(self):
        if self.speed <= 1:
            return

        self.speed = self.speed - 1

    def count_moves(self, x2: int, y2: int) -> int:
        return abs(self.x - x2) // self.speed + abs(self.y - y2) // self.speed

    def print_pos(self):
        print(f"[{self.x}, {self.y}]")


def turtle():
    """
    Создайте класс Черепашка, который хранит позиции x и y черепашки, а также
    s - количество клеточек, на которое она перемещается за ход
    """

    t = Turtle()
    t.go_up()
    t.go_up()

    length = t.count_moves(9, 4)
    print(length)


if __name__ == "__main__":
    turtle()
