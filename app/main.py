# Расчет себестоимости кристалов и шотов
def SelfPrice(grade: str, item_price: int, cry_amount: int):
    so = 275
    spo = 440
    one_cry_price = item_price // cry_amount
    # D GRADE
    if str(grade).upper() == "D":
        ssd = ((so * 3) + one_cry_price) // 156
        bssd = ((spo * 8) + (one_cry_price * 2)) // 100
        return one_cry_price,ssd,bssd
    # C GRADE
    elif str(grade).upper() == "C":
        ssc = ((so * 15) + one_cry_price) // 476
        bssc = ((spo * 30) + (one_cry_price * 2)) // 200
        return one_cry_price,ssc,bssc
    # B GRADE
    elif str(grade).upper() == "B":
        ssb = ((so * 54) + one_cry_price) // 450
        bssb = ((spo * 16) + (one_cry_price * 2)) // 100
        return one_cry_price,ssb,bssb
    # A GRADE
    elif str(grade).upper() == "A":
        ssa = ((so * 36) + one_cry_price) // 300
        bssa = ((spo * 70) + (one_cry_price * 2)) // 200
        return one_cry_price,ssa,bssa
    # S GRADE
    elif str(grade).upper() == "S":
        sss = ((so * 40) + one_cry_price) // 350
        bsss = ((spo * 50) + (one_cry_price * 2)) // 100
        return one_cry_price,sss,bsss
    else:
        return print('Не верный ввод.\n')

# SouShots Enter grade(D,C,B,A,S),
def SoulShot(grade: str, cry: int):
    ss = 0
    socryd = 3
    socryc = 15
    socryb = 54
    socrya = 36
    socrys = 40
    nsocry = 0
    if str(grade).upper() == "D":
        for c in range(cry):
            ss += 156
            nsocry = socryd * cry
        return nsocry, ss
        # C GRADE
    elif str(grade).upper() == "C":
        for c in range(cry):
            ss += 156
            nsocry = socryc * cry
        return nsocry, ss
        # B GRADE
    elif str(grade).upper() == "B":
        for c in range(cry):
            ss += 156
            nsocry = socryb * cry
        return nsocry, ss
        # A GRADE
    elif str(grade).upper() == "A":
        for c in range(cry):
            ss += 156
            nsocry = socrya * cry
        return nsocry, ss
        # S GRADE
    elif str(grade).upper() == "S":
        for c in range(cry):
            ss += 156
            nsocry = socrys * cry
        return nsocry,ss
    else:
        return print('Не верный ввод.\n')



def BlessedSpiritShot(grade: str, cry: int):
    bss = 0
    spod = 8
    spoc = 30
    spob = 16
    spoa = 70
    spos = 50
    nsod = 0
    if str(grade).upper() == "D":
        for c in range(cry // 2):
            bss += 100
            nsod = cry // 2 * spod
        return nsod, bss
        # C GRADE
    elif str(grade).upper() == "C":
        for c in range(cry // 2):
            bss += 100
            nsod = cry // 2 * spoc
        return nsod, bss
        # B GRADE
    elif str(grade).upper() == "B":
        for c in range(cry // 2):
            bss += 100
            nsod = cry // 2 * spob
        return nsod, bss
        # A GRADE
    elif str(grade).upper() == "A":
        for c in range(cry // 2):
            bss += 100
            nsod = cry // 2 * spoa
        return nsod, bss
        # S GRADE
    elif str(grade).upper() == "S":
        for c in range(cry // 2):
            bss += 100
            nsod = cry // 2 * spos
        return nsod,bss
    else:
        return print('Не верный ввод.\n')

def sub_menu():
    recipes = ['[1] - SoulShot', '[2] - BlessedSpiritShot']
    for r in range(len(recipes)):
        print(recipes[r])
    sub_choice = input("Выберите подпункт (1-2): ")
    if sub_choice == "1":
        print('\n')
        grd = str(input(f"Введите тип (D,C,B,A,S): ")).upper()
        cry = int(input(f"Введите количество имеющехся кристалов: "))
        res1,res2 = SoulShot(grd,cry)
        print('\n')
        print(
            f"Результат:\nУ вас {cry} кристал(ов) {grd} грейда\nВам нужно {res1} SoulOre\nВы получите {res2} SS{grd}")
    elif sub_choice == "2":
        print('\n')
        grd = str(input(f"Введите тип (D,C,B,A,S): ")).upper()
        cry = int(input(f"Введите количество имеющехся кристалов: "))
        res1,res2 = BlessedSpiritShot(grd,cry)
        print('\n')
        print(
            f"Результат:\nУ вас {cry} кристал(ов) {grd} грейда\nВам нужно {res1} SiritOre\nВы получите {res2} BSS{grd}")
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
            grd = str(input(f"Выберете тип (D,C,B,A,S): ")).upper()
            ip = int(input(f"Введите цену разбиваемого предмета: "))
            crya = int(input(f"Введите кол-во получившихся кристалов при кристализации: "))
            res1,res2,res3 = SelfPrice(grd,ip,crya)
            print('\n')
            print(f"Результат:\nСебестоимость 1 кристала: {res1}\nСебестоимость 1 SS{grd}: {res2}\nСебестоимость 1 BSS{grd}: {res3}")
        elif choice == "2":
            sub_menu()
        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
