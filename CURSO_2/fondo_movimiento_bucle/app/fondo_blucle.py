import pygame
from pygame.locals import *
import sys

#Iniciacion de pygame
pygame.init()

#Pantalla -ventana
W,H = 800, 475
PANTALLA = pygame.display.set_mode((W,H))
FPS = 2000
RELOJ = pygame.time.Clock()

#Fondo del juegp
fondo = pygame.image.load('./fondo_movimiento_bucle/img/fondo.jpg').convert()
x = 0

#Icono y titulo
pygame.display.set_caption("santos 1.1")
icono = pygame.image.load('./fondo_movimiento_bucle/iconos/jugador_img.png')
pygame.display.set_icon(icono)

#Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width ,0))
    if x_relativa < W:
        PANTALLA.blit(fondo,(x_relativa,0))
    
    x -= 1
    pygame.display.update()
    RELOJ.tick(FPS)