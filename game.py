import pygame
from settings import WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform
from traps import Trap, MovingTrap
from ui import draw_deaths
from fake_platform import FakePlatform
from falling_block import FallingBlock
from trigger import Trigger
from settings import GOAL_COLOR
from settings import BACKGROUND

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.state = "MENU"

        self.player = Player(100, 100)
        self.trigger=Trigger(
            420,
            500,
            30,
            30
        )
        self.platforms = [
            Platform(0,550,800,50),
            Platform(200,450,200,20),
            FakePlatform(450,350,150,20),
            FallingBlock(600, 300, 100, 20)
        ]

        self.traps = [
            Trap(300, 530, 50, 20),
            MovingTrap(500, 430, 50, 20)
        ]

        self.goal=pygame.Rect(700,500,50,50)
        self.goal_direction=1

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

            elif self.state == "WIN":
                self.win()

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

        if self.trigger.activated:
            self.goal.x += 3*self.goal_direction
            if self.goal.x>720:
                self.goal_direction=-1
            if self.goal.x<500:
                self.goal_direction=1

        if self.player.rect.colliderect(self.trigger.rect):
            self.trigger.activate()
            for platform in self.platforms:
                if isinstance(platform,FakePlatform):
                    platform.touch()
        
        for trap in self.traps:
            if isinstance(trap, MovingTrap):
                trap.update()
                
            if self.player.rect.colliderect(trap.rect):
                self.player.respawn()

        for platform in self.platforms:
            if isinstance(platform, FakePlatform):
                if self.player.rect.colliderect(platform.rect):
                    platform.touch()

        for platform in self.platforms:
            if isinstance(platform,FallingBlock):
                if self.player.rect.colliderect(platform.rect):
                    platform.falling=True
                platform.update()

        if self.player.rect.colliderect(self.goal):
            self.state="WIN"

    def draw(self):
        self.screen.fill(BACKGROUND)
        
        self.player.draw(self.screen)
        
        pygame.draw.rect(
            self.screen,
            (0,0,255),
            self.trigger.rect
            )
        
        for p in self.platforms:
            if hasattr(p,"active"):
                if p.active:
                    p.draw(self.screen)
            else:
                p.draw(self.screen)
            
        for trap in self.traps:
            trap.draw(self.screen)
            
        pygame.draw.rect(
            self.screen,
            GOAL_COLOR,
            self.goal
            )
        
        pygame.draw.line(
            self.screen,
            (255,255,255),
            (self.goal.x+10,self.goal.y),
            (self.goal.x+10,self.goal.y+50),
            3
            )
        
        pygame.draw.polygon(
            self.screen,
            (255,0,255),
            [
                (self.goal.x+10,self.goal.y),
                (self.goal.x+35,self.goal.y+10),
                (self.goal.x+10,self.goal.y+20)
                ]
            )
        
        draw_deaths(self.screen, self.player.deaths)

    def win(self):
        self.screen.fill((0,0,0))
        
        font=pygame.font.SysFont("Arial",50)
        
        text=font.render(
            "YOU WIN!",
            True,
            (255,255,255)
            )
        
        self.screen.blit(text,(250,250))