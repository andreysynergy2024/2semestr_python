def get_all_even_numbers_on_a_given_interval():
    """
    Вводятся целые числа A и B.
    Гарантируется, что A ≤ B.
    Выведите все четные числа на заданном отрезке через пробел.
    """

    a = int(input("Введите нижнюю границу интервала:"))
    b = int(input("Введите верхнюю границу интервала:"))

    if a > b:
        return

    for n in range(a, b):
        if n % 2 == 0:
            print(n, end=" ")


if __name__ == "__main__":
    get_all_even_numbers_on_a_given_interval()