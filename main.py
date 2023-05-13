import math
import sys

import pygame
from pygame.locals import *

import Enemy
import Player
import game_over

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


def main():
    pygame.init()
    clock = pygame.time.Clock()

    display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_surf.fill(WHITE)
    pygame.display.set_caption("Game")

    player = Player.Player()

    ennemies = [Enemy.Enemy() for _ in range(10)]
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
                display_surf.blit(pygame.transform.scale(grass, (100, 100)), (x, y + bg_offset))

        # Draw ennemies
        player_coords = player.rect.center
        player_radius = player.rect.height / 2
        for ennemie in ennemies:
            ennemie.move()
            ennemie.draw(display_surf)

            # collision detection
            ennemie_coords = ennemie.rect.center
            ennemie_radius = ennemie.rect.height / 2
            if math.sqrt((player_coords[0] - ennemie_coords[0]) ** 2 + (player_coords[1] - ennemie_coords[1]) ** 2) < (
                    player_radius + ennemie_radius):
                game_over.game_over()

        player.draw(display_surf)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
