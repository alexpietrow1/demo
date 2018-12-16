# this file was created by Alex Pietrow
'''Sources: goo.gl/2KMivS - thanks Chris Bradfield!
            Mr. Cozort
'''
'''
**********What I changed about the game dynamics:
The character is constantly jumping
New player function (sink): When you press 's', the character sinks downward until you hit 
 another spring and bounce up
New platform function (compress): When you jump on the springs, which are the new platforms,
 the spring you jumped on compresses
Mobs spawn at a faster rate
When the player hits the side or bottom of the mob, it bounces off of it in the opposite direction
The screen size is larger so more platforms spawn in a larger location range

**********What I changed about the game cosmetics
The character is a different bunny
The platforms are springs and are compressed when jumped on
Mobs are spikeballs
Background color is different

**********Challenges I faced
I had trouble making the platform uncompress after it was jumped on:
    I tried getting ticks from pygame, but I could not figure out how to create a time delay between
     functions without making the game lag like crazy
I wasn't sure how to make the player bounce off the mobs in all directions, only 4 directions
    Since the mob is recognized as a rectangle by pygame, I wasn't sure how to make pygame
     recognize it like a circle

**********Bugs
Very rarely, when the player sinks, it sinks through a platform
If you press 's' right after the player dies, the pygame window crashes
It takes a long time for the mobs to die out once they are out of view of the screen
'''
import pygame as pg
import random
from settings import *
from sprites import *
from os import path

