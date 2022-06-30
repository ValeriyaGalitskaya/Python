r = [8, 5, 2, 2, 1, 1, 1]
a = len(r)
b = int(input("Введите новое значение для рейтинга: "))
i = 0
while i + 1 <= a:
    c = int(r[i])
    if b == c:
        r.insert(i + 1, b)
        break
    elif b > c:
        r.insert(i, b)
        break
    i = i + 1
print(r)
