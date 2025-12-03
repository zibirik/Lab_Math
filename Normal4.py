from numpy import sqrt
import matplotlib.pyplot as plt


"""Константы"""
steps = 50
x0 = 0.2


def my_variant(x, r):
    """Функия N = 2"""
    return r * x * ((1 - x)**2)

def get_data(r, x0, steps):
    """Получение данных по формуле"""
    data = [x0]
    curr = x0
    for _ in range(steps):
        curr = my_variant(curr, r)
        data.append(curr)
    return data


plt.figure(figsize = (11, 6))

"""Случай 1: r ≤ 1 и сходимость к 0"""
r1 = 0.9
y1 = get_data(r1, x0, steps)
plt.plot(y1, "o-", label = f"r = {r1}")

"""Случай 2: 1 < r < 4 и сходимость к точке равновесия"""
r2 = 2.5
y2 = get_data(r2, x0, steps)
x_star = 1 - 1/sqrt(r2)
plt.plot(y2, "o-", label = f"r = {r2}, к {x_star:.4f}")
"""График линии равновесия"""
plt.axhline(x_star, color = "black", linestyle = "--", alpha = 0.5)

"""Случай 3: r ≥ 4, колебание"""
r3 = 5.0
y3 = get_data(r3, x0, steps)
plt.plot(y3, "o-", label = f"r = {r3}")

plt.title(f"Динамика для $x_{{n+1}} = r x (1 - x)^2$")
plt.xlabel("n")
plt.ylabel("$x_n$")
plt.legend()
plt.grid()

plt.show()
