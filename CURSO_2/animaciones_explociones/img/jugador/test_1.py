import pygame
import random
import os

carpeta_juego = os.path.dirname(__file__)

carpeta_imagenes = os.path.join(carpeta_juego, "img")



#Tamaño
ANCHO = 800
ALTO = 600

#FPS
FPS = 30

#Paleta de colores
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

#Fuete
Consolas = pygame.font.match_font('consolas')
arial = pygame.font.match_font('arial')
times = pygame.font.match_font('times')

