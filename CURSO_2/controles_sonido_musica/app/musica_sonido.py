import pygame
from pygame.locals import *
import sys

#Iniciacion de Pygame
pygame.init()

#Pantalla - ventana
W,H = 800, 500
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("santos 1.2")
icono =  pygame.image.load('./personaje_animacion_controles/iconos/jugador_img.png')
pygame.display.set_icon(icono)

#Fondo del juego
fondo = pygame.image.load('./personaje_animacion_controles/img/fondo.jpg')

#Musica de Fondo
pygame.mixer.music.load('./personaje_animacion_controles/sonido/musica_1.ogg')
pygame.mixer.music.play(-1)


#personajes
quieto = pygame.image.load('./personaje_animacion_controles/img/idle1.png')

caminaDerecho = [pygame.image.load('./personaje_animacion_controles/img/run1.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run2.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run3.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run4.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run5.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run6.png')]

caminaIzquierda = [pygame.image.load('./personaje_animacion_controles/img/run1-izq.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run2-izq.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run3-izq.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run4-izq.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run5-izq.png'),
                    pygame.image.load('./personaje_animacion_controles/img/run6-izq.png')]

salta =  [pygame.image.load('./personaje_animacion_controles/img/jump1.png'),
            pygame.image.load('./personaje_animacion_controles/img/jump2.png'),
            pygame.image.load('./personaje_animacion_controles/img/jump3.png')]

#Sonido
sonido_arriba = pygame.image.load('./personaje_animacion_controles/sonido/volume_up.png')
sonido_abajo = pygame.image.load('./personaje_animacion_controles/sonido/volume_down.png')
sonido_mute = pygame.image.load('./personaje_animacion_controles/sonido/volume_muted.png')
sonido_max = pygame.image.load('./personaje_animacion_controles/sonido/volume_max.png')

x = 0
px = 50
py = 200
ancho = 40
velocidad = 10

#Control de FPS 
reloj = pygame.time.Clock()

#Variables salto
salto = False
#Altua del salto
cuentaSalto = 10 

#Variables direccion
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargarPantalla():
    #Variables globales
    global cuentaPasos
    global x
    
    #Fondo en moviemientos
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    #Contador de pasos
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0
    #Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    
    
    
    #Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecho[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
        
    elif salto + 1 >= 2:
        cuentaSalto = 0
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
        
    
        
    else:
        PANTALLA.blit(quieto,(int(px), int(py)))
        
        
    #Actualizacion de la ventana
    pygame.display.update()
    
ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    reloj.tick(18)
    
    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
            
    #Opcion de la tecla pausa
    keys = pygame.key.get_pressed()
    
    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
        
    #TEcla D - Moviento a la derecha
    elif keys[pygame.K_d] and px < 700 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True
        
    #Personaje quieto
    else:
        izquierda =  False
        derecha = False
        cuentaPasos = 0
        
    #Tecla w - Movimiento hacia abajo
    if keys[pygame.K_w] and py > 100:
        py -= velocidad
        
    #Tecla S - Movimiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
        
    #Tecla SPACE - Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto =  True
            izquierda = False
            derecha = False
            cuentaPasos = 0     
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.3
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False
    
    #BAja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(sonido_abajo, (650, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(sonido_mute, (650, 25))
        
    #Sube Volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        PANTALLA.blit(sonido_arriba, (650, 25))
    elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
        PANTALLA.blit(sonido_max, (650, 25))
        
    #Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (850, 25))
        
    #Reactivar Sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (650, 25))
            
    #Llamada a la funcion de actualizacion de la ventana
    recargarPantalla()
    
#Salida del juego
pygame.quit()
        
        
        
        








