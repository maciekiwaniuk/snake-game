import pygame
from pygame.math import Vector2
import random
from constants import *


# initialize all imported pygame modules
pygame.init()

# initialize fonts
pygame.font.init()


class Fruit:
    def __init__(self, data_object):
        self.randomize_position()

        self.data_object = data_object

    # draws image in random coordinates got from randomize_method
    def draw_fruit(self):
        position = (int(self.position.x * CELL_SIZE), int(self.position.y * CELL_SIZE))
        apple_image = pygame.image.load(os.path.join("assets", "fruits", self.data_object.fruit_skin + ".png")).convert_alpha()
        apple_image = pygame.transform.scale(apple_image, (40, 40))
        screen.blit(apple_image, position)

    # setting random coordinates of fruit
    def randomize_position(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(1, CELL_NUMBER)
        self.position = Vector2(self.x, self.y)
