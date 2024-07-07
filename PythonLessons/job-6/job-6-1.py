def get_number_of_integers_equal_to_zero():
    """
    Сначала вводится число N, затем вводится ровно N целых чисел.
    Подсчитайте, сколько из них равны нулю, и выведите это количество.
    """

    N = int(input("Введите количество чисел: "))

    numbers = []
    for i in range(N):
        n = int(input("Введите целое число: "))
        numbers.append(n)

    zero_count = 0
    for n in numbers:
        if n == 0:
            zero_count = zero_count + 1

    print(zero_count)


if __name__ == "__main__":
    get_number_of_integers_equal_to_zero()