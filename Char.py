import math

import pygame
import random
import main


def get_start_pos():
    # random timings for the start y
    return random.randint(0, main.SCREEN_WIDTH), random.randint(-main.SCREEN_HEIGHT, 0)


CHAR_SPEED = 3


class Char(pygame.sprite.Sprite):
    def __init__(self, char_type: str):
        super().__init__()
        self.base_image = pygame.transform.scale(pygame.image.load(f"images/{char_type}.png"), (47, 100))
        self.char_type = char_type

        self.angle = random.randint(0, 360)
        self.constant_adding_angle = random.randint(-100, 100) / 200

        #self.rotated_image = None
        self.rect = self.base_image.get_rect()
        self.compute_rotated_image()
        self.rect = self.rotated_image.get_rect()
        self.rect.center = get_start_pos()

    def compute_rotated_image(self):
        self.angle += self.constant_adding_angle
        self.rotated_image = pygame.transform.rotate(self.base_image, self.angle + 180)
        self.rect = self.rotated_image.get_rect(center=self.rect.center)
        # self.rect = self.rotated_image.get_rect()

    def update(self):
        self.compute_rotated_image()

        angle_rad = (self.angle - 90) / 180 * math.pi

        # move in the direction of the angle
        x = CHAR_SPEED * math.cos(angle_rad)
        self.rect.move_ip(x,
                          -CHAR_SPEED * math.sin(angle_rad) + main.BACKGROUND_SPEED)
        if self.rect.bottom > main.SCREEN_HEIGHT + 50:
            self.rect.center = get_start_pos()

    def draw(self, surface):
        surface.blit(self.rotated_image, self.rect)
