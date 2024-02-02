import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla principal
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ventana Principal")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Función para mostrar texto en la pantalla
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

# Función para crear un botón
def button(msg, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    small_text = pygame.font.SysFont(None, 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)

# Función para abrir la segunda ventana
def open_second_window():
    # Configuración de la segunda ventana
    second_screen = pygame.display.set_mode((200, 150))
    pygame.display.set_caption("Segunda Ventana")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        second_screen.fill(white)
        pygame.display.update()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Crear el botón que abre la segunda ventana
    button("Abrir Ventana", 150, 150, 150, 50, (0, 200, 0), (0, 255, 0), open_second_window)

    pygame.display.update()