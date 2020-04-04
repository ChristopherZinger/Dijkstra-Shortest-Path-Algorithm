import pygame, sys
from settings import *
from pygame.locals import *
from nodes import node_list
import time
from settings import (
grid_start_x, grid_start_y,
colors
)
from random import randint
from buttons import Btn

'''
TODO:
-add text to buttons
'''
btn_width = 100
btn_gap = 5
btn_reset = Btn(
    grid_start_x+(btn_width + btn_gap), grid_start_y-40,
    btn_width ,35,'reset'
    )
btn_run = Btn(
    grid_start_x, grid_start_y-40,
    btn_width,35,'run',
    colors['orange']
    )
btn_endpoints = Btn(
    grid_start_x+((btn_width + btn_gap)*2), grid_start_y-40,
    btn_width,35,'start | end',
    )
btn_walls = Btn(
    grid_start_x+((btn_width + btn_gap)*3), grid_start_y-40,
    btn_width,35,'add walls',
    )

class Path:
    def __init__(self, start, end):
        self.start=None
        self.end=None
        self.set_start(start)
        self.set_end(end)

    def set_start(self, new_start):
        if self.start:
            self.start.distance = 1000000000
            self.start.color = colors['cream']
        self.start = new_start
        self.start.distance = 0
        self.start.color = colors['orange']

    def set_end(self, new_end):
        if self.end:
            self.end.color = colors['cream']
        self.end = new_end
        self.end.color = colors['dark']

    def find_path(self):
        global NODES_TO_CHECK, PATH
        nodes = [node for node in NODES_TO_CHECK]
        # find the shortest path
        while len(nodes) > 0:
            get_events()
            #create tuple with node and its distance
            nodes = [( node, node.distance ) for node in nodes]
            #sort the tuples
            sorted_nodes = sorted(nodes, key=lambda node: node[1])
            # create sorted node list
            nodes = [ node[0] for node in sorted_nodes ]
            nodes = self.check_nodes_around(nodes[0], nodes)
            render()
        # draw the path
        prev_node = PATH.end
        while prev_node != PATH.start:
            prev_node.color = colors['orange']
            prev_node = prev_node.prev_node
            render()

    def check_nodes_around(self,test_node, nodes):
        adjacent_addresses = test_node.adjacent_addresses()
        for address in adjacent_addresses:
            for node in nodes:
                if address == node.address:
                    if test_node.distance + 1 < node.distance:
                        node.prev_node = test_node
                        node.distance = test_node.distance + 1
        nodes.remove(test_node)
        test_node.color = colors['dark-beige'] if test_node != PATH.start and test_node != PATH.end else test_node.color
        return nodes






def add_endpoints():
    global NODES_TO_CHECK, PATH
    endpoints = [
        ['start','orange'],
        ['end','dark']
        ]

    #reset colors
    for node in NODES_TO_CHECK:
        node.color = colors['cream']

    #highlight hovered node
    for i, endpoint in enumerate(endpoints):
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    #highlight hovered node
                    for node in NODES_TO_CHECK:
                        if node.click_check(event.pos) and node != PATH.start and node != PATH.end:
                            node.color = colors['dark-beige']
                        else:
                            if node != PATH.start and node != PATH.end :
                                node.color = colors['cream']

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # set new start and end
                    for node in NODES_TO_CHECK:
                        if node.click_check(event.pos):
                            flag = False
                            if i == 0:
                                PATH.set_start(node)
                            else:
                                PATH.set_end(node)
            render()



def get_events():
    global PATH
    # check for exit
    for event in pygame.event.get():
        if event.type == QUIT:
            #exit
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # click btn_reset
            if btn_reset.click_check(event.pos):
                reset_grid()
            # click btn_run
            if btn_run.click_check(event.pos):
                PATH.find_path()
            # click btn_endpoints
            if btn_endpoints.click_check(event.pos):
                add_endpoints()
            #click  btn_walls
            if btn_walls.click_check(event.pos):
                btn_walls.toggles_state()
                if btn_walls.state:
                     remove_nodes()

        if event.type == pygame.KEYDOWN:
            # run path finder
            if event.key == pygame.K_RETURN:
                PATH.find_path()

def reset_grid():
    global NODES_TO_CHECK, PATH
    NODES_TO_CHECK = [node for node in node_list]
    for node in NODES_TO_CHECK:
        if node != PATH.start and node != PATH.end:
            node.color = colors['cream']



def render():
    global NODES_TO_CHECK
    # RENDER ELEMENTS
    for node in NODES_TO_CHECK:
        node.draw()
    # render buttons
    btn_reset.draw()
    btn_run.draw()
    btn_endpoints.draw()
    btn_walls.draw()
    # # reset first and last node color

    # UPDATE SURFACE
    pygame.display.update()
    fpsClock.tick(FPS) # control speed or FPS

def remove_nodes():
    global NODES_TO_CHECK, PATH
    flag_a = True
    flag_b = False
    while flag_a:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if clicked on grid start erasing nodes
                for node in NODES_TO_CHECK:
                    if node.click_check(event.pos):
                        flag_b=True
                        flag_a=False
                        break
                        print('startj ereasing')
        render()

    nodes_to_remove = []
    while flag_b:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                # hide the hovered nodes
                for node in NODES_TO_CHECK:
                    if node.click_check(event.pos) and node != PATH.start and node != PATH.end:
                        node.color = colors['beige']
                        nodes_to_remove.append(node)

            # stop removing
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag_b, flag_a = False, False

        render()
    # remove the nodes for real
    for node in nodes_to_remove:
        try:
            NODES_TO_CHECK.remove(node)
        except Exception as e:
            pass
    btn_walls.toggles_state()





if __name__=='__main__':

    PATH = Path(node_list[1],node_list[512])
    pygame.init()

    #Caption
    pygame.display.set_caption('Dijkstra Shortes Path Algorithm - Visualisation')
    NODES_TO_CHECK = [node for node in node_list]

    #Main Loop
    while True:

        DISPLAYSURF.fill(colors['beige'])
        get_events()

        #render all elements
        render()
