import math

one = 0
ten = 1
hundred = 2
thousand = 3
ten_thousand = 4


def split_into_number_parts(number_text: str) -> list[float]:
    return [float(number_text[n]) for n in range(len(number_text) - 1, -1, -1)]


def raising_number_of_tens_to_power_of_number_of_units():
    number_text = input("Введите произвольное число: ")

    num = split_into_number_parts(number_text)

    a = math.pow(num[ten], num[one])

    b = a * num[hundred]

    c = b / (num[ten_thousand] - num[thousand])

    print(c)


if __name__ == "__main__":
    raising_number_of_tens_to_power_of_number_of_units()
