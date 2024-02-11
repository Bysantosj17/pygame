import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen =  a_game.screen
        
        self.image = pygame.transform.scale(pygame.image.load("./img/alien.png"),(60,70))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.juego =  a_game
        #self.velocidad_Alien = a_game.velocidad_Alien
        
    def update(self):
        #self.x +=  self.velocidad_Alien
        self.x += (self.juego.velocidad_Alien * self.juego.flota_dire)
        self.rect.x = self.x
        
        
    def checa_bordes(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        