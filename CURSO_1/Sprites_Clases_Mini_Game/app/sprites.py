import pygame,sys, random

white = (255, 255, 255)
black = (0, 0, 0)

class Covenat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Sprites_Clases_Mini_Game/img/covenant_img.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
class MaterChef(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Sprites_Clases_Mini_Game/img/jugador_img.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
        
pygame.init()

screen = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()
score = 0

done = False

Covenat_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

player = MaterChef()
all_sprite_list.add(player)

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
            
    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]
    
    Covena_hit_list = pygame.sprite.spritecollide(player, Covenat_list, True)
    
    for Covenat in Covena_hit_list:
        score += 1
        print(score)
    
    screen.fill(white)
    
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()