import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.arange(-10, 10, .1)
y = [0] * len(x)
for i in range(int(len(y) / 3.0), int(len(y) / 2.0)):
    y[i] = 10

c = 1
dt = 0.001
dx = .1

ut = []
for j in range(150):
    yn = [y[0]]
    for i in range(1, len(y)):
        yn.append(y[i] - c * ((dt * j) / dx) * (y[i] - y[i - 1]))
    y = yn
    ut.append(yn)

plt.grid()
plot, = plt.plot(x, ut[0])

axdt = plt.axes([0.13, 0.02, 0.78, 0.03], facecolor='lightgoldenrodyellow')
sdt = Slider(axdt, 't', 0, len(ut) - 1, valinit=0)

def update(val):
    plot.set_ydata(ut[int(val)])
sdt.on_changed(update)

plt.show()
