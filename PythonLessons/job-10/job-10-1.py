OWNER = "Имя владельца"
BREED = "Порода"
AGE = "Возраст"


def get_pet_attributes():
    pet_name = input("Введите кличку:")
    pet_breed = input("Введите породу:")
    pet_age = int(input("Введите возраст:"))
    pet_owner = input("Введите имя владельца:")
    return pet_name, pet_breed, pet_age, pet_owner


def format_age(age: int) -> str:
    def fmt(a, k):
        return f"{a} {k}"

    if age % 10 == 1 and age != 11:
        return fmt(age, "год")
    elif age % 10 in [2, 3, 4] and (age < 10 or age > 20):
        return fmt(age, "года")
    else:
        return fmt(age, "лет")


def print_pet(pet_name: str, pet: dict):
    # Можно обратиться к словарю так:
    for pet_name in pet.keys():
        any_pet = pet.get(pet_name)
        for k, v in any_pet.items():
            print(k, v)

    # но лучше - так:
    pet_breed = pet[pet_name][BREED]
    pet_age = pet[pet_name][AGE]
    pet_owner = pet[pet_name][OWNER]

    print(f"Это {pet_breed} по кличке \"{pet_name}\". Возраст {format_age(pet_age)}. Имя владельца {pet_owner}.")


def fill_dictionary():
    pets = {}

    pet_name, pet_breed, pet_age, pet_owner = get_pet_attributes()

    pets[pet_name] = {}
    pets[pet_name][BREED] = pet_breed
    pets[pet_name][AGE] = pet_age
    pets[pet_name][OWNER] = pet_owner

    print_pet(pet_name, pets)


if __name__ == "__main__":
    fill_dictionary()
