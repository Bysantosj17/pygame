import pygame, random
from pygame.locals import *
import sys

#Iniciar pygame
pygame.init()

#Crear ventana
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

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
for i in range(5):
    a = random.randint(40, 100)
    b = random.randint(40, 100)
    c = random.randint(40, 100)
    d = random.randint(40, 100)
    box = pygame.Rect(a, b, c, d)
    boxes.append(box)
    


#Bucle del juego
run = True
while run:
    
    for box in boxes:
        pygame.draw.rect(PANTALLA, RED, box)
    
    for event in pygame.event.get():   
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num
                        

        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].move_ip(event.rel)
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 0:
                    active_box = None
                
        if event.type == pygame.QUIT:
            run = False         
            
    CUADRO = pygame.draw.rect(PANTALLA, BLUE, (400, 70, 550, 500))
        
        
    pygame.display.update()
    
pygame.quit()

