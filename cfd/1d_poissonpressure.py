from solvepoisson import poisson1d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

nx = 50
nt = 300
xmin = 0
xmax = 2
dx = (xmax - xmin) / (nx - 1)
p = np.zeros((nx))
pn = np.zeros((nx))
b = np.zeros((nx))

b[int(nx / 4)] = 100
b[int(3 * nx / 4)] = -100
x = np.linspace(xmin, xmax, nx)

def bc(p):
    p[0] = 0
    p[nx - 1] = 0

pt = poisson1d(p, b, dx, nt, bc)

plt.grid()
plot, = plt.plot(x, pt[0])
plt.ylim(-1, 1)

axdt = plt.axes([0.13, 0.02, 0.78, 0.03], facecolor='lightgoldenrodyellow')
sdt = Slider(axdt, 't', 0, nt - 1, valinit=0)

def update(val):
    plot.set_ydata(pt[int(val)])
sdt.on_changed(update)

plt.show()
