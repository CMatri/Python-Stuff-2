import math
import matplotlib.pyplot as plt
import numpy as np

def derive(f, x, e=1e-10):
    d = f(x + e) - f(x)
    d /= e
    return d

def f(x):
    return .5*x**3

x_vals = np.arange(-10, 10, 0.1)
f_vals = [f(x) for x in x_vals]
d_vals = [derive(f, x) for x in x_vals]

plt.plot(x_vals, f_vals)
plt.plot(x_vals, d_vals)
plt.axis([-10, 10, -10, 10])
plt.grid(True)
plt.show()

print(derive(f, 0))
