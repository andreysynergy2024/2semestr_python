human_development_stages = {
    1: ("Австралопитек",
        "Человек больше похожий на обезьяну, но уже который может ходить на двух ногах. Они существовали 3 - 4 миллионов лет назад. На этом этапе формировался череп, органы, он учился ходить на двух ногах."),
    2: ("Человек умелый",
        "Освоили хождение на двух ногах, начали добывать первое орудие труда, камни, палки и т.д. Внешне человек был еще похож на обезьяну, формировались так же черты лица и череп."),
    3: ("Человек прямоходящий",
        "Ну здесь из одного названия уже можно понять, что человек научился держать спину прямо, полностью освоил хождение на двух ногах. Существовали 1.5 млн. лет назад."),
    4: ("Неандерталец",
        "Стали больше походить на человека. Череп уже практически сформировался, волосиной покров стал меньше. Научились делать новые орудия труда."),
    5: ("Человек разумный разумный",
        "Появились 40 тыс. лет назад. Они полностью уже были похожи на людей. Умели охотиться, добывать огонь и пищу и разговаривать. Появлялись новые орудия труда.")
}


def show_form_with_questions():
    actual_stage_names = prompt_enter_stages()
    show_actual_stages(actual_stage_names)


def prompt_enter_stages():
    total_stages = len(human_development_stages)
    print(f"Введите {total_stages} последовательных стадий развития человека.")

    actual_stage_names = []
    for num in range(1, total_stages + 1):
        stage_name = input(f"Стадия {num}? ")
        actual_stage_names.append(stage_name)

    return actual_stage_names


def show_actual_stages(actual_stage_names):
    print("=>".join(actual_stage_names))


if __name__ == "__main__":
    show_form_with_questions()
