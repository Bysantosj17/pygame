import pygame, sys
from cargar_img import *
from bala import *
from alien import *
from estadisticas import *
from time import sleep
from botones import *
from puntajes import *

class GalagaPirata:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.ancho = 700
        self.alto = 700
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Galaga Pirata")
        self.color = (230, 230, 230)
        self.velocidad = 1
        self.anchobala = 3
        self.altobala = 15
        self.colorbala = (255, 0, 0)
        self.naves_restantes = 1
        self.nave = Nave(self)
        self.bullets =  pygame.sprite.Group()
        self.balas_totales =100
        self.aliens =  pygame.sprite.Group()
        self.velocidad_Alien = 0.5
        self.flota_veocidad = 150
        self.flota_dire = .5
        self.juego_activado = False
        self.estadisticas = Estadisticas(self)
        self.tablaP = Puntaje(self)
        self.play_boton = Boton(self, "Play")
        
        #Musica
        pygame.mixer.music.load("./musica/ambiente_1.wav")
        #play Musica
        pygame.mixer.music.play(-1)
        #Sonido de la musica
        pygame.mixer.music.set_volume(0.0)
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    self.checaBoton(mousePos)
                        
            if self.juego_activado:    
                self.nave.mover()
                self.screen.fill(self.color)
                self.nave.corre()
                self.bullets.update()
                self.update_alien()
            
                for bullet in self.bullets.copy():
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
                
                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()
                self.aliens.draw(self.screen)  
                
                
                
            
            if not self.juego_activado:
                self.play_boton.Dibuja_boton()
                
            pygame.display.flip()
            
    def fire_bullet(self):
        if self.balas_totales != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.balas_totales =  self.balas_totales - 1
            
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availableSpace = self.ancho - (1 * alien_width)
        numerodeAliens = availableSpace // ( 2 * alien_width)
        nave_height = self.nave.rect.height
        availableSpacey = self.alto - (3 * alien_height) - nave_height
        numerodeFilas = availableSpacey // (2 * alien_height)
        
        for fila in range(numerodeFilas):
            for numeroAlien in range(numerodeAliens):
                self._create_alien(numeroAlien, fila)
                
    def _create_alien(self, numeroAlien, fila):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * numeroAlien
        alien.rect.x =  alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * fila
        self.aliens.add(alien)
        
    def checa_bordesFlota(self):
        for alien in self.aliens.sprites():
            if alien.checa_bordes():
                self.cambia_dire()
                break
            
    def cambia_dire(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.flota_veocidad
        self.flota_dire *= -1
        
            
    def update_alien(self):
        self.checa_bordesFlota()
        self.aliens.update()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        if pygame.sprite.spritecollideany(self.nave, self.aliens):
            self.nave_colisionada()
            
    def nave_colisionada(self):
        if self.naves_restantes > 1:
            self.naves_restantes -= 1
            
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.nave.centrar_nave()
            
            sleep(0.5) 
            
        else: 
            self.juego_activado = False
            
    def checaBoton(self, mousePos):
        self.boton_inicio = self.play_boton.rect.collidepoint(mousePos)
        if self.boton_inicio and not self.juego_activado:
            self.estadisticas.reini()
            self.juego_activado = True
            
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.nave.centrar_nave()
                
if __name__ == "__main__":
    a = GalagaPirata()
    a.corre_juego()