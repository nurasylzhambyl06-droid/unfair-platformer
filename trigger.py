import pygame

class Trigger:

    def __init__(self,x,y,w,h):

        self.rect=pygame.Rect(x,y,w,h)

        self.activated=False

    def activate(self):

        self.activated=True