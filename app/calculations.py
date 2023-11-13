def calculate_self_price(grade: str, item_price: int, cry_amount: int):
    so = 275
    spo = 440
    one_cry_price = item_price // cry_amount

    grade_factors = {'D': (3, 8, 156, 100), 'C': (15, 30, 476, 200), 'B': (54, 16, 450, 100), 'A': (36, 70, 300, 200), 'S': (40, 50, 350, 100)}

    if (grade := grade.upper()) in grade_factors:
        s, b, sg, bg = grade_factors[grade]
        ssd = (so * s + one_cry_price) // sg
        bssd = (spo * b + one_cry_price * 2) // bg
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
