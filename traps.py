import pygame
from settings import TRAP_COLOR, sx

class Trap:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self,screen):
        x=self.rect.x
        y=self.rect.y
        
        points=[
            (x,y+self.rect.height),
            (x+self.rect.width//2,y),
            (x+self.rect.width,y+self.rect.height)
            ]
        
        pygame.draw.polygon(
            screen,
            TRAP_COLOR,
            points
            )

class MovingTrap(Trap):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.direction = 1
        self.speed = 3

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.x <= 400 or self.rect.x >= 700:
            self.direction *= -1