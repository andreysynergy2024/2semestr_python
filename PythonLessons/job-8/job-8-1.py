def reverse_number_array():
    """
    В первой строке вводится число N.
    Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке.
    Все числа по модулю не превышают 10e5.
    Переверните массив чисел.
    Выведите N чисел - перевернутый массив.
    """

    max_num_count = 10000
    max_num_value = 10E5

    total_numbers = int(input("Введите количество чисел: "))
    if total_numbers > max_num_count:
        return

    numbers = []
    for i in range(total_numbers):
        num = float(input(f"Число {i}: "))
        if abs(num) <= max_num_value:
            numbers.append(num)

    reversed_numbers = numbers[::-1]

    print(reversed_numbers)


if __name__ == "__main__":
    reverse_number_array()
