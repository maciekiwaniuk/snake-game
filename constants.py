import pygame
import os

# initialize sounds
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()


# initialize all imported pygame modules
pygame.init()

# initialize fonts
pygame.font.init()

# region Colors
BLACK = (0, 0, 0)
BROWN = (240, 140, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_DARK = (177, 7, 7)
GREEN = (81, 229, 29)
YELLOW = (180, 180, 47)
GREEN_DARK = (10, 165, 15)
GREY = (112, 128, 144)
GREY_LIGHT = (178, 169, 174)
BLUE = (0, 0, 200)
LIGHT_BLUE = (173, 216, 230)
ORANGE = (255, 127, 39)
ORANGE_DARK = (199, 106, 42)
BACKGROUND = (113, 210, 69)
GRASS_COLOR = (167, 209, 61)
MENU_COLOR = (181, 230, 29)

# COLORS FOR BOARDS
MINT_CLEAR = (109, 225, 158)
ORANGE_CLEAR = (234, 188, 165)
BLACK_CLEAR = (0, 0, 0)
WHITE_CLEAR = (224, 243, 236)

BLCKBRNZ_SQUARED_1 = (0, 0, 0)
BLCKBRNZ_SQUARED_2 = (81, 68, 68)
BLCK_WHT_1 = (0, 0, 0)
BLCK_WHT_2 = (255, 255, 255)
DEFAULT_1 = (112, 210, 71)
DEFAULT_2 = (167, 209, 61)
GREEN_SQUARED_1 = (140, 255, 171)
GREEN_SQUARED_2 = (113, 231, 145)
MINTPRP_SQUARED_1 = (112, 169, 143)
MINTPRP_SQUARED_2 = (92, 55, 138)
MINT_SQUARED_1 = (84, 228, 171)
MINT_SQUARED_2 = (63, 127, 102)
ORANGE_SQUARED_1 = (234, 188, 165)
ORANGE_SQUARED_2 = (220, 179, 38)
PINK_SQUARED_1 = (174, 70, 180)
PINK_SQUARED_2 = (231, 84, 241)
PRPLE_SQUARED_1 = (85, 0, 255)
PRPLE_SQUARED_2 = (112, 69, 198)
REDBLU_SQUARED_1 = (73, 107, 210)
REDBLU_SQUARED_2 = (184, 104, 143)
REDWHT_SQUARED_1 = (193, 188, 188)
REDWHT_SQUARED_2 = (232, 135, 135)
YELLOW_SQUARED_1 = (231, 181, 50)
YELLOW_SQUARED_2 = (231, 231, 50)
# endregion

LEFT_CLICK = 1
RIGHT_CLICK = 3

# region Application parameters
CELL_SIZE = 40  # cell 40px - 40px
CELL_NUMBER = 20
INTERFACE_HEIGHT = 20  # interface for coins, pause, points - 20px
WIDTH = CELL_NUMBER * CELL_SIZE  # 800px --> 20cells x 20 cells
HEIGHT = (CELL_NUMBER * CELL_SIZE) + 40  # 800px + 40px --> 20cells x 20 cells + 1x20cells for interface
RESOLUTION = (WIDTH, HEIGHT)  # 800px - 800px
# endregion


# region Fonts
MAIN_TITLE_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Black.ttf"), 90)
MAIN_TITLE_BORDER_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Black.ttf"), 94)
DIFFICULTIES_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 35)
MENU_BUTTON_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 50)
COINS_MENU_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 25)
LOGOUT_MENU_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 16)
LOGOUT_TEXT_MENU_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 15)
LOGOUT_NICKNAME_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Bold.ttf"), 18)

GAME_BAR_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 22)

YOU_LOST_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 28)
RESTART_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 30)
TO_MENU_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 32)

OPTIONS_VOLUME_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 45)
OPTIONS_VOLUME_SIZE_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 28)
OPTIONS_MUSIC_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 45)
OPTIONS_EFFECTS_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 45)
OPTIONS_FPS_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 45)
OPTIONS_FPS_QUESTION_MARK_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 12)
OPTIONS_BUTTON_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 35)

SHOP_SELECT_BUTTONS_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 30)
SHOP_BUY_BUTTONS_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 27)
SHOP_PAGE_NUMBER_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 32)

OPTIONS_X_WINDOW_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 35)
INFO_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 15)
TITLE_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Black.ttf"), 80)

STATS_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 31)

UPGRADES_TITLE_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 30)
UPGRADES_BUTTON_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 40)
UPGRADES_PRICE_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 33)
UPGRADES_BUY_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 37)
UPGRADES_NAME_FONT = pygame.font.Font(os.path.join("assets", "fonts", "Lato", "Lato-Regular.ttf"), 45)
# endregion

# setting variable which contains window application
screen = pygame.display.set_mode(RESOLUTION)

# setting name of window application
pygame.display.set_caption("Snake")

# an object that allows us to specify game FPS in game loop
clock = pygame.time.Clock()

# region timers --> delay between updates on screen --> moving snake
EASY_DIFF_LVL_UPDATE = pygame.USEREVENT + 0
pygame.time.set_timer(EASY_DIFF_LVL_UPDATE, 140)

MEDIUM_DIFF_LVL_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(MEDIUM_DIFF_LVL_UPDATE, 105)

HARD_DIFF_LVL_UPDATE = pygame.USEREVENT + 2
pygame.time.set_timer(HARD_DIFF_LVL_UPDATE, 80)
# endregion

# game timer
GAME_TIMER_UPDATE = pygame.USEREVENT + 3
pygame.time.set_timer(GAME_TIMER_UPDATE, 1000)

# region sounds
click_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "click.mp3"))
punch_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "punch.mp3"))
slurp_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "slurp.mp3"))
buy_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "buy.mp3"))
equip_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "equip.mp3"))
menu_music_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "menu_music.mp3"))
game_music_easy_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "game_music_easy.mp3"))
game_music_medium_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "game_music_medium.mp3"))
game_music_hard_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "game_music_hard.mp3"))
game_music_speed_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "game_music_speed.mp3"))
upgrade_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "upgrade.mp3"))
# endregion

# region images
return_arrow = pygame.image.load(os.path.join("assets", "images", "return_arrow.png")).convert_alpha()
return_arrow = pygame.transform.scale(return_arrow, (100, 75))
# endregion

# cursor image
cursor_image = pygame.image.load(os.path.join("assets", "images", "cursor.png")).convert_alpha()
cursor_image = pygame.transform.scale(cursor_image, (22, 22))

