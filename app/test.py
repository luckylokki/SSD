def calculate_self_price(grade: str, item_price: int, cry_amount: int):
    so = 275
    spo = 440
    one_cry_price = item_price // cry_amount

    grade_factors = {'D': (3, 8), 'C': (15, 30), 'B': (54, 16), 'A': (36, 70), 'S': (40, 50)}

    if (grade := grade.upper()) in grade_factors:
        s, b = grade_factors[grade]
        ssd = (so * s + one_cry_price) // 156
        bssd = (spo * b + one_cry_price * 2) // 100
        return one_cry_price, ssd, bssd
    else:
        return print('Неверный ввод.\n')


def calculate_shot(grade: str, cry: int, grade_to_factor):
    ss = 0
    nsocry = 0

    if (grade := grade.upper()) in grade_to_factor:
        factor = grade_to_factor[grade]
        for _ in range(cry):
            ss += 156
            nsocry = factor * cry

        return nsocry, ss
    else:
        return print('Не верный ввод.\n')


def soul_shot(grade: str, cry: int):
    return calculate_shot(grade, cry, {'D': 3, 'C': 15, 'B': 54, 'A': 36, 'S': 40})


def blessed_spirit_shot(grade: str, cry: int):
    return calculate_shot(grade, cry, {'D': 8, 'C': 30, 'B': 16, 'A': 70, 'S': 50})


def display_result(cry, grade, result, shot_type):
    if result is not None and len(result) >= 2:
        print(
            f"Результат:\nУ вас {cry} кристал(ов) {grade} грейда\nВам нужно {result[0]} SoulOre\nВы получите {result[1]} {shot_type} {grade}")
    else:
        print(f"Не удалось получить результат для {shot_type}{grade}.")


def sub_menu():
    shot_types = {'1': soul_shot, '2': blessed_spirit_shot}
    for key, value in shot_types.items():
        print(f'[{key}] - {value.__name__}')

    sub_choice = input("Выберите подпункт (1-2): ")

    if sub_choice in shot_types:
        print('\n')
        grade = input(f"Введите тип (D,C,B,A,S): ").upper()
        cry = int(input(f"Введите количество имеющихся кристалов: "))

        result_func = shot_types[sub_choice]
        result = result_func(grade, cry)

        display_result(cry, grade, result, result_func.__name__)
    else:
        print("Неверный ввод. Пожалуйста, выберите снова.")



def menu():
    print('\n')
    print("1. Узнать Себестоимость кристалов и шотов:")
    print("   (Необходимо знать цену разбиваемого предмета(0 для выбитых) и количество полученных кристалов)")
    print("2. Имея кристалы узнать сколько нудно SpiritOre/SoulOre и сколько щотов получите")
    print("0. Выйти\n")


def main():
    while True:
        menu()
        choice = input("Выберите пункт меню (0-3): ")

        if choice == "1":
            grade = input(f"Выберете тип (D,C,B,A,S): ").upper()
            item_price = int(input(f"Введите цену разбиваемого предмета: "))
            cry_amount = int(input(f"Введите кол-во получившихся кристалов при кристализации: "))
            result = calculate_self_price(grade, item_price, cry_amount)
            print('\n')
            print(f"Результат:\nСебестоимость 1 кристала: {result[0]}\n"
                  f"Себестоимость 1 SS{grade}: {result[1]}\n"
                  f"Себестоимость 1 BSS{grade}: {result[2]}")
        elif choice == "2":
            sub_menu()
        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
