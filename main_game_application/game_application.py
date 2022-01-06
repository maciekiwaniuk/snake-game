import pygame
from pygame.math import Vector2
import random
import os
import json
import sys
import requests

from constants import *
from env import VERSION, SECRET_GAME_KEY, URL
from main_game_application.snake_game.snake_game import SnakeGame

from main_game_application.tabs.welcome import WelcomeMenu
from main_game_application.tabs.shop import ShopMenu
from main_game_application.tabs.inventory import InventoryMenu
from main_game_application.tabs.options import OptionsMenu
from main_game_application.tabs.statistics import StatisticsMenu
from main_game_application.tabs.upgrades import UpgradesMenu

from main_game_application.user_data import UserData

# initialize sounds
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

# initialize all imported pygame modules
pygame.init()

# initialize fonts
pygame.font.init()

# set game icon
game_icon = pygame.image.load(os.path.join('assets', 'others', 'icon.png'))
pygame.display.set_icon(game_icon)


# class for main program which handles all actions
class MainProgram:
    def __init__(self):
        self.user_data = UserData()
        self.user_data.create_open_game_log()

        self.snake_game = SnakeGame(self.user_data)

        self.welcome = WelcomeMenu(self.user_data)

        self.shop = ShopMenu(self.user_data)

        self.inventory = InventoryMenu(self.user_data)

        self.options = OptionsMenu(self.user_data)

        self.upgrades = UpgradesMenu(self.user_data)

        self.statistics = StatisticsMenu(self.user_data)

        # default when first time opens app
        self.play_game = False
        self.open_welcome_menu = True
        self.open_shop = False
        self.open_inventory = False
        self.open_options = False
        self.open_upgrades = False
        self.open_statistics = False

        self.welcome.play_menu_music()

    def play_click_sound(self):
        if self.user_data.effects == True:
            click_sound.set_volume(self.user_data.volume)
            click_sound.play()

    def reset_selected_menu(self):
        self.play_game = False
        self.open_welcome_menu = False
        self.open_shop = False
        self.open_inventory = False
        self.open_options = False
        self.open_upgrades = False
        self.open_statistics = False

    def selected_welcome_menu(self):
        if self.play_game == True:
            self.snake_game.stop_game_music()
            self.welcome.play_menu_music()

        self.reset_selected_menu()
        self.open_welcome_menu = True

    def selected_play_snake(self):
        self.reset_selected_menu()
        self.play_game = True

        self.welcome.stop_menu_music()
        self.snake_game.play_game_music()

    def selected_options(self):
        self.reset_selected_menu()
        self.open_options = True

    def selected_shop(self):
        self.reset_selected_menu()
        self.open_shop = True

    def selected_inventory(self):
        self.reset_selected_menu()
        self.open_inventory = True

    def selected_upgrades(self):
        self.reset_selected_menu()
        self.open_upgrades = True

    def selected_statistics(self):
        self.reset_selected_menu()
        self.open_statistics = True

    def exit_program(self):
        self.user_data.save_user_data()
        self.user_data.create_exit_game_log()
        pygame.quit()
        sys.exit()


main_program = MainProgram()


