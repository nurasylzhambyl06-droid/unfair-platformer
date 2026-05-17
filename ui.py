import pygame

pygame.font.init()

font = pygame.font.SysFont("Arial", 30)

def draw_deaths(screen, deaths):
    text = font.render(f"Deaths: {deaths}", True, (255, 255, 255))
    screen.blit(text, (10, 10))