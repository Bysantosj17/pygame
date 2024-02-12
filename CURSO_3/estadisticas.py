import pygame

class Estadisticas:
    def __init__(self, a_game):
        self.juego = a_game
        self.reini()
        
        
    def reini(self):
        self.naves_restantes = self.juego.naves_restantes