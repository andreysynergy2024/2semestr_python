def get_the_number_of_vowels():
    """
    Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв?
    Гласными называют буквы «a», «e», «i», «o», «u».
    Для решения задачи создайте переменную и в неё положите слово с помощью input()
    А также определите количество каждой из этих гласных букв
    Если какой-то из перечисленных букв нет - Выведите False
    """

    word = "Anaconda"

    vowels = ["a", "e", "i", "o", "u"]

    vowels_with_counts = dict()
    for v in word.lower():
        if v in vowels:
            if vowels_with_counts.get(v) is None:
                vowels_with_counts[v] = 1
                continue
            vowels_with_counts[v] = vowels_with_counts[v] + 1

    for v in vowels:
        if vowels_with_counts.get(v) is None:
            vowels_with_counts[v] = 0

    for v in vowels_with_counts:
        count = vowels_with_counts[v]
        if count != 0:
            print(v, count)
        else:
            print(v, False)


if __name__ == "__main__":
    get_the_number_of_vowels()
