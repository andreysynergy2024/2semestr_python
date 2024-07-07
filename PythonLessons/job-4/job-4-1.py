def normalize_input(user_input) -> [str]:
    parts = user_input.split(" ")
    for p in parts:
        yield p.strip()


def to_numbers(numbers: [str]) -> [float]:
    for n in numbers:
        s = n.replace(",", ".")
        yield float(s)


def get_rectangle_area(rect: list[float]) -> float:
    return rect[0] * rect[1]


def get_rectangle_perimeter(rect: list[float]) -> float:
    return rect[0] * 2 + rect[1] * 2


def get_area_and_perimeter_of_a_rectangle():
    user_input = input("Введите 2 стороны прямоугольника (через пробел): ")
    rect = list(to_numbers(normalize_input(user_input)))

    area = get_rectangle_area(rect)
    perimeter = get_rectangle_perimeter(rect)

    print(f"Площадь прямоугольника {area}, периметр {perimeter}.")


if __name__ == "__main__":
    get_area_and_perimeter_of_a_rectangle()