from solvepoisson import poisson2d
import numpy as np
from matplotlib import pyplot as plt, cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

nx = 25
ny = 25
nt = 300
xmin = 0
xmax = 2
ymin = 0
ymax = 1

dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

p = np.zeros((ny, nx))
pn = np.zeros((ny, nx))
b = np.zeros((ny, nx))
x = np.linspace(xmin, xmax, nx)
y = np.linspace(xmin, xmax, ny)

b[int(ny / 4), int(nx / 4)] = 100
b[int(3 * ny / 4), int(3 * nx / 4)] = -100

def bc(p):
    p[0, :] = 0
    p[ny - 1, :] = 0
    p[:, 0] = 0
    p[:, nx - 1] = 0

pt = poisson2d(p, b, dx, dy, nt, bc)

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
surf = ax.plot_surface(X, Y, pt[0][:], rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=False)

def update(val):
    ax.clear()
    ax.set_zlim(-0.2, 0.2)
    surf = ax.plot_surface(X, Y, pt[int(val)][:], rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=False)

axdt = plt.axes([0.13, 0.02, 0.78, 0.03], facecolor='lightgoldenrodyellow')
sdt = Slider(axdt, 't', 0, nt - 1, valinit=0)
sdt.on_changed(update)

plt.show()