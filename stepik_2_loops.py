
# 12x+13y = 777
# 28n+30k+31m=365.
"""
если принять, что все члены слагаемых с неизвестным,кроме одного,
равны нулю, то их можно откинуть и определить максимальные значения
для каждого неизвестного: 12x+13y=777
если y = 0, то второе слагаемое отбрасываем и получаем 12x=777,
отсюда x = 777 / 12 = 64,75 — округляем в меньшую сторону.
аналогично для y и т.д.
"""
# 28n = 365
# n = int(365/28)
# k = int(365/30)
# m = int(365/31)


def func_1():
    total = 0
    for x in range(1, n+1):
        for y in range(1, k+1):
            for z in range(1, m+1):
                # 28n+30k+31m=365.
                if 28 * x + 30 * y + 31 * z == 365:
                    total += 1
                    print('n =', x, 'k =', y, 'm =', z)
    print('Общее количество натуральных решений =', total)


"""
Имеется 100 рублей. Сколько быков, коров и телят
 можно купить на все эти деньги,
 если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля
  и надо купить 100 голов скота?
"""
max_max = 100
n = int(max_max/10)
k = int(max_max/5)
m = int(max_max/0.5)


def func_11():
    total = 0
    for n in range(1, 100+1):
        for k in range(1, 100+1):
            for m in range(1, 100+1):
                if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                    total += 1
                    print('быка =', n, 'корову =', k, 'теленка =', m)
    print('Общее количество натуральных решений =', total)


def func_2():
    total = 0
    for x in range(1, 45):
        for y in range(1, 45):
            for z in range(1, 45):
                if x ** 2 + y ** 2 + z ** 2 == 2020:
                    total += 1
                    print('x =', x, 'y =', y, 'z =', z)
    print('Общее количество натуральных решений =', total)


if __name__ == "__main__":
    func_11()
