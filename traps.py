import pygame

class Trap:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
traps = [
    Trap(300, 530, 50, 20),
    Trap(500, 430, 50, 20)
]