def run_game_application():
    while True:
        # fps clock
        clock.tick(main_program.user_data.fps)

        # setting default value after refreshing
        click = False
        slider_dragging = False

        # current mouse positions x = width, y = height
        curr_mouse_x, curr_mouse_y = pygame.mouse.get_pos()

        # WELCOME MENU
        if main_program.open_welcome_menu == True:
            main_program.welcome.draw_welcome_menu(curr_mouse_x, curr_mouse_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                # SHORTCUTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        main_program.selected_play_snake()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        # MEDIUM AND HARD ISNT UNLOCKED
                        if main_program.user_data.medium_diff == 0 and main_program.user_data.hard_diff == 0:
                            if main_program.user_data.selected_lvl == "speed":
                                main_program.user_data.selected_lvl = "easy"

                        # MEDIUM UNLOCKED BUT HARD NOT
                        if main_program.user_data.medium_diff == 1 and main_program.user_data.hard_diff == 0:
                            if main_program.user_data.selected_lvl == "medium":
                                main_program.user_data.selected_lvl = "easy"
                            if main_program.user_data.selected_lvl == "speed":
                                main_program.user_data.selected_lvl = "medium"

                        # MEDIUM UNLOCKED AND HARD UNLOCKED
                        if main_program.user_data.medium_diff == 1 and main_program.user_data.hard_diff == 1:
                            if main_program.user_data.selected_lvl == "medium":
                                main_program.user_data.selected_lvl = "easy"
                            if main_program.user_data.selected_lvl == "hard":
                                main_program.user_data.selected_lvl = "medium"
                            if main_program.user_data.selected_lvl == "speed":
                                main_program.user_data.selected_lvl = "hard"

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        # MEDIUM AND HARD ISNT UNLOCKED
                        if main_program.user_data.medium_diff == 0 and main_program.user_data.hard_diff == 0:
                            if main_program.user_data.selected_lvl == "easy":
                                if main_program.user_data.speed_diff == 1:
                                    main_program.user_data.selected_lvl = "speed"

                        # MEDIUM UNLOCKED BUT HARD NOT
                        if main_program.user_data.medium_diff == 1 and main_program.user_data.hard_diff == 0:
                            if main_program.user_data.selected_lvl == "medium":
                                if main_program.user_data.speed_diff:
                                    main_program.user_data.selected_lvl = "speed"
                            if main_program.user_data.selected_lvl == "easy":
                                main_program.user_data.selected_lvl = "medium"

                        # MEDIUM UNLOCKED AND HARD UNLOCKED
                        if main_program.user_data.medium_diff == 1 and main_program.user_data.hard_diff == 1:
                            if main_program.user_data.selected_lvl == "hard":
                                if main_program.user_data.speed_diff:
                                    main_program.user_data.selected_lvl = "speed"
                            if main_program.user_data.selected_lvl == "medium":
                                main_program.user_data.selected_lvl = "hard"
                            if main_program.user_data.selected_lvl == "easy":
                                main_program.user_data.selected_lvl = "medium"

                if click:
                    if main_program.welcome.exit_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.exit_program()

                    if main_program.welcome.play_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_play_snake()

                    if main_program.welcome.shop_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_shop()

                    if main_program.welcome.inventory_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_inventory()

                    if main_program.welcome.options_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_options()

                    if main_program.welcome.upgrades_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_upgrades()

                    if main_program.welcome.stats_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_statistics()

                    # EASY
                    if main_program.welcome.easy_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.selected_lvl != "easy":
                            main_program.play_click_sound()
                            main_program.user_data.selected_lvl = "easy"

                    # MEDIUM
                    if main_program.welcome.medium_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.medium_diff == True:
                            if main_program.user_data.selected_lvl != "medium":
                                main_program.play_click_sound()
                                main_program.user_data.selected_lvl = "medium"

                    # HARD
                    if main_program.welcome.hard_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.hard_diff == True:
                            if main_program.user_data.selected_lvl != "hard":
                                main_program.play_click_sound()
                                main_program.user_data.selected_lvl = "hard"

                    # SPEED
                    if main_program.welcome.speed_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.speed_diff == True:
                            if main_program.user_data.selected_lvl != "speed":
                                main_program.play_click_sound()
                                main_program.user_data.selected_lvl = "speed"

                    if main_program.welcome.logout_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.user_data.save_user_data()
                        main_program.user_data.create_logout_game_log()
                        path = f"{os.getenv('APPDATA')}/SnakeGame/api_token.ini"
                        with open(path, "w") as api_token_file:
                            api_token_file.write("")
                        pygame.quit()
                        sys.exit()
                        # import application
                        # application.application()

        # GAME
        if main_program.play_game == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                if click:
                    # CLICK IN RETURN
                    if main_program.snake_game.return_bar_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.snake_game = SnakeGame(main_program.user_data)
                        main_program.selected_welcome_menu()
                        break

                    # CLICK ON RESTART / MENU RETURN WHEN LOST
                    if main_program.snake_game.lost_game == True:
                        if main_program.snake_game.restart_window_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                                main_program.play_click_sound()
                                main_program.snake_game.lost_game = False
                                main_program.snake_game = SnakeGame(main_program.user_data)
                                break
                        if main_program.snake_game.return_window_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                                main_program.play_click_sound()
                                main_program.snake_game.lost_game = False
                                main_program.snake_game = SnakeGame(main_program.user_data)
                                main_program.selected_welcome_menu()
                                break

                # difficulty levels
                if main_program.user_data.selected_lvl == "easy":
                    if event.type == EASY_DIFF_LVL_UPDATE:
                        if main_program.snake_game.lost_game == False:
                            main_program.snake_game.update()
                if main_program.user_data.selected_lvl == "medium":
                    if event.type == MEDIUM_DIFF_LVL_UPDATE:
                        if main_program.snake_game.lost_game == False:
                            main_program.snake_game.update()
                if main_program.user_data.selected_lvl == "hard":
                    if event.type == HARD_DIFF_LVL_UPDATE:
                        if main_program.snake_game.lost_game == False:
                            main_program.snake_game.update()
                if main_program.user_data.selected_lvl == "speed":
                    if event.type == main_program.snake_game.SPEED_LVL_TIMER_UPDATE:
                        if main_program.snake_game.lost_game == False:
                            main_program.snake_game.update()

                # update time playing data - increase 1s
                if event.type == GAME_TIMER_UPDATE:
                    if main_program.snake_game.lost_game == False:
                        if main_program.snake_game.snake.direction != Vector2(0, 0):
                            main_program.user_data.play_time_seconds += 1

                # SNAKE MOVEMENT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if main_program.snake_game.snake.direction.y != 1:
                            if main_program.snake_game.snake.body[0].y != (main_program.snake_game.snake.body[1].y) + 1:
                                # add games amount +1 to data when snake moved first time
                                if main_program.snake_game.snake.direction == Vector2(0, 0):
                                    main_program.user_data.games_amount += 1
                                main_program.snake_game.snake.direction = Vector2(0, -1)
                                main_program.user_data.clicks += 1

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if main_program.snake_game.snake.direction.y != -1:
                            if main_program.snake_game.snake.body[0].y != (main_program.snake_game.snake.body[1].y) - 1:
                                if main_program.snake_game.snake.direction == Vector2(0, 0):
                                    main_program.user_data.games_amount += 1
                                main_program.snake_game.snake.direction = Vector2(0, 1)
                                main_program.user_data.clicks += 1


                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if main_program.snake_game.snake.direction.x != 1:
                            if main_program.snake_game.snake.body[0].x != (main_program.snake_game.snake.body[1].x) + 1:
                                if main_program.snake_game.snake.direction == Vector2(0, 0):
                                    main_program.user_data.games_amount += 1
                                main_program.snake_game.snake.direction = Vector2(-1, 0)
                                main_program.user_data.clicks += 1

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if main_program.snake_game.snake.direction.x != -1:
                            if main_program.snake_game.snake.body[0].x != (main_program.snake_game.snake.body[1].x) - 1:
                                if main_program.snake_game.snake.direction == Vector2(0, 0):
                                    main_program.user_data.games_amount += 1
                                main_program.snake_game.snake.direction = Vector2(1, 0)
                                main_program.user_data.clicks += 1

                    # SHORTCUTS
                    if main_program.snake_game.lost_game == True:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            main_program.snake_game.lost_game = False
                            main_program.snake_game = SnakeGame(main_program.user_data)

                    if event.key == pygame.K_ESCAPE:
                        main_program.snake_game.lost_game = False
                        main_program.snake_game = SnakeGame(main_program.user_data)
                        main_program.selected_welcome_menu()

                # draw elements on screen GAME
                main_program.snake_game.draw_elements(curr_mouse_x, curr_mouse_y)

        # SHOP
        if main_program.open_shop == True:
            main_program.shop.draw_shop(curr_mouse_x, curr_mouse_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                # SHORTCUTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_program.selected_welcome_menu()

                if click:
                    # CLICK RETURN BUTTON
                    if main_program.options.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_welcome_menu()

                    # CLICK SHOP ITEMS SELECT BUTTON
                    if main_program.shop.heads_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.shop.selected_heads == False:
                            main_program.play_click_sound()
                        main_program.shop.selected_heads = True
                        main_program.shop.selected_bodies = False
                        main_program.shop.selected_fruits = False
                        main_program.shop.selected_boards = False
                        main_program.shop.selected_first_page = True
                        main_program.shop.selected_second_page = False
                    if main_program.shop.bodies_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.shop.selected_bodies == False:
                            main_program.play_click_sound()
                        main_program.shop.selected_heads = False
                        main_program.shop.selected_bodies = True
                        main_program.shop.selected_fruits = False
                        main_program.shop.selected_boards = False
                        main_program.shop.selected_first_page = True
                        main_program.shop.selected_second_page = False
                    if main_program.shop.fruits_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.shop.selected_fruits == False:
                            main_program.play_click_sound()
                        main_program.shop.selected_heads = False
                        main_program.shop.selected_bodies = False
                        main_program.shop.selected_fruits = True
                        main_program.shop.selected_boards = False
                        main_program.shop.selected_first_page = True
                        main_program.shop.selected_second_page = False
                    if main_program.shop.boards_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.shop.selected_boards == False:
                            main_program.play_click_sound()
                        main_program.shop.selected_heads = False
                        main_program.shop.selected_bodies = False
                        main_program.shop.selected_fruits = False
                        main_program.shop.selected_boards = True
                        main_program.shop.selected_first_page = True
                        main_program.shop.selected_second_page = False

                    # CLICK ON BUY BUTTONS
                    if main_program.shop.selected_first_page:
                        if main_program.shop.but1_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(0)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but2_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(1)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but3_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(2)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but4_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(3)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but5_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(4)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but6_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(5)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but7_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(6)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but8_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(7)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                    elif main_program.shop.selected_second_page:

                        if main_program.shop.but1_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(8)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but2_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(9)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but3_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(10)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but4_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(11)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but5_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(12)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but6_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(13)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)

                        if main_program.shop.but7_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.shop.buy_item(14)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                            main_program.inventory = InventoryMenu(main_program.user_data)


                    # CLICK ON PAGE BUTTONS
                    if main_program.shop.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.shop.selected_second_page:
                            main_program.play_click_sound()
                            main_program.shop.selected_first_page = True
                            main_program.shop.selected_second_page = False

                    if main_program.shop.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.shop.selected_first_page:
                            main_program.play_click_sound()
                            main_program.shop.selected_second_page = True
                            main_program.shop.selected_first_page = False

        # INVENTORY
        if main_program.open_inventory == True:
            main_program.inventory.draw_inventory(curr_mouse_x, curr_mouse_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                # SHORTCUTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_program.selected_welcome_menu()

                if click:
                    # CLICK RETURN BUTTON
                    if main_program.options.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_welcome_menu()

                    # CLICK SNAKES BUTTON
                    if main_program.inventory.heads_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_heads == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = True
                        main_program.inventory.selected_bodies = False
                        main_program.inventory.selected_fruits = False
                        main_program.inventory.selected_boards = False
                        main_program.inventory.selected_first_page = True
                        main_program.inventory.selected_second_page = False
                    if main_program.inventory.bodies_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_bodies == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = False
                        main_program.inventory.selected_bodies = True
                        main_program.inventory.selected_fruits = False
                        main_program.inventory.selected_boards = False
                        main_program.inventory.selected_first_page = True
                        main_program.inventory.selected_second_page = False
                    if main_program.inventory.fruits_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_fruits == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = False
                        main_program.inventory.selected_bodies = False
                        main_program.inventory.selected_fruits = True
                        main_program.inventory.selected_boards = False
                        main_program.inventory.selected_first_page = True
                        main_program.inventory.selected_second_page = False
                    if main_program.inventory.boards_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_boards == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = False
                        main_program.inventory.selected_bodies = False
                        main_program.inventory.selected_fruits = False
                        main_program.inventory.selected_boards = True
                        main_program.inventory.selected_first_page = True
                        main_program.inventory.selected_second_page = False

                    # CLICK INVENTORY ITEMS SELECT BUTTON
                    if main_program.inventory.heads_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_heads == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = True
                        main_program.inventory.selected_bodies = False
                        main_program.inventory.selected_fruits = False
                        main_program.inventory.selected_boards = False
                    if main_program.inventory.bodies_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_bodies == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = False
                        main_program.inventory.selected_bodies = True
                        main_program.inventory.selected_fruits = False
                        main_program.inventory.selected_boards = False
                    if main_program.inventory.fruits_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_fruits == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = False
                        main_program.inventory.selected_bodies = False
                        main_program.inventory.selected_fruits = True
                        main_program.inventory.selected_boards = False
                    if main_program.inventory.boards_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.inventory.selected_boards == False:
                            main_program.play_click_sound()
                        main_program.inventory.selected_heads = False
                        main_program.inventory.selected_bodies = False
                        main_program.inventory.selected_fruits = False
                        main_program.inventory.selected_boards = True

                    # CLICKS ON SELECT SKIN BUTTONS
                    if main_program.inventory.selected_first_page:
                        if main_program.inventory.but1_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(0)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but2_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(1)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but3_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(2)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but4_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(3)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but5_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(4)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but6_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(5)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but7_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(6)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but8_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(7)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                    if main_program.inventory.selected_second_page:
                        if main_program.inventory.but1_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(8)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but2_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(9)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but3_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(10)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but4_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(11)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but5_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(12)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but6_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(13)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but7_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(14)
                            main_program.snake_game = SnakeGame(main_program.user_data)
                        if main_program.inventory.but8_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                            main_program.inventory.select_item(15)
                            main_program.snake_game = SnakeGame(main_program.user_data)


                    # CLICKS ON PAGE BUTTONS
                    if ((main_program.inventory.selected_heads and len(main_program.inventory.heads_in_inventory) > 8) or
                        (main_program.inventory.selected_bodies and len(main_program.inventory.bodies_in_inventory) > 8) or
                        (main_program.inventory.selected_fruits and len(main_program.inventory.fruits_in_inventory) > 8) or
                        (main_program.inventory.selected_boards and len(main_program.inventory.boards_in_inventory) > 8)):
                        if main_program.inventory.selected_first_page:
                            if main_program.inventory.second_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                                main_program.play_click_sound()
                                main_program.inventory.selected_second_page = True
                                main_program.inventory.selected_first_page = False
                        if main_program.inventory.selected_second_page:
                            if main_program.inventory.first_page_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                                main_program.play_click_sound()
                                main_program.inventory.selected_second_page = False
                                main_program.inventory.selected_first_page = True

        # OPTIONS
        if main_program.open_options == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                # SHORTCUTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_program.selected_welcome_menu()

                # HOLDING MOUSE BUTTON
                if pygame.mouse.get_pressed()[0]:
                    if main_program.options.volume_slider_drag_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.options.draw_options_menu(curr_mouse_x, curr_mouse_y)
                        main_program.options.draw_volume(hover=True, mouse_down=True)
                        slider_dragging = True
                else:
                    if main_program.options.volume_slider_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.options.draw_options_menu(curr_mouse_x, curr_mouse_y)
                        main_program.options.draw_volume(hover=True, mouse_down=False)
                    else:
                        main_program.options.draw_options_menu(curr_mouse_x, curr_mouse_y)
                        main_program.options.draw_volume(hover=False, mouse_down=False)

                # WHEN HOLDING MOUSE ON VOLUME SLIDER
                if slider_dragging == True:
                    main_program.options.change_slider_position(curr_mouse_x)
                    main_program.options.check_for_changed_volume(curr_mouse_x)

                if click:
                    # CLICK SOUND ON SLIDER BUTTON
                    if main_program.options.volume_slider_border_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()

                    # CLICK RETURN BUTTON
                    if main_program.options.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_welcome_menu()

                    # CLICK ON MUSIC BUTTONS
                    if main_program.options.music_on_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.music == 0:
                            main_program.play_click_sound()
                            main_program.user_data.music = 1
                            main_program.welcome.play_menu_music()
                    if main_program.options.music_off_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.music == 1:
                            main_program.play_click_sound()
                            main_program.welcome.stop_menu_music()
                            main_program.user_data.music = 0

                    # CLICK ON EFFECTS BUTTONS
                    if main_program.options.effects_on_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.effects == 0:
                            main_program.user_data.effects = 1
                            main_program.play_click_sound()
                    if main_program.options.effects_off_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.effects == 1:
                            main_program.user_data.effects = 0

                    # SWITCH FPS BUTTONS
                    if main_program.options.fps30_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.fps != 30:
                            main_program.play_click_sound()
                            main_program.user_data.fps = 30
                    if main_program.options.fps60_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.fps != 60:
                            main_program.play_click_sound()
                            main_program.user_data.fps = 60
                    if main_program.options.fps144_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.fps != 144:
                            main_program.play_click_sound()
                            main_program.user_data.fps = 144
                    if main_program.options.fps240_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        if main_program.user_data.fps != 240:
                            main_program.play_click_sound()
                            main_program.user_data.fps = 240

        # UPGRADES
        if main_program.open_upgrades == True:
            main_program.upgrades.draw_upgrades(curr_mouse_x, curr_mouse_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                # SHORTCUTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_program.selected_welcome_menu()

                if click:
                    # CLICK RETURN BUTTON
                    if main_program.upgrades.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_welcome_menu()

                    # CLICK BUY FRUIT UPGRADE BUTTON
                    if main_program.upgrades.buy_fruit_but.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.buy_fruit_upgrade()

                    # CLICK SELECT FRUIT UPGRADE BUTTON
                    if main_program.upgrades.select_fruit_but1.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.select_fruit_upgrade(0)
                    if main_program.upgrades.select_fruit_but2.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.select_fruit_upgrade(1)
                    if main_program.upgrades.select_fruit_but3.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.select_fruit_upgrade(2)

                    # CLICK BUY LVL BUTTON
                    if main_program.upgrades.buy_lvl_but.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.buy_lvl_upgrades()

                    # CLICK BUY COINS UPGRADE LVL
                    if main_program.upgrades.buy_coins_but.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.buy_coins_upgrade()

                    # CLICK BUY POINTS UPGRADE LVL
                    if main_program.upgrades.buy_points_but.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.upgrades.buy_points_upgrade()

        # STATISTICS
        if main_program.open_statistics == True:
            main_program.statistics.draw_statistics(curr_mouse_x, curr_mouse_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_program.exit_program()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    click = True

                # SHORTCUTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_program.selected_welcome_menu()

                if click:
                    # CLICK RETURN BUTTON
                    if main_program.statistics.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                        main_program.play_click_sound()
                        main_program.selected_welcome_menu()

        # screen update FPS times per second
        pygame.display.update()
