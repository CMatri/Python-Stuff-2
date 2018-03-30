from fluid import Fluid
import numpy as np
import pygame, sys, math
from pygame import surfarray
from pygame.locals import *
surfarray.use_arraytype('numpy')

w = h = 800

fluid = Fluid(w, h)

data = np.zeros((w * h))
data[fluid.ix(5, 2):fluid.ix(20, 20)] = 2

#for i in range(10):
#    print(i)
#    fluid.diffuse(fluid.dens, data, 0.8)

pygame.init()
disp = pygame.display.set_mode((w, h), 0, 32)
clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)
    print(dt)
    #fluid.diffuse(fluid.dens, data, 0.8, dt)
    #fluid.add_source(fluid.dens, data, dt)

    striped = np.zeros((w, h, 3), np.int32)
    striped[:] = (0, 0, 0)
    striped[1:30, 2:50] = (255, 255, 255)
    print(fluid.dens.shape)
    dens_img = np.resize(fluid.dens, (w, h, 3))
    #dens_img = np.array([fluid.dens.reshape((w, h))] * 3).reshape((w, h, 3))
    surfarray.blit_array(disp, dens_img)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
              pos = pygame.mouse.get_pos()
              data = np.zeros((w * h))
              print(data.shape)
              data[10:20] = 200#fluid.ix(pos[0] - 5, pos[1] - 5):fluid.ix(pos[0] + 5, pos[1] + 5)
              fluid.add_source(fluid.dens, data, dt)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
