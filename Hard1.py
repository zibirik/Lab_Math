from numpy import arange


def formula(x, r):
    return r * x * (1 - x)

def cylegth(r):
    x = 0.1
    for _ in range(2000):
        x = formula(x, r)

    path = []
    for _ in range(100):
        x = formula(x, r)
        val = round(x, 4) 
        if val not in path:
            path.append(val)

    return len(path)

for r in arange(2.0, 3.569945, 0.0001):
    length = cylegth(r)
    print(f"r = {r:.7f}, m = {length}")
