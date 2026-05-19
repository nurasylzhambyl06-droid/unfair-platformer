from platform import Platform

class FallingBlock(Platform):

    def __init__(self,x,y,w,h):

        super().__init__(x,y,w,h)

        self.falling=False
        self.speed=0

    def update(self):

        if self.falling:

            self.speed+=0.5
            self.rect.y+=self.speed