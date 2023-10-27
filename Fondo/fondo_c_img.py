import pygame,sys
pygame.init()

screen = pygame.display.set_mode((768,480))
clock = pygame.time.Clock()

done = False

background = pygame.image.load("./Fondo/fondo_img.jpg").convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    
    screen.blit(background, [ 0, 0])
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()