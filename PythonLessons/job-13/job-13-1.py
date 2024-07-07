import random
from pprint import pprint


def create_matrix(width: int, height: int, init_func) -> [[]]:
    return [[init_func() for _ in range(width)] for _ in range(height)]


def create_random_matrix(width: int, height: int, upper: int = 0, lower: int = 9) -> [[]]:
    return create_matrix(width, height, lambda: random.randrange(upper, lower))


def multiply(a: [[]], b: [[]]) -> [[]]:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Размеры матриц не совпадают")

    c = create_matrix(len(b[0]), len(b), lambda: 0)

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c


def matrix_mult():
    a = create_random_matrix(10, 10, 0, 9)
    b = create_random_matrix(10, 10, 0, 9)

    c = multiply(a, b)

    pprint(c)


if __name__ == "__main__":
    matrix_mult()
