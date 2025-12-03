from numpy import linspace
import matplotlib.pyplot as plt


"""Константы"""
r = 1  # r ∈ (0; 1]
x0 = 0.1 # x0 ∈ (0; 1)
steps = 20

def formula(x, r):
    """Формула"""
    return r * x * (1 - x)


"""Траектория"""
trajectory = [x0]
x = x0
for _ in range(steps):
    x = formula(x, r)
    trajectory.append(x)

plt.figure(figsize=(11, 6))

"""Монотонность убывания при r ∈ (0; 1]"""
plt.subplot(1, 2, 1)
plt.plot(trajectory, "o-")
plt.title(f"Монотонное убывание r = {r}")
plt.xlabel("n")
plt.ylabel("$x_n$")
plt.grid()

"""График самой параболы"""
plt.subplot(1, 2, 2)
x_vals = linspace(0, 1, 100)
plt.plot(x_vals, formula(x_vals, r), "b-", label = "Парабола")
plt.plot(x_vals, x_vals, "k--", label = "y = x")

plt.title("График параболы при r ∈ (0; 1]")
plt.xlabel("$x_n$")
plt.ylabel("$x_{n+1}$")
plt.legend()
plt.grid()

plt.show()
