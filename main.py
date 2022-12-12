import pygame
import math
import random
import time
import glob
from PIL import Image
import os

ITERATION_LIMIT = 25000
SPEED = 480 #fps

HEIGHT = 900
WIDTH = 900
LENGTH = 800
BLACK = (0, 0, 0)
H = LENGTH * math.sin(math.radians(60))
BASE_X = (WIDTH - LENGTH) / 2
BASE_Y = (HEIGHT + H) / 2
points = []
vertices = []
RADIUS = 1

def make_gif():
    filename = "fractal.gif"
    frames = [Image.open(image) for image in glob.glob(f"./screens/*.jpeg")]
    frame_one = frames[0]
    frame_one.save(filename, format="GIF", append_images=frames,
               save_all=True, duration=len(frames)*10, loop=1)
    files = list(filter(os.path.isfile, glob.glob("./screens/" + "*")))
    [os.remove(file) for file in files if file != filename]


def init_caos(screen):
    global vertices
    global points
    pygame.draw.circle(screen, BLACK, [BASE_X, BASE_Y], RADIUS)
    vertices.append([BASE_X, BASE_Y])
    pygame.draw.circle(screen, BLACK, [BASE_X + LENGTH, BASE_Y], RADIUS)
    vertices.append([BASE_X + LENGTH, BASE_Y])
    pygame.draw.circle(screen, BLACK, [BASE_X + LENGTH / 2, BASE_Y - H], RADIUS)
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
    pygame.draw.circle(screen, BLACK, [x, y], RADIUS)





if __name__ == "__main__":
    random.seed(int(time.time() * 1000))
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    screen.fill((255, 255, 255)) # Fill the background with white
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
        """if cont % 10 == 0:
            pygame.image.save(screen, f"./screens/screenshot{cont}.jpeg")"""
        cont = cont+1

    pygame.quit()
    #make_gif() #takes too long and don't generate a good gif, to fix



