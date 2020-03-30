import pygame, sys
from settings import *
from pygame.locals import *
from nodes import node_list


pygame.init()

#Caption
pygame.display.set_caption('Dijkstra Shortes Path Algorithm - Visualisation')

#Main Loop
while True:

    DISPLAYSURF.fill(colors['black'])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for node in node_list:
        node.draw()
    # print('loop')

    # UPDATE SURFACE
    pygame.display.update()
    fpsClock.tick(FPS) # control speed or FPS
