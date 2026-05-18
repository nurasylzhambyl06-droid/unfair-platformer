import pygame

class Trap:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class MovingTrap(Trap):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.direction = 1
        self.speed = 3

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.x <= 400 or self.rect.x >= 700:
            self.direction *= -1