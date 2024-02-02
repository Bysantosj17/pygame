import pygame, sys

sys.path.append("juego1")

from juego1.app_juego1.telefono_descompuesto import *

if __name__ == "__main__":
    a = Telefono_descompuesto()
    a.corre_juego1()