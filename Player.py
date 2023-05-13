import math

import pygame
import main


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Player.png"), (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 858)

        self.height_limit = 500

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        is_diagonal = pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_RIGHT] or \
                      pressed_keys[pygame.K_DOWN] and pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_DOWN] and pressed_keys[pygame.K_RIGHT]
        speed = main.SPEED if not is_diagonal else main.SPEED / math.sqrt(2)

        if main.SCREEN_HEIGHT - self.rect.top < self.height_limit and pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -speed)
        if main.SCREEN_HEIGHT - self.rect.bottom > 130 and pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, speed)

        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if self.rect.right < main.SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(speed, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
