import pygame, sys
from cargar_img import *
from bala import *
from alien import *

class GalagaPirata:
    def __init__(self):
        pygame.init()
        self.ancho = 800
        self.alto = 500
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Galaga Pirata")
        self.color = (230, 230, 230)
        self.velocidad = 1
        self.anchobala = 3
        self.altobala = 15
        self.colorbala = (255, 0, 0) 
        self.nave = Nave(self)
        self.bullets =  pygame.sprite.Group()
        self.balas_totales = 3
        self.aliens =  pygame.sprite.Group()
        self._create_fleet()
        
    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = True
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = True
                    
                    if event.key == pygame.K_SPACE:
                        self.fire_bullet()
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False
                        
                        
            self.nave.mover()
            self.screen.fill(self.color)
            self.nave.corre()
            self.bullets.update()
            
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
                
            pygame.display.flip()
            
    def fire_bullet(self):
        if self.balas_totales != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.balas_totales =  self.balas_totales - 1
            
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        availableSpace = self.ancho - (2 * alien_width)
        numerodeAlien = availableSpace // ( 1 * alien_width)
        
        for numeroAlien in range(numerodeAlien):
            alien =  Alien(self)
            alien.x = alien_width + 2* alien_width * numeroAlien
            alien.rect.x =  alien.x
            self.aliens.add(alien)
        
        #self.aliens.add(alien)
        
            
if __name__ == "__main__":
    a = GalagaPirata()
    a.corre_juego()