a = int(input("Введите номер месяца: "))
b = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
for k in b.keys():
    if a in b[k]:
        print(k)
