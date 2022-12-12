import re

import pygame
import math
import random
import time
import glob
from PIL import Image
import os

ITERATION_LIMIT = 25000
SPEED = 240 #fps

HEIGHT = 600
WIDTH = 600
LENGTH = 600
WALLPAPER = (13, 17, 23) #my git hub wallpaper
WHITE = (255, 255, 255)
H = LENGTH * math.sin(math.radians(60))
BASE_X = (WIDTH - LENGTH) / 2
BASE_Y = (HEIGHT + H) / 2
points = []
vertices = []
RADIUS = 1

def make_gif():
    filename = "fractal.gif"
    files = list(filter(os.path.isfile, glob.glob("./screens/" + "*")))
    files.sort(key = lambda s: int(re.search(r'\d+', s).group()))
    files.reverse()
    print(files)
    frames = [Image.open(image) for image in files]
    frames.reverse()
    frame_one = frames[0]
    frame_one.save(filename, format="GIF", append_images=[frames[i] for i in range(0,len(frames)) if i % 10 == 0],
               save_all=True, duration=20, loop=1)
    [os.remove(file) for file in files if file != filename]


def init_caos(screen):
    global vertices
    global points
    pygame.draw.circle(screen, WHITE, [BASE_X, BASE_Y], RADIUS)
    vertices.append([BASE_X, BASE_Y])
    pygame.draw.circle(screen, WHITE, [BASE_X + LENGTH, BASE_Y], RADIUS)
    vertices.append([BASE_X + LENGTH, BASE_Y])
    pygame.draw.circle(screen, WHITE, [BASE_X + LENGTH / 2, BASE_Y - H], RADIUS)
    vertices.append([BASE_X + LENGTH / 2, BASE_Y - H])

    #adding the first random point

    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    points.append([x, y])
    pygame.draw.circle(screen, (0, 255, 0), points[0], RADIUS)


def draw_point(screen):
    global vertices
    global points
    vertex = vertices[random.randint(0,len(vertices)-1)]
    point = points[len(points)-1]
    x = ((point[0] - vertex[0]) / 2) + vertex[0]
    y = ((vertex[1] - point[1]) / 2) + point[1]
    points.append([x, y])
    pygame.draw.circle(screen, WHITE, [x, y], RADIUS)





if __name__ == "__main__":
    random.seed(int(time.time() * 1000))
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    screen.fill(WALLPAPER) # Fill the background with white
    clock = pygame.time.Clock()
    cont = 0
    init_caos(screen)
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if cont >= ITERATION_LIMIT:
            running = False
        draw_point(screen)
        pygame.display.flip()
        clock.tick(SPEED)
        #pygame.image.save(screen, f"./screens/screenshot{cont}.jpeg") #decomment to save every frame
        cont = cont+1

    pygame.quit()
    #make_gif() #decomment if you want to create a gif (also decomment the image.save in the while loop)



