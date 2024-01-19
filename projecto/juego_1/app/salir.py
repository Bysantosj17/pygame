import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho, ventana_alto = 400, 300
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ventana con Botón de Salida")

# Color de fondo
fondo_color = (255, 255, 255)

# Función para salir
def salir():
    pygame.quit()
    sys.exit()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                salir()

    # Limpiar la pantalla
    ventana.fill(fondo_color)

    # Dibujar el botón de salida
    pygame.draw.rect(ventana, (255, 0, 0), (150, 120, 100, 50))  # Rectángulo rojo
    font = pygame.font.Font(None, 36)
    texto = font.render("Salir", True, (255, 255, 255))
    ventana.blit(texto, (165, 135))  # Posiciona el texto en el botón

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del programa al finalizar
pygame.quit()
sys.exit()