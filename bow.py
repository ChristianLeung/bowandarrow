import pygame

class Bow(pygame.sprite.Sprite):

    # Define constant values
    IMAGE = pygame.image.load('assets/bow3.png')
    SIZE = (256,256)
    SCREEN_DIM=(790,790)
    MOVE_DIST=10
    Bow_pos = (-20, 480)
    # Creates a frog object
    def __init__(self):
        # sprite setup
        super().__init__()
        self.image = Bow.IMAGE
        self.rect = pygame.Rect((0, 0), Bow.SIZE)
        self.rect.center = Bow.Bow_pos
        self.direction=True
        self.x_position=0
    def move(self):
        if(self.direction):
            if (self.rect.centerx<=60):
                self.direction=False
            self.rect.centerx-=Bow.MOVE_DIST
        else:
            if(self.rect.centerx>=Bow.SCREEN_DIM[0]-250):
                self.direction=True
            self.rect.centerx+=Bow.MOVE_DIST