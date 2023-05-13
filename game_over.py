import sys
import time

import pygame

import main
from Explosion import Explosion


def game_over(ennemies, display_surf, player, fps_clock):
    pygame.display.update()
    for entity in ennemies:
        entity.kill()
    contact_boum = pygame.mixer.Sound("sound/boum.mp3")
    contact_boum.set_volume(0.03)
    contact_boum.play()
    boum = Explosion(player.rect.center[0], player.rect.center[1])

    boum.draw(display_surf)

    # remove P1
    player.kill()
    player.rect.center = -1000, -1000
    player.draw(display_surf)
    pygame.display.update()
    fps_clock.tick(main.FPS)

    start_sleep = time.time()
    while time.time() - start_sleep < 2:
        main.quit_if_requested()
        pygame.display.update()
        fps_clock.tick(main.FPS)

    # display game over
    font = pygame.font.SysFont("Copperplate Gothic", 100)
    text = font.render("Game Over", True, main.BLACK)
    display_surf.fill(main.RED)
    display_surf.blit(text, (main.SCREEN_WIDTH / 2 - text.get_width() / 2, main.SCREEN_HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    fps_clock.tick(main.FPS)

    start_sleep = time.time()
    while time.time() - start_sleep < 2:
        main.quit_if_requested()
        pygame.display.update()
        fps_clock.tick(main.FPS)

    pygame.quit()
    sys.exit()
