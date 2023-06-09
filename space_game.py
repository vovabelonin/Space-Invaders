import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import Score

def run():

    pygame.init()
    screen = pygame.display.set_mode((700,620))
    pygame.display.set_caption("Space defenders")
    bg_color = (0, 1, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Score(screen, stats)
    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game == True:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, gun, aliens, bullets)



run()