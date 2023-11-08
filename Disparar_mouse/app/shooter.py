import pygame,random
pygame.init()

class Covenant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Disparar_mouse/img/covenant_img.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Disparar_mouse/img/jugador_img.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 510
        
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()
done = False
score = 0

all_sprite_list = pygame.sprite.Group()
covenant_list = pygame.sprite.Group()

for i in range(50):
    covenat = Covenant()
    covenat.rect.x = random.randrange(880)
    covenat.rect.y = random.randrange(450)
    
    covenant_list.add(covenat)
    all_sprite_list.add(covenat)

player = Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    all_sprite_list.update()        
            
    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()