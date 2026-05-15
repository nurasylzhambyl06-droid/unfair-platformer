import pygame
from settings import WIDTH, HEIGHT, FPS
from player import Player
from platform import Platform

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(100, 100)

platforms = [
    Platform(0, 550, 800, 50),
    Platform(200, 450, 200, 20)
]

running = True

while running:
    clock.tick(FPS)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(platforms)

    player.draw(screen)

    for p in platforms:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()