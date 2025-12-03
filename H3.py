import matplotlib.pyplot as plt

def my_variant(x, r):
    """Формула"""
    return r * x * ((1 - x) ** 2)

def get_trajectory(r, x0 = 0.3, warmup = 500, steps = 50):
    """Получить установившуюся траекторию"""
    x = x0

    for _ in range(warmup):
        x = my_variant(x, r)

    traj = []
    for _ in range(steps):
        x = my_variant(x, r)
        traj.append(x)
    return traj


fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (11, 6))

"""График 1: r = 4.5"""
r1 = 4.5
y1 = get_trajectory(r1)
ax1.plot(y1, "o-", markersize = 6, linewidth = 1.5)
ax1.set_title(f"r = {r1}", fontsize = 12)
ax1.set_xlabel("n")
ax1.set_ylabel("$x_n$")
ax1.grid(True, alpha = 0.3)

"""График 2: r = 5.4"""
r2 = 5.4
y2 = get_trajectory(r2)
ax2.plot(y2, "o-", markersize = 6, linewidth = 1.5, color = "green")
ax2.set_title(f"r = {r2}", fontsize = 12)
ax2.set_xlabel("n")
ax2.set_ylabel("$x_n$")
ax2.grid(True, alpha = 0.3)

plt.tight_layout()
plt.savefig('H3.png', dpi=150)
plt.show()
