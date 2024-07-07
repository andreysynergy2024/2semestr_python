def get_number_of_divisors(n):
    i = 1
    o = 0
    while i * i <= n:
        if n % i == 0 and i * i != n:
            o += 2
        elif n % i == 0 and i * i == n:
            o += 1
        i += 1
    return o

def get_number_of_natural_divisors():
    """
    Вводится натуральное число X.
    Подсчитайте количество натуральных делителей числа X (включая 1 и само число).
    x ≤ 2e9 (2 миллиарда)
    """

    natural_number = int(input("Ввелите натуральное число: "))

    n = 1
    div = 0
    while n * n <= natural_number:
        if natural_number % n == 0 and n * n != natural_number:
            div = div + 2
        elif natural_number % n == 0 and n * n == natural_number:
            div = div + 1
        n += 1

    print(div)


if __name__ == "__main__":
    get_number_of_natural_divisors()
