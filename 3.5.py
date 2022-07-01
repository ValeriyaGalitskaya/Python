def calc_sum(*args):
    s = 0
    f = False
    for a in args:
        try:
            if a:
                s = s + float(a)

            """"создаём исключения"""
            
        except ValueError:
            f = True
    return s, f


ss = 0

while True:
    ns = input('Введите числа через пробел: ').split(' ')
    s, sf = calc_sum(*ns)
    ss = ss + s
    print(f'сумма {ss:.3f}')

    if sf:
        break
