import pygame, sys, math
from pygame.locals import *

height = 400
width = 500
p_height = 30
p_width = 10
pygame.init()
disp = pygame.display.set_mode((width, height), 0, 32)

def draw_paddle(x, center_y, height, col):
    y = center_y - height / 2
    pygame.draw.rect(disp, col, (x, y, p_width, height))

def draw_ball(x, y, col):
    pygame.draw.circle(disp, col, (x, y), 5)

def collides(left, rect_width, rect_height, rect_x, rect_y, bx, by, r):
    if by - r <= rect_y + rect_height / 2 and by + r >= rect_y - rect_height / 2:
        if left:
            return bx - r <= rect_x + rect_width
        else:
            return bx + r >= rect_x - rect_width
    return False

def main():
    fY = lambda y: abs(40 * math.sin((math.pi * y) / 200))

    p1 = height / 2
    p2 = height / 2

    white = (255,255,255)
    blue = (0,0,255)
    red = (255,0,0)

    dx = 0.2
    dy = 0.1
    pdy0 = 0
    pdy1 = 0
    bx = width // 2
    by = height // 2

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60)
        bx += dx * dt
        by += dy * dt
        p1 += pdy1 * dt
        p2 += pdy0 * dt#p2 = by

        disp.fill(white)
        draw_paddle(width - 12 - fY(p2), p2, p_height, blue)
        draw_paddle(2 + fY(p1), p1, p_height, blue)#2 + fY(p1)
        draw_ball(int(bx), int(by), red)

        if collides(True, p_width, p_height, 2 + fY(p1), p1, bx, by, 5):
            dx = -dx
        elif collides(False, p_width, p_height, width - 2 - fY(p2), p2, bx, by, 5):
            dx = -dx

        if by - 5 <= 0 or by + 5 >= height: dy = -dy
        if bx <= 0 or bx >= width:
            bx = width // 2
            by = height // 2
            dx = 0.2
            dy = 0.1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pdy1 = -0.2
                if event.key == pygame.K_s:
                    pdy1 = 0.2
                if event.key == pygame.K_UP:
                    pdy0 = -0.2
                if event.key == pygame.K_DOWN:
                    pdy0 = 0.2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pdy0 = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    pdy1 = 0

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
