def get_minimum_boats_count():
    """
    На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
    Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек.
    Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков
    В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка.
    Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков.
    В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника.
    Программа должна вывести одно число - минимальное количество лодок,
    необходимое для переправки всех рыбаков на противоположный берег.
    """

    max_mass = int(input("Введите максимальную перевозимую массу:"))
    if max_mass > 10E6:
        return

    total_fisherman = int(input("Введите количество рыбаков:"))
    if total_fisherman > 100:
        return

    fisherman_mass = []

    for i in range(total_fisherman):
        mass = int(input(f"Масса {i} рыбака:"))
        fisherman_mass.append(mass)

    boats = []
    for x in range(len(fisherman_mass)):
        if min(fisherman_mass) > max_mass:
            if fisherman_mass[x] > max_mass:
                continue
            else:
                boats.append([[fisherman_mass[x]]])
        else:
            boats.append([[fisherman_mass[x], min(fisherman_mass)]])
            fisherman_mass[x] += max_mass
            fisherman_mass[fisherman_mass.index(min(fisherman_mass))] += max_mass

    total_boats = len(boats)

    print(f"Минимальное количество лодок: {total_boats}")


if __name__ == "__main__":
    get_minimum_boats_count()
