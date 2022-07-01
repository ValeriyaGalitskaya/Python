x = float(input("Введите положительное число: "))
y = int(input("Введите целое отрицательное число: "))


def st(x, y):
    return x ** y


s = st(x, y)
print(f"{s:.8f}")
