import pygame

import main

class Char(pygame.sprite.Sprite):
    def __init__(self, chartype):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("image/Sherman.png"), (400, 400)
        self.chartype = (sherman)