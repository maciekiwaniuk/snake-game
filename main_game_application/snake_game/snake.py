import pygame
from pygame.math import Vector2
import random
import os
import json
import sys
from constants import *


# initialize all imported pygame modules
pygame.init()

# initialize fonts
pygame.font.init()


class Snake:
    def __init__(self, data_object):
        # starting position of snake --> body[0] --> Snake's head
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        # moving direction of snake
        self.direction = Vector2(0, 0)
        # when new_block is False means that Snake didn't eat fruit yet
        # snake eats fruit --> new_block = True --> changing if statement in 'move_snake' method
        self.new_block = False

        # region Head images
        self.head_up = pygame.image.load(os.path.join("assets", "heads", data_object.head_skin, "up.png")).convert_alpha()
        self.head_down = pygame.image.load(os.path.join("assets", "heads", data_object.head_skin, "down.png")).convert_alpha()
        self.head_right = pygame.image.load(os.path.join("assets", "heads", data_object.head_skin, "right.png")).convert_alpha()
        self.head_left = pygame.image.load(os.path.join("assets", "heads", data_object.head_skin, "left.png")).convert_alpha()

        self.head_up = pygame.transform.scale(self.head_up, (40, 40))
        self.head_down = pygame.transform.scale(self.head_down, (40, 40))
        self.head_right = pygame.transform.scale(self.head_right, (40, 40))
        self.head_left = pygame.transform.scale(self.head_left, (40, 40))
        # endregion

        # region Tail images
        self.tail_up = pygame.image.load(os.path.join("assets", "bodies", data_object.body_skin, "tail_up.png")).convert_alpha()
        self.tail_down = pygame.image.load(os.path.join("assets", "bodies", data_object.body_skin, "tail_down.png")).convert_alpha()
        self.tail_right = pygame.image.load(os.path.join("assets", "bodies", data_object.body_skin, "tail_right.png")).convert_alpha()
        self.tail_left = pygame.image.load(os.path.join("assets", "bodies", data_object.body_skin, "tail_left.png")).convert_alpha()

        self.tail_up = pygame.transform.scale(self.tail_up, (40, 40))
        self.tail_down = pygame.transform.scale(self.tail_down, (40, 40))
        self.tail_right = pygame.transform.scale(self.tail_right, (40, 40))
        self.tail_left = pygame.transform.scale(self.tail_left, (40, 40))
        # endregion

        # region Body images
        self.body_horizontal = pygame.image.load(
            os.path.join("assets", "bodies", data_object.body_skin, "body_horizontal.png")).convert_alpha()
        self.body_vertical = pygame.image.load(
            os.path.join("assets", "bodies", data_object.body_skin, "body_vertical.png")).convert_alpha()

        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (40, 40))
        self.body_vertical = pygame.transform.scale(self.body_vertical, (40, 40))

        self.body_up_right = pygame.image.load(
            os.path.join("assets", "bodies", data_object.body_skin, "body_up_right.png")).convert_alpha()
        self.body_up_left = pygame.image.load(
            os.path.join("assets", "bodies", data_object.body_skin, "body_up_left.png")).convert_alpha()
        self.body_down_right = pygame.image.load(
            os.path.join("assets", "bodies", data_object.body_skin, "body_down_right.png")).convert_alpha()
        self.body_down_left = pygame.image.load(
            os.path.join("assets", "bodies", data_object.body_skin, "body_down_left.png")).convert_alpha()

        self.body_up_right = pygame.transform.scale(self.body_up_right, (40, 40))
        self.body_up_left = pygame.transform.scale(self.body_up_left, (40, 40))
        self.body_down_right = pygame.transform.scale(self.body_down_right, (40, 40))
        self.body_down_left = pygame.transform.scale(self.body_down_left, (40, 40))
        # endregion

    def draw_snake(self):
        # index -> current index of the block
        # each block contains Vector2(x, y)
        for index, block in enumerate(self.body):
            x_position = int(block.x * CELL_SIZE)
            y_position = int(block.y * CELL_SIZE)
            block_position = (x_position, y_position)
            block_size = (CELL_SIZE, CELL_SIZE)
            block_rect = pygame.Rect(block_position, block_size)

            # when current block is snake's head
            if index == 0:
                self.update_head_graphics()
                screen.blit(self.head, block_rect)

            # when current block is snake's tail
            elif index == len(self.body) - 1:
                self.update_tail_graphics()
                screen.blit(self.tail, block_rect)

            # when current block is snake's body segment
            else:
                self.update_body_graphics(index)
                screen.blit(self.body_segment, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_body_graphics(self, index_of_block):
        previous_block = self.body[index_of_block - 1]
        current_block = self.body[index_of_block]
        next_block = self.body[index_of_block + 1]

        current_previous_relation = current_block - previous_block
        current_next_relation = current_block - next_block

        if previous_block.y == next_block.y: self.body_segment = self.body_horizontal
        if previous_block.x == next_block.x: self.body_segment = self.body_vertical

        if ((current_next_relation == Vector2(0, 1) and current_previous_relation == Vector2(1, 0)) or
            (current_previous_relation == Vector2(0, 1) and current_next_relation == Vector2(1, 0))):
            self.body_segment = self.body_up_left

        if ((current_next_relation == Vector2(0, 1) and current_previous_relation == Vector2(-1, 0)) or
            (current_previous_relation == Vector2(0, 1) and current_next_relation == Vector2(-1, 0))):
            self.body_segment = self.body_up_right

        if ((current_next_relation == Vector2(0, -1) and current_previous_relation == Vector2(-1, 0)) or
            (current_previous_relation == Vector2(0, -1) and current_next_relation == Vector2(-1, 0))):
            self.body_segment = self.body_down_right

        if ((current_next_relation == Vector2(0, -1) and current_previous_relation == Vector2(1, 0)) or
            (current_previous_relation == Vector2(0, -1) and current_next_relation == Vector2(1, 0))):
            self.body_segment = self.body_down_left

    def update_tail_graphics(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up

    def move_snake(self):
        # if snake didn't eat fruit
        if self.new_block == False:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
        # if snake ate fruit
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False

    def add_block(self):
        self.new_block = True
