import numpy as np
import math

f0 = lambda x: 4.0 / (x**2 + 1)
f1 = lambda x: math.sin(x**2)
f2 = lambda x: (1.0 / math.cos(x))**7.2

n_steps = [2, 10, 100, 1000, 10000]
funcs = [[f0, (0, 1)], [f1, (0, 3)], [f2, (0, 0.7)]]

def lr_integral(f, a, b, n, left=True):
    y_vals = [f(x) for x in np.arange(a, b, (b - a) / n)]
    y_vals = y_vals[:-1] if left else y_vals[1:]
    return sum(y_vals) * ((b - a) / n)

def center_integral(f, a, b, n):
    y_vals = [f(x) for x in np.arange(a, b, (b - a) / n)]
    return sum(y_vals) * ((b - a) / n)
    
def trapezoid_integral(f, a, b, n):
    y_vals = [f(x) for x in np.arange(a, b, (b - a) / n)]
    return sum([(y_vals[i - 1] + y_vals[i]) / 2 * ((b - a) / n) for i in range(1, len(y_vals))])

def simpson_integral(f, a, b, n):
    h = (b - a) / n
    return (f(a) + f(b) + sum([4 * f(a + i * h) for i in np.arange(1, n, 2)]) + sum([2 * f(a + i * h) for i in np.arange(0, n - 1, 2)])) * h / 3

for i, data in enumerate(funcs):
    print("Operating on f" + str(i))
    for n in n_steps:
        f = data[0]
        a = data[1][0]
        b = data[1][1]
        print("Left sum of f" + str(i) + ", n=" + str(n) + " : " + str(lr_integral(f, a, b, n, left=True)))
        print("Right sum of f" + str(i) + ", n=" + str(n) + " : " + str(lr_integral(f, a, b, n, left=False)))
        print("Center sum of f" + str(i) + ", n=" + str(n) + " : " + str(center_integral(f, a, b, n)))
        print("Trapezoid sum of f" + str(i) + ", n=" + str(n) + " : " + str(trapezoid_integral(f, a, b, n)))
        print("Simpson sum of f" + str(i) + ", n=" + str(n) + " : " + str(simpson_integral(f, a, b, n)))
        print()