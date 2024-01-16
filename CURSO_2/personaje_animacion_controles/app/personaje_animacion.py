import pygame
from pygame.locals import *
import sys

#Iniciacion de Pygame
pygame.init()

#Pantalla - ventana
W,H = 800, 500
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("santos 1.2")
icono =  pygame.image.load('./personaje_animacion_controles/iconos/jugador_img.png')