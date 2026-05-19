import pygame
from settings import GRAVITY, PLAYER_SPEED, JUMP_POWER, sy, sx
from settings import PLAYER_COLOR

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 50)
        self.vel_y = 0
        self.on_ground = False
        self.spawn_x = x
        self.spawn_y = y
        self.deaths = 0

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        #movement
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

        # jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -JUMP_POWER
            self.on_ground = False

        # gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # collisions
        self.on_ground = False
        for platform in platforms:
            if hasattr(platform,"active"):
                if not platform.active:
                    continue

            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

    def respawn(self):
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
        self.vel_y = 0
        self.deaths += 1

    def draw(self,screen):
        pygame.draw.rect(screen,PLAYER_COLOR,self.rect)
        
        pygame.draw.rect(
            screen,
            (0,0,0),
            (self.rect.x+8,self.rect.y+10,5,5)
            )
        
        pygame.draw.rect(
            screen,
            (0,0,0),
            (self.rect.x+25,self.rect.y+10,5,5)
            )