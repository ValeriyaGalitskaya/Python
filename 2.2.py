a = list(input("Введите желаемый список: "))
b = len(a)
c = b - 1
i = 0
print(a)
print(b)
while (i < c):
    n = (a[i])
    (a[i]) = (a[i + 1])
    (a[i + 1]) = n
    i = i + 2
print(a)
