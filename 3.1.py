def divi():
    arg_1 = float(input("Введите делимое: "))
    arg_2 = float(input("Введите делитель: "))
    if arg_2 != 0:
        s_div = arg_1 / arg_2
    else:
        print("error")
    return s_div

d = divi()
print(f"{d:.4f}")
