def convert_all_consecutive_spaces_into_one():
    """
    Дана строка, длина которой не превосходит 1000.
    Вам требуется преобразовать все идущие подряд пробелы в один.
    Выведите измененную строку.
    """

    text = "Вам требуется     преобразовать все      идущие       подряд пробелы     в один"

    if len(text) > 1000:
        return

    normalized_text = ""

    i = 0
    space = " "
    while i < len(text):
        letter = text[i]

        if letter != " ":
            normalized_text += letter

        prev_pos = i - 1
        if prev_pos > 0 and text[prev_pos] != space and text[i] == space:
            normalized_text += space

        i += 1

    print(normalized_text)


if __name__ == "__main__":
    convert_all_consecutive_spaces_into_one()