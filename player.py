import pygame
from settings import *

class Player:

    def __init__(self,x,y):

        self.rect=pygame.Rect(x,y,40,50)

        self.vel_y=0
        self.on_ground=False

        self.spawn_x=x
        self.spawn_y=y

        self.deaths=0

    def update(self,platforms):

        keys=pygame.key.get_pressed()

        dx=0

        if keys[pygame.K_a]:
            dx=-PLAYER_SPEED

        if keys[pygame.K_d]:
            dx=PLAYER_SPEED

        # X movement
        self.rect.x+=dx

        for platform in platforms:

            if hasattr(platform,"active"):
                if not platform.active:
                    continue

            if self.rect.colliderect(platform.rect):

                if dx>0:
                    self.rect.right=platform.rect.left

                if dx<0:
                    self.rect.left=platform.rect.right


        # jump
        if keys[pygame.K_SPACE] and self.on_ground:

            self.vel_y=-JUMP_POWER
            self.on_ground=False


        # gravity
        self.vel_y+=GRAVITY

        self.rect.y+=self.vel_y

        self.on_ground=False

        # Y collision
        for platform in platforms:

            if hasattr(platform,"active"):
                if not platform.active:
                    continue

            if self.rect.colliderect(platform.rect):

                # falling
                if self.vel_y>0:

                    self.rect.bottom=platform.rect.top
                    self.vel_y=0
                    self.on_ground=True

                # jumping into platform
                elif self.vel_y<0:

                    self.rect.top=platform.rect.bottom
                    self.vel_y=0


    def respawn(self):

        self.rect.x=self.spawn_x
        self.rect.y=self.spawn_y

        self.vel_y=0

        self.deaths+=1


    def draw(self,screen):

        pygame.draw.rect(
            screen,
            PLAYER_COLOR,
            self.rect
        )

        pygame.draw.circle(
            screen,
            (0,0,0),
            (self.rect.x+12,self.rect.y+15),
            3
        )

        pygame.draw.circle(
            screen,
            (0,0,0),
            (self.rect.x+28,self.rect.y+15),
            3
        )