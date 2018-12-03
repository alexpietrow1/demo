#sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

vec = pg.math.Vector2

class Player(Sprite) :
    def __init__(self , game) :
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT /2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def update(self) :
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a] :
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d] :
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #jump to other side of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos
    def jump(self) :
        self.rect.y += 1
        #if sprites are touching each other, you are able to jump
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits :
            self.vel.y = -PLAYER_JUMP

class Platform(Sprite) :
    def __init__(self, x, y, w, h) :
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# class Enemy(Sprite) :
#     def __init__(self) :
#         Sprite.__init__(self)
#         self.image = pg.Surface((30, 40))
#         self.image.fill(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2 , HEIGHT / 2)
#         self.vx = 0
#         self.vy = 0
#         self.falling = False
#     def update(self) :
#         self.vx = 0
#         self.gravity()
#         keys = pg.key.get_pressed()
#         if keys[pg.K_a] :
#             self.vx = -10
#         if keys[pg.K_d] :
#             self.vx = 10
#         if keys[pg.K_w] and self.falling == False:
#             self.jump()
#         self.rect.x += self.vx
#         self.rect.y += self.vy
#     def jump(self) :
#         self.vy = -75
#     def gravity(self) :
#         if self.rect.y < HEIGHT-40 :
#             self.falling = True
#             print("gravity is not happening. " + str(self.rect.y))
#             print("falling " + str(self.falling))
#             self.vy += 10
#         elif self.rect.y <=HEIGHT :
#             self.falling = False
#             self.vy = 0
#             self.rect.y = HEIGHT-40