import pygame

class Trigger:

    def __init__(self,x,y,w,h,target=None):

        self.rect = pygame.Rect(x,y,w,h)
        
        self.target = target
        self.activated = False

    def check(self, player):

        if self.activated:
            return

        if self.rect.colliderect(player.rect):
            self.activate()

    def activate(self):

        self.activated = True

        if not self.target:
            return

        # case 1: trap system
        if hasattr(self.target, "activate"):
            self.target.activate()

        # case 2: fake platform
        elif hasattr(self.target, "active"):
            self.target.active = False