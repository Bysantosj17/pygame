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

#Fuete
Consolas = pygame.font.match_font('consolas')
arial = pygame.font.match_font('arial')
times = pygame.font.match_font('times')

class Jugador(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./coliciones_sprites/img/img.png").convert()
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.radius = 45
        #pygame.draw.circle(self.image, GREEN, self.rect.center, self.radius)
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
            #Jugador.disparo2()
            #Jugador.disparo3()
        
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
        
    '''def disparo2(self):
        bala = Disparos(self.rect.centerx + 20, self.rect.top)
        balas.add(bala)'''
        
    '''def disparo3(self):
        bala = Disparos(self.rect.centerx - 20, self.rect.top)
        balas.add(bala)'''
        
        
class Enemigos1(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./coliciones_sprites/img/img2.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 48
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
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
            
class Enemigos2(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./Añadiendo_meteoritos_RANDOM_generación_INFINITA/img/enemigo_2.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 48
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
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
            
class Enemigos3(pygame.sprite.Sprite):
    #Sprite del jugador 
    def __init__(self):
        #Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("./Añadiendo_meteoritos_RANDOM_generación_INFINITA/img/enemigo_3.png").convert()
        self.image.set_colorkey(BLACK)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 48
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
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
            
'''class Enemigos2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load("./Añadiendo_meteoritos_RANDOM_generación_INFINITA/img/grunt.png"), (50,50))
            self.radius = 25
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load("./Añadiendo_meteoritos_RANDOM_generación_INFINITA/img/enemigo_2.png"), (100,100)) 
            self.radius = 50
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load("./Añadiendo_meteoritos_RANDOM_generación_INFINITA/img/enemigo_3.png").convert(), (100,100))
            self.radius =  50
        self.image.set_colorkey(BLACK)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocidad_y =  random.randrange(1, 10)
        
    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = -self.rect.width
            #Ancho
            self.velocidad_y = random.randrange(1, 10)
'''



#Fondo del juegp
fondo = pygame.image.load('./creando_disparos/img/fondo.jpg')
x = 0

#Sistema de puntacion
puntacion = 0

def muestra_texto(pantalla, fuente, texto, color, dimesiones, x, y):
    tipo_letra = pygame.font.Font(fuente, dimesiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    
    pantalla.blit(superficie, rectangulo)


#Inicializacion de Pygame, creacion de la ventana, tituloy control de reloj
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con esprites")
clock = pygame.time.Clock()

#Grupo de sprites, instancias del objeto jugador
Enemigos_list = pygame.sprite.Group()
balas = pygame.sprite.Group()
sprites = pygame.sprite.Group()

Enemigos_1 = pygame.sprite.Group()
Enemigos_2 = pygame.sprite.Group()
Enemigos_3 = pygame.sprite.Group()

'''MasEnemigos =  pygame.sprite.Group()'''

#Instanciaciones de los jugador
Jugador = Jugador()
sprites.add(Jugador)

'''Enemigos1 = Enemigos1()
Enemigos_1.add(Enemigos1)

Enemigos2 = Enemigos2()
Enemigos_1.add(Enemigos2)

Enemigos3 = Enemigos3()
Enemigos_1.add(Enemigos3)'''

'''for x in range(10):
    Enemigos1 =  Enemigos2()
    MasEnemigos.add(Enemigos1)'''

#Instanciaciones de los enemigos
'''for x in range(random.randrange(10) + 5):
    Enemigo = Enemigos()
    Enemigos_list.add(Enemigo)'''
    
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
    #MasEnemigos.update()
    Enemigos_1.update()
    Enemigos_2.update()
    Enemigos_3.update()
    
    colision_disparos_1 = pygame.sprite.groupcollide(Enemigos_1, balas, True, True, pygame.sprite.collide_circle)
    colision_disparos_2 = pygame.sprite.groupcollide(Enemigos_2, balas, True, True, pygame.sprite.collide_circle)
    colision_disparos_3 = pygame.sprite.groupcollide(Enemigos_3, balas, True, True, pygame.sprite.collide_circle)
    
    if colision_disparos_1:
        puntacion += 5
        
    if colision_disparos_2:
        puntacion += 10
        
    if colision_disparos_3:
        puntacion += 20
        
    if not Enemigos_1 and not Enemigos_2 and not Enemigos_3:
        enemigos1 = Enemigos1()
        Enemigos_1.add(enemigos1)

        enemigos2 = Enemigos2()
        Enemigos_1.add(enemigos2)

        enemigos3 = Enemigos3()
        Enemigos_1.add(enemigos3)
    
    #Colision de los enemigos a jugador
    #colision = pygame.sprite.spritecollide(Jugador, Enemigos_list, False, pygame.sprite.collide_circle)
    
    #colision_jugador = pygame.sprite.spritecollide(Jugador, MasEnemigos, False, pygame.sprite.collide_circle)
    
    #colision_balas = pygame.sprite.groupcollide(MasEnemigos, balas, False, False)
    
    '''if colision_jugador:
        print("Colision de la nave...")
    if colision_balas:
        print("Colision por disparo")'''
    
    #Fondo de pantalla. dibujo y formas geometricas
    pantalla.blit(fondo, [ 0, 0])
    #asEnemigos.draw(pantalla)
    Enemigos_list.draw(pantalla)
    balas.draw(pantalla)
    sprites.draw(pantalla)
    Enemigos_1.draw(pantalla)
    Enemigos_2.draw(pantalla)
    Enemigos_3.draw(pantalla)
    
    pygame.draw.line(pantalla, RED, (400,0), (400, 800), 2 )
    pygame.draw.line(pantalla, WHITE, (0, 360), (800, 360), 2)
    #Actualiza el contenido de la pantalla
    pygame.display.flip()
    
    #Dibuja los textos en la pantalla
    muestra_texto(pantalla, Consolas, str(puntacion), RED, 40, 700, 50)
    
pygame.quit()