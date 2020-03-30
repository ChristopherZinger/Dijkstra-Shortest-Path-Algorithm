import pygame, sys
from settings import (
    DISPLAYSURF,
    colors, grid_x, grid_y,
    nr_of_rows, nr_of_collumns,
    grid_start_x, grid_start_y
)


class Node:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.wx= grid_x-1
        self.wy=grid_y-1
        self.color = colors['white']

        print(self.x)

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
                    x=row*grid_x+grid_start_x,
                    y=collumn*grid_x+grid_start_y
                )
            )
    return node_list

node_list = create_grid(
    nr_of_rows,
    nr_of_collumns,
)
