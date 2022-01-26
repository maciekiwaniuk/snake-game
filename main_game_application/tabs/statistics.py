import pygame
from pygame.math import Vector2
from constants import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

pygame.init()

pygame.font.init()


class StatisticsMenu:
    def __init__(self, data_object):
        self.data_object = data_object

        self.return_button_rect = pygame.Rect(33, 33, 98, 74)

    def draw_statistics(self, curr_mouse_x, curr_mouse_y):
        self.draw_title_and_background()
        self.draw_info_stats()
        self.draw_horizontal_lines()

        if self.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_return_button(hover=True)
        else:
            self.draw_return_button(hover=False)

        # print(f"x --> {curr_mouse_x}")
        # print(f"y --> {curr_mouse_y}\n")

    def draw_return_button(self, hover):
        if hover == True: color = GREEN
        if hover == False: color = GRASS_COLOR
        return_button_border = pygame.Rect(30, 30, 104, 80)
        return_arrow_position = return_arrow.get_rect(center = (83, 72))

        pygame.draw.rect(screen, BLACK, return_button_border)
        pygame.draw.rect(screen, color, self.return_button_rect)
        screen.blit(return_arrow, return_arrow_position)

    @staticmethod
    def draw_title_and_background():
        # screen.fill(MENU_COLOR)

        background_image = pygame.image.load(os.path.join("assets", "images", "background.png")).convert_alpha()
        screen.blit(background_image, (0, 0))

        main_title_text = "Statystyki"
        main_title = TITLE_FONT.render(main_title_text, True, BLACK)
        main_title_position = main_title.get_rect(center=(WIDTH / 2, 85))
        screen.blit(main_title, main_title_position)

        window_rect_border = pygame.Rect(50, 147, 700, 654)
        window_rect = pygame.Rect(55, 152, 690, 644)

        pygame.draw.rect(screen, BLACK, window_rect_border)
        pygame.draw.rect(screen, GRASS_COLOR, window_rect)

    def draw_info_stats(self):
        points_string = "Punkty"
        coins_string = "Monety"
        games_string = "Gry"
        time_spent_playing_string = "Czas spędzony podczas grania (minuty)"
        ate_fruits_string = "Zjedzone owoce"
        hit_snake_string = "Uderzenia w węża"
        hit_wall_string = "Uderzenia w ścianę"
        easy_record_string = "Rekord na Easy"
        medium_record_string = "Rekord na Medium"
        hard_record_string = "Rekord na Hard"
        speed_record_string = "Rekord na Speed"
        clicks_string = "Wciśnięte klawisze:"

        points_text = STATS_FONT.render(points_string, True, BLACK)
        coins_text = STATS_FONT.render(coins_string, True, BLACK)
        games_text = STATS_FONT.render(games_string, True, BLACK)
        time_spent_playing_text = STATS_FONT.render(time_spent_playing_string, True, BLACK)
        ate_fruits_text = STATS_FONT.render(ate_fruits_string, True, BLACK)
        hit_snake_text = STATS_FONT.render(hit_snake_string, True, BLACK)
        hit_wall_text = STATS_FONT.render(hit_wall_string, True, BLACK)
        easy_record_text = STATS_FONT.render(easy_record_string, True, BLACK)
        medium_record_text = STATS_FONT.render(medium_record_string, True, BLACK)
        hard_record_text = STATS_FONT.render(hard_record_string, True, BLACK)
        speed_record_text = STATS_FONT.render(speed_record_string, True, BLACK)
        clicks_text = STATS_FONT.render(clicks_string, True, BLACK)

        points_value_text = STATS_FONT.render(str(self.data_object.points), True, BLACK)
        coins_value_text = STATS_FONT.render(str(self.data_object.coins), True, BLACK)
        games_value_text = STATS_FONT.render(str(self.data_object.games_amount), True, BLACK)
        time_spent_playing_value_text = STATS_FONT.render(str(self.data_object.play_time_seconds // 60), True, BLACK)
        ate_fruits_value_text = STATS_FONT.render(str(self.data_object.ate_fruits_amount), True, BLACK)
        hit_snake_value_text = STATS_FONT.render(str(self.data_object.hit_snake), True, BLACK)
        hit_wall_value_text = STATS_FONT.render(str(self.data_object.hit_wall), True, BLACK)
        easy_record_value_text = STATS_FONT.render(str(self.data_object.easy_record), True, BLACK)
        medium_record_value_text = STATS_FONT.render(str(self.data_object.medium_record), True, BLACK)
        hard_record_value_text = STATS_FONT.render(str(self.data_object.hard_record), True, BLACK)
        speed_record_value_text = STATS_FONT.render(str(self.data_object.speed_record), True, BLACK)
        clicks_value_text = STATS_FONT.render(str(self.data_object.clicks), True, BLACK)

        points_position = (70, 155)
        coins_position = (70, 208)
        games_position = (70, 261)
        time_spent_position = (70, 314)
        ate_fruits_position = (70, 371)
        hit_snake_position = (70, 426)
        hit_wall_position = (70, 481)
        easy_record_position = (70, 534)
        medium_record_position = (70, 587)
        hard_record_position = (70, 642)
        speed_record_position = (70, 696)
        clicks_position = (70, 752)

        points_value_position = points_value_text.get_rect(topright=(730, 155))
        coins_value_position = coins_value_text.get_rect(topright=(730, 208))
        games_value_position = games_value_text.get_rect(topright=(730, 261))
        time_spent_value_position = time_spent_playing_value_text.get_rect(topright=(730, 314))
        ate_fruits_value_position = ate_fruits_value_text.get_rect(topright=(730, 371))
        hit_snake_value_position = hit_snake_value_text.get_rect(topright=(730, 426))
        hit_wall_value_position = hit_wall_value_text.get_rect(topright=(730, 481))
        easy_record_value_position = easy_record_value_text.get_rect(topright=(730, 534))
        medium_record_value_position = medium_record_value_text.get_rect(topright=(730, 587))
        hard_record_value_position = hard_record_value_text.get_rect(topright=(730, 642))
        speed_record_value_position = speed_record_value_text.get_rect(topright=(730, 696))
        clicks_value_position = clicks_value_text.get_rect(topright=(730, 752))

        screen.blit(points_text, points_position)
        screen.blit(coins_text, coins_position)
        screen.blit(games_text, games_position)
        screen.blit(time_spent_playing_text, time_spent_position)
        screen.blit(ate_fruits_text, ate_fruits_position)
        screen.blit(hit_snake_text, hit_snake_position)
        screen.blit(hit_wall_text, hit_wall_position)
        screen.blit(easy_record_text, easy_record_position)
        screen.blit(medium_record_text, medium_record_position)
        screen.blit(hard_record_text, hard_record_position)
        screen.blit(speed_record_text, speed_record_position)
        screen.blit(clicks_text, clicks_position)

        screen.blit(points_value_text, points_value_position)
        screen.blit(coins_value_text, coins_value_position)
        screen.blit(games_value_text, games_value_position)
        screen.blit(time_spent_playing_value_text, time_spent_value_position)
        screen.blit(ate_fruits_value_text, ate_fruits_value_position)
        screen.blit(hit_snake_value_text, hit_snake_value_position)
        screen.blit(hit_wall_value_text, hit_wall_value_position)
        screen.blit(easy_record_value_text, easy_record_value_position)
        screen.blit(medium_record_value_text, medium_record_value_position)
        screen.blit(hard_record_value_text, hard_record_value_position)
        screen.blit(speed_record_value_text, speed_record_value_position)
        screen.blit(clicks_value_text, clicks_value_position)

    @staticmethod
    def draw_horizontal_lines():
        line1 = pygame.Rect(55, 200, 690, 5)
        line2 = pygame.Rect(55, 252, 690, 5)
        line3 = pygame.Rect(55, 304, 690, 5)
        line4 = pygame.Rect(55, 360, 690, 5)
        line5 = pygame.Rect(55, 416, 690, 5)
        line6 = pygame.Rect(55, 472, 690, 5)
        line7 = pygame.Rect(55, 526, 690, 5)
        line8 = pygame.Rect(55, 578, 690, 5)
        line9 = pygame.Rect(55, 632, 690, 5)
        line10 = pygame.Rect(55, 687, 690, 5)
        line11 = pygame.Rect(55, 741, 690, 5)

        pygame.draw.rect(screen, BLACK, line1)
        pygame.draw.rect(screen, BLACK, line2)
        pygame.draw.rect(screen, BLACK, line3)
        pygame.draw.rect(screen, BLACK, line4)
        pygame.draw.rect(screen, BLACK, line5)
        pygame.draw.rect(screen, BLACK, line6)
        pygame.draw.rect(screen, BLACK, line7)
        pygame.draw.rect(screen, BLACK, line8)
        pygame.draw.rect(screen, BLACK, line9)
        pygame.draw.rect(screen, BLACK, line10)
        pygame.draw.rect(screen, BLACK, line11)