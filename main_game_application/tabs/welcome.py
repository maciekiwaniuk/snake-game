import pygame
from pygame.math import Vector2
from constants import *

# initialize sounds
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

pygame.init()

pygame.font.init()


class WelcomeMenu:
    def __init__(self, data_object):
        # data_object contains user_data
        self.data_object = data_object

        self.easy_button_rect = pygame.Rect(185, 123, 78, 46)
        self.medium_button_rect = pygame.Rect(275, 123, 138, 46)
        self.hard_button_rect = pygame.Rect(425, 123, 86, 46)
        self.speed_button_rect = pygame.Rect(523, 123, 101, 46)

        self.play_button_rect = pygame.Rect(350, 198, 100, 65)
        self.inventory_button_rect = pygame.Rect(278, 384, 248, 65)
        self.shop_button_rect = pygame.Rect(336, 291, 130, 65)
        self.upgrades_button_rect = pygame.Rect(274, 477, 253, 64)
        self.options_button_rect = pygame.Rect(274, 567, 253, 64)
        self.stats_button_rect = pygame.Rect(284, 655, 233, 64)
        self.exit_button_rect = pygame.Rect(309, 749, 182, 66)

        self.logout_button_rect = pygame.Rect(60, 83, 90, 24)

    @staticmethod
    def stop_menu_music():
        menu_music_sound.stop()

    def play_menu_music(self):
        if self.data_object.music == True:
            menu_music_sound.set_volume(self.data_object.volume)
            menu_music_sound.play(-1)

    def draw_welcome_menu(self, curr_mouse_x, curr_mouse_y):
        self.draw_title_and_background()

        # PLAY
        if self.play_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_play_button(hover=True)
        else:
            self.draw_play_button(hover=False)

        # SHOP
        if self.shop_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_shop_button(hover=True)
        else:
            self.draw_shop_button(hover=False)

        # INVENTORY
        if self.inventory_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_inventory_button(hover=True)
        else:
            self.draw_inventory_button(hover=False)

        # SPEED
        if self.speed_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_speed_button(self.data_object.speed_diff,
                                   self.data_object.selected_lvl,
                                   hover=True)
            if self.data_object.speed_diff == False:
                self.draw_speed_button_hover_info()
        else:
            self.draw_speed_button(self.data_object.speed_diff,
                                   self.data_object.selected_lvl,
                                   hover=False)

        # HARD
        if self.hard_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_hard_button(self.data_object.hard_diff,
                                  self.data_object.selected_lvl,
                                  hover=True)

            if self.data_object.hard_diff == False:
                self.draw_hard_button_hover_info()
        else:
            self.draw_hard_button(self.data_object.hard_diff,
                                  self.data_object.selected_lvl,
                                  hover=False)

        # MEDIUM
        if self.medium_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_medium_button(self.data_object.medium_diff,
                                    self.data_object.selected_lvl,
                                    hover=True)

            if self.data_object.medium_diff == False:
                self.draw_medium_button_hover_info()
        else:
            self.draw_medium_button(self.data_object.medium_diff,
                                    self.data_object.selected_lvl,
                                    hover=False)

        # EASY
        if self.easy_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_easy_button(self.data_object.selected_lvl, hover=True)
        else:
            self.draw_easy_button(self.data_object.selected_lvl, hover=False)

        # OPTIONS
        if self.options_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_options_button(hover=True)
        else:
            self.draw_options_button(hover=False)

        # UPGRADES
        if self.upgrades_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_upgrades_button(hover=True)
        else:
            self.draw_upgrades_button(hover=False)

        # STATS
        if self.stats_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_stats_button(hover=True)
        else:
            self.draw_stats_button(hover=False)

        # EXIT
        if self.exit_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_exit_button(hover=True)
        else:
            self.draw_exit_button(hover=False)

        # LOGOUT
        if self.logout_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_logout_button(hover=True)
        else:
            self.draw_logout_button(hover=False)

        # TEXT ABOVE LOGOUT
        self.draw_text_above_logout_button()

        # COINS BAR
        self.draw_coins_bar()

        # cursor
        screen.blit(cursor_image, (curr_mouse_x, curr_mouse_y))

    @staticmethod
    def draw_title_and_background():
        # screen.fill(MENU_COLOR)

        background_image = pygame.image.load(os.path.join("assets", "images", "background.png")).convert_alpha()
        screen.blit(background_image, (0, 0))

        main_title_text = "Snake"
        main_title = MAIN_TITLE_FONT.render(main_title_text, True, BLACK)
        main_title_position = main_title.get_rect(center=(WIDTH / 2, 60))
        screen.blit(main_title, main_title_position)
        # main_title_image = pygame.image.load(os.path.join("assets", "images", "title.jpg")).convert_alpha()
        # screen.blit(main_title_image, (265, 17))

    def draw_easy_button(self, selected, hover):
        if selected == "easy": color = WHITE
        if selected != "easy":
            if hover == False: color = GREEN
            if hover == True: color = GREEN_DARK

        easy_button_rect_border = pygame.Rect(183, 121, 82, 50)
        pygame.draw.rect(screen, BLACK, easy_button_rect_border)

        pygame.draw.rect(screen, color, self.easy_button_rect)

        easy_text = "Easy"
        easy_difficulty = DIFFICULTIES_FONT.render(easy_text, True, BLACK)
        easy_difficulty_position = (188, 121)
        screen.blit(easy_difficulty, easy_difficulty_position)

    @staticmethod
    def draw_medium_button_hover_info():
        window_info_rect = pygame.Rect(380, 216, 255, 92)
        window_info_border_rect = pygame.Rect(377, 213, 261, 98)
        pygame.draw.rect(screen, BLACK, window_info_border_rect)
        pygame.draw.rect(screen, GREY_LIGHT, window_info_rect)

        arrow_point_1 = (465, 215)
        arrow_point_2 = (425, 215)
        arrow_point_3 = (410, 175)

        pygame.draw.polygon(screen, GREY_LIGHT, (arrow_point_1, arrow_point_2, arrow_point_3))
        pygame.draw.line(screen, BLACK, arrow_point_1, arrow_point_3, 3)
        pygame.draw.line(screen, BLACK, arrow_point_2, arrow_point_3, 3)

        medium_info_1 = "Aby odblokować poziom trudności"
        medium_info_2 = "Medium (Średni) musisz zdobyć"
        medium_info_3 = "minimum 50 punktów podczas jednej"
        medium_info_4 = "rozgrywki na poziomie Easy (Łatwy)."

        medium_info_1_text = INFO_FONT.render(medium_info_1, True, BLACK)
        medium_info_2_text = INFO_FONT.render(medium_info_2, True, BLACK)
        medium_info_3_text = INFO_FONT.render(medium_info_3, True, BLACK)
        medium_info_4_text = INFO_FONT.render(medium_info_4, True, BLACK)

        medium_info_1_position = (387, 220)
        medium_info_2_position = (387, 240)
        medium_info_3_position = (387, 260)
        medium_info_4_position = (387, 280)

        screen.blit(medium_info_1_text, medium_info_1_position)
        screen.blit(medium_info_2_text, medium_info_2_position)
        screen.blit(medium_info_3_text, medium_info_3_position)
        screen.blit(medium_info_4_text, medium_info_4_position)

    def draw_medium_button(self, unlocked, selected, hover):
        if unlocked == True:
            if selected == "medium": color = WHITE
            if selected != "medium":
                if hover == False: color = GREEN
                if hover == True: color = GREEN_DARK
        if unlocked == False: color = RED_DARK

        medium_rect_border = pygame.Rect(273, 121, 142, 50)
        pygame.draw.rect(screen, BLACK, medium_rect_border)

        pygame.draw.rect(screen, color, self.medium_button_rect)

        medium_text = "Medium"
        medium_difficulty = DIFFICULTIES_FONT.render(medium_text, True, BLACK)
        medium_difficulty_position = medium_difficulty.get_rect(center=(342, 143))
        screen.blit(medium_difficulty, medium_difficulty_position)

    @staticmethod
    def draw_hard_button_hover_info():
        window_info_rect = pygame.Rect(380, 216, 275, 92)
        window_info_border_rect = pygame.Rect(377, 213, 281, 98)
        pygame.draw.rect(screen, BLACK, window_info_border_rect)
        pygame.draw.rect(screen, GREY_LIGHT, window_info_rect)

        arrow_point_1 = (445, 215)
        arrow_point_2 = (485, 215)
        arrow_point_3 = (490, 175)

        pygame.draw.polygon(screen, GREY_LIGHT, (arrow_point_1, arrow_point_2, arrow_point_3))
        pygame.draw.line(screen, BLACK, arrow_point_1, arrow_point_3, 3)
        pygame.draw.line(screen, BLACK, arrow_point_2, arrow_point_3, 3)

        hard_info_1 = "Aby odblokować poziom trudności"
        hard_info_2 = "Hard (Trudny) musisz zdobyć"
        hard_info_3 = "minimum 50 punktów podczas jednej"
        hard_info_4 = "rozgrywki na poziomie Medium (Średni)."

        hard_info_1_text = INFO_FONT.render(hard_info_1, True, BLACK)
        hard_info_2_text = INFO_FONT.render(hard_info_2, True, BLACK)
        hard_info_3_text = INFO_FONT.render(hard_info_3, True, BLACK)
        hard_info_4_text = INFO_FONT.render(hard_info_4, True, BLACK)

        hard_info_1_position = (387, 220)
        hard_info_2_position = (387, 240)
        hard_info_3_position = (387, 260)
        hard_info_4_position = (387, 280)

        screen.blit(hard_info_1_text, hard_info_1_position)
        screen.blit(hard_info_2_text, hard_info_2_position)
        screen.blit(hard_info_3_text, hard_info_3_position)
        screen.blit(hard_info_4_text, hard_info_4_position)

    def draw_hard_button(self, unlocked, selected, hover):
        if unlocked == True:
            if selected == "hard": color = WHITE
            if selected != "hard":
                if hover == False: color = GREEN
                if hover == True: color = GREEN_DARK
        if unlocked == False: color = RED_DARK

        hard_button_rect_border = pygame.Rect(423, 121, 90, 50)
        pygame.draw.rect(screen, BLACK, hard_button_rect_border)

        pygame.draw.rect(screen, color, self.hard_button_rect)

        hard_text = "Hard"
        hard_difficulty = DIFFICULTIES_FONT.render(hard_text, True, BLACK)
        hard_difficulty_position = (428, 121)
        screen.blit(hard_difficulty, hard_difficulty_position)

    @staticmethod
    def draw_speed_button_hover_info():
        window_info_rect = pygame.Rect(380, 216, 275, 50)
        window_info_border_rect = pygame.Rect(377, 213, 281, 56)
        pygame.draw.rect(screen, BLACK, window_info_border_rect)
        pygame.draw.rect(screen, GREY_LIGHT, window_info_rect)

        arrow_point_1 = (545, 215)
        arrow_point_2 = (585, 215)
        arrow_point_3 = (590, 175)

        pygame.draw.polygon(screen, GREY_LIGHT, (arrow_point_1, arrow_point_2, arrow_point_3))
        pygame.draw.line(screen, BLACK, arrow_point_1, arrow_point_3, 3)
        pygame.draw.line(screen, BLACK, arrow_point_2, arrow_point_3, 3)

        speed_info_1 = "Aby odblokować poziom trudności"
        speed_info_2 = "Speed odwiedź zakładkę Ulepszenia."

        speed_info_1_text = INFO_FONT.render(speed_info_1, True, BLACK)
        speed_info_2_text = INFO_FONT.render(speed_info_2, True, BLACK)

        speed_info_1_position = (387, 220)
        speed_info_2_position = (387, 240)

        screen.blit(speed_info_1_text, speed_info_1_position)
        screen.blit(speed_info_2_text, speed_info_2_position)

    def draw_speed_button(self, unlocked, selected, hover):
        if unlocked == True:
            if selected == "speed": color = WHITE
            if selected != "speed":
                if hover == False: color = GREEN
                if hover == True: color = GREEN_DARK
        if unlocked == False: color = RED_DARK

        speed_button_rect_border = pygame.Rect(521, 121, 105, 50)
        pygame.draw.rect(screen, BLACK, speed_button_rect_border)

        pygame.draw.rect(screen, color, self.speed_button_rect)

        speed_text = "Speed"
        speed_difficulty = DIFFICULTIES_FONT.render(speed_text, True, BLACK)
        speed_difficulty_position = (527, 121)
        screen.blit(speed_difficulty, speed_difficulty_position)

    def draw_play_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK

        play_button_rect_border = pygame.Rect(348, 196, 104, 69)
        pygame.draw.rect(screen, BLACK, play_button_rect_border)

        pygame.draw.rect(screen, color, self.play_button_rect)

        play_text = "Graj"
        play_button = MENU_BUTTON_FONT.render(play_text, True, BLACK)
        play_button_position = play_button.get_rect(center=(WIDTH / 2, 226))
        screen.blit(play_button, play_button_position)

    def draw_shop_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK

        shop_button_rect_border = pygame.Rect(334, 289, 134, 69)
        pygame.draw.rect(screen, BLACK, shop_button_rect_border)
        pygame.draw.rect(screen, color, self.shop_button_rect)

        shop_text = "Sklep"
        shop_button = MENU_BUTTON_FONT.render(shop_text, True, BLACK)
        shop_button_position = shop_button.get_rect(center=(WIDTH / 2, 319))
        screen.blit(shop_button, shop_button_position)

    def draw_inventory_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK
        inventory_button_rect_border = pygame.Rect(276, 382, 252, 69)
        pygame.draw.rect(screen, BLACK, inventory_button_rect_border)

        pygame.draw.rect(screen, color, self.inventory_button_rect)

        inventory_text = "Ekwipunek"
        inventory_button = MENU_BUTTON_FONT.render(inventory_text, True, BLACK)
        inventory_button_position = inventory_button.get_rect(center=(WIDTH / 2, 411))
        screen.blit(inventory_button, inventory_button_position)

    def draw_upgrades_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK

        upgrades_button_rect_border = pygame.Rect(272, 475, 257, 68)
        pygame.draw.rect(screen, BLACK, upgrades_button_rect_border)

        pygame.draw.rect(screen, color, self.upgrades_button_rect)

        upgrades_text = "Ulepszenia"
        upgrades_button = MENU_BUTTON_FONT.render(upgrades_text, True, BLACK)
        upgrades_button_position = upgrades_button.get_rect(center=(WIDTH / 2, 505))
        screen.blit(upgrades_button, upgrades_button_position)

    def draw_options_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK

        options_button_rect_border = pygame.Rect(272, 565, 257, 68)
        pygame.draw.rect(screen, BLACK, options_button_rect_border)

        pygame.draw.rect(screen, color, self.options_button_rect)

        options_text = "Ustawienia"
        options_button = MENU_BUTTON_FONT.render(options_text, True, BLACK)
        options_button_position = options_button.get_rect(center=(WIDTH / 2, 597))
        screen.blit(options_button, options_button_position)

    def draw_stats_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK

        stats_button_rect_border = pygame.Rect(282, 653, 237, 68)
        pygame.draw.rect(screen, BLACK, stats_button_rect_border)

        pygame.draw.rect(screen, color, self.stats_button_rect)

        stats_text = "Statystyki"
        stats_button = MENU_BUTTON_FONT.render(stats_text, True, BLACK)
        stats_button_position = stats_button.get_rect(center = (400, 683))
        screen.blit(stats_button, stats_button_position)

    def draw_exit_button(self, hover):
        if hover == False: color = GREEN
        if hover == True: color = GREEN_DARK

        exit_button_rect_border = pygame.Rect(307, 747, 186, 70)
        pygame.draw.rect(screen, BLACK, exit_button_rect_border)

        pygame.draw.rect(screen, color, self.exit_button_rect)

        exit_text = "Wyjście"
        exit_button = MENU_BUTTON_FONT.render(exit_text, True, BLACK)
        exit_button_position = exit_button.get_rect(center=(WIDTH / 2, 776))
        screen.blit(exit_button, exit_button_position)

    def draw_logout_button(self, hover):
        if hover == False: color = ORANGE
        if hover == True: color = ORANGE_DARK
        logout_rect_border = pygame.Rect(58, 81, 94, 28)
        pygame.draw.rect(screen, BLACK, logout_rect_border)

        pygame.draw.rect(screen, color, self.logout_button_rect)

        logout_text = "Wyloguj"
        logout_button = LOGOUT_MENU_FONT.render(logout_text, True, BLACK)
        logout_button_position = logout_button.get_rect(center=(105, 95))
        screen.blit(logout_button, logout_button_position)

    def draw_text_above_logout_button(self):
        logged_as_text = "Zalogowany jako:"
        logged_as = LOGOUT_TEXT_MENU_FONT.render(logged_as_text, True, BLACK)
        logged_text_position = logged_as.get_rect(center = (106, 40))
        screen.blit(logged_as, logged_text_position)

        nickname_text = self.data_object.name
        nickname = LOGOUT_NICKNAME_FONT.render(nickname_text, True, BLACK)
        nickname_text_position = nickname.get_rect(center=(106, 64))
        screen.blit(nickname, nickname_text_position)

    def draw_coins_bar(self):
        coins_bar_rect_border = pygame.Rect(665, 28, 104, 42)
        pygame.draw.rect(screen, BLACK, coins_bar_rect_border)

        coins_bar_rect = pygame.Rect(667, 30, 100, 38)
        pygame.draw.rect(screen, ORANGE, coins_bar_rect)

        coins_amount_text = f"$ {str(self.data_object.coins)}"
        coins_amount = COINS_MENU_FONT.render(coins_amount_text, True, BLACK)
        coins_amount_position = coins_amount.get_rect(center = (716, 49))
        screen.blit(coins_amount, coins_amount_position)