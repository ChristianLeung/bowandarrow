import pygame, sys
pygame.init()
from bow import Bow
from arrow import Arrow
size=width,height=640,4800
SCREEN_DIM=width,height=600,700
SCREEN = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption('Hit The Target!')

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)
LIGHT_BLUE=(63,161,246)

bow = Bow()
arrow = Arrow()

while True:
    CLOCK.tick(FPS)
    SCREEN.fill(LIGHT_BLUE)

    SCREEN.blit(bow.image, bow.rect)
    SCREEN.blit(arrow.image, arrow.rect)
    bow.move()
    arrow.move()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # S
                arrow.moving= True
    arrow.move_up(bow)


pygame.quit()