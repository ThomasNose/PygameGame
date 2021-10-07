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
                 (3/2*WIDTH / 4, 400 , 400, 25),
                 (WIDTH/3, 620, 200, 25),
                 (WIDTH/2 + 20,620,200,25)]
FLOOR_LIST = [(0,HEIGHT - 40, 2*WIDTH, 40)]

#colours
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)
BLUE=(0,150,255)
RED=(255,0,0)
