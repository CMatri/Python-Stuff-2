import numpy as np

def poisson2d(u, b, dx, dy, nt, bc):
    ut = [u]
    un = np.zeros((len(u), len([0])))
    for it in range(nt):
        un = u.copy()
        un[1:-1, 1:-1] = (((u[1:-1, 2:] + u[1:-1, :-2]) * dy**2 + 
            (u[2:, 1:-1] + u[:-2, 1:-1]) * dx**2 - 
            b[1:-1, 1:-1] * dx**2 * dy**2) / 
            (2 * (dx**2 + dy**2)))
        bc(un)
        ut.append(un)
        u = un
    return ut

def poisson1d(u, b, dx, nt, bc):
    ut = [u]
    for i in range(nt):
        un = u.copy()
        un[1:-1] = -((b[1:-1] * dx**2 - u[0:-2] - u[2:]) / 2)   
        bc(un)
        ut.append(un)
        u = un
    return ut

# TODO: create n-dimensional poisson solver by building a string for each term on top and using eval()
#def poisson(u, b, d, nt, bc):
#    n = len(u.shape)
#    print(n)