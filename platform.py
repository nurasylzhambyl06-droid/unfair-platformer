import pygame
from settings import PLATFORM_COLOR

class Platform:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self,screen):
        pygame.draw.rect(
            screen,
            PLATFORM_COLOR,
            self.rect
            )
        
        pygame.draw.rect(
            screen,
            (150,150,150),
            self.rect,
            2
            )
        