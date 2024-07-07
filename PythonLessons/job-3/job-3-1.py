def ask_user_for_a_description_of_pet():
    """
    Урок №3. Ввод-вывод и базовые переменные
    Задание №1
    """
    pet_name = input("Введите кличку:")
    pet_breed = input("Введите породу:")
    pet_age = input("Введите возраст:")

    print(f"Это {pet_breed} по кличке \"{pet_name}\". Возраст {pet_age} года.")


if __name__ == "__main__":
    ask_user_for_a_description_of_pet()
