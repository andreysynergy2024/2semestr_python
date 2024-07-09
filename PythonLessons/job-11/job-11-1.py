def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n


def clac_factorial():
    number = int(input("Введите число:"))
    factorials = []
    for n in range(factorial(number), 0, -1):
        f = factorial(n)
        factorials.append(f)

    print(factorials)


if __name__ == "__main__":
    clac_factorial()
