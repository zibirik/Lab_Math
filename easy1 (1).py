from numpy import random, linspace
import matplotlib.pyplot as plt

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

"""График параболы для различных r"""
x = linspace(0, 1, 500)
plt.figure(figsize=(11, 6))

"""Строим параболы для r = 1.0, 2.5, 4.0"""
r_values = [1.0, 2.5, 4.0]
for r in r_values:
    y = r * x * (1 - x)
    plt.plot(x, y, linewidth=2, label=f'r = {r}')

# Диагональ y=x
plt.plot([0, 1], [0, 1], 'k--', alpha=0.3, label='y = x')

plt.title("Влияние r")
plt.xlabel("$x_{n-1}$")
plt.ylabel("$x_n$")
plt.legend()
plt.grid(True)
plt.savefig('logistic_parabolas.png')
plt.show()
