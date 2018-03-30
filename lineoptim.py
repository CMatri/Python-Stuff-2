import matplotlib.pyplot as plt
import numpy as np
import math

f = lambda x: math.sin(x / 4.0) * 7.0#(x + 10)**3 * (x / 100.0) * ((x / 2.0 - 5)**2 / 50.0)

verts = [(x0, f(x0)) for x0 in np.arange(-30, 30, 0.01)]

xx = [0,0]
yy = [0,0]
px = 4
py = 8

def drawUpdate(mx, my):
    global xx, yy, px, py
    iters = 90
    step = 0.2
    i = mx
    it = 0
    d = [-1,-1]
    px = mx
    py = my

    plt.clf()
    plt.cla()

    y = [x0[1] for x0 in verts]
    x = [x0[0] for x0 in verts]

    def derive(f, x, e=1e-10):
        d = f(x + e) - f(x)
        d /= e
        return d

    dy = lambda xx2: math.sqrt((mx - xx2)**2 + (my - f(xx2))**2)
    dy2 = lambda xx2: abs(mx - xx2) + abs(my - f(xx2))

    if mx:
        '''
        while it < iters:
            nx = i + (-it if not it % 2 else it) * step
            ny = f(nx)
            dist = math.sqrt((nx - mx)**2 + (ny - my)**2)
            if dist < d[0] or d[0] == -1:
                xx[0] = nx
                yy[0] = ny
                d[0] = dist
            dist = (abs(mx - nx) + abs(my - ny))
            plt.plot([nx, mx], [ny, my], color='purple', alpha=0.2)
            if dist < d[1] or d[1] == -1:
                xx[1] = nx
                yy[1] = ny
                d[1] = dist
            it += 1
            lim = 1
        '''
        
        a = 0.5
        x2 = np.arange(-30, 30, 0.01)
        y2 = [dy(xx2) for xx2 in x2]
        dyy2 = [derive(dy, xx2) for xx2 in x2]
        x3 = np.arange(-30, 30, 0.01)
        y3 = [dy2(xx2) for xx2 in x3]
        dyy3 = [derive(dy2, xx2) for xx2 in x3]
        plt.plot(x2, y2, color='red', alpha=a)
        plt.plot(x2, dyy2, '--', color='red', alpha=a)
        plt.plot(x3, y3, color='green', alpha=a)
        plt.plot(x3, dyy3, '--', color='green', alpha=a)
        
        xx = [x2[y2.index(min(y2))], x3[y3.index(min(y3))]]
        yy = [f(xx[0]), f(xx[1])]
        plt.plot(x, y)
        plt.plot([xx[0], xx[0], mx], [min(y2), yy[0], my], color='red')
        plt.plot([xx[1], xx[1], mx], [min(y3), yy[1], my], color='green')
        plt.scatter(xx, yy, color=['red',   'green'])
        plt.scatter(xx, [min(y2), min(y3)], color=['red', 'green'])
        plt.scatter(mx, my, color='orange')

    plt.xlim(-30, 30)
    plt.ylim(-30, 30)
    plt.grid()
    plt.draw()

def onclick(event):
    drawUpdate(event.xdata, event.ydata)

drawUpdate(px, py)

plt.gcf().canvas.mpl_connect('motion_notify_event', onclick)

y = [x0[1] for x0 in verts]
x = [x0[0] for x0 in verts]

plt.plot(x, y)
plt.scatter(xx, yy)
plt.xlim(-30, 30)
plt.ylim(-30, 30)
plt.grid()
plt.show()