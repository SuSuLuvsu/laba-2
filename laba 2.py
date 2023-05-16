def proc21():
    pas = input("Введите пароль:")

    is_num = False
    is_up = False
    is_low = False
    is_sp = False
    for char in pas:
        if char.isnumeric():
            is_num = TrueQ
        elif char.islower():
            is_low = True
        elif char.isupper():
            is_up = True
        elif char in "@#$%":
            is_sp = True

    if len(pas) > 4 and is_num and is_up and is_sp and is_low:
        print("Пароль подтвержден")
    elif is_num:
        print("Пароль должен содержать буквы нижнего и верхнего регистра,цифры и специальные символы")
    elif is_up:
        print("Пароль должен содержать буквы нижнего и верхнего регистра,цифры и специальные символы")
    elif is_low:
        print("Пароль должен содержать буквы нижнего и верхнего регистра,цифры и специальные символы")
    elif is_sp:
        print("Пароль должен содержать буквы нижнего и верхнего регистра,цифры и специальные символы")


def proc22():
    a = int(input("Введите номер места:"))
    if a % 2 == 0 and a <= 36:
        print(a, "- Верхнее место в купэ")
    elif a % 2 != 0 and a <= 36:
        print(a, "- Нижние место в купэ")
    elif a % 2 == 0 and a >= 54:
        print(a, "- Верхнее боковое место в купэ")
    else:
        print(a, "- Нижнее боковое место в купэ")


def proc23():
    god = input('введите год:')
    if (int(god) % 4 == 0 and int(god) % 100 != 0) or int(god) % 400 == 0:
        print(god, "- весокосный год")
    else:
        print(god, "- не весокосный год")


def proc24():
    a = input()
    b = input()
    if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('фиолетовый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('оранжевый')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')
    elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
        print('зеленый')
    elif a == 'синий' and b == 'синий':
        print('синий')
    else:
        print('ошибка')


proc21(), proc22(), proc23(), proc24()