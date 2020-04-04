import pygame, sys
from settings import (
    DISPLAYSURF,
    colors, grid_x, grid_y,
    nr_of_rows, nr_of_collumns,
    grid_start_x, grid_start_y
)


class Node:
    def __init__(self, x=None, y=None, name=None, prev_node=None):
        self.name = name
        self.prev_node = prev_node
        self.distance = 1000000000
        self.x = x
        self.y = y
        self.address = [x,y]
        self.wx= grid_x-1
        self.wy=grid_y-1
        self.color = colors['cream']

    def adjacent_addresses(self):
        vectors = (
            [-1*grid_x,0],
            [grid_x,0],
            [0,grid_y],
            [0,-1*grid_y],
        )
        return [ [self.x+v[0], self.y+v[1]] for v in vectors ]

    def click_check(self, mouse):
        if (
            (self.x <= mouse[0] and self.x + self.wx >= mouse[0])
            and
            (self.y <= mouse[1] and self.y + self.wy >= mouse[1])
        ):
            return True

    def draw(self):
        pygame.draw.rect(
            DISPLAYSURF,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )

# Create Matrix of Nodes
def create_grid(nr_of_rows, nr_of_collumns):
    node_list = []
    for row in range(nr_of_rows):
        for collumn in range(nr_of_collumns):
            node_list.append(
                Node(
                    name='{}-{}'.format(collumn, row),
                    x=collumn*grid_x+grid_start_y,
                    y=row*grid_x+grid_start_x,
                )
            )
    return node_list

node_list = create_grid(
    nr_of_rows,
    nr_of_collumns,
)
