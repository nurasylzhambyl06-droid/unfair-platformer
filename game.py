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
from save_system import SaveSystem

class Game:
    def __init__(self):
        pygame.init()
        self.shake_timer=0
        self.shake_power=0

        self.best_score=SaveSystem.load()

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
        self.death_flash=0
        
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
        self.screen.fill((10,10,20))
        title_font=pygame.font.SysFont("Arial",70)
        
        small_font=pygame.font.SysFont("Arial",35)
        
        title=title_font.render(
            "UNFAIR PLATFORMER",
            True,
            (255,255,255)
            )
        start=small_font.render(
            "PRESS ENTER",
            True,
            (180,180,180)
            )
        
        self.screen.blit(
            title,
            (WIDTH//2-300,250)
            )
        self.screen.blit(
            start,
            (WIDTH//2-120,380)
            )
        
        pygame.draw.circle(
            self.screen,
            (60,60,80),
            (WIDTH//2,300),
            180,
            2
            )
        
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            self.state="PLAYING"

    def update(self):   
        self.player.update(self.platforms)
        
        if self.death_flash>0:
            self.death_flash-=1

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
                self.death_flash = 10
                self.shake(8,15)

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

        if self.player.rect.y > HEIGHT:
            self.death_flash = 10
            self.shake(8,15)
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
        
        if self.shake_timer>0:
            self.shake_timer-=1

    def draw(self):
        import random
        offset_x = 0
        offset_y = 0
        if self.shake_timer > 0:
            offset_x = random.randint(
                -self.shake_power,
                self.shake_power
                )
            offset_y = random.randint(
                -self.shake_power,
                self.shake_power
                )
        
        game_surface = pygame.Surface((WIDTH, HEIGHT))
        
        game_surface.fill((15,15,25))
        
        for y in range(HEIGHT):
            shade = min(255,15+(y//10))
            
            pygame.draw.line(
                game_surface,
                (shade,shade,shade+8),
                (0,y),
                (WIDTH,y)
                )
            
        for i in range(50):
            x=(i*83)%WIDTH
            y=(i*57)%HEIGHT
            
            pygame.draw.circle(
                game_surface,
                (200,200,220),
                (x,y),
                1
                )
            
        self.player.draw(game_surface)
        
        if self.trigger:
            pygame.draw.rect(
                game_surface,
                (0,0,255),
                self.trigger.rect
                )
        
        for p in self.platforms:
            if hasattr(p,"active"):
                if p.active:
                    p.draw(game_surface)
            else:
                p.draw(game_surface)
                
        for trap in self.traps:
            trap.draw(game_surface)
            
        pygame.draw.rect(
            game_surface,
            GOAL_COLOR,
            self.goal
            )
        
        pygame.draw.line(
            game_surface,
            (255,255,255),
            (self.goal.x+10,self.goal.y),
            (self.goal.x+10,self.goal.y+50),
            3
            )
        
        pygame.draw.polygon(
            game_surface,
            (255,0,255),
            [
                (self.goal.x+10,self.goal.y),
                (self.goal.x+35,self.goal.y+10),
                (self.goal.x+10,self.goal.y+20)
                ]
                )
        
        draw_deaths(
            game_surface,
            self.player.deaths
            )
        
        font = pygame.font.SysFont("Arial",25)
        score = font.render(
            f"Best: {self.best_score}",
            True,
            (255,255,255)
            )
        game_surface.blit(
            score,
            (10,50)
            )
        
        self.screen.blit(
            game_surface,
            (offset_x,offset_y)
            )
        
        if self.death_flash>0:
            overlay = pygame.Surface((WIDTH,HEIGHT))
            overlay.set_alpha(120)
            overlay.fill((255,0,0))
            
            self.screen.blit(
                overlay,
                (0,0)
                )


    def win(self):
        self.screen.fill((10,10,20))
        title_font=pygame.font.SysFont(
            "Arial",
            80
            )
        small_font=pygame.font.SysFont(
            "Arial",
            35
            )
        if self.player.deaths<self.best_score:
            self.best_score=self.player.deaths
            SaveSystem.save(self.player.deaths)
        
        title=title_font.render(
            "YOU WIN!",
            True,
            (255,220,0)
            )
        
        deaths=small_font.render(
            f"Deaths: {self.player.deaths}",
            True,
            (255,255,255)
            )
        best=small_font.render(
            f"Best Score: {self.best_score}",
            True,
            (255,255,255)
            )
        restart=small_font.render(
            "Press R to play again",
            True,
            (180,180,180)
            )
        
        self.screen.blit(
            title,
            (WIDTH//2-180,220)
            )
        
        self.screen.blit(
            deaths,
            (WIDTH//2-80,350)
            )
        
        self.screen.blit(
            best,
            (WIDTH//2-100,400)
            )
        
        self.screen.blit(
            restart,
            (WIDTH//2-160,500)
            )
        
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            self.current_level=0
            self.player.deaths=0
            self.load_level()
            self.state="MENU"

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

    def shake(self,power,time):
        self.shake_power=power
        self.shake_timer=time