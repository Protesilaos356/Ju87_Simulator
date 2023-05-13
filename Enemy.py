import random

import pygame

import main


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Sfire.png"), (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.get_start_pos()

    def get_start_pos(self):
        # random timings for the start y
        return random.randint(0, main.SCREEN_WIDTH), random.randint(-1000, 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > main.SCREEN_HEIGHT + 50:
            self.rect.top = 0
            self.rect.center = self.get_start_pos()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
