import os

NAME = "Имя"
BREED = "Порода"
AGE = "Возраст"
OWNER = "Владелец"


def get_next_id(d: dict) -> int:
    if len(d) == 0:
        return 1
    else:
        all_keys = []
        for k in d.keys():
            all_keys.append(k)
        return all_keys[-1] + 1

    # return list(d.keys())[-1] + 1 if len(d) > 0 else 1


def format_age(age: int) -> str:
    def fmt(a, k):
        return f"{a} {k}"

    if age % 10 == 1 and age != 11:
        return fmt(age, "год")
    elif age % 10 in [2, 3, 4] and (age < 10 or age > 20):
        return fmt(age, "года")
    else:
        return fmt(age, "лет")


def show_pet(id: int, pet: dict):
    for pet_name in pet.keys():
        pet_attr = pet[pet_name]
        print(f"{id}: {pet_attr[BREED]} по кличке \"{pet_name}\". "
              f"Возраст питомца: {format_age(pet_attr[AGE])}. "
              f"Имя владельца: {pet_attr[OWNER]}.")


def show_pets_list(pets: dict):
    for k in pets.keys():
        show_pet(k, pets[k])


def get_pet_attributes():
    pet_name = input("Введите кличку:")
    pet_breed = input("Введите породу:")
    pet_age = input("Введите возраст:")
    pet_owner = input("Введите имя владельца:")
    return pet_name, pet_breed, pet_age, pet_owner


def get_pet(id: int, pets: dict) -> dict:
    return pets[id] if id in pets.keys() else False


def create(pets: dict):
    """
    Данная функция будет создавать новую запись с информацией о питомце
    и добавлять эту информацию в наш словарь pets
    """

    key = get_next_id(pets)
    pets[key] = {}

    # pet_name, pet_breed, pet_age, pet_owner = get_pet_attributes()
    pet_name, pet_breed, pet_age, pet_owner = "Суслик", "человек", 30, "Ленусик"

    pet = pets[key][pet_name] = {}
    pet[BREED] = pet_breed
    pet[AGE] = int(pet_age)
    pet[OWNER] = pet_owner

    show_pets_list(pets)


def read(pets: dict):
    """
    Данная функция будет отображать информацию о запрашиваемом питомце в виде:
    Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
    """

    pet_id = int(input("Введите ID записи:"))

    pet = get_pet(pet_id, pets)
    if pet is not False:
        show_pet(pet_id, pet)


def update(pets: dict):
    """
    Данная функция будет обновлять информацию об указанном питомце
    """

    pet_id = int(input("Введите ID записи:"))

    pet = get_pet(pet_id, pets)
    key = next(iter(pet))

    pet_name, pet_breed, pet_age, pet_owner = get_pet_attributes()

    if pet_breed != "":
        pet[key][BREED] = pet_breed

    if pet_age != "":
        pet[key][AGE] = int(pet_age)

    if pet_owner != "":
        pet[key][OWNER] = pet_owner

    if pet_name != "":
        pet[pet_name] = pet.pop(key)

    show_pets_list(pets)


def delete(pets: dict):
    """
    Данная функция будет удалять запись о существующем питомце
    """
    pet_id = int(input("Введите ID записи:"))

    pet = get_pet(pet_id, pets)
    if pet is not False:
        pets.pop(pet_id)

    show_pets_list(pets)


def list(pets: dict):
    """
    Перечисляет всех питомцев в БД
    """
    show_pets_list(pets)


def stop(pets: dict):
    os.abort()


def pet_clinic():
    pets = {}

    while True:
        command = input(">").strip()
        try:
            globals()[command](pets)
        except KeyError as e:
            print(f"Команда {command} не поддерживается.")


if __name__ == "__main__":
    pet_clinic()
