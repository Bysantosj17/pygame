import pygame, sys
pygame.init()

#Definir los colores
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#Definir un relog
#Controlador de FPS
clock = pygame.time.Clock()

#Cordenadas del cuadrado
cord_x = 400
cord_y = 200

#Velocidad a la que se movera mi cuadrado
speed_x = 3
speed_y = 3


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    cord_x += speed_x
    #Color de fondo
    screen.fill(WHITE)
    ### ----- ZONA DE DIBUJO

    pygame.sprite.draw(screen, RED, (cord_x, cord_y, 80, 80))
    
    ### ----- ZONA DE DIBUJO
    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
