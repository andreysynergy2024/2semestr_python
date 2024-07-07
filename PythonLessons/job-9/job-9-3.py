def print_yes_no():
    """
    Во входную строку водится последовательность чисел через пробел. Для
    каждого числа выведите слово ”YES” (в отдельной строке), если это число
    ранее встречалось в последовательности или ”NO”, если не встречалось.
    """

    numbers = list(map(int, input().split(" ")))

    uniq_numbers = set()

    for n in numbers:
        already_exists = n in uniq_numbers
        print(f"{n}={already_exists}")
        uniq_numbers.add(n)


if __name__ == "__main__":
    print_yes_no()