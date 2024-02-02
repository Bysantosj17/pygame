import pygame, sys

class GalagaPirata:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Galaga Pirata")
        
    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            
if __name__ == "__main__":
    a = GalagaPirata()
    a = GalagaPirata2()
    a.corre_juego()