from platform import Platform

class FakePlatform(Platform):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.active = True

    def touch(self):
        self.active = False