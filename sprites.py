#sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

class Player(Sprite) :
    def __init__(self) :
        Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.falling = False
    def update(self) :
        self.vx = 0
        self.gravity()
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] :
            self.vx = -10
        if keys[pg.K_RIGHT] :
            self.vx = 10
        if keys[pg.K_UP] and self.falling == False :
            self.jump()

        self.rect.x += self.vx
        self.rect.y += self.vy
    def jump(self) :
        self.vy = -75
    def gravity(self) :
        if self.rect.y < HEIGHT-40 :
            self.falling = True
            print("gravity is not happening. " + str(self.rect.y))
            print("falling " + str(self.falling))
            self.vy += 10
        elif self.rect.y <=HEIGHT :
            self.falling = False
            self.vy = 0
            self.rect.y = HEIGHT-40


class Enemy(Sprite) :
    def __init__(self) :
        Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.falling = False
    def update(self) :
        self.vx = 0
        self.gravity()
        keys = pg.key.get_pressed()
        if keys[pg.K_a] :
            self.vx = -10
        if keys[pg.K_d] :
            self.vx = 10
        if keys[pg.K_w] and self.falling == False:
            self.jump()

        self.rect.x += self.vx
        self.rect.y += self.vy
    def jump(self) :
        self.vy = -75
    def gravity(self) :
        if self.rect.y < HEIGHT-40 :
            self.falling = True
            print("gravity is not happening. " + str(self.rect.y))
            print("falling " + str(self.falling))
            self.vy += 10
        elif self.rect.y <=HEIGHT :
            self.falling = False
            self.vy = 0
            self.rect.y = HEIGHT-40
class Platform(Sprite) :
    def __init__(self) :
        Sprite.__init__(self)
        self.image = pg.Surface((200, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self) :
        self.vx = 0
        self.vx = 0
        self.rect.x += self.vx
        self.rect.y += self.vy
