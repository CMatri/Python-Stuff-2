from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
plot = fig.add_subplot(111)

def newton(a, eps=0.001, it=500):
    b = 0
    i = 0
    for _ in range(it):
        b = a - (f(a) / derive(f, a))
        if abs(b - a) <= eps: break
        a = b
        i += 1
    return b, i

def inv_quad_interp(x0, x1, x2, eps=0.001, it=500):
    i = 0
    for _ in range(it):
        a0 = (x0 * f(x1) * f(x2)) / ((f(x0) - f(x1)) * (f(x0) - f(x2))) 
        a1 = (x1 * f(x0) * f(x2)) / ((f(x1) - f(x0)) * (f(x1) - f(x2)))
        a2 = (x2 * f(x0) * f(x1)) / ((f(x2) - f(x0)) * (f(x2) - f(x1)))
        x = a0 + a1 + a2
        if min(abs(x - x0), abs(x - x1), abs(x - x2)) < eps: break
        x0 = x1
        x1 = x2
        x2 = x

        xx2 = [x0, x1, x2]
        yy2 = [f(xx0) for xx0 in xx2]
        f2 = interp1d(xx2, yy2, kind="quadratic")
        xnew = np.arange(xx2[0], xx2[2], 0.001)
        plot.plot(xnew, f2(xnew), alpha=i/it+0.3, label=str(i))

        i += 1
    return x2, i

def secant(a, b, eps=0.001, it=500):
    i = 0
    for _ in range(it):
        if abs(a - b) < eps: break
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        a = b
        b = c
        i += 1
    return b, i

def derive(f, x, e=1e-10):
    d = f(x + e) - f(x)
    d /= e
    return d

f = lambda x: x**5 - 8 * x**3 + 10 * x + 6

#rS = [secant(-1.5, -1, 0.00001), secant(-0.5, 0.5, 0.00001), secant(1.4, 1.7, 0.00001)]
rIQI = inv_quad_interp(0, 0.75, 1.1, 0.0000001, 100)
#rN = [newton(-1.5, 0.00001), newton(-0.3, 0.00001), newton(1.4, 0.00001)]

#print("Secant: " + str(rS))
print("Inv Quad Interp: " + str(rIQI))
#print("Newton: " + str(rN))

def on_plot_hover(event):
    for curve in plot.get_lines():
        if curve.contains(event)[0]:
            print("Over line " + curve.get_label() + " of " + str(rIQI[1]))

fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)

x = np.arange(-10, 10, 0.001)
y = [f(x0) for x0 in x]

plot.set_xlim([-4, 4])
plot.set_ylim([-20, 20])
plot.plot(x, y)
plot.scatter(rIQI[0], f(rIQI[0]))
plot.grid()
plt.show()
