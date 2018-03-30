import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import pyplot, cm

nx = 41
ny = 41
nt = 100
dt = 0.005
nt_pp = 50
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)
X, Y = np.meshgrid(x, y)

rho = 1
nu = .1

def solve_b(b, rho, dt, u, v, dx, dy):
    b[1:-1, 1:-1] = (rho * (1 / dt * 
                    ((u[1:-1, 2:] - u[1:-1, 0:-2]) / 
                     (2 * dx) + (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) -
                    ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 -
                      2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) *
                           (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx))-
                          ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2))
    return b

def pressure_poisson(p, dx, dy, b):
    pn = np.empty_like(p)
    pn = p.copy()

    for i in range(nt_pp):
        pn = p.copy()
        pn[1:-1, 1:-1] = (((p[1:-1, 2:] + p[1:-1, 0:-2]) * dy**2 + (p[2:, 1:-1] + p[0:-2, 1:-1]) * dx**2) / 
                        (2 * (dx**2 + dy**2)) - dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])
        pn[:, -1] = pn[:, -2]
        pn[0, :] = pn[1, :]
        pn[:, 0] = pn[:, 1]
        pn[-1, :] = 0
        p = pn
    return p

def solve_cavity(nt, u, v, dt, dx, dy, p, rho, nu):
    un = np.empty_like(u)
    vn = np.empty_like(v)
    b = np.zeros((ny, nx))

    solution = {'u': [], 'v': [], 'p': []}

    for n in range(nt):
        un = u.copy()
        vn = v.copy()

        b = solve_b(b, rho, dt, u, v, dx, dy)
        p = pressure_poisson(p, dx, dy, b)

        un[1:-1, 1:-1] = (u[1:-1, 1:-1]-
                         u[1:-1, 1:-1] * dt / dx *
                        (u[1:-1, 1:-1] - u[1:-1, 0:-2]) -
                         v[1:-1, 1:-1] * dt / dy *
                        (u[1:-1, 1:-1] - u[0:-2, 1:-1]) -
                         dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2]) +
                         nu * (dt / dx**2 *
                        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) +
                         dt / dy**2 *
                        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1])))

        vn[1:-1,1:-1] = (v[1:-1, 1:-1] -
                        u[1:-1, 1:-1] * dt / dx *
                       (v[1:-1, 1:-1] - v[1:-1, 0:-2]) -
                        v[1:-1, 1:-1] * dt / dy *
                       (v[1:-1, 1:-1] - v[0:-2, 1:-1]) -
                        dt / (2 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1]) +
                        nu * (dt / dx**2 *
                       (v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, 0:-2]) +
                        dt / dy**2 *
                       (v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[0:-2, 1:-1])))
        
        un[0, :] = 0
        un[:, 0] = 0
        un[:, -1] = 0
        un[-1, :] = 1
        vn[0, :] = 0
        vn[-1, :]=0
        vn[:, 0] = 0
        vn[:, -1] = 0

        u = un
        v = vn

        solution['u'].append(u)
        solution['v'].append(v)
        solution['p'].append(p)
    return solution

u = np.zeros((ny, nx))
v = np.zeros((ny, nx))
p = np.zeros((ny, nx))
b = np.zeros((ny, nx))
soln = solve_cavity(nt, u, v, dt, dx, dy, p, rho, nu)

fig = plt.figure(figsize=(11,7), dpi=100)
ax = fig.gca()

def update(val):
    try:
        if val < len(soln['p']):
            ax.clear()
            ax.contourf(X, Y, soln['p'][int(val)], alpha=0.5, cmap=cm.viridis)  
            #ax.colorbar()
            ax.contour(X, Y, soln['p'][int(val)], cmap=cm.viridis)  
            ax.quiver(X[::2, ::2], Y[::2, ::2], soln['u'][int(val)][::2, ::2], soln['v'][int(val)][::2, ::2]) 
    except ValueError:
        return

update(300)

axdt = plt.axes([0.13, 0.02, 0.78, 0.03], facecolor='lightgoldenrodyellow')
sdt = Slider(axdt, 't', 0, nt - 1, valinit=0)
sdt.on_changed(update)

plt.show()