from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

tol = lambda x1, x2, n: x2 + (((x1 / 100.0) * 280.059565 * pow(n, -0.412565956)) - x1)

def gen_time_data(x1, x2, n):
    x, z = np.meshgrid([x11 / 10.0 for x11 in range(1, n * 10)], x2)#[z1 / 10.0 for z1 in range(1, n * 10)])
    y = [tol(x1[int(i / 10)], x2[i], x[i]) for i in range(len(x))]
    return x, y, z

n = 7
x, y, z = gen_time_data([300 for i in range(n)], [i for i in range(90, 121)], n)

#for i in range(10):
#    ax.annotate(str(100 + (100 - i * 10)) + '% ' + str(int(y[0::n][i])) + ' ug', xy=(x[0::n][i], y[0::n][i]), xytext=(5, 7), textcoords='offset points')

fig = plt.figure()
ax = p3.Axes3D(fig)

#def update(num, data, line):
#    line.set_data(data[:2, :num])
#    line.set_3d_properties(data[2, :num])

#line, = 
ax.plot_wireframe(x, z, y)

#ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('days')

#ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('target')

#ax.set_zlim3d([0.0, 10.0])
ax.set_zlabel('ug')

#ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N, blit=False)
#ani.save('matplot003.gif', writer='imagemagick')
print(tol(250, 50, 7))
plt.show()