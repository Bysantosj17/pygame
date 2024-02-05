import pygame, sys,os

#colors
#BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

carpeta_proyecto = os.path.dirname(__file__)
carpeta_img_menu = os.path.join(carpeta_proyecto, "img_menu")

menu_img = pygame.image.load(os.path.join(carpeta_img_menu, "menu_img.jpg"))

class menu_game:
    def __init__(self):
        self.pantalla_menu = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Menu Principal")
        #Obtiene el rectangulo (sprite)
        self.pantalla_menu.blit(menu_img, [ 0, 0])
        
    def corre_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            