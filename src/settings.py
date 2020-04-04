import pygame, sys, os
BASE_DIR =  os.path.dirname(os.path.realpath(__file__))

# Display settings
FPS = 45

# grid
grid_x, grid_y = 25, 25
offset_x, offset_y = 100, 100
grid_start_x, grid_start_y = offset_x-(grid_x/2), offset_y-(grid_y/2)
nr_of_rows, nr_of_collumns = 25, 25

#Window
window_size = (
    nr_of_rows*grid_x+(offset_x*2),
    nr_of_collumns*grid_y+(offset_y*2)
    )
game_area = (300,700)
DISPLAYSURF = pygame.display.set_mode(window_size)
DISPLAYSURFALPHA = DISPLAYSURF.convert_alpha()

#Colors
colors = {
    'cian': (0,255,255),
    'white': (255,255,255),
    'red': (255,0,0),
    'blue': (0,0,255),
    'green': (0,255,0),
    'black': (0,0,0),
    'light-green': (0, 255, 119),
    'gray': (70,70,70),
    'beige':(216,213,206),
    'cream':(246,237,219),
    'dark':(34,34,34),
    'orange':(163,125,86),
    'dark-beige':(174,167,151),
}

#clock
fpsClock = pygame.time.Clock()
