import sys
import pygame

from time import sleep
from bullet import Bullet
from alien import Alien
from star import Star

def check_events(settings, screen, ship, aliens, bullets, stats, play_button, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, aliens, bullets, stats, score)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, score)

def check_keydown_events(event, settings, screen, ship, aliens, bullets, stats, score):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(settings, screen, ship, aliens, bullets, stats, score)

def check_play_button(settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, score):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        start_game(settings, screen, ship, aliens, bullets, stats, score)

def start_game(settings, screen, ship, aliens, bullets, stats, score):
    if not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        score.prep_images()
        settings.init_dynamic_settings()
        reset_game(settings, screen, ship, aliens, bullets)

def fire(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_limit:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, aliens, bullets, stars, stats, play_button, score):
    screen.fill(settings.bg_color)
    stars.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blitme()
    aliens.draw(screen)
    score.show_score()

    if not stats.game_active:
        play_button.draw()

    pygame.display.flip()

def update_bullets(settings, screen, ship, aliens, bullets, stats, score):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats, score)

def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats, score):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
        score.prep_score()
        check_high_score(stats, score)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        score.prep_level()
        create_fleet(settings, screen, ship, aliens)

def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()

def update_aliens(settings, screen, ship, aliens, bullets, stats, score):
    check_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, ship, aliens, bullets, stats, score)
    
    check_aliens_bottom(settings, screen, ship, aliens, bullets, stats, score)

def check_aliens_bottom(settings, screen, ship, aliens, bullets, stats, score):
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets, score)
            break        

def ship_hit(settings, screen, ship, aliens, bullets, stats, score):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        score.prep_ships()
        reset_game(settings, screen, ship, aliens, bullets)
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def reset_game(settings, screen, ship, aliens, bullets):
    aliens.empty()
    bullets.empty()
    create_fleet(settings, screen, ship, aliens)
    ship.center_ship()

def check_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_direction(settings, aliens)
            break

def change_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed
    settings.alien_direction *= -1

def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    max_alien_x = get_max_alien_x(settings, alien.rect.width)
    max_alien_y = get_max_alien_y(settings, ship.rect.height, alien.rect.height)

    for number_x in range(max_alien_x):
        for number_y in range(max_alien_y):
            creat_alien(settings, screen, aliens, number_x, number_y)

def get_max_alien_x(settings, alien_width):
    avl_space_x = settings.screen_width - 2 * alien_width
    max_alien_x = int(avl_space_x / (2 * alien_width))
    return max_alien_x

def get_max_alien_y(settings, ship_height, alien_height):
    avl_space_y = settings.screen_height - 2 * alien_height - ship_height
    max_alien_y = int(avl_space_y / alien_height)
    return max_alien_y

def creat_alien(settings, screen, aliens, number_x, number_y):
    alien = Alien(settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * number_x
    alien.y = alien.rect.height + alien.rect.height * number_y
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_stars(settings, screen, stars):
    max_stars = int((settings.screen_width + settings.screen_height) / 100)
    for number in range(max_stars):
        new_star = Star(settings, screen)
        stars.add(new_star)