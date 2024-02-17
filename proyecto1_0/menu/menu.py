import pygame, sys,os
import pygame.font

from juego1.app_juego1.telefono_sin_num import *
from menu.boton.boton_salir import *

# Inicializar Pygame
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


# Obtener las dimensiones de la pantalla del dispositivo
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
    
class menu_game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.color_font = (AZUL_CIELO)
        self.juego1_activado = True
        self.button = Button("Presionar", ((screen_width-300), (screen_height-700)), 200, 50)

    def corre_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.color_font)
            
            self.button.draw(self.screen)
            
            if not self.juego1_activado:
                self.btn_salir.Dibuja_boton(self.screen)
                
                    
            
            pygame.display.flip()
            
