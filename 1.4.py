a = int(input("Введите целое положительное число: "))
d = 0
b = 0
while a / 10 >= 0.1:
    b = int(a % 10)
    a = int(a / 10)
    if b > d:
        d = b
        print(d)
print("Наибольшшая цифра в Вашем числе - ", d)
