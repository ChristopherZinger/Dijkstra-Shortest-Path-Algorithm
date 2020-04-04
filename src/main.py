import pygame, sys
from settings import *
from pygame.locals import *
from nodes import node_list
from time import time
from settings import colors
from random import randint

# global START_FINDER, FIRST_NODE, LAST_NODE, NODES_TO_CHECK
START_FINDER = False
pygame.init()

#Caption
pygame.display.set_caption('Dijkstra Shortes Path Algorithm - Visualisation')

# Start and end
FIRST_NODE = node_list[1]
LAST_NODE = node_list[512]
FIRST_NODE.color = colors['dark']
LAST_NODE.color = colors['orange']
FIRST_NODE.distance = 0

current_node = FIRST_NODE
NODES_TO_CHECK = node_list


def check_nodes_around(test_node):
    global NODES_TO_CHECK
    adjacent_addresses = test_node.adjacent_addresses()
    for address in adjacent_addresses:
        for node in NODES_TO_CHECK:
            try:
                if address == node.address:
                    if test_node.distance + 1 < node.distance:
                        node.prev_node = test_node
                        node.distance = test_node.distance + 1
            except Exception as e:
                print(e)
    NODES_TO_CHECK.remove(test_node)
    test_node.color = colors['dark-beige']

def find_path():
    global NODES_TO_CHECK, START_FINDER, LAST_NODE, FIRST_NODE
    # find the shortest path
    while len(NODES_TO_CHECK) > 0:
        #create tuple with node and its distance
        nodes = [( node, node.distance ) for node in NODES_TO_CHECK]
        #sort the tuples
        sorted_nodes = sorted(nodes, key=lambda node: node[1])
        # create sorted node list
        NODES_TO_CHECK = [ node[0] for node in sorted_nodes ]
        check_nodes_around(NODES_TO_CHECK[0])
        render()



    prev_node = LAST_NODE
    while prev_node != FIRST_NODE:
        prev_node.color = colors['orange']
        prev_node = prev_node.prev_node
        render()
    START_FINDER = False

def render():
    # RENDER ELEMENTS
    for node in node_list:
        node.draw()

    # reset first and last node color
    FIRST_NODE.color=colors['orange']
    LAST_NODE.color=colors['dark']

    # UPDATE SURFACE
    pygame.display.update()
    fpsClock.tick(FPS) # control speed or FPS

c=0
#Main Loop
while True:

    DISPLAYSURF.fill(colors['beige'])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Remove node on click
            for node in node_list:
                if (
                    (node.x <= event.pos[0] and node.x + node.wx >= event.pos[0])
                    and
                    (node.y <= event.pos[1] and node.y + node.wy >= event.pos[1])
                    and
                    (node is not FIRST_NODE and node is not LAST_NODE)
                ):
                    NODES_TO_CHECK.remove(node)
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    START_FINDER = True


    if START_FINDER:
        find_path()

    # c+=1
    # print('loop: ', c)



    #render all elements
    render()
