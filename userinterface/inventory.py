import pygame
from pygame.math import Vector2
import random
import os
import json
import sys
from constants import *

# initialize sounds
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()


# initialize all imported pygame modules
pygame.init()

# initialize fonts
pygame.font.init()


class InventoryMenu:
    def __init__(self, data_object):
        self.data_object = data_object

        self.return_button_rect = pygame.Rect(33, 33, 98, 74)

        self.heads_button_rect = pygame.Rect(55, 185, 169, 55)
        self.bodies_button_rect = pygame.Rect(229, 185, 169, 55)
        self.fruits_button_rect = pygame.Rect(403, 185, 169, 55)
        self.boards_button_rect = pygame.Rect(577, 185, 168, 55)

        self.but1_button_rect = pygame.Rect(80, 432, 120, 40)
        self.but2_button_rect = pygame.Rect(254, 432, 120, 40)
        self.but3_button_rect = pygame.Rect(428, 432, 120, 40)
        self.but4_button_rect = pygame.Rect(602, 432, 120, 40)
        self.but5_button_rect = pygame.Rect(80, 692, 120, 40)
        self.but6_button_rect = pygame.Rect(254, 692, 120, 40)
        self.but7_button_rect = pygame.Rect(428, 692, 120, 40)
        self.but8_button_rect = pygame.Rect(602, 692, 120, 40)

        self.first_page_button_rect = pygame.Rect(354, 775, 42, 42)
        self.second_page_button_rect = pygame.Rect(406, 775, 42, 42)

        self.selected_heads = True
        self.selected_bodies = False
        self.selected_fruits = False
        self.selected_boards = False

        self.selected_first_page = True
        self.selected_second_page = False

        self.heads_in_inventory = []
        self.bodies_in_inventory = []
        self.fruits_in_inventory = []
        self.boards_in_inventory = []

    def draw_inventory(self, curr_mouse_x, curr_mouse_y):
        self.draw_title_and_background()
        self.draw_inventory_items(curr_mouse_x, curr_mouse_y)

        if self.selected_heads:
            if len(self.heads_in_inventory) > 8:
                if self.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=True, hover_second_page=False)
                elif self.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=True)
                else:
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=False)
        if self.selected_bodies:
            if len(self.bodies_in_inventory) > 8:
                if self.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=True, hover_second_page=False)
                elif self.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=True)
                else:
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=False)
        if self.selected_fruits:
            if len(self.fruits_in_inventory) > 8:
                if self.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=True, hover_second_page=False)
                elif self.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=True)
                else:
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=False)
        if self.selected_boards:
            if len(self.boards_in_inventory) > 8:
                if self.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=True, hover_second_page=False)
                elif self.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=True)
                else:
                    self.draw_page_buttons(hover_first_page=False, hover_second_page=False)

        # RETURN ARROW
        if self.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_return_button(hover=True)
        else:
            self.draw_return_button(hover=False)

        # SELECT BUTTONS
        if self.heads_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_select_buttons(hover_heads=True, hover_bodies=False, hover_fruits=False, hover_boards=False)
        elif self.bodies_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_select_buttons(hover_heads=False, hover_bodies=True, hover_fruits=False, hover_boards=False)
        elif self.fruits_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_select_buttons(hover_heads=False, hover_bodies=False, hover_fruits=True, hover_boards=False)
        elif self.boards_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_select_buttons(hover_heads=False, hover_bodies=False, hover_fruits=False, hover_boards=True)
        else:
            self.draw_select_buttons(hover_heads=False, hover_bodies=False, hover_fruits=False, hover_boards=False)

        # print(f"x --> {curr_mouse_x}")
        # print(f"y --> {curr_mouse_y}\n")

    def play_equip_sound(self):
        if self.data_object.effects == True:
            equip_sound.set_volume(self.data_object.volume)
            equip_sound.play()

    def draw_inventory_items(self, curr_mouse_x, curr_mouse_y):
        column = 1
        row = 1

        # HEADS
        if self.selected_heads:
            self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                            item_type="heads", item_name="default",
                                            column=column, row=row)
            if "default" not in self.heads_in_inventory:
                self.heads_in_inventory.append("default")
            column += 1

            if "purple" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="purple",
                                                column=column, row=row)
                if "purple" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("purple")
                column += 1

            if "blue" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="blue",
                                                column=column, row=row)
                column += 1
                if "blue" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("blue")

            if "pink" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="pink",
                                                column=column, row=row)
                if "pink" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("pink")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

            if "orange" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="orange",
                                                column=column, row=row)
                if "orange" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("orange")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

            if "golden" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="golden",
                                                column=column, row=row)
                if "golden" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("golden")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

            if "mint" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="mint",
                                                column=column, row=row)
                if "mint" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("mint")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "pnk-soft" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="pnk-soft",
                                                column=column, row=row)
                if "pnk-soft" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("pnk-soft")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "white" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="white",
                                                column=column, row=row)
                if "white" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("white")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "black" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="black",
                                                column=column, row=row)
                if "black" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("black")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "blu-soft" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="blu-soft",
                                                column=column, row=row)
                if "blu-soft" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("blu-soft")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "red" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="red",
                                                column=column, row=row)
                if "red" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("red")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "purp-lines" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="purp-lines",
                                                column=column, row=row)
                if "purp-lines" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("purp-lines")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "nightstars" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="nightstars",
                                                column=column, row=row)
                if "nightstars" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("nightstars")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "mushroom" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="mushroom",
                                                column=column, row=row)
                if "mushroom" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("mushroom")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "moro" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="heads", item_name="moro",
                                                column=column, row=row)
                if "moro" not in self.heads_in_inventory:
                    self.heads_in_inventory.append("moro")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

        # BODIES
        if self.selected_bodies:
            self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                            item_type="bodies", item_name="default",
                                            column=column, row=row)
            if "default" not in self.bodies_in_inventory:
                self.bodies_in_inventory.append("default")
            column += 1

            if "purple" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="purple",
                                                column=column, row=row)
                if "purple" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("purple")
                column += 1

            if "blue" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="blue",
                                                column=column, row=row)
                column += 1
                if "blue" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("blue")

            if "pink" in self.data_object.head_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="pink",
                                                column=column, row=row)
                if "pink" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("pink")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

            if "orange" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="orange",
                                                column=column, row=row)
                if "orange" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("orange")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

            if "golden" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="golden",
                                                column=column, row=row)
                if "golden" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("golden")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

            if "mint" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="mint",
                                                column=column, row=row)
                if "mint" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("mint")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "pnk-soft" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="pnk-soft",
                                                column=column, row=row)
                if "pnk-soft" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("pnk-soft")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "white" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="white",
                                                column=column, row=row)
                if "white" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("white")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "black" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="black",
                                                column=column, row=row)
                if "black" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("black")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "blu-soft" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="blu-soft",
                                                column=column, row=row)
                if "blu-soft" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("blu-soft")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "red" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="red",
                                                column=column, row=row)
                if "red" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("red")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "purp-lines" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="purp-lines",
                                                column=column, row=row)
                if "purp-lines" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("purp-lines")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "nightstars" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="nightstars",
                                                column=column, row=row)
                if "nightstars" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("nightstars")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "mushroom" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="mushroom",
                                                column=column, row=row)
                if "mushroom" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("mushroom")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "moro" in self.data_object.body_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="bodies", item_name="moro",
                                                column=column, row=row)
                if "moro" not in self.bodies_in_inventory:
                    self.bodies_in_inventory.append("moro")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

        # FRUITS
        if self.selected_fruits:

            if "courgette" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="courgette",
                                                column=column, row=row)
                if "courgette" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("courgette")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "pumpkin" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="pumpkin",
                                                column=column, row=row)
                if "pumpkin" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("pumpkin")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "grape_1" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="grape_1",
                                                column=column, row=row)
                if "grape_1" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("grape_1")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "avocado" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="avocado",
                                                column=column, row=row)
                if "avocado" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("avocado")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "acorn" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="acorn",
                                                column=column, row=row)
                if "acorn" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("acorn")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "lemon" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="lemon",
                                                column=column, row=row)
                if "lemon" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("lemon")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "kiwi" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="kiwi",
                                                column=column, row=row)
                if "kiwi" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("kiwi")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "orange" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="orange",
                                                column=column, row=row)
                if "orange" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("orange")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "default" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="default",
                                                column=column, row=row)
                if "default" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("default")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "peach" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="peach",
                                                column=column, row=row)
                if "peach" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("peach")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "watermelon" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="watermelon",
                                                column=column, row=row)
                if "watermelon" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("watermelon")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "raspberry" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="raspberry",
                                                column=column, row=row)
                if "raspberry" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("raspberry")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "pineaple" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="pineaple",
                                                column=column, row=row)
                if "pineaple" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("pineaple")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "banana" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="banana",
                                                column=column, row=row)
                if "banana" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("banana")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "pear" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="pear",
                                                column=column, row=row)
                if "pear" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("pear")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "grape_2" in self.data_object.fruit_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="fruits", item_name="grape_2",
                                                column=column, row=row)
                if "grape_2" not in self.fruits_in_inventory:
                    self.fruits_in_inventory.append("grape_2")
                column += 1
                if column == 5:
                    column = 1
                    row += 1


        # BOARDS
        if self.selected_boards:
            if "white-clear" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="white-clear",
                                                column=column, row=row)
                if "white-clear" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("white-clear")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "orange-clear" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="orange-clear",
                                                column=column, row=row)
                if "orange-clear" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("orange-clear")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "mint-clear" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="mint-clear",
                                                column=column, row=row)
                if "mint-clear" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("mint-clear")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "black-clear" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="black-clear",
                                                column=column, row=row)
                if "black-clear" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("black-clear")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "green-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="green-squared",
                                                column=column, row=row)
                if "green-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("green-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "yellow-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="yellow-squared",
                                                column=column, row=row)
                if "yellow-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("yellow-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "mint-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="mint-squared",
                                                column=column, row=row)
                if "mint-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("mint-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "default" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="default",
                                                column=column, row=row)
                if "default" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("default")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "blckbrnz-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="blckbrnz-squared",
                                                column=column, row=row)
                if "blckbrnz-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("blckbrnz-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "blck-wht" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="blck-wht",
                                                column=column, row=row)
                if "blck-wht" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("blck-wht")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "redwht-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="redwht-squared",
                                                column=column, row=row)
                if "redwht-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("redwht-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "redblu-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="redblu-squared",
                                                column=column, row=row)
                if "redblu-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("redblu-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "mintprp-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="mintprp-squared",
                                                column=column, row=row)
                if "mintprp-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("mintprp-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "pink-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="pink-squared",
                                                column=column, row=row)
                if "pink-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("pink-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "orange-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="orange-squared",
                                                column=column, row=row)
                if "orange-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("orange-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1
            if "prple-squared" in self.data_object.board_skins:
                self.draw_inventory_single_item(curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y,
                                                item_type="boards", item_name="prple-squared",
                                                column=column, row=row)
                if "prple-squared" not in self.boards_in_inventory:
                    self.boards_in_inventory.append("prple-squared")
                column += 1
                if column == 5:
                    column = 1
                    row += 1

    def draw_inventory_single_item(self, curr_mouse_x, curr_mouse_y,
                                   item_type, item_name,
                                   column, row):
        if column == 1:
            but_border_position_x = 77
            but_text_position_x = 139
            image_position_x = 90
            border_image_position_x = 85
            border_image_background_position_x = 87
        if column == 2:
            but_border_position_x = 251
            but_text_position_x = 314
            image_position_x = 265
            border_image_position_x = 260
            border_image_background_position_x = 262
        if column == 3:
            but_border_position_x = 425
            but_text_position_x = 487
            image_position_x = 440
            border_image_position_x = 435
            border_image_background_position_x = 437
        if column == 4:
            but_border_position_x = 599
            but_text_position_x = 661
            image_position_x = 615
            border_image_position_x = 610
            border_image_background_position_x = 612

        # FIRST PAGE
        if row == 1:
            but_border_position_y = 429
            but_text_position_y = 449
            image_position_y = 275
            border_image_position_y = 273
            border_image_background_position_y = 275
        if row == 2:
            but_border_position_y = 689
            but_text_position_y = 709
            image_position_y = 532
            border_image_position_y = 530
            border_image_background_position_y = 532
        # SECOND PAGE
        if row == 3:
            but_border_position_y = 429
            but_text_position_y = 449
            image_position_y = 275
            border_image_position_y = 273
            border_image_background_position_y = 275
        if row == 4:
            but_border_position_y = 689
            but_text_position_y = 709
            image_position_y = 532
            border_image_position_y = 530
            border_image_background_position_y = 532

        if item_type == "heads":
            image_name = "down.png"
            if item_name in self.data_object.head_skin:
                but_text = "Wybrany"
                color_button = ORANGE
            else:
                but_text = "Wybierz"
                color_button = GREEN_DARK

        if item_type == "bodies":
            image_name = "body_vertical.png"
            if item_name in self.data_object.body_skin:
                but_text = "Wybrany"
                color_button = ORANGE
            else:
                but_text = "Wybierz"
                color_button = GREEN_DARK

        if item_type == "fruits":
            if item_name in self.data_object.fruit_skin:
                but_text = "Wybrany"
                color_button = ORANGE
            else:
                but_text = "Wybierz"
                color_button = GREEN_DARK

        if item_type == "boards":
            if item_name in self.data_object.board_skin:
                but_text = "Wybrany"
                color_button = ORANGE
            else:
                but_text = "Wybierz"
                color_button = GREEN_DARK

        # FIRST PAGE
        if row == 1:
            if column == 1: self_button = self.but1_button_rect
            if column == 2: self_button = self.but2_button_rect
            if column == 3: self_button = self.but3_button_rect
            if column == 4: self_button = self.but4_button_rect
        if row == 2:
            if column == 1: self_button = self.but5_button_rect
            if column == 2: self_button = self.but6_button_rect
            if column == 3: self_button = self.but7_button_rect
            if column == 4: self_button = self.but8_button_rect
        # SECOND PAGE
        if row == 3:
            if column == 1: self_button = self.but1_button_rect
            if column == 2: self_button = self.but2_button_rect
            if column == 3: self_button = self.but3_button_rect
            if column == 4: self_button = self.but4_button_rect
        if row == 4:
            if column == 1: self_button = self.but5_button_rect
            if column == 2: self_button = self.but6_button_rect
            if column == 3: self_button = self.but7_button_rect
            if column == 4: self_button = self.but8_button_rect

        if self.selected_boards:
            image_size = 105
            image_position_difference = 3
        else:
            image_size = 100
            image_position_difference = 0

        if but_text == "Wybierz" and self_button.collidepoint(curr_mouse_x, curr_mouse_y):
            color_button = GREEN

        if item_type == "boards" or item_type == "fruits":
            image = pygame.image.load(os.path.join("assets", item_type, item_name + ".png"))
            image = pygame.image.load(os.path.join("assets", item_type, item_name + ".png"))
        else:
            image = pygame.image.load(os.path.join("assets", item_type, item_name, image_name))

        if self.selected_first_page and row <= 2:
            but_text = SHOP_BUY_BUTTONS_FONT.render(but_text, True, BLACK)
            but_border_position = (but_border_position_x, but_border_position_y)
            but_text_position = (but_text_position_x, but_text_position_y)
            but_text_position = but_text.get_rect(center=but_text_position)

            but_border_rect = pygame.Rect(but_border_position, (126, 46))
            pygame.draw.rect(screen, BLACK, but_border_rect)
            pygame.draw.rect(screen, color_button, self_button)
            screen.blit(but_text, but_text_position)



            image = pygame.transform.scale(image, (image_size, 100))
            border_image_rect = pygame.Rect(border_image_position_x, border_image_position_y, 109, 104)
            border_image_background_rect = pygame.Rect(border_image_background_position_x, border_image_background_position_y,
                                                       105, 100)
            pygame.draw.rect(screen, BLACK, border_image_rect)
            pygame.draw.rect(screen, GRASS_COLOR, border_image_background_rect)
            screen.blit(image, (image_position_x-image_position_difference, image_position_y))
        if self.selected_second_page and row > 2:
            but_text = SHOP_BUY_BUTTONS_FONT.render(but_text, True, BLACK)
            but_border_position = (but_border_position_x, but_border_position_y)
            but_text_position = (but_text_position_x, but_text_position_y)
            but_text_position = but_text.get_rect(center=but_text_position)

            but_border_rect = pygame.Rect(but_border_position, (126, 46))
            pygame.draw.rect(screen, BLACK, but_border_rect)
            pygame.draw.rect(screen, color_button, self_button)
            screen.blit(but_text, but_text_position)

            image = pygame.transform.scale(image, (image_size, 100))
            border_image_rect = pygame.Rect(border_image_position_x, border_image_position_y, 109, 104)
            border_image_background_rect = pygame.Rect(border_image_background_position_x,
                                                       border_image_background_position_y,
                                                       105, 100)
            pygame.draw.rect(screen, BLACK, border_image_rect)
            pygame.draw.rect(screen, GRASS_COLOR, border_image_background_rect)
            screen.blit(image, (image_position_x-image_position_difference, image_position_y))

    def select_item(self, index):
        if self.selected_heads:
            # if index is our of range
            try:
                if self.data_object.head_skin != self.heads_in_inventory[index]:
                    self.play_equip_sound()
                    self.data_object.head_skin = self.heads_in_inventory[index]
            except: pass

        if self.selected_bodies:
            try:
                if self.data_object.body_skin != self.bodies_in_inventory[index]:
                    self.play_equip_sound()
                    self.data_object.body_skin = self.bodies_in_inventory[index]
            except: pass

        if self.selected_fruits:
            try:
                if self.data_object.fruit_skin != self.fruits_in_inventory[index]:
                    self.play_equip_sound()
                    self.data_object.fruit_skin = self.fruits_in_inventory[index]
            except: pass

        if self.selected_boards:
            try:
                if self.data_object.board_skin != self.boards_in_inventory[index]:
                    self.play_equip_sound()
                    self.data_object.board_skin = self.boards_in_inventory[index]
            except: pass

    @staticmethod
    def draw_title_and_background():
        screen.fill(MENU_COLOR)

        main_title_text = "Ekwipunek"
        main_title = TITLE_FONT.render(main_title_text, True, BLACK)
        main_title_position = main_title.get_rect(center=(WIDTH / 2, 85))
        screen.blit(main_title, main_title_position)

        window_rect_border = pygame.Rect(50, 180, 700, 580)
        window_rect = pygame.Rect(55, 185, 690, 570)
        bottom_border_buttons = pygame.Rect(50, 240, 700, 5)
        heads_right_border = pygame.Rect(224, 180, 5, 60)
        bodies_right_border = pygame.Rect(398, 180, 5, 60)
        fruits_right_border = pygame.Rect(572, 180, 5, 60)

        pygame.draw.rect(screen, BLACK, window_rect_border)
        pygame.draw.rect(screen, GRASS_COLOR, window_rect)
        pygame.draw.rect(screen, BLACK, bottom_border_buttons)
        pygame.draw.rect(screen, BLACK, heads_right_border)
        pygame.draw.rect(screen, BLACK, bodies_right_border)
        pygame.draw.rect(screen, BLACK, fruits_right_border)

        first_column_line_rect = pygame.Rect(224, 225, 5, 535)
        second_column_line_rect = pygame.Rect(398, 225, 5, 535)
        third_column_line_rect = pygame.Rect(572, 225, 5, 535)
        horizontal_line_rect = pygame.Rect(55, 497, 690, 5)

        pygame.draw.rect(screen, BLACK, first_column_line_rect)
        pygame.draw.rect(screen, BLACK, second_column_line_rect)
        pygame.draw.rect(screen, BLACK, third_column_line_rect)
        pygame.draw.rect(screen, BLACK, horizontal_line_rect)

    def draw_select_buttons(self, hover_heads, hover_bodies, hover_fruits, hover_boards):
        color_rect_heads = GREEN_DARK
        color_rect_bodies = GREEN_DARK
        color_rect_fruits = GREEN_DARK
        color_rect_boards = GREEN_DARK

        if hover_heads:  color_rect_heads = GREEN
        if hover_bodies: color_rect_bodies = GREEN
        if hover_fruits: color_rect_fruits = GREEN
        if hover_boards: color_rect_boards = GREEN

        if self.selected_heads:
            left_button_border = pygame.Rect(50, 180, 5, 60)
            right_button_border = pygame.Rect(224, 181, 5, 60)
            bottom_button_border = pygame.Rect(50, 240, 179, 5)
            top_button_border = pygame.Rect(50, 180, 179, 5)
            color_rect_heads = GREEN

        if self.selected_bodies:
            left_button_border = pygame.Rect(224, 180, 5, 60)
            right_button_border = pygame.Rect(398, 181, 5, 60)
            bottom_button_border = pygame.Rect(224, 240, 179, 5)
            top_button_border = pygame.Rect(224, 180, 179, 5)
            color_rect_bodies = GREEN

        if self.selected_fruits:
            left_button_border = pygame.Rect(398, 180, 5, 60)
            right_button_border = pygame.Rect(572, 181, 5, 60)
            bottom_button_border = pygame.Rect(398, 240, 179, 5)
            top_button_border = pygame.Rect(398, 180, 179, 5)
            color_rect_fruits = GREEN

        if self.selected_boards:
            left_button_border = pygame.Rect(572, 180, 5, 60)
            right_button_border = pygame.Rect(745, 181, 5, 59)
            bottom_button_border = pygame.Rect(572, 240, 178, 5)
            top_button_border = pygame.Rect(572, 180, 178, 5)
            color_rect_boards = GREEN

        pygame.draw.rect(screen, color_rect_heads, self.heads_button_rect)
        pygame.draw.rect(screen, color_rect_bodies, self.bodies_button_rect)
        pygame.draw.rect(screen, color_rect_fruits, self.fruits_button_rect)
        pygame.draw.rect(screen, color_rect_boards, self.boards_button_rect)

        heads_string = "Głowy"
        bodies_string = "Tułowia"
        fruits_string = "Owoce"
        boards_string = "Plansze"

        heads_text = SHOP_SELECT_BUTTONS_FONT.render(heads_string, True, BLACK)
        bodies_text = SHOP_SELECT_BUTTONS_FONT.render(bodies_string, True, BLACK)
        fruits_text = SHOP_SELECT_BUTTONS_FONT.render(fruits_string, True, BLACK)
        boards_text = SHOP_SELECT_BUTTONS_FONT.render(boards_string, True, BLACK)

        heads_text_position = heads_text.get_rect(center = (138, 212))
        bodies_text_position = bodies_text.get_rect(center = (312, 212))
        fruits_text_position = fruits_text.get_rect(center = (487, 212))
        boards_text_position = boards_text.get_rect(center = (661, 212))

        screen.blit(heads_text, heads_text_position)
        screen.blit(bodies_text, bodies_text_position)
        screen.blit(fruits_text, fruits_text_position)
        screen.blit(boards_text, boards_text_position)

        pygame.draw.rect(screen, GREY, left_button_border)
        pygame.draw.rect(screen, GREY, right_button_border)
        pygame.draw.rect(screen, GREY, bottom_button_border)
        pygame.draw.rect(screen, GREY, top_button_border)

    def draw_return_button(self, hover):
        if hover == True: color = GREEN
        if hover == False: color = GRASS_COLOR
        return_button_border = pygame.Rect(30, 30, 104, 80)
        return_arrow_position = return_arrow.get_rect(center = (83, 72))

        pygame.draw.rect(screen, BLACK, return_button_border)
        pygame.draw.rect(screen, color, self.return_button_rect)
        screen.blit(return_arrow, return_arrow_position)

    def draw_page_buttons(self, hover_first_page, hover_second_page):
        color_first_page = GREEN_DARK
        color_second_page = GREEN_DARK
        color_first_page_border = BLACK
        color_second_page_border = BLACK

        if self.selected_first_page:
            color_first_page_border = GREY
            color_first_page = GREEN
        if self.selected_second_page:
            color_second_page_border = GREY
            color_second_page = GREEN
        if hover_first_page: color_first_page = GREEN
        if hover_second_page: color_second_page = GREEN

        first_string = "1"
        second_string = "2"
        first_text = SHOP_PAGE_NUMBER_FONT.render(first_string, True, BLACK)
        second_text = SHOP_PAGE_NUMBER_FONT.render(second_string, True, BLACK)
        first_text_position = first_text.get_rect(center=(374, 795))
        second_text_position = first_text.get_rect(center=(426, 795))

        first_page_button_border = pygame.Rect(352, 773, 46, 46)
        second_page_button_border = pygame.Rect(404, 773, 46, 46)
        pygame.draw.rect(screen, color_first_page_border, first_page_button_border)
        pygame.draw.rect(screen, color_second_page_border, second_page_button_border)
        pygame.draw.rect(screen, color_first_page, self.first_page_button_rect)
        pygame.draw.rect(screen, color_second_page, self.second_page_button_rect)
        screen.blit(first_text, first_text_position)
        screen.blit(second_text, second_text_position)