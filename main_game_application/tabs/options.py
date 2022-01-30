import pygame
from pygame.math import Vector2
from constants import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

pygame.init()

pygame.font.init()


class OptionsMenu:
    def __init__(self, data_object):
        self.data_object = data_object

        self.return_button_rect = pygame.Rect(33, 33, 98, 74)

        self.music_on_button_rect = pygame.Rect(235, 327, 100, 70)
        self.music_off_button_rect = pygame.Rect(365, 327, 100, 70)

        self.effects_on_button_rect = pygame.Rect(235, 457, 100, 70)
        self.effects_off_button_rect = pygame.Rect(365, 457, 100, 70)

        self.fps_hover_info_rect = pygame.Rect(45, 590, 100, 70)
        self.fps30_button_rect = pygame.Rect(235, 587, 100, 80)
        self.fps60_button_rect = pygame.Rect(365, 587, 100, 80)
        self.fps144_button_rect = pygame.Rect(495, 587, 100, 80)
        self.fps240_button_rect = pygame.Rect(625, 587, 100, 80)

        self.volume_slider_rect_position = (265 + (self.data_object.volume * 400), 208)
        self.volume_slider_border_position = (263 + (self.data_object.volume * 400), 206)
        self.volume_slider_drag_position = (255 + (self.data_object.volume * 400), 200)
        volume_slider_rect = (10, 50)
        volume_slider_border = (14, 54)
        volume_drag_slider = (50, 70)
        self.volume_slider_rect = pygame.Rect(self.volume_slider_rect_position, volume_slider_rect)
        self.volume_slider_border_rect = pygame.Rect(self.volume_slider_border_position, volume_slider_border)
        self.volume_slider_drag_rect = pygame.Rect(self.volume_slider_drag_position, volume_drag_slider)

    def change_slider_position(self, curr_mouse_x):
        if curr_mouse_x <= 665 and curr_mouse_x >= 265:
            self.volume_slider_rect_position = (curr_mouse_x, 208)
            self.volume_slider_border_position = (curr_mouse_x - 2, 206)
            self.volume_slider_drag_position = (curr_mouse_x - 100, 100)

            volume_slider_rect = (10, 50)
            volume_slider_border = (14, 54)
            volume_drag_slider = (300, 310)

            self.volume_slider_rect = pygame.Rect(self.volume_slider_rect_position, volume_slider_rect)
            self.volume_slider_border_rect = pygame.Rect(self.volume_slider_border_position, volume_slider_border)
            self.volume_slider_drag_rect = pygame.Rect(self.volume_slider_drag_position, volume_drag_slider)

    def check_for_changed_volume(self, curr_mouse_x):
        # 290 - 330 - 370 - 410 - 450 - 490 - 530 - 570 - 610 - 650 - 690
        if 265 <= curr_mouse_x < 305:
            self.data_object.volume = 0
            menu_music_sound.set_volume(self.data_object.volume)

        elif 305 <= curr_mouse_x < 345:
            self.data_object.volume = 0.1
            menu_music_sound.set_volume(self.data_object.volume)

        elif 345 <= curr_mouse_x < 385:
            self.data_object.volume = 0.2
            menu_music_sound.set_volume(self.data_object.volume)

        elif 385 <= curr_mouse_x < 425:
            self.data_object.volume = 0.3
            menu_music_sound.set_volume(self.data_object.volume)

        elif 425 <= curr_mouse_x < 465:
            self.data_object.volume = 0.4
            menu_music_sound.set_volume(self.data_object.volume)

        elif 465 <= curr_mouse_x < 505:
            self.data_object.volume = 0.5
            menu_music_sound.set_volume(self.data_object.volume)

        elif 505 <= curr_mouse_x < 545:
            self.data_object.volume = 0.6
            menu_music_sound.set_volume(self.data_object.volume)

        elif 545 <= curr_mouse_x < 585:
            self.data_object.volume = 0.7
            menu_music_sound.set_volume(self.data_object.volume)

        elif 585 <= curr_mouse_x < 625:
            self.data_object.volume = 0.8
            menu_music_sound.set_volume(self.data_object.volume)

        elif 625 <= curr_mouse_x < 665:
            self.data_object.volume = 0.9
            menu_music_sound.set_volume(self.data_object.volume)

        elif 665 <= curr_mouse_x:
            self.data_object.volume = 1
            menu_music_sound.set_volume(self.data_object.volume)

    def draw_volume(self, hover, mouse_down):
        if not hover and not mouse_down:
            color_rect = LIGHT_BLUE
            color_border = BLACK

        if hover and not mouse_down:
            color_rect = BLUE
            color_border = BLACK

        if hover and mouse_down:
            color_rect = BLUE
            color_border = GREY

        volume_string = "Głośność"
        volume_text_position = (55, 200)
        volume_text = OPTIONS_VOLUME_FONT.render(volume_string, True, BLACK)
        screen.blit(volume_text, volume_text_position)

        volume_long_rect = pygame.Rect(263, 223, 414, 20)
        volume_long_border = pygame.Rect(260, 220, 420, 26)
        pygame.draw.rect(screen, WHITE, volume_long_border)
        pygame.draw.rect(screen, ORANGE, volume_long_rect)
        pygame.draw.rect(screen, color_border, self.volume_slider_border_rect)
        pygame.draw.rect(screen, color_rect, self.volume_slider_rect)

        volume_size_rect = pygame.Rect(695, 210, 60, 50)
        volume_size_border = pygame.Rect(693, 208, 64, 54)
        pygame.draw.rect(screen, BLACK, volume_size_border)
        pygame.draw.rect(screen, BROWN, volume_size_rect)

        volume_size_string = str(round(self.data_object.volume * 10))
        volume_size_text = OPTIONS_VOLUME_SIZE_FONT.render(volume_size_string, True, BLACK)
        volume_size_position = volume_size_text.get_rect(center = (725, 235))
        screen.blit(volume_size_text, volume_size_position)

    def draw_options_menu(self, curr_mouse_x, curr_mouse_y):
        self.draw_title_and_background()

        # RETURN ARROW
        if self.return_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_return_button(hover=True)
        else:
            self.draw_return_button(hover=False)

        # MUSIC
        if self.music_on_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_music(hover_on=True, hover_off=False)
        elif self.music_off_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_music(hover_on=False, hover_off=True)
        else:
            self.draw_music(hover_on=False, hover_off=False)

        # EFFECTS
        if self.effects_on_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_effects(hover_on=True, hover_off=False)
        elif self.effects_off_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_effects(hover_on=False, hover_off=True)
        else:
            self.draw_effects(hover_on=False, hover_off=False)

        # FPS
        if self.fps30_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_fps(hover30=True, hover60=False, hover144=False, hover240=False)
        elif self.fps60_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_fps(hover30=False, hover60=True, hover144=False, hover240=False)
        elif self.fps144_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_fps(hover30=False, hover60=False, hover144=True, hover240=False)
        elif self.fps240_button_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_fps(hover30=False, hover60=False, hover144=False, hover240=True)
        else:
            self.draw_fps(hover30=False, hover60=False, hover144=False, hover240=False)

        # FPS HOVER INFO
        if self.fps_hover_info_rect.collidepoint(curr_mouse_x, curr_mouse_y):
            self.draw_fps_hover_info()

    @staticmethod
    def draw_title_and_background():
        # screen.fill(MENU_COLOR)

        background_image = pygame.image.load(os.path.join("assets", "images", "background.png")).convert_alpha()
        screen.blit(background_image, (0, 0))

        window_rect_border = pygame.Rect(30, 147, 740, 586)
        window_rect = pygame.Rect(35, 152, 730, 576)

        pygame.draw.rect(screen, BLACK, window_rect_border)
        pygame.draw.rect(screen, GRASS_COLOR, window_rect)

        main_title_text = "Ustawienia"
        main_title = TITLE_FONT.render(main_title_text, True, BLACK)
        main_title_position = main_title.get_rect(center=(WIDTH / 2, 85))
        screen.blit(main_title, main_title_position)

    def draw_return_button(self, hover):
        if hover == True: color = GREEN
        if hover == False: color = GRASS_COLOR
        return_button_border = pygame.Rect(30, 30, 104, 80)
        return_arrow_position = return_arrow.get_rect(center = (83, 72))

        pygame.draw.rect(screen, BLACK, return_button_border)
        pygame.draw.rect(screen, color, self.return_button_rect)
        screen.blit(return_arrow, return_arrow_position)

    def draw_music(self, hover_on, hover_off):
        if self.data_object.music == True:
            color_on = GREEN
            color_border_on = GREY
            color_off = RED_DARK
            color_border_off = BLACK

        elif self.data_object.music == False:
            color_off = RED
            color_border_off = GREY
            color_on = GREEN_DARK
            color_border_on = BLACK

        if self.data_object.music == 1 and hover_off is True:
            color_off = RED

        if self.data_object.music == 0 and hover_on is True:
            color_on = GREEN


        music_string = "Muzyka"
        music_text_position = (55, 330)
        music_text = OPTIONS_MUSIC_FONT.render(music_string, True, BLACK)
        screen.blit(music_text, music_text_position)

        on_string = "ON"
        on_text = OPTIONS_BUTTON_FONT.render(on_string, True, BLACK)
        on_text_position = on_text.get_rect(center = (285, 362))

        off_string = "OFF"
        off_text = OPTIONS_BUTTON_FONT.render(off_string, True, BLACK)
        off_text_position = off_text.get_rect(center = (415, 362))

        on_button_border = pygame.Rect(232, 324, 106, 76)
        pygame.draw.rect(screen, color_border_on, on_button_border)
        pygame.draw.rect(screen, color_on, self.music_on_button_rect)
        screen.blit(on_text, on_text_position)

        off_button_border = pygame.Rect(362, 324, 106, 76)
        pygame.draw.rect(screen, color_border_off, off_button_border)
        pygame.draw.rect(screen, color_off, self.music_off_button_rect)
        screen.blit(off_text, off_text_position)

    def draw_effects(self, hover_on, hover_off):
        if self.data_object.effects == 1:
            color_on = GREEN
            color_border_on = GREY
            color_off = RED_DARK
            color_border_off = BLACK

        elif self.data_object.effects == 0:
            color_off = RED
            color_border_off = GREY
            color_on = GREEN_DARK
            color_border_on = BLACK

        if self.data_object.effects == 1 and hover_off is True:
            color_off = RED

        if self.data_object.effects == 0 and hover_on is True:
            color_on = GREEN

        effects_string = "Efekty"
        effects_text_position = (55, 460)
        effects_text = OPTIONS_VOLUME_FONT.render(effects_string, True, BLACK)
        screen.blit(effects_text, effects_text_position)

        on_string = "ON"
        on_text = OPTIONS_BUTTON_FONT.render(on_string, True, BLACK)
        on_text_position = on_text.get_rect(center=(285, 492))

        off_string = "OFF"
        off_text = OPTIONS_BUTTON_FONT.render(off_string, True, BLACK)
        off_text_position = off_text.get_rect(center=(415, 492))

        on_button_border = pygame.Rect(232, 454, 106, 76)
        pygame.draw.rect(screen, color_border_on, on_button_border)
        pygame.draw.rect(screen, color_on, self.effects_on_button_rect)
        screen.blit(on_text, on_text_position)

        off_button_border = pygame.Rect(362, 454, 106, 76)
        pygame.draw.rect(screen, color_border_off, off_button_border)
        pygame.draw.rect(screen, color_off, self.effects_off_button_rect)
        screen.blit(off_text, off_text_position)

    @staticmethod
    def draw_fps_hover_info():
        window_info_rect = pygame.Rect(125, 416, 235, 170)
        window_info_border_rect = pygame.Rect(122, 413, 241, 176)
        pygame.draw.rect(screen, BLACK, window_info_border_rect)
        pygame.draw.rect(screen, GREY_LIGHT, window_info_rect)

        arrow_point_1 = (165, 586)
        arrow_point_2 = (235, 586)
        arrow_point_3 = (145, 610)

        pygame.draw.polygon(screen, GREY_LIGHT, (arrow_point_1, arrow_point_2, arrow_point_3))
        pygame.draw.line(screen, BLACK, arrow_point_1, arrow_point_3, 3)
        pygame.draw.line(screen, BLACK, arrow_point_2, arrow_point_3, 3)

        fps_info_1 = "FPS - Frames Per Second"
        fps_info_2 = "FPS oznacza ilość odświeżeń"
        fps_info_3 = "ekranu na sekundę. Im więcej"
        fps_info_4 = "tym rozgrywka jest płynniejsza,"
        fps_info_5 = "lecz procesor wówczas jest"
        fps_info_6 = "bardziej obciążony. Na słabszych"
        fps_info_7 = "urządzeniach zaleca się mniejsze"
        fps_info_8 = "wartości FPS."

        fps_info_1_text = INFO_FONT.render(fps_info_1, True, BLACK)
        fps_info_2_text = INFO_FONT.render(fps_info_2, True, BLACK)
        fps_info_3_text = INFO_FONT.render(fps_info_3, True, BLACK)
        fps_info_4_text = INFO_FONT.render(fps_info_4, True, BLACK)
        fps_info_5_text = INFO_FONT.render(fps_info_5, True, BLACK)
        fps_info_6_text = INFO_FONT.render(fps_info_6, True, BLACK)
        fps_info_7_text = INFO_FONT.render(fps_info_7, True, BLACK)
        fps_info_8_text = INFO_FONT.render(fps_info_8, True, BLACK)

        fps_info_1_position = (131, 420)
        fps_info_2_position = (131, 440)
        fps_info_3_position = (131, 460)
        fps_info_4_position = (131, 480)
        fps_info_5_position = (131, 500)
        fps_info_6_position = (131, 520)
        fps_info_7_position = (131, 540)
        fps_info_8_position = (131, 560)

        screen.blit(fps_info_1_text, fps_info_1_position)
        screen.blit(fps_info_2_text, fps_info_2_position)
        screen.blit(fps_info_3_text, fps_info_3_position)
        screen.blit(fps_info_4_text, fps_info_4_position)
        screen.blit(fps_info_5_text, fps_info_5_position)
        screen.blit(fps_info_6_text, fps_info_6_position)
        screen.blit(fps_info_7_text, fps_info_7_position)
        screen.blit(fps_info_8_text, fps_info_8_position)

    def draw_fps(self, hover30, hover60, hover144, hover240):
        color30_border = BLACK
        color60_border = BLACK
        color144_border = BLACK
        color240_border = BLACK

        color30 = GREEN_DARK
        color60 = GREEN_DARK
        color144 = GREEN_DARK
        color240 = GREEN_DARK

        if hover30 is True:
            color30 = GREEN
        if hover60 is True:
            color60 = GREEN
            color60_border = BLACK
        if hover144 is True:
            color144  = GREEN
            color144_border = BLACK
        if hover240 is True:
            color240 = GREEN
            color240_border = BLACK

        if self.data_object.fps == 30:
            color30 = GREEN
            color30_border = GREY
        if self.data_object.fps == 60:
            color60 = GREEN
            color60_border = GREY
        if self.data_object.fps == 144:
            color144 = GREEN
            color144_border = GREY
        if self.data_object.fps == 240:
            color240 = GREEN
            color240_border = GREY

        fps_string = "FPS"
        fps_text_position = (55, 600)
        fps_text = OPTIONS_VOLUME_FONT.render(fps_string, True, BLACK)
        screen.blit(fps_text, fps_text_position)

        fps_question_mark_string = "?"
        fps_question_mark_position = (133, 605)
        fps_question_mark_text = OPTIONS_FPS_QUESTION_MARK_FONT.render(fps_question_mark_string, True, BLACK)
        screen.blit(fps_question_mark_text, fps_question_mark_position)

        fps30_border_rect = pygame.Rect(232, 584, 106, 86)
        fps60_border_rect = pygame.Rect(362, 584, 106, 86)
        fps144_border_rect = pygame.Rect(492, 584, 106, 86)
        fps240_border_rect = pygame.Rect(622, 584, 106, 86)

        fps30_string = "30"
        fps30_text = OPTIONS_BUTTON_FONT.render(fps30_string, True, BLACK)
        fps30_position = fps30_text.get_rect(center = (285, 627))
        pygame.draw.rect(screen, color30_border, fps30_border_rect)
        pygame.draw.rect(screen, color30, self.fps30_button_rect)
        screen.blit(fps30_text, fps30_position)

        fps60_string = "60"
        fps60_text = OPTIONS_BUTTON_FONT.render(fps60_string, True, BLACK)
        fps60_position = fps60_text.get_rect(center = (415, 627))
        pygame.draw.rect(screen, color60_border, fps60_border_rect)
        pygame.draw.rect(screen, color60, self.fps60_button_rect)
        screen.blit(fps60_text ,fps60_position)

        fps144_string = "144"
        fps144_text = OPTIONS_BUTTON_FONT.render(fps144_string, True, BLACK)
        fps144_position = fps144_text.get_rect(center = (545, 627))
        pygame.draw.rect(screen, color144_border, fps144_border_rect)
        pygame.draw.rect(screen, color144, self.fps144_button_rect)
        screen.blit(fps144_text, fps144_position)

        fps240_string = "240"
        fps240_text = OPTIONS_BUTTON_FONT.render(fps240_string, True, BLACK)
        fps240_position = fps240_text.get_rect(center = (675, 627))
        pygame.draw.rect(screen, color240_border, fps240_border_rect)
        pygame.draw.rect(screen, color240, self.fps240_button_rect)
        screen.blit(fps240_text, fps240_position)

    @staticmethod
    def draw_cursor(curr_mouse_x, curr_mouse_y):
        screen.blit(cursor_image, (curr_mouse_x, curr_mouse_y))