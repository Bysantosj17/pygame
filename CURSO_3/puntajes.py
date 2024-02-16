import pygame.font
from pygame.sprite import Group
from corazones import corazones

class Puntaje:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.juego =  a_game
        self.estadisticas =  a_game.estadisticas
        
        self.colorTexto = (30,30,30)
        self.font = pygame.font.SysFont(None, 48, bold=False, italic=False)
        self.prep_score()
        self.prep_highScore()
        self.prep_corazones()
        
    def prep_score(self):
        self.scoreStr = str(self.juego.score)
        self.score_image = self.font.render(self.scoreStr, True, self.colorTexto, None)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_highScore(self):
        self.highScoreStr = str(self.juego.HighScore)
        self.Highscore_image = self.font.render(self.highScoreStr, True, self.colorTexto, None)
        
        self.highScore_rect = self.Highscore_image.get_rect()
        self.highScore_rect.centerx = self.screen_rect.centerx
        self.highScore_rect.top = self.screen_rect.top
        
    def checa_highScore(self):
        if self.juego.score > self.juego.HighScore:
            self.juego.HighScore = self.juego.score
            self.prep_highScore()
        
    def muestraScore(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.Highscore_image, self.highScore_rect)
        self.corazones.draw(self.screen)
        
    def prep_corazones(self):
        self.corazones = Group()
        for numero_corazones in range(self.juego.naves_restantes):
            corazon = corazones(self.juego)
            corazon.rect.x = numero_corazones * corazon.rect.width
            corazon.rect.y = 10
            self.corazones.add(corazon)