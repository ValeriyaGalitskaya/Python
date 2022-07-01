def my_func():
    arg_1 = float(input("Введите первое число: "))
    arg_2 = float(input("Введите второе число: "))
    arg_3 = float(input("Введите третье число: "))
    if (arg_1 >= arg_2 or arg_1 >= arg_3) and arg_2 >= arg_3:
        sum = arg_1 + arg_2
    elif (arg_2 >= arg_1 or arg_2 >= arg_3) and arg_3 >= arg_1:
        sum = arg_2 + arg_3
    elif (arg_3 >= arg_1 or arg_3 >= arg_2) and arg_1 >= arg_2:
        sum = arg_1 + arg_3
    return sum


s = my_func()
print(f"сумма двух наибольших чисел равна {s}")
