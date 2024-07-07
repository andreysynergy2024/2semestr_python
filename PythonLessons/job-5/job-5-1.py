def check_positive(num: float):
    return "положительное" if num > 0.0 else "отрицательное", False


def check_zero(num: float):
    return ("нулевое", True) if num == 0.0 else ("", False)


def check_even(num: float):
    return "четное" if num % 2 == 0.0 else "нечетное", False


number_perks = [check_zero, check_positive, check_even]


def print_number_description():
    """
    Пользователь вводит целое число.
    Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число",
    например, численным описанием числа 190 является строка "положительное четное число".
    Если число не является четным - выведите сообщение "число не является четным"
    """
    number_text = input("Введите число для проверки: ")
    number = float(number_text)

    # пропускать пустую строку
    description_parts = []
    for perk in number_perks:
        text, stop = perk(number)
        description_parts.append(text)
        if stop:
            break

    description = f"{' '.join(description_parts)} число"
    print(description)


if __name__ == "__main__":
    print_number_description()
