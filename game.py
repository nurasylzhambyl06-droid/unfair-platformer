import pygame
from settings import sx, sy, WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform
from traps import Trap, MovingTrap
import trigger
from ui import draw_deaths
from fake_platform import FakePlatform
from falling_block import FallingBlock
from trigger import Trigger
from settings import GOAL_COLOR
from settings import BACKGROUND
import levels.level1 as level1
import levels.level2 as level2
import levels.level3 as level3
from settings import HEIGHT

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.state = "MENU"

        self.player = Player(100, 100)
        
        fake_platform = FakePlatform(
             sx(450),
             sy(350),
             sx(150),
             sy(20)
             )
        
        self.platforms = [
            Platform(sx(0),sy(550),sx(800),sy(50)),
            Platform(sx(200),sy(450),sx(200),sy(20)),
            fake_platform
            ] 

        self.levels=[
            level1,
            level2,
            level3
            ]
        
        self.current_level=0
        self.triggers = []
        self.load_level()

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
        
        self.screen.blit(title, (WIDTH//2-280, 312))
        self.screen.blit(start, (WIDTH//2-250, 412))
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            self.state = "PLAYING"

    def update(self):   
        self.player.update(self.platforms)

        if self.trigger and self.trigger.activated:
            self.goal.x += 3 * self.goal_direction
            if self.goal.x > sx(1000):
                self.goal_direction = -1
            
            if self.goal.x < sx(700):
                self.goal_direction = 1


        if self.trigger:
            self.trigger.check(self.player)
        
        for trap in self.traps:
            if hasattr(trap,"update"):
                trap.update(self.player)
            
            if self.player.rect.colliderect(trap.rect):
                self.player.respawn()
                self.load_level()

        for platform in self.platforms:
            if isinstance(platform,FakePlatform):
                if not platform.active:
                    continue
                if self.player.rect.colliderect(platform.rect):
                    if self.player.vel_y > 0:
                        if self.player.rect.bottom<=platform.rect.top+10:
                            platform.touch()

        for platform in self.platforms:
            if isinstance(platform,FallingBlock):
                if self.player.rect.colliderect(platform.rect):
                    platform.falling=True
                platform.update()

        if self.player.rect.y>HEIGHT:
            self.restart_level()

        for trigger in self.triggers:
            trigger.check(self.player)

        if self.player.rect.colliderect(self.goal):
            self.current_level+=1
            
            if self.current_level<len(self.levels):
                self.load_level()
                
            else:
                self.state="WIN"

        if self.goal_moving and self.trigger.activated:
            self.goal.x += 6*self.goal_direction
            if self.goal.x>sx(1000):
                self.goal_direction=-1
                
            if self.goal.x<sx(600):
                self.goal_direction=1

    def draw(self):
        self.screen.fill(BACKGROUND)
        
        self.player.draw(self.screen)
        
        if self.trigger:
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
        
        font=pygame.font.SysFont("Arial", 50)
        
        text=font.render(
            "YOU WIN!",
            True,
            (255,255,255)
            )
        
        self.screen.blit(text,(sx(300),sy(250)))

    def load_level(self):
        level=self.levels[self.current_level]
        import copy
        self.platforms=copy.deepcopy(level.platforms)
        self.traps=copy.deepcopy(level.traps)
        
        self.goal=pygame.Rect(
            level.goal_position[0],
            level.goal_position[1],
            sx(50),
            sy(50)
            )
        
        self.goal_moving = getattr(level, "goal_moving", False)
        self.goal_direction = 1

        self.trigger=getattr(level, "trigger", [])

        spawn=level.player_spawn
        
        self.player.rect.x=spawn[0]
        self.player.rect.y=spawn[1]
        
        self.player.spawn_x=spawn[0]
        self.player.spawn_y=spawn[1]

    def restart_level(self):
        self.player.respawn()
        self.load_level()
        self.trigger.activated=False