import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.colorbala
        self.rect =  pygame.Rect(0,0, a_game.anchobala, a_game.altobala)
        self.rect.midtop = a_game.nave.rect.midtop
        self.juego =  a_game
        self.y = float(self.rect.y)
        self.bullets_allowed = 3
        self.aliensPuntaje = 50
        self.sonido = pygame.mixer.Sound("./sonido/disparo_1.wav")
        self.sonido.play()
        
        
    def update(self):
        self.y -= self.juego.velocidad
        self.rect.y = self.y
        self.bullets = self.juego.bullets
        self.aliens =  self.juego.aliens
        
        self.choques = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if self.choques:
            for aliens in self.choques.values():
                self.juego.score += self.aliensPuntaje * len(aliens)
                self.juego.tablaP.prep_score()
                self.juego.tablaP.checa_highScore()
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    