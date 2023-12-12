import pygame,sys

pygame.init()

PANTALLA =  pygame.display.set_mode((1000,800))
Titulo = pygame.display.set_caption('Mi primer juego')

blanco = (255,255,255)
negro  = (  0,  0,  0)
rojo   = (255,  0,  0)
azul   = (  0,  0,255)
verde  = (  0,255,  5)

azul_fuerte = (27, 14, 225)
aqua   = (45, 255, 239)

PANTALLA.fill(blanco)

rectangulo_1 = pygame.draw.rect(PANTALLA, rojo, (100,50,100,50))
print(rectangulo_1)

linea_1 = pygame.draw.line(PANTALLA, azul, (100,104), (199,104), 10)
print(linea_1)

circulo_1 = pygame.draw.circle(PANTALLA, aqua, (122,250), 50, 0)
print(circulo_1)

elipse_1 = pygame.draw.ellipse(PANTALLA, verde,(275,200,40,60))

puntos = [(100, 300), (100,100), (150,100), (200,100)]
poligono = pygame.draw.polygon(PANTALLA, (0, 150, 255), puntos, 8)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
            
    pygame.display.update()