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


class ShopMenu:
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

        self.head_prices = [
            200, 300, 300, 400,
            500, 600, 700, 1000,
            1500, 2000, 2500, 2500,
            5000, 5000, 7500
        ]
        self.head_names = [
            "purple", "blue", "pink", "orange",
            "golden", "mint", "pnk-soft", "white",
            "black", "blu-soft", "red", "purp-lines",
            "nightstars", "mushroom", "moro"
         ]

        self.body_prices = [
            200, 300, 300, 400,
            500, 600, 700, 1000,
            1500, 2000, 2500, 2500,
            5000, 5000, 7500
        ]
        self.body_names = [
            "purple", "blue", "pink", "orange",
            "golden", "mint", "pnk-soft", "white",
            "black", "blu-soft", "red", "purp-lines",
            "nightstars", "mushroom", "moro"
         ]

        self.fruit_prices = [
            300, 300, 300, 300,
            500, 500, 500, 500,
            1000, 1000, 1000, 1000,
            2000, 2000, 2000
        ]
        self.fruit_names = [
            "courgette", "pumpkin", "grape_1", "avocado",
            "acorn", "lemon", "kiwi", "orange",
            "pear", "watermelon", "raspberry", "peach",
            "banana", "pineaple", "grape_2"
        ]

        self.board_prices = [
            500, 500, 500, 500,
            500, 500, 500, 500,
            1000, 1000, 1000, 1000,
            1000, 1000, 1000
        ]
        self.board_names = [
            "white-clear", "orange-clear", "mint-clear", "black-clear",
            "green-squared", "mint-squared", "orange-squared", "blckbrnz-squared",
            "blck-wht", "redwht-squared", "redblu-squared", "mintprp-squared",
            "pink-squared", "yellow-squared", "prple-squared"
        ]

        self.selected_heads = True
        self.selected_bodies = False
        self.selected_fruits = False
        self.selected_boards = False

        self.selected_first_page = True
        self.selected_second_page = False

    def play_buy_sound(self):
        if self.data_object.effects == True:
            buy_sound.set_volume(self.data_object.volume)
            buy_sound.play()

    def draw_shop(self, curr_mouse_x, curr_mouse_y):
        self.draw_title_and_background()
        self.draw_coins_bar()
        self.draw_shop_items_buttons(curr_mouse_x, curr_mouse_y)

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

        # PAGE BUTTONS
        if self.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_page_buttons(hover_first_page=True, hover_second_page=False)
        elif self.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_page_buttons(hover_first_page=False, hover_second_page=True)
        else:
            self.draw_page_buttons(hover_first_page=False, hover_second_page=False)


        # print(f"x --> {curr_mouse_x}")
        # print(f"y --> {curr_mouse_y}\n")

    def draw_shop_items_buttons(self, curr_mouse_x, curr_mouse_y):
        self.draw_shop_pictures()

        # FIRST PAGE
        if self.selected_first_page:
            # ITEM 1
            self.draw_item_in_shop(self_button_variable=self.but1_button_rect,
                                   head_price=self.head_prices[0], body_price=self.body_prices[0],
                                   fruit_price=self.fruit_prices[0], board_price=self.board_prices[0],
                                   head_name=self.head_names[0], body_name=self.body_names[0],
                                   fruit_name=self.fruit_names[0], board_name=self.board_names[0],
                                   column=1, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)
            # ITEM 2
            self.draw_item_in_shop(self_button_variable=self.but2_button_rect,
                                   head_price=self.head_prices[1], body_price=self.body_prices[1],
                                   fruit_price=self.fruit_prices[1], board_price=self.board_prices[1],
                                   head_name=self.head_names[1], body_name=self.body_names[1],
                                   fruit_name=self.fruit_names[1], board_name=self.board_names[1],
                                   column=2, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 3
            self.draw_item_in_shop(self_button_variable=self.but3_button_rect,
                                   head_price=self.head_prices[2], body_price=self.body_prices[2],
                                   fruit_price=self.fruit_prices[2], board_price=self.board_prices[2],
                                   head_name=self.head_names[2], body_name=self.body_names[2],
                                   fruit_name=self.fruit_names[2], board_name=self.board_names[2],
                                   column=3, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 4
            self.draw_item_in_shop(self_button_variable=self.but4_button_rect,
                                   head_price=self.head_prices[3], body_price=self.body_prices[3],
                                   fruit_price=self.fruit_prices[3], board_price=self.board_prices[3],
                                   head_name=self.head_names[3], body_name=self.body_names[3],
                                   fruit_name=self.fruit_names[3], board_name=self.board_names[3],
                                   column=4, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 5
            self.draw_item_in_shop(self_button_variable=self.but5_button_rect,
                                   head_price=self.head_prices[4], body_price=self.body_prices[4],
                                   fruit_price=self.fruit_prices[4], board_price=self.board_prices[4],
                                   head_name=self.head_names[4], body_name=self.body_names[4],
                                   fruit_name=self.fruit_names[4], board_name=self.board_names[4],
                                   column=1, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 6
            self.draw_item_in_shop(self_button_variable=self.but6_button_rect,
                                   head_price=self.head_prices[5], body_price=self.body_prices[5],
                                   fruit_price=self.fruit_prices[5], board_price=self.board_prices[5],
                                   head_name=self.head_names[5], body_name=self.body_names[5],
                                   fruit_name=self.fruit_names[5], board_name=self.board_names[5],
                                   column=2, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 7
            self.draw_item_in_shop(self_button_variable=self.but7_button_rect,
                                   head_price=self.head_prices[6], body_price=self.body_prices[6],
                                   fruit_price=self.fruit_prices[6], board_price=self.board_prices[6],
                                   head_name=self.head_names[6], body_name=self.body_names[6],
                                   fruit_name=self.fruit_names[6], board_name=self.board_names[6],
                                   column=3, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 8
            self.draw_item_in_shop(self_button_variable=self.but8_button_rect,
                                   head_price=self.head_prices[7], body_price=self.body_prices[7],
                                   fruit_price=self.fruit_prices[7], board_price=self.board_prices[7],
                                   head_name=self.head_names[7], body_name=self.body_names[7],
                                   fruit_name=self.fruit_names[7], board_name=self.board_names[7],
                                   column=4, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

        # SECOND PAGE
        if self.selected_second_page:
            # ITEM 1
            self.draw_item_in_shop(self_button_variable=self.but1_button_rect,
                                   head_price=self.head_prices[8], body_price=self.body_prices[8],
                                   fruit_price=self.fruit_prices[8], board_price=self.board_prices[8],
                                   head_name=self.head_names[8], body_name=self.body_names[8],
                                   fruit_name=self.fruit_names[8], board_name=self.board_names[8],
                                   column=1, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)
            # ITEM 2
            self.draw_item_in_shop(self_button_variable=self.but2_button_rect,
                                   head_price=self.head_prices[9], body_price=self.body_prices[9],
                                   fruit_price=self.fruit_prices[9], board_price=self.board_prices[9],
                                   head_name=self.head_names[9], body_name=self.body_names[9],
                                   fruit_name=self.fruit_names[9], board_name=self.board_names[9],
                                   column=2, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 3
            self.draw_item_in_shop(self_button_variable=self.but3_button_rect,
                                   head_price=self.head_prices[10], body_price=self.body_prices[10],
                                   fruit_price=self.fruit_prices[10], board_price=self.board_prices[10],
                                   head_name=self.head_names[10], body_name=self.body_names[10],
                                   fruit_name=self.fruit_names[10], board_name=self.board_names[10],
                                   column=3, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 4
            self.draw_item_in_shop(self_button_variable=self.but4_button_rect,
                                   head_price=self.head_prices[11], body_price=self.body_prices[11],
                                   fruit_price=self.fruit_prices[11], board_price=self.board_prices[11],
                                   head_name=self.head_names[11], body_name=self.body_names[11],
                                   fruit_name=self.fruit_names[11], board_name=self.board_names[11],
                                   column=4, row=1,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 5
            self.draw_item_in_shop(self_button_variable=self.but5_button_rect,
                                   head_price=self.head_prices[12], body_price=self.body_prices[12],
                                   fruit_price=self.fruit_prices[12], board_price=self.board_prices[12],
                                   head_name=self.head_names[12], body_name=self.body_names[12],
                                   fruit_name=self.fruit_names[12], board_name=self.board_names[12],
                                   column=1, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 6
            self.draw_item_in_shop(self_button_variable=self.but6_button_rect,
                                   head_price=self.head_prices[13], body_price=self.body_prices[13],
                                   fruit_price=self.fruit_prices[13], board_price=self.board_prices[13],
                                   head_name=self.head_names[13], body_name=self.body_names[13],
                                   fruit_name=self.fruit_names[13], board_name=self.board_names[13],
                                   column=2, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 7
            self.draw_item_in_shop(self_button_variable=self.but7_button_rect,
                                   head_price=self.head_prices[14], body_price=self.body_prices[14],
                                   fruit_price=self.fruit_prices[14], board_price=self.board_prices[14],
                                   head_name=self.head_names[14], body_name=self.body_names[14],
                                   fruit_name=self.fruit_names[14], board_name=self.board_names[14],
                                   column=3, row=2,
                                   curr_mouse_x=curr_mouse_x, curr_mouse_y=curr_mouse_y)

            # ITEM 8
            # ONLY 15 ITEMS IN SHOP

    def draw_item_in_shop(self, self_button_variable,
                          head_price, body_price, fruit_price, board_price,
                          head_name, body_name, fruit_name, board_name,
                          column, row,
                          curr_mouse_x, curr_mouse_y):
        buy_text = "Kup"
        bought_text = "Kupiony"

        if column == 1:
            price_position_x = 139
            but_border_position_x = 77
            but_text_position_x = price_position_x
        if column == 2:
            price_position_x = 314
            but_border_position_x = 251
            but_text_position_x = price_position_x
        if column == 3:
            price_position_x = 487
            but_border_position_x = 425
            but_text_position_x = price_position_x
        if column == 4:
            price_position_x = 661
            but_border_position_x = 599
            but_text_position_x = price_position_x

        if row == 1:
            price_position_y = 402
            but_border_position_y = 429
            but_text_position_y = 449
        if row == 2:
            price_position_y = 662
            but_border_position_y = 689
            but_text_position_y = 709

        price_position = (price_position_x, price_position_y)
        but_border_position = (but_border_position_x, but_border_position_y)
        but_text_position = (but_text_position_x, but_text_position_y)

        if self.selected_heads:
            price_string = f"{head_price}$"
            price_text = SHOP_BUY_BUTTONS_FONT.render(price_string, True, BLACK)

            # if user bought skin
            if head_name in self.data_object.head_skins:
                but_text = SHOP_BUY_BUTTONS_FONT.render(bought_text, True, BLACK)
            else: # if DIDNT buy skin
                but_text = SHOP_BUY_BUTTONS_FONT.render(buy_text, True, BLACK)
                price_position = price_text.get_rect(center=price_position)
                screen.blit(price_text, price_position)

        if self.selected_bodies:
            price_string = f"{body_price}$"
            price_text = SHOP_BUY_BUTTONS_FONT.render(price_string, True, BLACK)

            if body_name in self.data_object.body_skins:
                but_text = SHOP_BUY_BUTTONS_FONT.render(bought_text, True, BLACK)
            else:
                but_text = SHOP_BUY_BUTTONS_FONT.render(buy_text, True, BLACK)
                price_position = price_text.get_rect(center=price_position)
                screen.blit(price_text, price_position)

        if self.selected_fruits:
            price_string = f"{fruit_price}$"
            price_text = SHOP_BUY_BUTTONS_FONT.render(price_string, True, BLACK)

            if fruit_name in self.data_object.fruit_skins:
                but_text = SHOP_BUY_BUTTONS_FONT.render(bought_text, True, BLACK)
            else:
                but_text = SHOP_BUY_BUTTONS_FONT.render(buy_text, True, BLACK)
                price_position = price_text.get_rect(center=price_position)
                screen.blit(price_text, price_position)

        if self.selected_boards:
            price_string = f"{board_price}$"
            price_text = SHOP_BUY_BUTTONS_FONT.render(price_string, True, BLACK)

            if board_name in self.data_object.board_skins:
                but_text = SHOP_BUY_BUTTONS_FONT.render(bought_text, True, BLACK)
            else:
                but_text = SHOP_BUY_BUTTONS_FONT.render(buy_text, True, BLACK)
                price_position = price_text.get_rect(center=price_position)
                screen.blit(price_text, price_position)

        but_color = GREEN_DARK
        but_border = BLACK

        # color on button HOVER
        if self_button_variable.collidepoint(curr_mouse_x, curr_mouse_y):
            but_color = GREEN

        # if user bought this skin
        if self.selected_heads and head_name in self.data_object.head_skins:
            but_border = GREY
            but_color = ORANGE
        elif self.selected_bodies and body_name in self.data_object.body_skins:
            but_border = GREY
            but_color = ORANGE
        elif self.selected_fruits and fruit_name in self.data_object.fruit_skins:
            but_border = GREY
            but_color = ORANGE
        elif self.selected_boards and board_name in self.data_object.board_skins:
            but_border = GREY
            but_color = ORANGE
        else: # if user doesn't have skin
            # if user doesn't have enough money for skin
            if self.selected_heads and head_price > self.data_object.coins:
                but_color = RED_DARK
            if self.selected_bodies and body_price > self.data_object.coins:
                but_color = RED_DARK
            if self.selected_fruits and fruit_price > self.data_object.coins:
                but_color = RED_DARK
            if self.selected_boards and board_price > self.data_object.coins:
                but_color = RED_DARK

        but_border_rect = pygame.Rect(but_border_position, (126, 46))
        but_text_position = but_text.get_rect(center=but_text_position)
        pygame.draw.rect(screen, but_border, but_border_rect)
        pygame.draw.rect(screen, but_color, self_button_variable)
        screen.blit(but_text, but_text_position)

    def draw_shop_pictures(self):
        if self.selected_first_page:
            if self.selected_heads:
                image1 = pygame.image.load(os.path.join("assets", "heads", self.head_names[0], "down.png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "heads", self.head_names[1], "down.png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "heads", self.head_names[2], "down.png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "heads", self.head_names[3], "down.png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "heads", self.head_names[4], "down.png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "heads", self.head_names[5], "down.png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "heads", self.head_names[6], "down.png")).convert_alpha()
                image8 = pygame.image.load(os.path.join("assets", "heads", self.head_names[7], "down.png")).convert_alpha()
            if self.selected_bodies:
                image1 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[0], "body_vertical.png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[1], "body_vertical.png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[2], "body_vertical.png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[3], "body_vertical.png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[4], "body_vertical.png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[5], "body_vertical.png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[6], "body_vertical.png")).convert_alpha()
                image8 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[7], "body_vertical.png")).convert_alpha()
            if self.selected_fruits:
                image1 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[0] + ".png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[1] + ".png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[2] + ".png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[3] + ".png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[4] + ".png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[5] + ".png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[6] + ".png")).convert_alpha()
                image8 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[7] + ".png")).convert_alpha()
            if self.selected_boards:
                image1 = pygame.image.load(os.path.join("assets", "boards", self.board_names[0] + ".png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "boards", self.board_names[1] + ".png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "boards", self.board_names[2] + ".png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "boards", self.board_names[3] + ".png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "boards", self.board_names[4] + ".png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "boards", self.board_names[5] + ".png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "boards", self.board_names[6] + ".png")).convert_alpha()
                image8 = pygame.image.load(os.path.join("assets", "boards", self.board_names[7] + ".png")).convert_alpha()
        if self.selected_second_page:
            if self.selected_heads:
                image1 = pygame.image.load(os.path.join("assets", "heads", self.head_names[8], "down.png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "heads", self.head_names[9], "down.png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "heads", self.head_names[10], "down.png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "heads", self.head_names[11], "down.png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "heads", self.head_names[12], "down.png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "heads", self.head_names[13], "down.png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "heads", self.head_names[14], "down.png")).convert_alpha()
            if self.selected_bodies:
                image1 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[8], "body_vertical.png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[9], "body_vertical.png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[10], "body_vertical.png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[11], "body_vertical.png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[12], "body_vertical.png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[13], "body_vertical.png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "bodies", self.body_names[14], "body_vertical.png")).convert_alpha()
            if self.selected_fruits:
                image1 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[8] + ".png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[9] + ".png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[10] + ".png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[11] + ".png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[12] + ".png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[13] + ".png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "fruits", self.fruit_names[14] + ".png")).convert_alpha()
            if self.selected_boards:
                image1 = pygame.image.load(os.path.join("assets", "boards", self.board_names[8] + ".png")).convert_alpha()
                image2 = pygame.image.load(os.path.join("assets", "boards", self.board_names[9] + ".png")).convert_alpha()
                image3 = pygame.image.load(os.path.join("assets", "boards", self.board_names[10] + ".png")).convert_alpha()
                image4 = pygame.image.load(os.path.join("assets", "boards", self.board_names[11] + ".png")).convert_alpha()
                image5 = pygame.image.load(os.path.join("assets", "boards", self.board_names[12] + ".png")).convert_alpha()
                image6 = pygame.image.load(os.path.join("assets", "boards", self.board_names[13] + ".png")).convert_alpha()
                image7 = pygame.image.load(os.path.join("assets", "boards", self.board_names[14] + ".png")).convert_alpha()


        border1_rect = pygame.Rect(85, 273, 109, 104)
        border2_rect = pygame.Rect(260, 273, 109, 104)
        border3_rect = pygame.Rect(435, 273, 109, 104)
        border4_rect = pygame.Rect(610, 273, 109, 104)
        border5_rect = pygame.Rect(85, 530, 109, 104)
        border6_rect = pygame.Rect(260, 530, 109, 104)
        border7_rect = pygame.Rect(435, 530, 109, 104)

        background1_rect = pygame.Rect(87, 275, 105, 100)
        background2_rect = pygame.Rect(262, 275, 105, 100)
        background3_rect = pygame.Rect(437, 275, 105, 100)
        background4_rect = pygame.Rect(612, 275, 105, 100)
        background5_rect = pygame.Rect(87, 532, 105, 100)
        background6_rect = pygame.Rect(262, 532, 105, 100)
        background7_rect = pygame.Rect(437, 532, 105, 100)

        pygame.draw.rect(screen, BLACK, border1_rect)
        pygame.draw.rect(screen, BLACK, border2_rect)
        pygame.draw.rect(screen, BLACK, border3_rect)
        pygame.draw.rect(screen, BLACK, border4_rect)
        pygame.draw.rect(screen, BLACK, border5_rect)
        pygame.draw.rect(screen, BLACK, border6_rect)
        pygame.draw.rect(screen, BLACK, border7_rect)

        pygame.draw.rect(screen, GRASS_COLOR, background1_rect)
        pygame.draw.rect(screen, GRASS_COLOR, background2_rect)
        pygame.draw.rect(screen, GRASS_COLOR, background3_rect)
        pygame.draw.rect(screen, GRASS_COLOR, background4_rect)
        pygame.draw.rect(screen, GRASS_COLOR, background5_rect)
        pygame.draw.rect(screen, GRASS_COLOR, background6_rect)
        pygame.draw.rect(screen, GRASS_COLOR, background7_rect)

        if self.selected_boards:
            image_size = 105
            image_position_difference = 3
        else:
            image_size = 100
            image_position_difference = 0

        image1_transformed = pygame.transform.scale(image1, (image_size, 100))
        image2_transformed = pygame.transform.scale(image2, (image_size, 100))
        image3_transformed = pygame.transform.scale(image3, (image_size, 100))
        image4_transformed = pygame.transform.scale(image4, (image_size, 100))
        image5_transformed = pygame.transform.scale(image5, (image_size, 100))
        image6_transformed = pygame.transform.scale(image6, (image_size, 100))
        image7_transformed = pygame.transform.scale(image7, (image_size, 100))

        image1_position = (90 - image_position_difference, 275)
        image2_position = (265 - image_position_difference, 275)
        image3_position = (440 - image_position_difference, 275)
        image4_position = (615 - image_position_difference, 275)
        image5_position = (90 - image_position_difference, 532)
        image6_position = (265 - image_position_difference, 532)
        image7_position = (440 - image_position_difference, 532)
        image8_position = (615 - image_position_difference, 532)

        screen.blit(image1_transformed, image1_position)
        screen.blit(image2_transformed, image2_position)
        screen.blit(image3_transformed, image3_position)
        screen.blit(image4_transformed, image4_position)
        screen.blit(image5_transformed, image5_position)
        screen.blit(image6_transformed, image6_position)
        screen.blit(image7_transformed, image7_position)

        if self.selected_first_page:
            border8_rect = pygame.Rect(610, 530, 109, 104)
            background8_rect = pygame.Rect(612, 532, 105, 100)
            pygame.draw.rect(screen, BLACK, border8_rect)
            pygame.draw.rect(screen, GRASS_COLOR, background8_rect)
            image8_transformed = pygame.transform.scale(image8, (image_size, 100))
            screen.blit(image8_transformed, image8_position)

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

    def draw_coins_bar(self):
        coins_bar_rect_border = pygame.Rect(665, 28, 104, 42)
        pygame.draw.rect(screen, BLACK, coins_bar_rect_border)

        coins_bar_rect = pygame.Rect(667, 30, 100, 38)
        pygame.draw.rect(screen, ORANGE, coins_bar_rect)

        coins_amount_text = f"$ {str(self.data_object.coins)}"
        coins_amount = COINS_MENU_FONT.render(coins_amount_text, True, BLACK)
        coins_amount_position = coins_amount.get_rect(center = (716, 49))
        screen.blit(coins_amount, coins_amount_position)

    @staticmethod
    def draw_title_and_background():
        # screen.fill(MENU_COLOR)

        background_image = pygame.image.load(os.path.join("assets", "images", "background.png")).convert_alpha()
        screen.blit(background_image, (0, 0))

        main_title_text = "Sklep"
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

    # BUYING ITEM MECHANISM
    def buy_item(self, index):
        if self.selected_heads:
            # if user doesn't have clicked skin to buy
            if self.head_names[index] not in self.data_object.head_skins:
                # if user has enough money to buy it
                if self.data_object.coins >= self.head_prices[index]:
                    # buying it clicked skin
                    self.play_buy_sound()
                    self.data_object.coins -= self.head_prices[index]
                    self.data_object.head_skins += f",{self.head_names[index]}"
                    self.data_object.head_skin = self.head_names[index]
        if self.selected_bodies:
            # if user doesn't have clicked skin to buy
            if self.body_names[index] not in self.data_object.body_skins:
                # if user has enough money to buy it
                if self.data_object.coins >= self.body_prices[index]:
                    # buying it clicked skin
                    self.play_buy_sound()
                    self.data_object.coins -= self.body_prices[index]
                    self.data_object.body_skins += f",{self.body_names[index]}"
                    self.data_object.body_skin = self.body_names[index]
        if self.selected_fruits:
            # if user doesn't have clicked skin to buy
            if self.fruit_names[index] not in self.data_object.fruit_skins:
                # if user has enough money to buy it
                if self.data_object.coins >= self.fruit_prices[index]:
                    # buying it clicked skin
                    self.play_buy_sound()
                    self.data_object.coins -= self.fruit_prices[index]
                    self.data_object.fruit_skins += f",{self.fruit_names[index]}"
                    self.data_object.fruit_skin = self.fruit_names[index]
        if self.selected_boards:
            # if user doesn't have clicked skin to buy
            if self.board_names[index] not in self.data_object.board_skins:
                # if user has enough money to buy it
                if self.data_object.coins >= self.board_prices[index]:
                    # buying it clicked skin
                    self.play_buy_sound()
                    self.data_object.coins -= self.board_prices[index]
                    self.data_object.board_skins += f",{self.board_names[index]}"
                    self.data_object.board_skin = self.board_names[index]
        self.data_object.save_user_data()

    def select_tab(self, tab):
        self.reset_selected_tab()

        if tab == "heads": self.selected_heads = True
        elif tab == "bodies": self.selected_bodies = True
        elif tab == "fruits": self.selected_fruits = True
        elif tab == "boards": self.selected_boards = True

    def reset_selected_tab(self):
        self.selected_heads = False
        self.selected_bodies = False
        self.selected_fruits = False
        self.selected_boards = False
        self.selected_first_page = True
        self.selected_second_page = False
