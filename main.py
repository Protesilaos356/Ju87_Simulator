import math
import sys

import pygame
from pygame.locals import *

import Char
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
    fps_clock = pygame.time.Clock()

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface.fill(WHITE)
    pygame.display.set_caption("Game")

    player = Player.Player()

    enemies = [Enemy.Enemy() for _ in range(10)]
    chars = [Char.Char("Sherman") for _ in range(5)]
    grass = pygame.image.load("images/grass.jpg")

    bg_offset = 0

    while True:
        quit_if_requested()
        player.update()

        # Make the background as a moving repetitive grass texture
        bg_offset += BACKGROUND_SPEED
        bg_offset = bg_offset % 100
        for x in range(0, SCREEN_WIDTH, 100):
            for y in range(-100, SCREEN_HEIGHT, 100):
                surface.blit(pygame.transform.scale(grass, (100, 100)), (x, y + bg_offset))

        for char in chars:
            char.update()
            char.draw(surface)

        # Draw enemies
        player_coords = player.rect.center
        player_radius = player.rect.height / 2

        for enemy in enemies:
            enemy.update()
            enemy.draw(surface)

            # collision detection
            enemy_coords = enemy.rect.center
            enemy_radius = enemy.rect.height / 2
            if math.sqrt((player_coords[0] - enemy_coords[0]) ** 2 + (player_coords[1] - enemy_coords[1]) ** 2) < (
                    player_radius + enemy_radius):
                game_over.game_over(enemies, surface, player, fps_clock)

        player.draw(surface)

        pygame.display.update()
        fps_clock.tick(FPS)


def quit_if_requested():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
