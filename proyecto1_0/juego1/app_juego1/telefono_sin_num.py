import pygame, sys

#Tamaño de la pantalla
ANCHO = 700
ALTO = 500

#FPS
FPS = 30

#Paleta de colores
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

#Fuetes
Consolas = pygame.font.match_font('consolas')
arial = pygame.font.match_font('arial')
times = pygame.font.match_font('times')

class Telefono_sin_num:
    def __init__(self):
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("telefono sin numeros")
        
    def corre_juego1(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
