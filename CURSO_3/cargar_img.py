import pygame,sys

class Nave:
    def __init__(self, a_game):
        self.screen =  a_game.screen
        self.screen_rect =  a_game.screen.get_rect()
        self.img =  pygame.image.load("./img/idle1.png")
        self.rect = self.img.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.mover_derecha = False
        self.mover_izquierda =  False
    
    def mover(self):
        if self.mover_derecha and self.rect.right < self.screen_rect.right:
            self.rect.x += 0.7
        if self.mover_izquierda and self.rect.left > 0:
            self.rect.x -= 0.7
        
        
    def corre(self):
        self.screen.blit(self.img, self.rect)