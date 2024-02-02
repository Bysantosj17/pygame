import pygame, sys

class menu_game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Menu Principal")
        
            
    def corre_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            
if __name__ == "__main__":
    a = menu_game()
    a.corre_menu()