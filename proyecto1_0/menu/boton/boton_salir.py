import pygame.font

background_color = (255, 255, 255)
button_color = (100, 100, 100)
text_color = (255, 255, 255)
class Button:
    def __init__(self, text, position, width, height):
        self.text = text
        self.position = position
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, button_color, (self.position[0], self.position[1], self.width, self.height))
        font = pygame.font.SysFont(None, 36)
        text = font.render(self.text, True, text_color)
        text_rect = text.get_rect(center=(self.position[0] + self.width / 2, self.position[1] + self.height / 2))
        surface.blit(text, text_rect)