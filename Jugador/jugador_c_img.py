import pygame,sys
pygame.init()

screen = pygame.display.set_mode((768,480))
clock = pygame.time.Clock()

done = False

background = pygame.image.load("./Fondo/fondo_img.jpg").convert()

player = pygame.image.load("./Jugador/jugador_img.png").convert()
player.set_colorkey([0, 0 ,0])

pygame.mouse.set_visible(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    
    screen.blit(background, [ 0, 0])
    screen.blit(player, [x,y])
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()