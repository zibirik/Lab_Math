import matplotlib.pyplot as plt


def formula(x, r):
    """Формула"""
    return r * x * (1 - x)


"""Константы"""
r = 2.9  # r ∈ (2; 3)
x0 = 0.7 # x2n > x∗, x2n+1 < x∗
steps = 30

"""Точка равновесия"""
x_star = 1 - 1/r

"""Последовательность"""
pos = [x0]
curr = x0
for _ in range(steps):
    curr = formula(curr, r)
    pos.append(curr)

"""Подпоследовательности"""
evens = pos[0::2]  # Чет
odds = pos[1::2]   # Нечет
n_evens = list(range(0, steps+1, 2))
n_odds = list(range(1, steps+1, 2))

plt.figure(figsize = (11, 6))

"""График линии равновесия"""
plt.axhline(x_star, color = "gray", linestyle = "--", label = f"Равновесие x* = {x_star:.4f}")

"""Чет"""
plt.plot(n_evens, evens, "ro-", label = "$x_{2n}$ - Убывают")

"""Нечет"""
plt.plot(n_odds, odds, "bo-", label = "$x_{2n+1}$ - Растут")

plt.title(f"Сходимость подпоследовательностей при r = {r}")
plt.xlabel("n")
plt.ylabel("$x_n$")
plt.legend()
plt.grid()
plt.savefig('N3.png')
plt.show()
