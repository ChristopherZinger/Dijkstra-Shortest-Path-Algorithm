import pygame, sys
from settings import *
from pygame.locals import *
from nodes import node_list
from time import time
from settings import colors
from random import randint


pygame.init()

#Caption
pygame.display.set_caption('Dijkstra Shortes Path Algorithm - Visualisation')


# Clock
last_time = time()
active_node = node_list[0]
active_node.color = colors['orange']

# Start and end
first_node = node_list[1]
last_node = node_list[512]
first_node.color = colors['dark']
last_node.color = colors['orange']
first_node.distance = 0

current_node = first_node
nodes_to_check = node_list

def check_nodes_around(test_node):
    adjacent_addresses = test_node.adjacent_addresses()
    for address in adjacent_addresses:
        for node in nodes_to_check:
            try:
                if address == node.address:
                    node.prev_node = test_node
                    node.distance = node.distance+1 if node.distance<999999999 else 1
            except Exception as e:
                print(e)
    nodes_to_check.remove(test_node)
    test_node.color = colors['dark-beige']
    # print(nodes_to_check)
    # print(' ')



#Main Loop
while True:

    DISPLAYSURF.fill(colors['beige'])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if len(nodes_to_check) > 0:
        nodes = [( node, node.distance ) for node in nodes_to_check]
        sorted_nodes = sorted(nodes, key=lambda node: node[1])
        nodes_to_check = [ node[0] for node in sorted_nodes ]
        check_nodes_around(nodes_to_check[0])
    else:
        prev_node = last_node

        while prev_node != first_node:
            prev_node.color = colors['orange']
            prev_node = prev_node.prev_node

    first_node.color=colors['orange']
    last_node.color=colors['dark']
    # check if node needs to be updated
    # if time() != last_time:
    #     last_time=time()
    #     new_node = None
    #     counter = 0
    #     while new_node == None:
    #
    #         # find new direction
    #         x,y = 0, 0
    #         while x == 0 and y==0:
    #             x = randint(-1,1) *25
    #             y = randint(-1,1) *25
    #         print('x: ', x)
    #         print('y: ', y)
    #         # check if node exists in the list
    #         for node in node_list:
    #             if node.x == active_node.x + x and node.y == active_node.y + y:
    #                 new_node = node
    #         print('inloop')
    #         counter += 1
    #         if counter > 500:
    #             print(' pres 1 to exit')
    #             choice = input()
    #             if choice == "1":
    #                 break
    #     active_node.color = colors['dark-beige']
    #     node_list.remove(active_node)
    #     active_node = new_node
    #     active_node.color = colors['orange']









    # RENDER ELEMENTS
    for node in node_list:
        node.draw()
    # print('loop')

    # UPDATE SURFACE
    pygame.display.update()
    fpsClock.tick(FPS) # control speed or FPS