class Game:
    ##### INIT METHOD
    def __init__(self):
        #init game window
        # init pygame and create window
        pg.init()
        # init sound mixer
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("springy")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
    ##### LOAD DATA METHOD
    def load_data(self):
        print("load data is called...")
        # sets up directory name for images
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        # opens file with write options
        ''' with is a contextual option that handles both opening and closing of files to avoid
        issues with forgetting to close
        '''
        try:
            # changed to r to avoid overwriting error
            with open(path.join(self.dir, "highscore.txt"), 'r') as f:
                self.highscore = int(f.read())
                print(self.highscore)
        except:
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                self.highscore = 0
                print("exception")
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET)) 
        #load cloud images
        self.cloud_images = []
        for i in range(1,4):
            self.cloud_images.append(pg.image.load(path.join(img_dir, 'cloud{}.png'.format(i))).convert())
        # load sounds
        # great place for creating sounds: https://www.bfxr.net/
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = [pg.mixer.Sound(path.join(self.snd_dir, 'Jump18.wav')),
                            pg.mixer.Sound(path.join(self.snd_dir, 'Jump24.wav'))]
        self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump29.wav'))
        self.head_jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump39.wav'))
    ##### NEW METHOD
    def new(self):
        self.score = 0
        self.paused = False
        # add all sprites to the pg group
        # below no longer needed - using LayeredUpdate group
        # self.all_sprites = pg.sprite.Group()
        self.all_sprites = pg.sprite.LayeredUpdates()
        # create platforms group
        self.platforms = pg.sprite.Group()
        # create clouds group
        self.clouds = pg.sprite.Group()
        # add powerups
        self.powerups = pg.sprite.Group()
        # add cacti
        self.cacti = pg.sprite.Group()
        
        self.mob_timer = 0
        # add a player 1 to the group
        self.player = Player(self)
        # add mobs
        self.mobs = pg.sprite.Group()
        # no longer needed after passing self.groups in Sprites library file
        # self.all_sprites.add(self.player)
        # instantiate new platform 
        for plat in PLATFORM_LIST:
            # no longer need to assign to variable because we're passing self.groups in Sprite library
            # p = Platform(self, *plat)
            Platform(self, *plat)
            # no longer needed because we pass in Sprite lib file
            # self.all_sprites.add(p)
            # self.platforms.add(p)
        for i in range(8):
            c = Cloud(self)
            c.rect.y += 500
        # load music
        pg.mixer.music.load(path.join(self.snd_dir, 'happy.ogg'))
        # call the run method
        self.run()
    def run(self):
        # game loop
        # play music
        pg.mixer.music.play(loops=-1)
        # set boolean playing to true
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(1000)
        # other things that happen when not playing anymore
    ##### UPDATE METHOD
    def update(self):
        self.all_sprites.update()
        # shall we spawn a mob?
        now = pg.time.get_ticks()
        # check for mob collisions
        #I changed timer so that more mobs spawn
        if now - self.mob_timer > 1250 + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Mob(self)
        # now using collision mask to determine collisions
        # can use rectangle collisions here first if we encounter performance issues
        '''CHANGE: PLAYER BOUNCES OFF ALL DIRECTIONS OF MOB'''
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False, pg.sprite.collide_mask)
        if mob_hits:
            #subtracting 35 or 30 from the player position optimizes the player hitbox
            if self.player.pos.y - 35 < mob_hits[0].rect.top:
                print("hit top")
                print("player is " + str(self.player.pos.y))
                print("mob is " + str(mob_hits[0].rect.top))
                self.head_jump_sound.play()
                self.player.vel.y = -BOOST_POWER
            elif self.player.pos.y - 35 > mob_hits[0].rect.bottom:
                self.head_jump_sound.play()
                self.player.vel.y = BOOST_POWER
            elif self.player.pos.x + 30 > mob_hits[0].rect.right:
                self.head_jump_sound.play()
                self.player.vel.x = BOOST_POWER
            elif self.player.pos.x - 30 < mob_hits[0].rect.left:
                self.head_jump_sound.play()
                self.player.vel.x = -BOOST_POWER
        '''CHANGES: PLATFORM IS NOW LIKE THE MOB'S HEAD BECAUSE PLAYER CAN ONLY BOUNCE OFF IT 
                    SPRING COMPRESSES WHEN PLAYER JUMPS ON IT BUT UNCOMPRESSES MOMENTS AFTER'''
        #plat_hits checks for player and platform group collision
        plat_hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #sets player to not touching the platform
        self.player.touching = False
        #player can only jump if it is not currently being boosted by a powerup
        #this is because a powerup is the only way for the player to be going faster than 30
        if self.player.vel.y >= 0:
            #checks individual instances of player group colliding with platforms group
            if plat_hits:
            #checks for if bottom of player touches top of platform
                if self.player.pos.y - 35 < plat_hits[0].rect.top:
                    print("hit top")
                    print("player is " + str(self.player.pos.y))
                    print("mob is " + str(plat_hits[0].rect.top))
                    #everytime the bottom of player hits a platform, the player will bounce off the platform
                    self.player.vel.y = -PLAYER_JUMP
                    self.jump_sound[choice([0,1])].play()
                    '''sets player as touching platform for that split second, which is info that
                    will later be used to check to see if player is able to perform the sink function'''
                    self.player.touching = True
                    #compresses the individual springs whose top collided with the bottom of the player
                    for plat_hit in plat_hits:
                        plat_hit.compress()
                    #could not figure out how to get spring to uncompress
                    '''for plat_hit in plat_hits:
                            plat_hit.uncompress() '''
                    
        # if player reaches top 1/4 of screen...
        if self.player.rect.top <= HEIGHT / 4:
            # spawn a cloud
            if randrange(100) < 13:
                Cloud(self)
            # set player location based on velocity
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for cloud in self.clouds:
                cloud.rect.y += max(abs(self.player.vel.y / randrange(2,10)), 2)
            # creates slight scroll at the top based on player y velocity
            # scroll plats and mobs with player
            for mob in self.mobs:
                # creates slight scroll based on player y velocity
                mob.rect.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                # creates slight scroll based on player y velocity
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT + 40:
                    plat.kill()
                    self.score += 10
        # if player hits a power up
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.boost_sound.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False
        cacti_hits = pg.sprite.spritecollide(self.player, self.cacti, False)
        if cacti_hits:    
            if self.player.vel.y > 0 and self.player.pos.y > cacti_hits[0].rect.top:
                    print("falling")
                    print("player is " + str(self.player.pos.y))
                    print("mob is " + str(cacti_hits[0].rect.top))
        # Die!
        if self.player.rect.bottom > HEIGHT:
            '''make all sprites fall up when player falls'''
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                '''get rid of sprites as they fall up'''
                if sprite.rect.bottom < -25:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False
        # generate new random platforms
        while len(self.platforms) < 22:
            width = random.randrange(50, 200)
            ''' removed widths and height params to allow for sprites '''
            """ changed due to passing into groups through sprites lib file """
            # p = Platform(self, random.randrange(0,WIDTH-width), 
            #                 random.randrange(-75, -30))
            Platform(self, random.randrange(0,WIDTH-width), 
                            random.randrange(-200, -10))
            # self.platforms.add(p)
            # self.all_sprites.add(p)
    ##### EVENTS METHOD
    def events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                '''CHANGE: JUMP IS NO LONGER IN EVENTS, BUT THERE IS NOW A SINKING FUNCTION FOR THE PLAYER'''
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        '''player can only sink if the bottom of the player is not touching the top of a platform
                        and player's y velocity is greater than or equal to 0'''
                        if self.player.touching == False:
                            self.player.sink()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_p:
                        """ pause """
                        self.paused = True
    ##### DRAW METHOD
    def draw(self):
        self.screen.fill(SKY_BLUE)
        self.all_sprites.draw(self.screen)
        """ # not needed now that we're using LayeredUpdates """
        # self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        # double buffering - renders a frame "behind" the displayed frame
        pg.display.flip()
    ##### WAIT FOR KEY METHOD
    def wait_for_key(self): 
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type ==pg.KEYUP:
                    waiting = False
    ##### SHOW START SCREEN METHOD
    def show_start_screen(self):
        """ # game splash screen """
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("AD to move, S to sink", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press any key to play...", 22, WHITE, WIDTH / 2, HEIGHT * 3/4)
        self.draw_text("High score " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
    ##### SHOW GO SCREEN METHOD
    def show_go_screen(self):
        """ # game splash screen """
        if not self.running:
            print("not running...")
            return
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("AD to move, S to sink", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press any key to play...", 22, WHITE, WIDTH / 2, HEIGHT * 3/4)
        self.draw_text("High score " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT/2 + 40)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("new high score!", 22, WHITE, WIDTH / 2, HEIGHT/2 + 60)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))

        else:
            self.draw_text("High score " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT/2 + 40)


        pg.display.flip()
        self.wait_for_key()
    ##### DRAW TEXT METHOD
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
    try:
        g.show_go_screen()
    except:
        print("can't load go screen...")