from numpy import random


"""Константные параметры"""
trysteps = 10000
fails = 0


def formula(x, r):
    """Формула"""
    return r * x * (1 - x)


def proof(x0, r, steps):
    """Проверка"""
    x = x0
    for n in range(steps):
        x = formula(x, r)

        """Проверка выхода за границы"""
        if x < 0 or x > 1:
            return False, n + 1, x

    return True, steps, x


for i in range(trysteps):
    """Перебираем случайные значения для оптимизации"""
    x0 = random.uniform(0.0000000001, 0.9999999999)
    r = random.uniform(0, 1)

    ok, step, x_last = proof(x0, r, 1000)

    if not ok:
        fails += 1
        print(f"Ошибка: {x0} {r} {step} {x_last}")
        break

if fails == 0:
    print("ЧТД")
