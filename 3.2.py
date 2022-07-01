def dano():
    arg_1 = str(input("Введите Имя: "))
    arg_2 = str(input("Введите Фамилию: "))
    arg_3 = str(input("Введите год рождения: "))
    arg_4 = str(input("Введите город проживания: "))
    arg_5 = str(input("Введите e-mail: "))
    arg_6 = str(input("Введите телефон: "))
    ex = arg_1 + " " + arg_2 + " " + arg_3 + " " + arg_4 + " " + arg_5 + " " + arg_6
    return ex


nex = str(dano())
print(nex)
