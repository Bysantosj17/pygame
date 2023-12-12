import pygame, sys
pygame.init()

black = (  0,  0,  0)
white = (255,255,255)
red   = (255,  0,  0)

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(white)
    
    pygame.draw.rect(screen, red, ( x, y, 100, 100))
    pygame.display.flip()
    clock.tick(60)