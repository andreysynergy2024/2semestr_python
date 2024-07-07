def get_startup_preconditions():
    """
    Два инвестора - Майкл и Иван хотят вложиться в стартап.
    Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно.
    У Майкла A долларов, у Ивана B долларов.
    Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan,
    если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
    """

    min_investment_amount = 1000

    mike_amount = 900
    ivan_amount = 100

    if mike_amount >= min_investment_amount and ivan_amount >= min_investment_amount:
        print(2)
    elif mike_amount >= min_investment_amount:
        print("Mike")
    elif ivan_amount >= min_investment_amount:
        print("Ivan")
    elif (mike_amount + ivan_amount) >= min_investment_amount:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    get_startup_preconditions()