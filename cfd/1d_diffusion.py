import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, sys

nx = 41
dx = 2./(nx-1)
nt = 200    #the number of timesteps we want to calculate
nu = 0.9   #the value of viscosity
sigma = .5 #sigma is a parameter, we'll learn more about it later
dt = sigma*dx**2/nu #dt is defined using sigma ... more later!


u = np.ones(nx)
un = np.ones(nx)
u0 = np.linspace(0, 2, nx)
u[int(.5/dx) : int(1/dx+1)]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
uO = u.copy()

un = np.ones(nx) #our placeholder array, un, to advance the solution in time
a = []

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

for n in range(nt):
    un = u.copy()
    for i in range(1,nx-1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i + 1] - 2 * un[i] + un[i - 1])
    a.append(un)

def animate(i):
    u = a[i]
    ax1.clear()
    plt.plot(u0, u, color='red', label='Density at each x')
    plt.plot(u0, uO, color='green', label='Original Density at each x')
    plt.plot(0, 0, color='blue', label='Elapsed time ' + str(round(i * dt, 2)))
    plt.grid(True)
    plt.title('Diffusion')
    plt.legend()

for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i + 1] - 2 * un[i] + un[i - 1])

anim = animation.FuncAnimation(fig, animate, frames=nt, interval=10)
plt.show()
