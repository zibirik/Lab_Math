from numpy import linspace
import matplotlib.pyplot as plt


def formula(x, r):
    """Формула"""
    return r * x * (1 - x)

def lamerey(f, r, x0 = 0.2, steps = 40):
    """"Построение лестницы Ламерея"""
    xs, ys = [], []
    x = x0
    for _ in range(steps):
        y = f(x, r)
        xs.append(x); ys.append(y)
        xs.append(y); ys.append(y)
        x = y
    return xs, ys


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 6))

x = linspace(0, 1, 400)

"""График 1: r = 3.2"""
r1 = 3.2
ax1.plot(x, formula(x, r1), "b-", linewidth = 2, label = "f(x)")
ax1.plot(x, x, "k--", linewidth = 1, label = "y = x")
xs, ys = lamerey(formula, r1, x0 = 0.15, steps = 25)
ax1.plot(xs, ys, "r-", linewidth = 1.2, alpha = 0.7)
ax1.grid(True, alpha = 0.3)
ax1.set_title(f"r = {r1}", fontsize = 12)
ax1.set_xlabel("$x_n$")
ax1.set_ylabel("$x_{n+1}$")
ax1.legend()

"""График 2: r = 3.5"""
r2 = 3.5
ax2.plot(x, formula(x, r2), "b-", linewidth = 2, label = "f(x)")
ax2.plot(x, x, "k--", linewidth = 1, label = "y = x")
xs, ys = lamerey(formula, r2, x0 = 0.15, steps = 40)
ax2.plot(xs, ys, "r-", linewidth = 1.2, alpha = 0.7)
ax2.grid(True, alpha = 0.3)
ax2.set_title(f"r = {r2}", fontsize = 12)
ax2.set_xlabel("$x_n$")
ax2.set_ylabel("$x_{n+1}$")
ax2.legend()

plt.tight_layout()
plt.savefig("H2.png", dpi = 150)
plt.show()
