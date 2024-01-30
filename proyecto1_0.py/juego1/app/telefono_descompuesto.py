import pygame

#Tamaño de la pantalla
ANCHO = 1000
ALTO = 800

#FPS
FPS = 30

#Paleta de colores
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

#Fuetes
Consolas = pygame.font.match_font('consolas')
arial = pygame.font.match_font('arial')
times = pygame.font.match_font('times')

#Inicializacion de Pygame, creacion de la ventana, tituloy control de reloj
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))

#Fondo del juegp
pygame.display.set_caption("Telefono descompuesto")
clock = pygame.time.Clock()

ejecutando =  True
while ejecutando:
    #Es lo que especifica  la velocidad del bucle de juego
    clock.tick(FPS)

    #Eventos
    for event in pygame.event.get():
        #Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
            
    pygame.display.flip()
    
    #Dibuja los textos en la pantalla
    
pygame.quit()

import pygame, sys

