import pygame, sys
from settings import DISPLAYSURF, colors

pygame.init() # required to use pytgame fonts

class Btn:
    def __init__(self, x, y, wx, wy, text, color=colors['cream']):

        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy
        self.text = text
        self.color = color
        self.state = False
        self.font = pygame.font.SysFont("Agency FB", 21)
        self.text = self.font.render(text, True, colors['dark'])

    def draw(self):
        pygame.draw.rect(
            DISPLAYSURF,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )
        DISPLAYSURF.blit(self.text,
                (self.x + ((self.wx - self.text.get_width())//2) , self.y + ((self.wy - self.text.get_height())//2)))

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
