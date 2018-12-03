from random import randint
TITLE = "jumpy"
#screen dims
WIDTH = 480
HEIGHT = 600
#player settings
PLAYER_ACC = 0.75
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.98
PLAYER_JUMP = 25
#starting platforms
PLATFORM_LIST = [(0, HEIGHT - 10, WIDTH, 10),
                 (80, HEIGHT - 110, 80, 10),
                 (240, HEIGHT - 200, 70, 10),
                 (160, HEIGHT - 310, 75, 10),
                 (320, HEIGHT - 390, 80, 10),
                 (80, HEIGHT - 500, 75, 10)]

#frames per second
FPS = 60
#colors
WHITE = (randint(0,255), randint(0,255), randint(0,255))
BLACK = (randint(0,255), randint(0,255), randint(0,255))
BLACK_2 = (0, 0, 0)
REDDISH = (randint(0,255), randint(0,255), randint(0,255))
#font
FONT_NAME = "arial"