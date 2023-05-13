import time

import pygame

from Explosion import Explosion
import main


def game_over():
    pygame.display.update()
    for entity in main.ennemies:
        entity.kill()
    Contact_boum = pygame.mixer.Sound("sound/boum.mp3")
    Contact_boum.set_volume(0.03)
    Contact_boum.play()
    boum = Explosion(main.player.rect.center[0], main.player.rect.center[1])

    boum.draw(main.DISPLAYSURF)

    # remove P1
    main.player.kill()
    main.player.rect.center = -1000, -1000
    main.player.draw(main.DISPLAYSURF)
    pygame.display.update()
    main.FramePerSec.tick(main.FPS)

    time.sleep(2)

    # display game over
    font = pygame.font.SysFont("Copperplate Gothic", 100)
    text = font.render("Game Over", True, main.BLACK)
    main.DISPLAYSURF.fill(main.RED)
    main.DISPLAYSURF.blit(text, (main.SCREEN_WIDTH / 2 - text.get_width() / 2, main.SCREEN_HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    main.FramePerSec.tick(main.FPS)

    time.sleep(2)

    pygame.quit()
    sys.exit()
