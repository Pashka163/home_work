import pygame
from pygame.locals import *
import math

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((640, 240))

start = (0, 0)
size = (0, 0)
drawing = False
shapes = []

running = True

def create_polygon(center, radius, sides):
    points = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    return points

def draw_predefined_shapes():

    pygame.draw.circle(screen, GREEN, (100, 60), 30, 2)

    pygame.draw.ellipse(screen, YELLOW, (200, 30, 80, 40), 2)

    triangle = create_polygon((400, 60), 30, 3)
    pygame.draw.polygon(screen, BLUE, triangle, 2)

    hexagon = create_polygon((500, 60), 30, 6)
    pygame.draw.polygon(screen, RED, hexagon, 2)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                start = event.pos
                size = 0, 0
                drawing = True

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                shapes.append(('ellipse', pygame.Rect(start, size), BLUE))
                drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    screen.fill(GRAY)
    draw_predefined_shapes()

    for shape in shapes:
        if shape[0] == 'ellipse':
            pygame.draw.ellipse(screen, shape[2], shape[1], 1)

    if drawing:
        pygame.draw.ellipse(screen, BLUE, (start, size), 1)
    pygame.display.update()

pygame.quit()