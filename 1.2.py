a = int(input("Введите время:"))
b = int(a / 3600)
c = a % 3600
d = int(c / 60)
e = int(c % 60)
print(f"{b}:{d}:{e}")
