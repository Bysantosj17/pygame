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
        self.speed_x = 0
        self.speed_y = 0
        
    def changespeed(self, x):
        self.speed_x += x
        
    def update(self):
        self.rect.x += self.speed_x
        player.rect.y = 510
        
    ##def update(self):
    #   mouse_pos = pygame.mouse.get_pos()
    #  player.rect.x = mouse_pos[0]
    #   player.rect.y = 510
        
class Bala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Disparar_teclado_sonido/img/bala1_img.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y -= 5
        
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()
done = False
score = 0

all_sprite_list = pygame.sprite.Group()
covenant_list = pygame.sprite.Group()
bala_list = pygame.sprite.Group()

for i in range(50):
    covenat = Covenant()
    covenat.rect.x = random.randrange(880)
    covenat.rect.y = random.randrange(450)
    
    covenant_list.add(covenat)
    all_sprite_list.add(covenat)

player = Player()
all_sprite_list.add(player)

sound = pygame.mixer.Sound("./Disparar_teclado_sonido/sound/sonido_bala.mp3")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        ##-----Teclado#-----#
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5)
            if event.key == pygame.K_RIGHT:
                player.changespeed(5)
            if event.key == pygame.K_SPACE:
                bala = Bala()
                bala.rect.x = player.rect.x + 45
                bala.rect.y = player.rect.y - 20
                
                all_sprite_list.add(bala)
                bala_list.add(bala)
                sound.play()
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-5)

            
    all_sprite_list.update()
    
    for bala in bala_list:
        covenant_hit_list = pygame.sprite.spritecollide(bala, covenant_list, True)
        for covenat in covenant_hit_list:
            all_sprite_list.remove(bala)
            bala_list.remove(bala)
            score += 1
            print(score)
        if bala.rect.y < -10:
            all_sprite_list.remove(bala)
            bala_list.remove(bala)
            
    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()