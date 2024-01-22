import pygame
import random
import sys

pygame.init()

class celular(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./juego_1/img/celular.jpg").convert()
        self.image.set_colorkey()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
def salir():
    pygame.quit()
    sys.exit()

#colors
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

numero = "numero"

#game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
title = pygame.display.set_caption('telefono_descompuesto')
telefono = pygame.image.load('./juego_1/icono/icono_telefono.png')
pygame.display.set_icon(telefono)




active_box = None
boxes = []
for i in range(9):
    caja1 = random.randint(50, 50)
    b = random.randint(50, 50)
    c = random.randint(50, 50)
    d = random.randint(50, 50)
    box = pygame.Rect(caja1, b, c, d)
    boxes.append(box)
    
boxes = []
for j in range(9):
    e = random.randint(50, 50)
    f = random.randint(50, 50)
    g = random.randint(50, 50)
    h = random.randint(50, 50)
    box = pygame.Rect(e, f, g, h)
    boxes.append(box)
    
celular_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(1):
    celular1 = celular()
    celular1.rect.x = (650)
    celular1.rect.y = (25)
    
    celular_list.add(celular1)
    all_sprite_list.add(celular1)

run = True
while run:

    screen.fill(WHITE)
    
    all_sprite_list.draw(screen)

    #update and draw items
    for box in boxes:
        pygame.draw.rect(screen, "blue", box)
        
        
    salir = pygame.draw.rect(screen, "red", (100, 100, 50, 50))  

    for event in pygame.event.get():                                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num
                        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None

        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].move_ip(event.rel)
                                        
    pygame.display.flip()
        
pygame.quit()
sys.exit()
