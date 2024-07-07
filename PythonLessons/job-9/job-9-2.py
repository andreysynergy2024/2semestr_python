def get_list_intersections():
    """
    Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый.
    Все числа каждого списка находятся на отдельной строке.
    Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.
    """

    left_list = [1, 2, 3, 4, 5, 6]
    right_list = [9, 8, 7, 6, 5]

    common_numbers = set(left_list).intersection(right_list)

    print(common_numbers)
    print(len(common_numbers))


if __name__ == "__main__":
    get_list_intersections()
