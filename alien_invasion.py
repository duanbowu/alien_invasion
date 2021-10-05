import pygame

import game_functions as gf

from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(settings)
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()

    play_button = Button(settings, screen, "Play")
    score = Scoreboard(settings, screen, stats)

    gf.create_fleet(settings, screen, ship, aliens)
    gf.create_stars(settings, screen, stars)

    while True:
        gf.check_events(settings, screen, ship, aliens, bullets, stats, play_button, score)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets, stats, score)
            gf.update_aliens(settings, screen, ship, aliens, bullets, stats, score)
        
        gf.update_screen(settings, screen, ship, aliens, bullets, stars, stats, play_button, score)

run_game()