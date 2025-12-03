from numpy import linspace
import matplotlib.pyplot as plt


def formula(x, r):
    """Формула"""
    return r * x * (1 - x)


x = linspace(0, 1, 100)
plt.figure(figsize = (11, 6))

"""Случай 1: когда r ≤ 1"""
plt.subplot(1, 2, 1)
r1 = 1 - 0.1
plt.plot(x, formula(x, r1), label = f"Парабола r = {r1}")
plt.plot(x, x, "k--", label = "y = x")

plt.plot(0, 0, "ro", label = "0 всегда существует")
plt.title(f"Случай, когда r ≤ 1 \n Одна точка")
plt.xlabel("$x_n$")
plt.ylabel("$x_{n+1}$")
plt.legend()
plt.grid()


"""Случай 2: r > 1"""
plt.subplot(1, 2, 2)
r2 = 1 + 1
plt.plot(x, formula(x, r2), label = f"Парабола r = {r2}")
plt.plot(x, x, "k--", label = "y = x")
plt.plot(0, 0, "ro")

x2 = 1 - 1 / r2
plt.plot(x2, x2, "ro", label = f"Точки 0 и {x2:.3f}")
plt.title(f"Случай, когда r > 1 \n Два паересечения")
plt.xlabel("$x_n$")
plt.ylabel("$x_{n+1}$")
plt.legend()
plt.grid()

plt.show()
