import pygame as pg
#game options
TITLE="Late to lecture"
WIDTH=1024
HEIGHT=720
FPS=60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET= "spritesheet_jumper1.png"
Test_char= "Test_char1.png"

#player properties
PLAYER_ACC=0.5
PLAYER_FRICTION=-0.12
PLAYER_GRAVITY=0.5
PLAYER_JUMP=15
PLAYER_LIVES=3

#starting platforms
PLATFORM_LIST = [(0,HEIGHT - 40, 2*WIDTH, 40),
                 (120,HEIGHT - 40, 2*WIDTH, 40),
                 (240,HEIGHT - 40, 2*WIDTH, 40),
                 (360,HEIGHT - 40, 2*WIDTH, 40),
                 (480,HEIGHT - 40, 2*WIDTH, 40),
                 (600,HEIGHT - 40, 2*WIDTH, 40),
                 (720,HEIGHT - 40, 2*WIDTH, 40),
                 (840,HEIGHT - 40, 2*WIDTH, 40),
                 (120,HEIGHT - 240, 2*WIDTH, 40),
                 (300,HEIGHT - 240, 2*WIDTH, 40),
                 (480,HEIGHT - 240, 2*WIDTH, 40),
                 (660,HEIGHT - 240, 2*WIDTH, 40),
                 (840,HEIGHT - 240, 2*WIDTH, 40),
                 (1020,HEIGHT - 240, 2*WIDTH, 40),
                 (1200,HEIGHT - 240, 2*WIDTH, 40),
                 (1380,HEIGHT - 240, 2*WIDTH, 40),
                 (1560,HEIGHT - 240, 2*WIDTH, 40),
                 (1740,HEIGHT - 240, 2*WIDTH, 40),
                 (1920,HEIGHT - 240, 2*WIDTH, 40),
                 (2100,HEIGHT - 240, 2*WIDTH, 40),
                 (2280,HEIGHT - 240, 2*WIDTH, 40),
                 (2460,HEIGHT - 240, 2*WIDTH, 40),
                 (2640,HEIGHT - 240, 2*WIDTH, 40),
                 (2820,HEIGHT - 240, 2*WIDTH, 40),
                 (3000,HEIGHT - 240, 2*WIDTH, 40)]

FLOOR_LIST = [(0,HEIGHT - 40, 2*WIDTH, 40)]

#colours
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)
BLUE=(0,150,255)
RED=(255,0,0)
