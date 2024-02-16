import pygame.font

class Puntaje:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.juego =  a_game
        self.estadisticas =  a_game.estadisticas
        
        self.colorTexto = (30,30,30)
        self.font = pygame.font.SysFont(None, 48, bold=False, italic=False)
        self.prep_score()
        
    def prep_score(self):
        self.scoreStr = str(self.juego.score)
        self.score_image = self.font.render(self.scoreStr, True, self.colorTexto, None)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        
    def muestraScore(self):
        self.screen.blit(self.score_image, self.score_rect)