import math


def create_dictionary_with_numbers():
    """
    С помощью цикла создайте словарь, в котором ключи будут, например от числа 10, до -5 (включительно).
    А значениями этих ключей будут сами эти числа возведённые в степени равных этим числам
    """

    numbers = {}
    for n in range(10, -5 - 1, -1):
        numbers[n] = math.pow(n, n)

    print(numbers)


if __name__ == "__main__":
    create_dictionary_with_numbers()