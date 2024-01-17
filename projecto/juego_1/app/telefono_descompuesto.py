import pygame
from pygame.locals import *
import sys

#Iniciar pygame
pygame.init()

#Crear ventana
w,h = 1000, 650
PANTALLA = pygame.display.set_mode((w,h))

#Crear telefono
telefono = pygame.image.load('./juego_1/img/celular.jpg').convert()
PANTALLA.blit(telefono,(0,20))

#Icono y titulo
pygame.display.set_caption("Telefono descompuesto")
icono = pygame.image.load('./juego_1/icono/icono_telefono.png')
pygame.display.set_icon(icono)

#numeros
boxes = []
for i in range(2):
    x

#Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()    
    pygame.display.update()

