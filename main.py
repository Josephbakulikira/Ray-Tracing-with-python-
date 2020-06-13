import pygame
import os
import functions
from classes import *
from math import pi

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 200, 200
white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
resolution = 200
screen.fill(black)

sphere = Sphere(point(0, 0, 0))
sphere.material = Material()
sphere.material.color = (1, 0.2, 1)

light_position = point(-10, 10, -10)
light_color = (1, 1, 1)
light = pointLight(light_position, light_color)

camera = point(0, 0, -5)
wall = point(0, 0, 10)
wall_size = 10

half = wall_size/2

for x in range(width):
    for y in range(height):
        pixel_size = wall_size / resolution
        world_x = -half + pixel_size * x
        world_y = half - pixel_size * y
        pixel = point(world_x, world_y, wall.z)
        direction = functions.NormalizeVector(functions.SubtractingTuples(pixel , camera))

        # functions.set_transform(sphere, functions.ScalingMatrix(0.5, 1, 1))
        r = ray(camera, direction)
        xs = functions.Intersect(sphere, r)
        if functions.hit(xs) is not None:
            p = functions.Position(r, functions.hit(xs))
            norm = functions.normal_at(xs[0].obj, p)
            eye = functions.NegatingTuples(r.direction)
            color = functions.Lighting(xs[0].obj.material, light, p, eye, norm)
            print("{} and {}".format(x, y))

            if color[0]*255 > 255:
                print(color[0])
                color = (1, color[1], color[2])
            if color[1]*255 > 255:
                color[1]
                color = (color[0], 1 , color[2])
            if color[2]*255 > 255:
                color[2]
                color = (color[0], color[1], 1)
            pygame.draw.rect(screen, (color[0]*255, color[1]*255, color[2]*255), [x, y, pixel_size, pixel_size])

pygame.display.update()
#screen capture
screenshot_path ="./progress/"
# pygame.image.save(screen, "sphere2dcaling.png")

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit
