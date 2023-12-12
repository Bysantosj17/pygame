import pygame, sys
pygame.init()

black = (  0,  0,  0)
white = (255,255,255)
red   = (255,  0,  0)

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

#Cordenadas de cuadro
coord_x = 10
coord_y = 10

#Velocidad
x_speed = 0
y_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        #EVENTOS TECLADO
        if event.type == pygame.KEYDOWN:
            #Izquierda y derecha
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            #Arriba y abajo
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        
        if event.type == pygame.KEYUP:
            #Izquierda y derecha
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            #Arriba y abajo
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
    
    screen.fill(white)
    
    coord_x += x_speed
    coord_y += y_speed
    
    pygame.draw.rect(screen, red, (coord_x, coord_y, 100, 100))
    
    pygame.display.flip()
    clock.tick(60)