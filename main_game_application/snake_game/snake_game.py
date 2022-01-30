import random
import os
import json
import sys
import pygame
from pygame.math import Vector2

from constants import *

from main_game_application.snake_game.fruit import Fruit
from main_game_application.snake_game.snake import Snake

# initialize all imported pygame modules
pygame.init()

# initialize fonts
pygame.font.init()


class SnakeGame:
    # creating snake and fruit objects
    def __init__(self, data_object):
        self.data_object = data_object

        self.snake = Snake(data_object)

        self.fruit = Fruit(data_object)
        self.fruit2 = Fruit(data_object)
        self.fruit3 = Fruit(data_object)

        while (self.fruit.position in self.snake.body):
            self.fruit = Fruit(data_object)

        if self.data_object.selected_fruits_upgrade_lvl > 0:
            while (self.fruit2.position in self.snake.body or self.fruit2.position == self.fruit.position):
                self.fruit2 = Fruit(data_object)

        if self.data_object.selected_fruits_upgrade_lvl > 1:
            while (self.fruit3.position in self.snake.body or self.fruit3.position == self.fruit.position or
                   self.fruit3.position == self.fruit2.position):
                self.fruit3 = Fruit(data_object)

        # FOR SPEED LVL DIFFICULTY
        self.SNAKE_SPEED_LVL_VALUE = 115
        self.SPEED_LVL_TIMER_UPDATE = pygame.USEREVENT + 4
        pygame.time.set_timer(self.SPEED_LVL_TIMER_UPDATE, self.SNAKE_SPEED_LVL_VALUE)

        self.return_bar_button_rect = pygame.Rect(20, 5, 100, 30)
        self.restart_window_button_rect = pygame.Rect(275, 350, 250, 70)
        self.return_window_button_rect = pygame.Rect(300, 457, 200, 70)

        self.lost_game = False

        you_lost_tab = [
            "Następnym razem będzie lepiej!",
            "Ups...",
            "Coś chyba poszło nie tak...",
            "Nie poddawaj się!",
            "Dobrze było!",
            "Ajajajajjj...",
            "Cóż za niefart...",
            "O cholera...",
            "Dobrze żarło i zdechło..",
            "Ale pech..."
        ]
        self.you_lost_text = random.choice(you_lost_tab)

    # updating snake's position
    def update(self):
        if self.snake.direction != Vector2(0, 0):
            self.snake.move_snake()

        # checking if snake ate fruit
        self.check_collision()

        # checking if snake went out of the board
        self.check_fail()

    # speed increase for SPEED lvl difficulty
    def make_snake_faster(self):
        score = len(self.snake.body) - 3

        self.SNAKE_SPEED_LVL_VALUE -= 1

        if score >= 26:
            if score % 2 == 0:
                self.SNAKE_SPEED_LVL_VALUE += 1

        pygame.time.set_timer(self.SPEED_LVL_TIMER_UPDATE, self.SNAKE_SPEED_LVL_VALUE)

    # checking if snake's ate fruit
    def check_collision(self):
        ate_fruit = False
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize_position()
            self.snake.add_block()
            self.play_eat_fruit_sound()
            self.data_object.ate_fruits_amount += 1
            ate_fruit = True

        if self.data_object.selected_fruits_upgrade_lvl > 0:
            if self.fruit2.position == self.snake.body[0]:
                self.fruit2.randomize_position()
                self.snake.add_block()
                self.play_eat_fruit_sound()
                self.data_object.ate_fruits_amount += 1
                ate_fruit = True

        if self.data_object.selected_fruits_upgrade_lvl > 1:
            if self.fruit3.position == self.snake.body[0]:
                self.fruit3.randomize_position()
                self.snake.add_block()
                self.play_eat_fruit_sound()
                self.data_object.ate_fruits_amount += 1
                ate_fruit = True

        # ate fruit
        if ate_fruit:
            ate_fruit = False

            if self.data_object.selected_lvl == "speed":
                self.make_snake_faster()

            coins_gain = 1
            points_gain = 10

            # COINS UPGRADE LVL
            if self.data_object.coins_upgrade_lvl == 1: coins_gain += 1
            elif self.data_object.coins_upgrade_lvl == 2: coins_gain += 2
            elif self.data_object.coins_upgrade_lvl == 3: coins_gain += 3

            # POINTS UPGRADE LVL
            if self.data_object.points_upgrade_lvl == 1: points_gain += 10
            elif self.data_object.points_upgrade_lvl == 2: points_gain += 20
            elif self.data_object.points_upgrade_lvl == 3: points_gain += 30

            if self.data_object.selected_lvl == "easy":
                rounds_bonus = self.score // 20
                coins_gain += (rounds_bonus * 1)
                points_gain += self.score
                self.data_object.coins += coins_gain
                self.data_object.total_coins_earned += coins_gain
                self.data_object.points += points_gain
                self.data_object.ate_fruits_on_easy += 1

            if self.data_object.selected_lvl == "medium":
                rounds_bonus = self.score // 15
                coins_gain += 2
                coins_gain += (rounds_bonus * 1)
                points_gain += 20
                points_gain += self.score
                self.data_object.coins += coins_gain
                self.data_object.total_coins_earned += coins_gain
                self.data_object.points += points_gain
                self.data_object.ate_fruits_on_medium += 1

            if self.data_object.selected_lvl == "hard":
                rounds_bonus = self.score // 10
                coins_gain += 4
                coins_gain += (rounds_bonus * 1)
                points_gain += 40
                points_gain += self.score
                self.data_object.coins += coins_gain
                self.data_object.total_coins_earned += coins_gain
                self.data_object.points += points_gain
                self.data_object.ate_fruits_on_hard += 1

            if self.data_object.selected_lvl == "speed":
                # easy
                if self.score < 5:
                    rounds_bonus = self.score // 20
                    coins_gain += (rounds_bonus * 1)
                    points_gain += self.score
                # medium
                elif self.score < 10:
                    rounds_bonus = self.score // 15
                    coins_gain += 2
                    coins_gain += (rounds_bonus * 1)
                    points_gain += 20
                    points_gain += self.score
                # hard
                elif self.score < 40:
                    rounds_bonus = self.score // 15
                    coins_gain += 3
                    coins_gain += (rounds_bonus * 1)
                    points_gain += 30
                    points_gain += self.score
                # harder
                else:
                    rounds_bonus = self.score // 10
                    coins_gain += 4
                    coins_gain += (rounds_bonus * 1)
                    points_gain += 40
                    points_gain += self.score

                self.data_object.coins += coins_gain
                self.data_object.total_coins_earned += coins_gain
                self.data_object.points += points_gain
                self.data_object.ate_fruits_on_speed += 1

            while (self.fruit.position in self.snake.body):
                self.fruit.randomize_position()

            if self.data_object.selected_fruits_upgrade_lvl > 0:
                while (self.fruit2.position in self.snake.body or self.fruit.position == self.fruit2.position):
                    self.fruit2.randomize_position()

            if self.data_object.selected_fruits_upgrade_lvl > 1:
                while (self.fruit3.position in self.snake.body or self.fruit.position == self.fruit3.position or
                       self.fruit2.position == self.fruit3.position):
                    self.fruit3.randomize_position()

    # checking if snake went out of the board or ran into body segment
    def check_fail(self):
        if (self.snake.body[0].x >= CELL_NUMBER or 0 > self.snake.body[0].x or
            self.snake.body[0].y >= (CELL_NUMBER + 1) or 1 > self.snake.body[0].y):
            self.lost_game = True
            self.play_punch_sound()
            self.data_object.hit_wall += 1
            self.data_object.save_user_data()

        for body_segment in self.snake.body[1:]:
            if body_segment == self.snake.body[0]:
                self.lost_game = True
                self.play_punch_sound()
                self.data_object.hit_snake += 1
                self.data_object.save_user_data()

    def play_eat_fruit_sound(self):
        if self.data_object.effects == True:
            slurp_sound.set_volume(self.data_object.volume)
            slurp_sound.play()

    def play_punch_sound(self):
        if self.data_object.effects == True:
            punch_sound.set_volume(self.data_object.volume)
            punch_sound.play()

    def play_game_music(self):
        if self.data_object.music == True:
            if self.data_object.selected_lvl == "easy":
                game_music_easy_sound.set_volume(self.data_object.volume)
                game_music_easy_sound.play(-1)
            elif self.data_object.selected_lvl == "medium":
                game_music_medium_sound.set_volume(self.data_object.volume)
                game_music_medium_sound.play(-1)
            elif self.data_object.selected_lvl == "hard":
                game_music_hard_sound.set_volume(self.data_object.volume)
                game_music_hard_sound.play(-1)
            elif self.data_object.selected_lvl == "speed":
                game_music_speed_sound.set_volume(self.data_object.volume)
                game_music_speed_sound.play(-1)

    def stop_game_music(self):
        if self.data_object.selected_lvl == "easy":
            game_music_easy_sound.stop()
        elif self.data_object.selected_lvl == "medium":
            game_music_medium_sound.stop()
        elif self.data_object.selected_lvl == "hard":
            game_music_hard_sound.stop()
        elif self.data_object.selected_lvl == "speed":
            game_music_speed_sound.stop()

    def draw_elements(self, curr_mouse_x, curr_mouse_y):
        self.draw_board()
        self.draw_game_top_bar()
        self.draw_current_score()
        self.draw_coins_amount()
        self.draw_current_record()
        self.draw_current_lvl()

        if self.return_bar_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_return_button(True)
        else:
            self.draw_return_button(False)

        if self.lost_game == False:
            self.fruit.draw_fruit()
            if self.data_object.selected_fruits_upgrade_lvl > 0:
                self.fruit2.draw_fruit()
            if self.data_object.selected_fruits_upgrade_lvl > 1:
                self.fruit3.draw_fruit()
            self.snake.draw_snake()

        if self.lost_game == True:
            if self.return_window_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                self.draw_lost_window(True, False)
            elif self.restart_window_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
                self.draw_lost_window(False, True)
            else:
                self.draw_lost_window(False, False)

        screen.blit(cursor_image, (curr_mouse_x, curr_mouse_y))

    def draw_lost_window(self, return_hover, restart_hover):
        if return_hover == True: color_return = GRASS_COLOR
        if return_hover == False: color_return = GREEN_DARK
        if restart_hover == True: color_restart = GRASS_COLOR
        if restart_hover == False: color_restart = GREEN_DARK
        window_rect = pygame.Rect(200, 280, 400, 280)
        window_rect_border = pygame.Rect(197, 277, 406, 286)

        you_lost_text = YOU_LOST_FONT.render(self.you_lost_text, True, BLACK)
        you_lost_text_position = you_lost_text.get_rect(center = (WIDTH/2, 300))

        restart_window_button_border = pygame.Rect(272, 347, 256, 76)
        restart_string = "Zagraj ponownie"
        restart_text = RESTART_FONT.render(restart_string, True, BLACK)
        restart_position = restart_text.get_rect(center = (400, 385))

        return_window_button_border = pygame.Rect(297, 454, 206, 76)
        return_window_string = "Menu"
        return_window_text = TO_MENU_FONT.render(return_window_string, True, BLACK)
        return_window_position = return_window_text.get_rect(center = (400, 492))

        pygame.draw.rect(screen, WHITE, window_rect_border)
        pygame.draw.rect(screen, YELLOW, window_rect)
        screen.blit(you_lost_text, you_lost_text_position)

        pygame.draw.rect(screen, WHITE, return_window_button_border)
        pygame.draw.rect(screen, color_return, self.return_window_button_rect)
        screen.blit(return_window_text, return_window_position)


        pygame.draw.rect(screen, WHITE, restart_window_button_border)
        pygame.draw.rect(screen, color_restart, self.restart_window_button_rect)
        screen.blit(restart_text, restart_position)

    @staticmethod
    def draw_game_top_bar():
        interface_width = (CELL_SIZE * CELL_NUMBER)
        interface_height = CELL_SIZE

        interface_rect = pygame.Rect(0, 0, interface_width, interface_height)
        interface_bottom_border = pygame.Rect(0, CELL_SIZE, interface_width, 2)

        pygame.draw.rect(screen, BLACK, interface_rect)
        pygame.draw.rect(screen, WHITE, interface_bottom_border)

    def draw_return_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GRASS_COLOR
        return_button_border = pygame.Rect(19, 4, 102, 32)
        return_button_string = "Powrót"
        return_button_text = GAME_BAR_FONT.render(return_button_string, True, BLACK)
        return_button_text_position = return_button_text.get_rect(center=(70, 19))

        pygame.draw.rect(screen, WHITE, return_button_border)
        pygame.draw.rect(screen, color, self.return_bar_button_rect)
        screen.blit(return_button_text, return_button_text_position)

    def draw_current_lvl(self):
        current_lvl_border = pygame.Rect(160, 4, 133, 32)
        current_lvl_rect = pygame.Rect(161, 5, 131, 30)
        current_lvl_string = f"LVL: {self.data_object.selected_lvl.capitalize()}"

        current_lvl_text = GAME_BAR_FONT.render(current_lvl_string, True, BLACK)
        current_lvl_text_position = current_lvl_text.get_rect(center=(226, 19))

        pygame.draw.rect(screen, WHITE, current_lvl_border)
        pygame.draw.rect(screen, GRASS_COLOR, current_lvl_rect)
        screen.blit(current_lvl_text, current_lvl_text_position)

    def draw_current_record(self):
        current_record_border = pygame.Rect(345, 4, 121, 32)
        current_record_rect = pygame.Rect(346, 5, 119, 30)

        lvl = self.data_object.selected_lvl
        if lvl == "easy": record = self.data_object.easy_record
        if lvl == "medium": record = self.data_object.medium_record
        if lvl == "hard": record = self.data_object.hard_record
        if lvl == "speed": record = self.data_object.speed_record
        if self.score > record:
            record = self.score
            if lvl == "easy": self.data_object.easy_record = record
            if lvl == "medium": self.data_object.medium_record = record
            if lvl == "hard": self.data_object.hard_record = record
            if lvl == "speed": self.data_object.speed_record = record
        current_record_string = f"Rekord: {record}"
        current_record_text = GAME_BAR_FONT.render(current_record_string, True, BLACK)
        current_record_text_position = current_record_text.get_rect(center = (404, 18))

        pygame.draw.rect(screen, WHITE, current_record_border)
        pygame.draw.rect(screen, GRASS_COLOR, current_record_rect)
        screen.blit(current_record_text, current_record_text_position)

        # checks for record in easy and medium, then unlocks lvls
        if lvl == "easy" and self.data_object.medium_diff == 0 and record >= 50:
            self.data_object.medium_diff = 1
        if lvl == "medium" and self.data_object.hard_diff == 0 and record >= 50:
            self.data_object.hard_diff = 1

    def draw_current_score(self):
        current_score_border = pygame.Rect(510, 4, 113, 32)
        current_score_rect = pygame.Rect(511, 5, 111, 30)

        self.score = len(self.snake.body) - 3
        current_score_string = f"Wynik: {self.score}"
        current_score_text = GAME_BAR_FONT.render(current_score_string, True, BLACK)
        current_score_text_position = current_score_text.get_rect(center = (565, 18))

        pygame.draw.rect(screen, WHITE, current_score_border)
        pygame.draw.rect(screen, GRASS_COLOR, current_score_rect)
        screen.blit(current_score_text, current_score_text_position)

    def draw_coins_amount(self):
        coins_amount_border = pygame.Rect(675, 4, 104, 32)
        coins_amount_rect = pygame.Rect(676, 5, 102, 30)

        coins_amount_string = f"$ {self.data_object.coins}"
        coins_amount_text = GAME_BAR_FONT.render(coins_amount_string, True, BLACK)
        coins_amount_text_position = coins_amount_text.get_rect(center = (727, 19))

        pygame.draw.rect(screen, WHITE, coins_amount_border)
        pygame.draw.rect(screen, GRASS_COLOR, coins_amount_rect)
        screen.blit(coins_amount_text, coins_amount_text_position)

    def draw_board(self):
        if "clear" in self.data_object.board_skin:
            if "white-clear" in self.data_object.board_skin: color = WHITE_CLEAR
            elif "orange-clear" in self.data_object.board_skin: color = ORANGE_CLEAR
            elif "mint-clear" in self.data_object.board_skin: color = MINT_CLEAR
            elif "black-clear" in self.data_object.board_skin: color = BLACK_CLEAR
            screen.fill(color)

        else:
            if "blckbrnz-squared" in self.data_object.board_skin:
                color1 = BLCKBRNZ_SQUARED_1
                color2 = BLCKBRNZ_SQUARED_2
            elif "blck-wht" in self.data_object.board_skin:
                color1 = BLCK_WHT_1
                color2 = BLCK_WHT_2
            elif "green-squared" in self.data_object.board_skin:
                color1 = GREEN_SQUARED_1
                color2 = GREEN_SQUARED_2
            elif "mintprp-squared" in self.data_object.board_skin:
                color1 = MINTPRP_SQUARED_1
                color2 = MINTPRP_SQUARED_2
            elif "mint-squared" in self.data_object.board_skin:
                color1 = MINT_SQUARED_1
                color2 = MINT_SQUARED_2
            elif "orange-squared" in self.data_object.board_skin:
                color1 = ORANGE_SQUARED_1
                color2 = ORANGE_SQUARED_2
            elif "pink-squared" in self.data_object.board_skin:
                color1 = PINK_SQUARED_1
                color2 = PINK_SQUARED_2
            elif "prple-squared" in self.data_object.board_skin:
                color1 = PRPLE_SQUARED_1
                color2 = PRPLE_SQUARED_2
            elif "redblu-squared" in self.data_object.board_skin:
                color1 = REDBLU_SQUARED_1
                color2 = REDBLU_SQUARED_2
            elif "redwht-squared" in self.data_object.board_skin:
                color1 = REDWHT_SQUARED_1
                color2 = REDWHT_SQUARED_2
            elif "yellow-squared" in self.data_object.board_skin:
                color1 = YELLOW_SQUARED_1
                color2 = YELLOW_SQUARED_2
            elif "default" in self.data_object.board_skin:
                color1 = DEFAULT_1
                color2 = DEFAULT_2

            screen.fill(color2)
            for row in range(CELL_NUMBER+1):
                if row % 2 == 0:
                    for column in range(CELL_NUMBER):
                        if column % 2 == 0:
                            cell_rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                            pygame.draw.rect(screen, color1, cell_rect)
                if row % 2 == 1:
                    for column in range(CELL_NUMBER):
                        if column % 2 == 1:
                            cell_rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                            pygame.draw.rect(screen, color1, cell_rect)

