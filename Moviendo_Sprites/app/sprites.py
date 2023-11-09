import pygame,sys, random

white = (255, 255, 255)
black = (0, 0, 0)

class Covenat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Sprites_Clases_Mini_Game/img/covenant_img.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.rect.y = -100
            self.rect.x = random.randrange(900)
        
class MaterChef(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Sprites_Clases_Mini_Game/img/jugador_img.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.y = mouse_pos[1]
        player.rect.x = mouse_pos[0]
        
        
pygame.init()

pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()
score = 0

done = False

Covenat_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    Covenat1 = Covenat()
    Covenat1.rect.x = random.randrange(900)
    Covenat1.rect.y = random.randrange(600)
    
    Covenat_list.add(Covenat1)
    all_sprite_list.add(Covenat1)
    
player = MaterChef()
all_sprite_list.add(player)    
    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    all_sprite_list.update()
        
    Covenant_hit_list = pygame.sprite.spritecollide(player, Covenat_list, True)
    
    for Covenat1 in Covenant_hit_list:
        score += 1
        print(score)
    
    screen.fill(white)
    
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()