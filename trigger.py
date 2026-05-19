import pygame

class Trigger:

    def __init__(self,x,y,w,h,target=None):

        self.rect = pygame.Rect(x,y,w,h)

        self.target = target

        self.activated=False

    def activate(self):
        if not self.activated:

            self.activated=True

            if self.target:
                self.target.touch()