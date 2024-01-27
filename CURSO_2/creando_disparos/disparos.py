import pygame, random

#Tamaño de la pantalla
ANCHO = 800
ALTO = 600

#FPS
FPS = 30

#Paleta de colores
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

class Jugador(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./coliciones_sprites/img/img.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        #Centra el rectangulo (sprite)
        self.rect.center = (ANCHO // 2, 500)
        #Velocidad del personaje (Inicial)
        self.velocidad_x =  0
        
    
    def update(self):

        #Velocidad predeterminada cada vuelta del bucle si no pulsas nada
        self.velocidad_x =  0
        self.velocidad_y =  0
        
        #Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        
        #Mueve el personaje hacia la izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -15   
        #Mueve el personaje hacia la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 15
        #Actualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        
        
        #Mueve el personaje hacia la arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -15   
        #Mueve el personaje hacia la abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 15
            
        #Disparar con la tecla espacio
        if teclas[pygame.K_SPACE]:
            Jugador.disparo()
            Jugador.disparo2()
            Jugador.disparo3()
        
        #Actualiza la velocidad del personaje
        self.rect.y += self.velocidad_y
        
        #Limita el margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        #Limita el margen derecho   
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            
        #Limita el top
        if self.rect.top < 0:
            self.rect.top = 0
        #Limita el buttom   
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            
    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top - 10)
        balas.add(bala)
        
    def disparo2(self):
        bala = Disparos(self.rect.centerx + 20, self.rect.top)
        balas.add(bala)
        
    def disparo3(self):
        bala = Disparos(self.rect.centerx - 20, self.rect.top)
        balas.add(bala)
        
        
class Enemigos(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./coliciones_sprites/img/img2.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)
        #Velocidad predeterminada cada vuelta del bucle si no pulsas nada
        self.velocidad_x =  random.randrange(2,10)
        self.velocidad_y =  random.randrange(2,10)
        
        
    def update(self):
        #Actualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        #Limita el margen derecho   
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
            
        #Limita el buttom   
        if self.rect.bottom > 300:
            self.velocidad_y -= 1
            
        #Limita el top
        if self.rect.top < 0:
            self.velocidad_y += 1
            
class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./creando_disparos/img/bala.png").convert(), (10,20))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        
    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()
            
#Fondo del juegp
fondo = pygame.image.load('./creando_disparos/img/fondo.jpg')
x = 0
            
#Inicializacion de Pygame, creacion de la ventana, tituloy control de reloj
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con esprites")
clock = pygame.time.Clock()

#Grupo de sprites, instancias del objeto jugador
Enemigos_list = pygame.sprite.Group()
balas = pygame.sprite.Group()
sprites = pygame.sprite.Group()

#Instanciaciones de los jugador
Jugador = Jugador()
sprites.add(Jugador)

#Instanciaciones de los enemigos
for x in range(2000):
    Enemigo = Enemigos()
    Enemigos_list.add(Enemigo)
    
#Bucle de juego
ejecutando =  True
while ejecutando:
    #Es lo que especifica  la velocidad del bucle de juego
    clock.tick(FPS)
    #Eventos
    for event in pygame.event.get():
        #Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
            
    #Actualizacion de sprite
    Enemigos_list.update()
    balas.update()
    sprites.update()
    
    #Colision de los enemigos a jugador
    colision = pygame.sprite.spritecollide(Jugador, Enemigos_list, False)
    if colision:
        Enemigo.image = pygame.image.load("./coliciones_sprites/img/explo.png").convert()
        Enemigo.image.set_colorkey(BLACK)
        Enemigo.velocidad_y += 1
    elif Enemigo.rect.top > ALTO:
        Enemigo.kill()
    
    #Fondo de pantalla. dibujo y formas geometricas
    pantalla.blit(fondo, [ 0, 0])
    Enemigos_list.draw(pantalla)
    balas.draw(pantalla)
    sprites.draw(pantalla)
    pygame.draw.line(pantalla, RED, (400,0), (400, 800), 2 )
    pygame.draw.line(pantalla, WHITE, (0, 360), (800, 360), 2)
    #Actualiza el contenido de la pantalla
    pygame.display.flip()
    
pygame.quit()