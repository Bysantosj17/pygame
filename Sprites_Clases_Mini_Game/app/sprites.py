import pygame,sys, random

white = (255, 255, 255)
black = (0, 0, 0)

class Covenat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("jugador_img.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        
        
pygame.init()

screen = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()

done = False

Covenat_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    Covenat1 = Covenat()
    Covenat1.rect.x = random.randrange(900)
    Covenat1.rect.y = random.randrange(600)
    
    Covenat_list.add(Covenat1)
    all_sprite_list.add(Covenat1)
    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    
    screen.fill(white)
    
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()