x = float(input("Введите положительное число: "))
y = int(input("Введите целое отрицательное число: "))


def st(x, y):
    i = 1
    sm = x
    while i > y:
        sm = sm / x
        i = i - 1
    return sm


s = st(x, y)
print(f"{s:.8f}")
