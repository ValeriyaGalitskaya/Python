a = int(input("Введите число n от 1 до 1000: "))
if (a / 1000 >= 1):
    b = a * 10001
    c = a * 100010001
    d = a + b + c
elif (a / 100 >= 1):
    b = a * 1001
    c = a * 1001001
    d = a + b + c
elif (a / 10 >= 1):
    b = a * 101
    c = a * 10101
    d = a + b + c
else:
    b = a * 11
    c = a * 111
    d = a + b + c
print(a, "+", b, "+", c, "=", d)