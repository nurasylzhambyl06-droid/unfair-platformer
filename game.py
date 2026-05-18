import pygame
from settings import WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform
from traps import Trap, MovingTrap
from ui import draw_deaths

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.state = "MENU"

        self.player = Player(100, 100)

        self.platforms = [
            Platform(0, 550, 800, 50),
            Platform(200, 450, 200, 20)
        ]

        self.traps = [
            Trap(300, 530, 50, 20),
            MovingTrap(500, 430, 50, 20)
        ]

        self.goal = pygame.Rect(700, 500, 50, 50)

        self.running = True
        self.won = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.state == "MENU":
                self.menu()

            elif self.state == "PLAYING":
                self.update()
                self.draw()

            pygame.display.flip()

        pygame.quit()
    
    def menu(self):
        self.screen.fill((20, 20, 20))
        font = pygame.font.SysFont("Arial", 50)
        
        title = font.render("UNFAIR PLATFORMER", True, (255, 255, 255))
        start = font.render("Press ENTER to Start", True, (255, 255, 255))
        
        self.screen.blit(title, (180, 200))
        self.screen.blit(start, (180, 300))
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            self.state = "PLAYING"

    def update(self):
        self.player.update(self.platforms)
        
        for trap in self.traps:
            if isinstance(trap, MovingTrap):
                trap.update()
                
            if self.player.rect.colliderect(trap.rect):
                self.player.respawn()
                
        if self.player.rect.colliderect(self.goal):
            self.won = True

    def draw(self):
        self.screen.fill((30, 30, 30))
        
        self.player.draw(self.screen)
        
        for p in self.platforms:
            p.draw(self.screen)
            
        for trap in self.traps:
            trap.draw(self.screen)
            
        pygame.draw.rect(self.screen, (255, 255, 0), self.goal)
        
        draw_deaths(self.screen, self.player.deaths)