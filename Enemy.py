import random

import pygame

import main

ENEMY_SPEED = 10


def get_start_pos():
    # random timings for the start y
    return random.randint(0, main.SCREEN_WIDTH), random.randint(-main.SCREEN_HEIGHT, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Sfire.png"), (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = get_start_pos()

    def update(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.bottom > main.SCREEN_HEIGHT + 50:
            self.rect.center = get_start_pos()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
