import pygame, sys
from settings import DISPLAYSURF, colors



class Btn:
    def __init__(self, x, y, wx, wy, text, color=colors['cream']):
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy
        self.text = text
        self.color = color
        self.state = False

    def draw(self):
        pygame.draw.rect(
            DISPLAYSURF,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )

    def click_check(self, mouse):
        if (
            (self.x <= mouse[0] and self.x + self.wx >= mouse[0])
            and
            (self.y <= mouse[1] and self.y + self.wy >= mouse[1])
        ):
            return True

    def toggles_state(self):
        if self.state :
            self.state = False
            self.color = colors['cream']
        else:
            self.state = True
            self.color = colors['dark']
