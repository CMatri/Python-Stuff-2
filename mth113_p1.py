import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (35.0 * x**4.0 - 30.0 * x**2.0 + 3.0) / (8.0)

def bisection(a, b):
    eps = 0.001
    c = (a + b) / 2.0
    log_y = -0.5
    iters = 0
    while abs(f(c)) > eps:
        iters += 1
        plt.plot([a, b], [log_y, log_y])
        plt.scatter([a, b], [f(a), f(b)])
        log_y -= 0.05
        c = (a + b) / 2.0

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print(iters)
    return c

def secant(a, b):
    log_y = -0.5
    iters = 10
    print(iters)
    for i in range(iters):
        if not f(b) - f(a):
            return b
        plt.plot([a, b], [log_y, log_y])
        plt.scatter([a, b], [f(a), f(b)])
        log_y -= 0.05
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        a = b
        b = c
    return b

x = np.arange(-1.25, 1.25, 0.001)
y = np.array([f(vx) for vx in x])

a = 0.1
b = 0.7

titles = ['Bisection Method', 'Secant Method']

for i, rf in enumerate([bisection, secant]):
    plt.figure()
    found_root = rf(a, b)
    print(found_root)
    plt.scatter(found_root, f(found_root))
    plt.title(titles[i])
    plt.plot(x, y)
    plt.grid()

plt.show()
