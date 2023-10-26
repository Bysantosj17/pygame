import pygame, sys
pygame.init()

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()