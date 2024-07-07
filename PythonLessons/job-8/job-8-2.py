def mutate_array():
    """
    В первую строчку вводится число N (1 ≤ N ≤ 100 000).
    В следующую строку через пробел вводятся N чисел (1 ≤ Ai ≤ 10e9).
    Вам требуется написать метод, который получает на вход массив и изменяет его таким образом,
    чтобы на первом месте стоял последний элемент, на втором - первый, на третьем - второй и т. д.
    Выведите N чисел - измененный массив.
    """

    total_min_value = 1
    total_max_value = 100000

    num_min_value = 1.0
    num_max_value = 10E9

    numbers = []

    total_numbers = int(input("Введите количество чисел: "))
    if total_min_value > total_numbers > total_max_value:
        return

    for i in range(total_numbers):
        num = float(input(f"Число {i}: "))
        if num_min_value <= num <= num_max_value:
            numbers.append(num)

    numbers.insert(0, numbers.pop())

    print(numbers)


if __name__ == "__main__":
    mutate_array()
