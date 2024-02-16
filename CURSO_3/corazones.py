import pygame
from pygame.sprite import Sprite


class corazones(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen =  a_game.screen
        self.screen_rect =  a_game.screen.get_rect()
        self.image = pygame.image.load("./img/corazon.png")
        self.rect = self.image.get_rect()