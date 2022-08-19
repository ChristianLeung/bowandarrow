import pygame
from bow import Bow

class Arrow(pygame.sprite.Sprite):

    # Define constant values
    IMAGE = pygame.image.load('assets/arrow3.png')
    SIZE = (150, 150)
    SCREEN_DIM = (790, 790)
    MOVE_DIST = 10

    Arrow_pos = (-20, 480)

    def __init__(self):
        # sprite setup
        super().__init__()
        self.image = Arrow.IMAGE
        self.rect = pygame.Rect((0, 0), Arrow.SIZE)
        self.rect.center = Arrow.Arrow_pos
        self.direction = True
        self.x_position = 0
        self.moving = False

    def move(self):
        if (self.direction):
            if (self.rect.centerx <= 55):
                self.direction = False
            self.rect.centerx -= Arrow.MOVE_DIST
        else:
            if (self.rect.centerx >= Arrow.SCREEN_DIM[0] - 266):
                self.direction = True
            self.rect.centerx += Arrow.MOVE_DIST

    def move_up(self, bow):
        if self.moving:

            if self.rect.top >=  -85:
                self.rect.centery -= Arrow.MOVE_DIST
            else:
                self.moving = False
                self.rect.center = bow.rect.center
                self.direction=bow.direction