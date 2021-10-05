import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        if randint(0, 100) % 2 == 0:
            self.image = pygame.image.load('images/star_big.bmp')
        else:
            self.image = pygame.image.load('images/star_small.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(0, self.settings.screen_height)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)