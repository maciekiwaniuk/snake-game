import pygame
from pygame.math import Vector2
from constants import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

pygame.init()

pygame.font.init()


class UpgradesMenu:
    def __init__(self, data_object):
        self.data_object = data_object

        self.return_button_rect = pygame.Rect(33, 33, 98, 74)

        self.select_fruit_but1 = pygame.Rect(103, 250, 80, 80)
        self.select_fruit_but2 = pygame.Rect(186, 250, 80, 80)
        self.select_fruit_but3 = pygame.Rect(269, 250, 80, 80)
        self.buy_fruit_but = pygame.Rect(145, 395, 160, 50)

        self.buy_lvl_but = pygame.Rect(478, 395, 192, 50)

        self.coins_upgrade_lvl = pygame.Rect(180, 534, 90, 90)
        self.buy_coins_but = pygame.Rect(145, 685, 160, 50)

        self.points_upgrade_lvl = pygame.Rect(527, 534, 90, 90)
        self.buy_points_but = pygame.Rect(494, 685, 160, 50)

    def draw_upgrades(self, curr_mouse_x, curr_mouse_y):
        self.draw_title_and_background()
        self.draw_upgrade_titles()
        self.draw_coins_bar()
        self.draw_fruit_upgrades(curr_mouse_x, curr_mouse_y)
        self.draw_coins_upgrades(curr_mouse_x, curr_mouse_y)
        self.draw_points_upgrades(curr_mouse_x, curr_mouse_y)
        self.draw_lvl_upgrades(curr_mouse_x, curr_mouse_y)

        if self.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_return_button(hover=True)
        else:
            self.draw_return_button(hover=False)

        # cursor
        screen.blit(cursor_image, (curr_mouse_x, curr_mouse_y))

    def draw_return_button(self, hover):
        if hover == True: color = GREEN
        if hover == False: color = GRASS_COLOR
        return_button_border = pygame.Rect(30, 30, 104, 80)
        return_arrow_position = return_arrow.get_rect(center = (83, 72))

        pygame.draw.rect(screen, BLACK, return_button_border)
        pygame.draw.rect(screen, color, self.return_button_rect)
        screen.blit(return_arrow, return_arrow_position)

    def draw_coins_bar(self):
        coins_bar_rect_border = pygame.Rect(665, 28, 104, 42)
        pygame.draw.rect(screen, BLACK, coins_bar_rect_border)

        coins_bar_rect = pygame.Rect(667, 30, 100, 38)
        pygame.draw.rect(screen, ORANGE, coins_bar_rect)

        coins_amount_text = f"$ {str(self.data_object.coins)}"
        coins_amount = COINS_MENU_FONT.render(coins_amount_text, True, BLACK)
        coins_amount_position = coins_amount.get_rect(center = (716, 49))
        screen.blit(coins_amount, coins_amount_position)

    def draw_fruit_upgrades(self, curr_mouse_x, curr_mouse_y):
        select_fruit1_color = GREEN_DARK
        select_fruit2_color = RED_DARK
        select_fruit3_color = RED_DARK

        if self.data_object.fruits_upgrade_lvl > 0:
            select_fruit2_color = GREEN_DARK
        if self.data_object.fruits_upgrade_lvl > 1:
            select_fruit3_color = GREEN_DARK

        if self.data_object.selected_fruits_upgrade_lvl == 0 or self.select_fruit_but1.collidepoint(curr_mouse_x, curr_mouse_y):
            select_fruit1_color = GREEN
        if (self.data_object.fruits_upgrade_lvl > 0 and
            (self.data_object.selected_fruits_upgrade_lvl == 1 or self.select_fruit_but2.collidepoint(curr_mouse_x, curr_mouse_y))):
            select_fruit2_color = GREEN
        if (self.data_object.fruits_upgrade_lvl > 1 and
            (self.data_object.selected_fruits_upgrade_lvl == 2 or self.select_fruit_but3.collidepoint(curr_mouse_x, curr_mouse_y))):
            select_fruit3_color = GREEN

        select_fruit1_border_color = BLACK
        select_fruit2_border_color = BLACK
        select_fruit3_border_color = BLACK

        select_fruit_but1_border = pygame.Rect(100, 247, 86, 86)
        select_fruit_but2_border = pygame.Rect(183, 247, 86, 86)
        select_fruit_but3_border = pygame.Rect(266, 247, 86, 86)

        pygame.draw.rect(screen, select_fruit1_border_color, select_fruit_but1_border)
        pygame.draw.rect(screen, select_fruit2_border_color, select_fruit_but2_border)
        pygame.draw.rect(screen, select_fruit3_border_color, select_fruit_but3_border)

        if self.data_object.selected_fruits_upgrade_lvl == 0:
            select_fruit1_border_color = GREY
            pygame.draw.rect(screen, select_fruit1_border_color, select_fruit_but1_border)
        elif self.data_object.selected_fruits_upgrade_lvl == 1:
            select_fruit2_border_color = GREY
            pygame.draw.rect(screen, select_fruit2_border_color, select_fruit_but2_border)
        elif self.data_object.selected_fruits_upgrade_lvl == 2:
            select_fruit3_border_color = GREY
            pygame.draw.rect(screen, select_fruit3_border_color, select_fruit_but3_border)

        pygame.draw.rect(screen, select_fruit1_color, self.select_fruit_but1)
        pygame.draw.rect(screen, select_fruit2_color, self.select_fruit_but2)
        pygame.draw.rect(screen, select_fruit3_color, self.select_fruit_but3)

        text_1 = UPGRADES_BUTTON_FONT.render("1", True, BLACK)
        text_2 = UPGRADES_BUTTON_FONT.render("2", True, BLACK)
        text_3 = UPGRADES_BUTTON_FONT.render("3", True, BLACK)

        text_1_position = (130, 265)
        text_2_position = (215, 265)
        text_3_position = (298, 265)

        screen.blit(text_1, text_1_position)
        screen.blit(text_2, text_2_position)
        screen.blit(text_3, text_3_position)

        # price mechanism
        if self.data_object.fruits_upgrade_lvl == 0:
            price = 500
            price_string = f"{price}$"
        elif self.data_object.fruits_upgrade_lvl == 1:
            price = 5000
            price_string = f"{price}$"
        elif self.data_object.fruits_upgrade_lvl == 2:
            price = 0
            price_string = ""
        # end price mechanism

        price_text = UPGRADES_PRICE_FONT.render(price_string, True, BLACK)
        price_text_position = price_text.get_rect(center = (225, 362))
        screen.blit(price_text, price_text_position)


        # buy button
        buy_fruit_but_color = RED_DARK

        if self.data_object.coins >= price:
            buy_fruit_but_color = GREEN_DARK
            if self.buy_fruit_but.collidepoint(curr_mouse_x, curr_mouse_y):
                buy_fruit_but_color = GREEN
        if self.data_object.fruits_upgrade_lvl == 2: buy_fruit_but_color = ORANGE_DARK

        buy_fruit_but_border_color = BLACK
        buy_fruit_but_border = pygame.Rect(142, 392, 166, 56)

        pygame.draw.rect(screen, buy_fruit_but_border_color, buy_fruit_but_border)
        pygame.draw.rect(screen, buy_fruit_but_color, self.buy_fruit_but)

        buy_fruit_string = "Ulepsz"
        if self.data_object.coins >= price: buy_fruit_string = "Ulepsz"
        if self.data_object.fruits_upgrade_lvl == 2: buy_fruit_string = "MAX"

        buy_fruit_text = UPGRADES_BUY_FONT.render(buy_fruit_string, True, BLACK)
        buy_fruit_text_position = buy_fruit_text.get_rect(center=(224, 419))
        screen.blit(buy_fruit_text, buy_fruit_text_position)

    def buy_fruit_upgrade(self):
        if self.data_object.fruits_upgrade_lvl == 0: price = 500
        elif self.data_object.fruits_upgrade_lvl == 1: price = 5000
        else: price = 0

        # upgrade isnt maxed
        if self.data_object.fruits_upgrade_lvl != 2:
            # if user has enough money for upgrade
            if self.data_object.coins >= price:
                self.play_upgrade_sound()
                self.data_object.coins -= price
                self.data_object.fruits_upgrade_lvl += 1
                self.data_object.selected_fruits_upgrade_lvl = self.data_object.fruits_upgrade_lvl

    def select_fruit_upgrade(self, select):
        if select == 0:
            if self.data_object.selected_fruits_upgrade_lvl != 0:
                self.play_click_sound()
                self.data_object.selected_fruits_upgrade_lvl = 0
        elif select == 1:
            if self.data_object.selected_fruits_upgrade_lvl != 1:
                if self.data_object.fruits_upgrade_lvl > 0:
                    self.play_click_sound()
                    self.data_object.selected_fruits_upgrade_lvl = 1
        elif select == 2:
            if self.data_object.selected_fruits_upgrade_lvl != 2:
                if self.data_object.fruits_upgrade_lvl > 1:
                    self.play_click_sound()
                    self.data_object.selected_fruits_upgrade_lvl = 2

    def draw_coins_upgrades(self, curr_mouse_x, curr_mouse_y):
        # upgrade lvl
        coins_upgrade_lvl_color = GREEN_DARK

        coins_upgrade_lvl_border_color = BLACK

        coins_upgrade_lvl_border = pygame.Rect(177, 531, 96, 96)

        pygame.draw.rect(screen, coins_upgrade_lvl_border_color, coins_upgrade_lvl_border)

        pygame.draw.rect(screen, coins_upgrade_lvl_color, self.coins_upgrade_lvl)

        if self.data_object.coins_upgrade_lvl == 0: text_upgrade_lvl_string = "+0$"
        elif self.data_object.coins_upgrade_lvl == 1: text_upgrade_lvl_string = "+1$"
        elif self.data_object.coins_upgrade_lvl == 2: text_upgrade_lvl_string = "+2$"
        elif self.data_object.coins_upgrade_lvl == 3: text_upgrade_lvl_string = "+3$"

        text_upgrade_lvl_text = UPGRADES_BUTTON_FONT.render(text_upgrade_lvl_string, True, BLACK)

        text_upgrade_lvl_position = text_upgrade_lvl_text.get_rect(center = (224, 579))

        screen.blit(text_upgrade_lvl_text, text_upgrade_lvl_position)

        # price
        if self.data_object.coins_upgrade_lvl == 0:
            price_coins_upgrade_string = "500$"
            price = 500
            buy_coins_string = "Ulepsz"
            color_buy_coins = GREEN_DARK
        elif self.data_object.coins_upgrade_lvl == 1:
            price_coins_upgrade_string = "2500$"
            price = 2500
            buy_coins_string = "Ulepsz"
            color_buy_coins = GREEN_DARK
        elif self.data_object.coins_upgrade_lvl == 2:
            price_coins_upgrade_string = "5000$"
            price = 5000
            buy_coins_string = "Ulepsz"
            color_buy_coins = GREEN_DARK
        elif self.data_object.coins_upgrade_lvl == 3:
            price_coins_upgrade_string = ""
            price = 0
            buy_coins_string = "MAX"
            color_buy_coins = ORANGE_DARK

        if self.data_object.coins_upgrade_lvl != 3:
            if self.data_object.coins >= price:
                if self.buy_coins_but.collidepoint(curr_mouse_x, curr_mouse_y):
                    color_buy_coins = GREEN
            if self.data_object.coins < price:
                color_buy_coins = RED_DARK

        price_coins_upgrade_text = UPGRADES_PRICE_FONT.render(price_coins_upgrade_string, True, BLACK)

        price_coins_upgrade_text_position = price_coins_upgrade_text.get_rect(center=(226, 656))

        screen.blit(price_coins_upgrade_text, price_coins_upgrade_text_position)

        # upgrade button
        buy_coins_border_but = pygame.Rect(142, 682, 166, 56)
        pygame.draw.rect(screen, BLACK, buy_coins_border_but)
        pygame.draw.rect(screen, color_buy_coins, self.buy_coins_but)

        buy_coins_text = UPGRADES_BUY_FONT.render(buy_coins_string, True, BLACK)
        buy_coins_text_position = buy_coins_text.get_rect(center=(224, 709))

        screen.blit(buy_coins_text, buy_coins_text_position)

    def buy_coins_upgrade(self):
        if self.data_object.coins_upgrade_lvl != 3:
            if self.data_object.coins_upgrade_lvl == 0: price = 500
            elif self.data_object.coins_upgrade_lvl == 1: price = 2500
            elif self.data_object.coins_upgrade_lvl == 2: price = 5000

            if self.data_object.coins >= price:
                self.play_upgrade_sound()
                self.data_object.coins -= price
                self.data_object.coins_upgrade_lvl += 1

    def draw_points_upgrades(self, curr_mouse_x, curr_mouse_y):
        # upgrade lvl
        points_upgrade_lvl_color = GREEN_DARK

        points_upgrade_lvl_border_color = BLACK

        points_upgrade_lvl_border = pygame.Rect(524, 531, 96, 96)

        pygame.draw.rect(screen, points_upgrade_lvl_border_color, points_upgrade_lvl_border)

        pygame.draw.rect(screen, points_upgrade_lvl_color, self.points_upgrade_lvl)

        if self.data_object.points_upgrade_lvl == 0:
            text_upgrade_lvl_string = "+0"
        elif self.data_object.points_upgrade_lvl == 1:
            text_upgrade_lvl_string = "+10"
        elif self.data_object.points_upgrade_lvl == 2:
            text_upgrade_lvl_string = "+20"
        elif self.data_object.points_upgrade_lvl == 3:
            text_upgrade_lvl_string = "+30"

        text_upgrade_lvl_text = UPGRADES_BUTTON_FONT.render(text_upgrade_lvl_string, True, BLACK)

        text_upgrade_lvl_position = text_upgrade_lvl_text.get_rect(center=(571, 579))

        screen.blit(text_upgrade_lvl_text, text_upgrade_lvl_position)

        # price
        if self.data_object.points_upgrade_lvl == 0:
            price_points_upgrade_string = "500$"
            price = 500
            buy_points_string = "Ulepsz"
            color_buy_points = GREEN_DARK
        elif self.data_object.points_upgrade_lvl == 1:
            price_points_upgrade_string = "2500$"
            price = 2500
            buy_points_string = "Ulepsz"
            color_buy_points = GREEN_DARK
        elif self.data_object.points_upgrade_lvl == 2:
            price_points_upgrade_string = "5000$"
            price = 5000
            buy_points_string = "Ulepsz"
            color_buy_points = GREEN_DARK
        elif self.data_object.points_upgrade_lvl == 3:
            price_points_upgrade_string = ""
            price = 0
            buy_points_string = "MAX"
            color_buy_points = ORANGE_DARK

        if self.data_object.points_upgrade_lvl != 3:
            if self.data_object.coins >= price:
                if self.buy_points_but.collidepoint(curr_mouse_x, curr_mouse_y):
                    color_buy_points = GREEN
            if self.data_object.coins < price:
                color_buy_points = RED_DARK

        price_points_upgrade_text = UPGRADES_PRICE_FONT.render(price_points_upgrade_string, True, BLACK)

        price_points_upgrade_text_position = price_points_upgrade_text.get_rect(center=(573, 656))

        screen.blit(price_points_upgrade_text, price_points_upgrade_text_position)

        # upgrade button
        buy_points_border_but = pygame.Rect(491, 682, 166, 56)
        pygame.draw.rect(screen, BLACK, buy_points_border_but)
        pygame.draw.rect(screen, color_buy_points, self.buy_points_but)

        buy_points_text = UPGRADES_BUY_FONT.render(buy_points_string, True, BLACK)
        buy_points_text_position = buy_points_text.get_rect(center=(573, 709))

        screen.blit(buy_points_text, buy_points_text_position)

    def buy_points_upgrade(self):
        if self.data_object.points_upgrade_lvl != 3:
            if self.data_object.points_upgrade_lvl == 0:
                price = 500
            elif self.data_object.points_upgrade_lvl == 1:
                price = 2500
            elif self.data_object.points_upgrade_lvl == 2:
                price = 5000

            if self.data_object.coins >= price:
                self.play_upgrade_sound()
                self.data_object.coins -= price
                self.data_object.points_upgrade_lvl += 1

    def draw_lvl_upgrades(self, curr_mouse_x, curr_mouse_y):
        # green rect title
        title_rect = pygame.Rect(498, 272, 147, 57)
        border_title_rect = pygame.Rect(495, 269, 153, 63)
        pygame.draw.rect(screen, BLACK, border_title_rect)
        pygame.draw.rect(screen, GREEN_DARK, title_rect)

        # title
        speed_string = "Speed"
        speed_text = UPGRADES_NAME_FONT.render(speed_string, True, BLACK)
        speed_text_position = (511, 270)
        screen.blit(speed_text, speed_text_position)

        # price
        if self.data_object.speed_diff == False:
            price = 1000
            speed_price_string = "1000$"
            speed_price_text = UPGRADES_PRICE_FONT.render(speed_price_string, True, BLACK)
            speed_price_text_position = speed_price_text.get_rect(center=(571, 362))
            screen.blit(speed_price_text, speed_price_text_position)

        # button
        if self.data_object.speed_diff == False:
            border_buy_lvl_but = pygame.Rect(475, 392, 198, 56)
            # (478, 395, 192, 50)
            buy_lvl_but_color = RED_DARK
            buy_lvl_string = "Odblokuj"
            if self.data_object.coins >= price:
                buy_lvl_but_color = GREEN_DARK
                if self.buy_lvl_but.collidepoint(curr_mouse_x, curr_mouse_y):
                    buy_lvl_but_color = GREEN

        if self.data_object.speed_diff == True:
            buy_lvl_but_color = ORANGE_DARK
            self.buy_lvl_but = pygame.Rect(444, 395, 260, 50)
            border_buy_lvl_but = pygame.Rect(441, 392, 266, 56)

            buy_lvl_string = "Odblokowany"

        # (444, 395, 260, 50)

        buy_lvl_text = UPGRADES_BUTTON_FONT.render(buy_lvl_string, True, BLACK)
        buy_lvl_text_position = buy_lvl_text.get_rect(center = (573, 419))

        pygame.draw.rect(screen, BLACK, border_buy_lvl_but)
        pygame.draw.rect(screen, buy_lvl_but_color, self.buy_lvl_but)
        screen.blit(buy_lvl_text, buy_lvl_text_position)

    def buy_lvl_upgrades(self):
        if self.data_object.speed_diff == 0:
            price = 1000
            if self.data_object.coins >= price:
                self.play_upgrade_sound()
                self.data_object.coins -= price
                self.data_object.speed_diff = 1

    @staticmethod
    def draw_upgrade_titles():
        coins_string = "Ilość owoców na planszy"
        lvls_string = "Tryb gry"
        coins_bonus_string = "Dodatkowe monety"
        points_bonus_string = "Dodatkowe punkty"

        coins_text = UPGRADES_TITLE_FONT.render(coins_string, True, BLACK)
        lvls_text = UPGRADES_TITLE_FONT.render(lvls_string, True, BLACK)
        coins_bonus_text = UPGRADES_TITLE_FONT.render(coins_bonus_string, True, BLACK)
        points_bonus_text = UPGRADES_TITLE_FONT.render(points_bonus_string, True, BLACK)

        coins_text_position = (64, 189)
        lvls_text_position = (519, 189)
        coins_bonus_position = (95, 479)
        points_bonus_position = (446, 479)

        screen.blit(coins_text, coins_text_position)
        screen.blit(lvls_text, lvls_text_position)
        screen.blit(coins_bonus_text, coins_bonus_position)
        screen.blit(points_bonus_text, points_bonus_position)

    @staticmethod
    def draw_title_and_background():
        # screen.fill(MENU_COLOR)

        background_image = pygame.image.load(os.path.join("assets", "images", "background.png")).convert_alpha()
        screen.blit(background_image, (0, 0))

        main_title_text = "Ulepszenia"
        main_title = TITLE_FONT.render(main_title_text, True, BLACK)
        main_title_position = main_title.get_rect(center=(WIDTH / 2, 85))
        screen.blit(main_title, main_title_position)

        window_rect_border = pygame.Rect(50, 180, 700, 580)
        window_rect = pygame.Rect(55, 185, 690, 570)

        pygame.draw.rect(screen, BLACK, window_rect_border)
        pygame.draw.rect(screen, GRASS_COLOR, window_rect)

        vertical_line_rect = pygame.Rect(397, 180, 6, 580)
        horizontal_line_rect = pygame.Rect(53, 467, 695, 6)

        pygame.draw.rect(screen, BLACK, vertical_line_rect)
        pygame.draw.rect(screen, BLACK, horizontal_line_rect)

    def play_upgrade_sound(self):
        if self.data_object.effects == True:
            upgrade_sound.set_volume(self.data_object.volume)
            upgrade_sound.play()

    def play_click_sound(self):
        if self.data_object.effects == True:
            click_sound.set_volume(self.data_object.volume)
            click_sound.play()