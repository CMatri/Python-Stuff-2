import numpy as np

class Fluid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.gsize = w * h
        self.u = np.zeros((self.gsize))
        self.v = np.zeros((self.gsize))
        self.u_prev = np.zeros((self.gsize))
        self.v_prev = np.zeros((self.gsize))
        self.dens = np.zeros((self.gsize))
        self.dens_prev = np.zeros((self.gsize))

    def ix(self, i, j):
        return i + self.w * j

    def add_source(self, x, s, dt):
        x += s * dt

    def diffuse(self, x, x0, diff, dt):
        i = j = k = 0
        a = dt * diff * self.gsize

        for k in range(20):
            for i in range(1, self.w - 1):
                for j in range(1, self.h - 1):
                    x[self.ix(i, j)] = (x0[self.ix(i, j)] + a * (x[self.ix(i - 1, j)] + x[self.ix(i + 1, j)] + x[self.ix(i, j - 1)] + x[self.ix(i, j + 1)])) / (1 + 4 * a)
