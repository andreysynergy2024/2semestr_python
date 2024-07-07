def enumerate_items(items: list, i: int = 0):
    if i >= len(items):
        print("Конец списка")
        return
    print(items[i])
    enumerate_items(items, i + 1)


def enumerate_recursive():
    """
    Напишите рекурсивную функцию, которая выведет все элементы от первого
    до последнего и в конце отобразит сообщение 'Конец списка', если выводить
    больше нечего. Циклы использовать запрещено
    """

    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    enumerate_items(my_list)


if __name__ == "__main__":
    enumerate_recursive()
