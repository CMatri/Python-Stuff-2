import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.pyplot as plt

f = lambda x: x**4 - 10 * x**2 + 9

def enum_roots(rng, step_size):
    x = np.arange(rng[0], rng[1], step_size)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.fill_between(x, 0, y, where=y > 0, facecolor='g', alpha=0.5)
    ax.fill_between(x, 0, y, where=y < 0, facecolor='r', alpha=0.5)
    roots = []

    for i in range(1, len(x)):
        if (y[i] < 0 and y[i - 1] > 0) or (y[i] > 0 and y[i - 1] < 0):
            roots.append((x[i], y[i]))

    return np.array(roots)

plt.scatter(*enum_roots([-4, 4], 0.001).T)
plt.grid()
plt.show()
