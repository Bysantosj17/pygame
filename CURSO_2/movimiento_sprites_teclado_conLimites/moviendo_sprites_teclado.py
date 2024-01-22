import pygame

#Tamaño de la pantalla
ANCHO = 800
ALTO = 800

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
        self.image = pygame.image.load("./movimiento_sprites_teclado_conLimites/img/img.png")
        #self.image.set_colorkey(GREEN)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        #Centra el rectangulo (sprite)
        self.rect.center = (ANCHO // 2, ALTO // 2)
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
            self.velocidad_x = -10   
        #Mueve el personaje hacia la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        #Actualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        
        
        #Mueve el personaje hacia la arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -10   
        #Mueve el personaje hacia la abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
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
        
        
class Jugador2(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./movimiento_sprites_teclado_conLimites/img/img2.png")
        #self.image.fill(GREEN)
        #self.image.set_colorkey()
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        #Centra el rectangulo (sprite)
        self.rect.center = (ANCHO // 2, ALTO // 2)
            
    def update(self):
        #Actualiza esto cada vueta de bucle


        #Velocidad predeterminada cada vuelta del bucle si no pulsas nada
        self.velocidad_x =  0
        self.velocidad_y =  0
        #Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        
        #Mueve el personaje hacia la izquierda
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -10   
        #Mueve el personaje hacia la derecha
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 10
        #Actualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        
        
        #Mueve el personaje hacia la arriba
        if teclas[pygame.K_UP]:
            self.velocidad_y = -10   
        #Mueve el personaje hacia la abajo
        if teclas[pygame.K_DOWN]:
            self.velocidad_y = 10
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
            
#Inicializacion de Pygame, creacion de la ventana, tituloy control de reloj
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con esprites")
clock = pygame.time.Clock()

#Grupo de sprites, instancias del objeto jugador
sprites = pygame.sprite.Group()
Jugador = Jugador()
Jugador2 = Jugador2()
sprites.add(Jugador, Jugador2)

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
    pygame.draw.line(pantalla, RED, (400,0), (400, 800), 1 )
    pygame.draw.line(pantalla, WHITE, (0, 300), (800, 300), 1)
    #Actualiza el contenido de la pantalla
    pygame.display.flip()
    
pygame.quit()