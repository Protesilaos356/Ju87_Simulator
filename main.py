import math
import sys

import pygame
from pygame.locals import *

import Enemy
import Player
from game_over import game_over

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (4, 186, 5)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (122, 122, 122)
# Screen information
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SPEED = 8
BACKGROUND_SPEED = 5

FPS = 60

DISPLAYSURF = None

player = None

ennemies = []

def main():
    global DISPLAYSURF, player, ennemies

    pygame.init()
    FramePerSec = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")

    player = Player.Player()

    ennemies = [Enemy.Enemy() for i in range(10)]
    grass = pygame.image.load("images/grass.jpg")

    bg_offset = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        player.update()

        # Make the background as a moving repetitive grass texture
        bg_offset += BACKGROUND_SPEED
        bg_offset = bg_offset % 100
        for x in range(0, SCREEN_WIDTH, 100):
            for y in range(-100, SCREEN_HEIGHT, 100):
                DISPLAYSURF.blit(pygame.transform.scale(grass, (100, 100)), (x, y + bg_offset))

        # Draw ennemies
        player_coords = player.rect.center
        player_radius = player.rect.height / 2
        for ennemie in ennemies:
            ennemie.move()
            ennemie.draw(DISPLAYSURF)

            # collision detection
            ennemie_coords = ennemie.rect.center
            ennemie_radius = ennemie.rect.height / 2
            if math.sqrt((player_coords[0] - ennemie_coords[0]) ** 2 + (player_coords[1] - ennemie_coords[1]) ** 2) < (
                    player_radius + ennemie_radius):
                game_over()

        player.draw(DISPLAYSURF)

        pygame.display.update()
        FramePerSec.tick(FPS)



if __name__ == "__main__":
    main()