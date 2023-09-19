import pygame as pg
import sys
import math
import random


class starship :
    x = 480 + 37
    y = 360 + 48
    img_num =0
    speed = 10

class bullet :
    x = 0
    y = 0
    a = 0
    speed = 0

    def __init__(self, x, y, a, speed):
        self.x = x
        self.y = y
        self.a = a
        self.speed = speed
class enemy :
    x = 0
    y = 0
    speed = 0

        
img_bg=pg.image.load("galaxy.png")
img_ss=[pg.image.load("spaceship_1.png")]
img_boss=pg.image.load("enemy_boss.png")
img_bul=pg.image.load("bullet.png")

s = starship()
e=enemy()
e_list=[]
bg_scroll=0

tmr=0
b_t=0
z_t=0

def move_ship(screen,key):
    global s

    if key[pg.K_LEFT]==1 and s.x>0:
        s.x-=s.speed
        s.img_num=1
    if key[pg.K_RIGHT]==1 and s.x<960-74:
        s.x+=s.speed
        s.img_num=2
    if key[pg.K_UP]==1 and s.y>0:
        s.y-=s.speed
    if key[pg.K_DOWN]==1 and s.y<720-96:
        s.y+=s.speed
    if key[pg.K_SPACE]==1:
        s.speed=7
    else:
        s.speed=15
def draw_boss(screen):
    global tmr


def draw_enemy(screen) :
    global tmr
    e.x+=1


            
    screen.blit(img_boss, [e.x,e.y])
def main():
    global s, img_bg,bg_scroll,tmr,e_list
    pg.init()
    pg.display.set_caption("와샌즈")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()

    running=True

    while running:
        tmr+=1
        print(e_list)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_F1:
                    screen=pg.display.set_mode((960,720))
                if event.key==pg.K_F2:
                    screen=pg.display.set_mode((960,720),pg.FULLSCREEN)
        key=pg.key.get_pressed()
        move_ship(screen,key)
        screen.blit(img_bg,[0,bg_scroll-720])
        screen.blit(img_bg,[0,bg_scroll])
        bg_scroll=(bg_scroll+5)%720
        screen.blit(img_ss[0],[s.x,s.y])
        
        draw_enemy(screen)
        clock.tick(50)

        pg.display.update()
        print(s.speed)
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
