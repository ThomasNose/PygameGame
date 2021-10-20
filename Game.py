# https://www.youtube.com/watch?v=Uj8MsbgpjaQ - "Potential for anything" VVVVVV Soundtrack 10/16




import pygame as pg
import numpy as np
import random
from settings import *
from sprites import *
from os import path

music = ['Medium.ogg','Dummy.ogg','CORE.ogg','Oi_Nah.mp3']


class Game:

    def __init__(self):
        # initialise game window, etc
        # Game is running
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # Loading graphics etc
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'images')
        with open(path.join(self.dir, HS_FILE), 'r+') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # Load sounds
        self.sound_dir = path.join(self.dir, 'sound')
        self.jump_sound = pg.mixer.Sound(path.join(self.sound_dir, 'Jumping_1'))
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites=pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player=Player(self)
        self.all_sprites.add(self.player)

        # Adding in platforms
        for plat in PLATFORM_LIST:
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        # Initial music setup
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.load(path.join(self.sound_dir, np.random.choice(music)))
        self.run()
    
    def run(self):
        # Game Loop
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

            
    
    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                # Falling off platform if foot not touching
                if self.player.pos.x <= lowest.rect.right + 100 and \
                   self.player.pos.x >= lowest.rect.left - 100:
                    if self.player.pos.y < hits[0].rect.bottom:
                        self.player.pos.y=lowest.rect.top+1
                        self.player.vel.y=0
                        self.player.jumping=False




        # Random music
        if pg.mixer.music.get_busy() == False:
            pg.mixer.music.load(path.join(self.sound_dir, np.random.choice(music)))
            pg.mixer.music.play(loops=1)

        
        # Check player location (scrolling)
        if self.player.rect.right >= 4 * WIDTH / 7:
            self.player.pos.x -= max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.right -= max(abs(self.player.vel.x),2)
                self.score +=1
        # Going left (comment out to only scroll right)
        #if self.player.rect.left <= WIDTH / 3:
        #    self.player.pos.x += max(abs(self.player.vel.x),2)
        #    for plat in self.platforms:
        #        plat.rect.left += max(abs(self.player.vel.x),2)

        # Stop going left (uncomment to place "invisible wall")
        if self.player.rect.left <= WIDTH/20:
            self.player.pos.x += max(abs(self.player.vel.x),2)
        
        # Dying (by falling)
        if self.player.rect.bottom > HEIGHT:
            self.playing = False
        # Scoring condition
                

    def events(self):
        # Game loops - events
        for event in pg.event.get():
            #Check for closing window
            if event.type==pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and self.player.vel.y == 0:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.jump_cut()

                                       

    def draw(self):
        #game loop - draw
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 22, WHITE, WIDTH/2, 100)
        pg.display.flip()
        
    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BLUE)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Arrow keys to move", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press any key to play", 16, WHITE, WIDTH/2, HEIGHT/2 + 50)
        self.draw_text("High-score: " + str(self.highscore), 22, WHITE, WIDTH/2, HEIGHT-50)
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.load(path.join(self.sound_dir, 'Pixel Galaxy.ogg'))
        pg.mixer.music.play(loops=-1)
        pg.display.flip()
        self.wait_for_key()
        
    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BLUE)
        self.draw_text("Game over", 32, WHITE, WIDTH/2, HEIGHT/2)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH-SCORE", 22, WHITE, WIDTH/2, HEIGHT/2 + 40)
            with open(path.join(self.dir, HS_FILE), 'r+') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High-score: " + str(self.highscore), 22, WHITE, WIDTH/2, HEIGHT-50)
        self.draw_text(("Your score: ") + str(self.score), 16, WHITE, WIDTH/2,HEIGHT/3)

        # Game over music
        pg.mixer.music.load(path.join(self.sound_dir, 'Determination.ogg'))
        pg.mixer.music.play(loops=1)

        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
    

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
        

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    #game over screen
    g.show_go_screen()

pg.quit()
