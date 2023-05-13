import math
import time

import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

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

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

SPEED = 8
BACKGROUND_SPEED = 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Sfire.png"), (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.get_start_pos()

    def get_start_pos(self):
        # random timings for the start y
        return random.randint(0, SCREEN_WIDTH), random.randint(-1000, 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.rect.top = 0
            self.rect.center = self.get_start_pos()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Player.png"), (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 858)

        self.height_limit = 500

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        is_diagonal = pressed_keys[K_UP] and pressed_keys[K_LEFT] or pressed_keys[K_UP] and pressed_keys[K_RIGHT] or \
                      pressed_keys[K_DOWN] and pressed_keys[K_LEFT] or pressed_keys[K_DOWN] and pressed_keys[K_RIGHT]
        speed = SPEED if not is_diagonal else SPEED / math.sqrt(2)

        if SCREEN_HEIGHT - self.rect.top < self.height_limit and pressed_keys[K_UP]:
            self.rect.move_ip(0, -speed)
        if SCREEN_HEIGHT - self.rect.bottom > 130 and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, speed)

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(speed, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/boum.gif"), (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


player = Player()

ennemies = [Enemy() for i in range(10)]
grass = pygame.image.load("images/grass.jpg")

bg_offset = 0


def game_over():
    pygame.display.update()
    for entity in ennemies:
        entity.kill()
    boum = Explosion(player.rect.center[0], player.rect.center[1])
    boum.draw(DISPLAYSURF)

    # remove P1
    player.kill()
    player.rect.center = -1000, -1000
    player.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(FPS)

    time.sleep(2)

    # display game over
    font = pygame.font.SysFont("Copperplate Gothic", 100)
    text = font.render("Game Over", True, BLACK)
    DISPLAYSURF.fill(RED)
    DISPLAYSURF.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    FramePerSec.tick(FPS)

    time.sleep(2)

    pygame.quit()
    sys.exit()


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
