import pygame, sys,os

from juego1.app_juego1.telefono_sin_num import *
from menu.boton.boton_salir import * 

pygame.init()

#colors
#BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
AZUL_CIELO = (92, 241, 254 )

carpeta_proyecto = os.path.dirname(__file__)
carpeta_img_menu = os.path.join(carpeta_proyecto, "img_menu")
    
class menu_game:
    def __init__(self):
        pygame.init()
        self.ancho = 700
        self.alto = 700
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.juego1_activado = False
        self.color_font = (AZUL_CIELO)
        self.btn_salir = Boton(self, "Play")
        
        

    
    def corre_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
        
            if not self.juego1_activado:
                self.btn_salir.Dibuja_boton()
                    
            
            self.screen.fill(self.color_font)
            pygame.display.flip()
            
            
    
