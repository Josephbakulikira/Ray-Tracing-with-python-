import pygame
import os

os.environ["SD_VIDEO_CENTERED"]='1'
width, height = 200, 200

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

screen.fill((52, 23, 123))
pygame.display.update()

# pygame.image.save(screen, "RGBA.ppm")

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit
