from numpy import linspace
import matplotlib.pyplot as plt


"""Константные параметры"""
maxGr = 27 / 4
mediumGr = 27 / 8
minGr = 1


def formula(x, r):
    """Формула"""
    return r * x * ((1 - x)**2)


x = linspace(0, 1, 500)
plt.figure(figsize=(9, 6))

"""
Значения для r, где:
- maxGr: Максимальное значение для устойчивого поведения
- mediumGr: Среднее значение для наблюдения переходных состояний
- minGr: Минимальное значение
"""
r_values = [maxGr, mediumGr, minGr]

for resalt in r_values:
    y = formula(x, resalt)
    plt.plot(x, y, label=f"r = {resalt}")

"""Функция y = x для наглядности"""
plt.plot([0, 1], [0, 1], "k--", alpha=0.3, label="y = x")

"""Настройки графика"""
plt.title(f"N = 2: $x_{{n+1}} = r * x_n (1 - x_n)^2$")
plt.xlabel("$x_n$")
plt.ylabel("$x_{n+1}$")
plt.legend()
plt.grid(True)
plt.show()
