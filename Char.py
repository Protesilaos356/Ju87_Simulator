import pygame
import random
import main


def get_start_pos():
    # random timings for the start y
    return random.randint(0, main.SCREEN_WIDTH), random.randint(-main.SCREEN_HEIGHT, 0)


class Char(pygame.sprite.Sprite):
    def __init__(self, char_type: str):
        super().__init__()
        self.base_image = pygame.transform.scale(pygame.image.load(f"images/{char_type}.png"), (400, 400))
        self.char_type = char_type

        self.angle = random.randint(0, 360)

        self.rotated_image = None
        self.rect = None
        self.compute_rotated_image()

    def compute_rotated_image(self):
        self.angle += random.randint(-1, 1)
        self.rotated_image = pygame.transform.rotate(self.base_image, self.angle)
        self.rect = self.rotated_image.get_rect()

    def update(self):
        self.compute_rotated_image()

        self.rect.move_ip(0, main.BACKGROUND_SPEED)
        if self.rect.bottom > main.SCREEN_HEIGHT + 50:
            self.rect.center = get_start_pos()

    def draw(self, surface):
        surface.blit(self.rotated_image, self.rect)
