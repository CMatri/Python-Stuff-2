import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib.collections import LineCollection

x = np.random.normal(0, 0.1, 0)
y = np.random.normal(0, 0.1, 0)

def drawCells(vor):
    center = vor.points.mean(axis=0)
    ptp_bound = vor.points.ptp(axis=0)
    finite_segments = []
    infinite_segments = []
    for pointidx, simplex in zip(vor.ridge_points, vor.ridge_vertices):
        simplex = np.asarray(simplex)
        if np.all(simplex >= 0):
            finite_segments.append(vor.vertices[simplex])
        else:
            i = simplex[simplex >= 0][0]  # finite end Voronoi verte
            t = vor.points[pointidx[1]] - vor.points[pointidx[0]]  # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal
            midpoint = vor.points[pointidx].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[i] + direction * ptp_bound.max()
            infinite_segments.append([vor.vertices[i], far_point])
    plt.gca().add_collection(LineCollection(finite_segments,
                                     linestyle='solid'))
    plt.gca().add_collection(LineCollection(infinite_segments,
                                     linestyle='dashed'))

def drawUpdate(mx, my):
    global x, y
    plt.clf()
    plt.cla()

    x = np.append(x, np.random.normal(mx, 0.1, 30))
    y = np.append(y, np.random.normal(my, 0.1, 30))
    vor = Voronoi(list(zip(x, y)))

    lim = 1
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.plot(vor.points[:,0], vor.points[:,1], '.')
    plt.plot(vor.vertices[:,0], vor.vertices[:,1], 'o')
    drawCells(vor)
    plt.draw()

def onclick(event):
    drawUpdate(event.xdata, event.ydata)

drawUpdate(0.1, 0.1)

plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.show()
