from random import randint
# title
TITLE = "springy"
# screen dims
WIDTH = 600
HEIGHT = 960
# frames per second
FPS = 75
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
REDDISH = (240,55,66)
SKY_BLUE = (255,160,122)
FONT_NAME = 'comic sans'
SPRITESHEET = "spritesheet_jumper.png"
SPRITESHEET2 = "spritesheet.png"
# data files
HS_FILE = "highscore.txt"
# player settings
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
#how fast the player will sink downwards
PLAYER_SINK = 30
# game settings
BOOST_POWER = 50
POW_SPAWN_PCT = 7
MOB_FREQ = 500
# layers - uses numerical value in layered sprites
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# platform settings
''' old platforms from drawing rectangles'''
'''
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (65, HEIGHT - 300, WIDTH-400, 40),
                 (20, HEIGHT - 350, WIDTH-300, 40),
                 (200, HEIGHT - 150, WIDTH-350, 40),
                 (200, HEIGHT - 450, WIDTH-350, 40)]
'''
#since the screen is larger, there are more starting platforms
PLATFORM_LIST = [(0, HEIGHT-40),
                (50, HEIGHT-40),
                (100, HEIGHT-40),
                (150, HEIGHT-40),
                 (65, HEIGHT - 300),
                 (20, HEIGHT - 350),
                 (200, HEIGHT - 150),
                 (200, HEIGHT - 450),
                 (WIDTH-50, HEIGHT-100),
                 (WIDTH-100, HEIGHT-200),
                 (WIDTH-150, HEIGHT-400),
                 (WIDTH-200, HEIGHT-250),
                 (WIDTH-250, HEIGHT-300),
                 (WIDTH-300, HEIGHT-550),
                 (WIDTH-400, HEIGHT-600),
                 (WIDTH-500, HEIGHT-750),
                 (WIDTH-350, HEIGHT-800),
                 (WIDTH-300, HEIGHT-200),
                 (WIDTH-300, HEIGHT-250),
                 (WIDTH-300, HEIGHT-350)]
