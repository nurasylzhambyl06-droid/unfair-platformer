import pygame
from settings import WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform
from traps import Trap
from ui import draw_deaths

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(100, 100)

platforms = [
    Platform(0, 550, 800, 50),
    Platform(200, 450, 200, 20),
    Platform(450, 350, 150, 20),
    Platform(650, 250, 100, 20)
]

traps = [
    Trap(300, 530, 50, 20),
    Trap(500, 330, 50, 20),
    Trap(680, 230, 50, 20)
]

goal = pygame.Rect(700, 500, 50, 50)
running = True
won = False

while running:
    clock.tick(FPS)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(platforms)
    for trap in traps:
        if player.rect.colliderect(trap.rect):
            player.respawn()

    player.draw(screen)

    for p in platforms:
        p.draw(screen)
    
    for trap in traps:
        trap.draw(screen)

    pygame.draw.rect(screen, (255, 255, 0), goal)
    draw_deaths(screen, player.deaths)

    if player.rect.colliderect(goal) and not won:
        print("YOU WIN")
        won = True
    pygame.display.flip()

pygame.quit()