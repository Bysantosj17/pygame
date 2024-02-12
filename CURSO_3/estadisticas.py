import pygame

class Estadisticas:
    def __init__(self, a_game):
        self.reinicia()
        self.juego =  a_game
        
        
    def reinicia(self):
        self.nave_restantes = self.juego.naves_restantes