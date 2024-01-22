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
        self.image = pygame.image.load("./creacion_enemigos_aleatorias/img/img.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        #Centra el rectangulo (sprite)
        self.rect.center = (ANCHO // 2, 500)
        #Velocidad del personaje (Inicial)
        self.velocidad_x =  0
        
    
    def update(self):
        #Actualiza esto cada vueta de bucle

            
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
        
        
class Enemigos(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./creacion_enemigos_aleatorias/img/img2.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)
            
#Inicializacion de Pygame, creacion de la ventana, tituloy control de reloj
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con esprites")
clock = pygame.time.Clock()

#Grupo de sprites, instancias del objeto jugador
sprites = pygame.sprite.Group()
Enemigos_list = pygame.sprite.Group()

Jugador = Jugador()
sprites.add(Jugador)

for x in range(random.randrange(20) + 5):
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
    sprites.update()
    
    #Fondo de pantalla. dibujo y formas geometricas
    pantalla.fill(BLUE)
    sprites.draw(pantalla)
    Enemigos_list.draw(pantalla)
    pygame.draw.line(pantalla, RED, (400,0), (400, 800), 1 )
    pygame.draw.line(pantalla, WHITE, (0, 300), (800, 300), 1)
    #Actualiza el contenido de la pantalla
    pygame.display.flip()
    
pygame.quit()