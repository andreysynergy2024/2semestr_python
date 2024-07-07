import decimal
from math import floor


class CacheRegistry:
    def __init__(self):
        self.amount: decimal = 0.0

    def top_up(self, money: decimal):
        if money <= 0:
            raise ValueError("Недопустимо отрицательное значение")

        self.amount = self.amount + money

    def count_1000(self) -> decimal:
        return floor(self.amount / 1000)

    def take_away(self, money: decimal):
        if money <= 0:
            raise ValueError("Недопустимо отрицательное значение")

        balance = self.amount - money

        if money > self.amount:
            raise ValueError("Привышение доступной суммы!")

        self.amount = balance

    def __str__(self):
        return f"Денег в кассе: {self.amount}"


def cache_register():
    """
    Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
    -top_up(X) - пополнить на X
    -count_1000() - выводит сколько целых тысяч осталось в кассе
    -take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
    """

    cache_registry = CacheRegistry()

    cache_registry.top_up(5000.50)
    print(cache_registry)
    print(f"В кассе {cache_registry.count_1000()} тысяч")
    cache_registry.take_away(4500.0)
    print(cache_registry)
    cache_registry.take_away(0.50)
    print(cache_registry)


if __name__ == "__main__":
    cache_register()
