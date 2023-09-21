import pygame as pg
import sys
import math
import random


class starship :
    x = 480 + 37
    y = 360 + 48
    img_num =0
    speed = 10

img_bg=pg.image.load("galaxy.png")
img_ss=[
                pg.image.load("starship.png"),
                pg.image.load("starship_l.png"),
                pg.image.load("starship_r.png"),
                pg.image.load("starship_burner.png")
                     ]
img_bul=pg.image.load("bullet.png")
s = starship()
bg_scroll=0

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
    if key[pg.K_LEFT]!=1 or key[pg.K_RIGHT]!=1:
        s.img_num=0
    if key[pg.K_1]==1:
        s.speed+=5
    if key[pg.K_2]==1:
        s.speed-=5



def main():
    global s, img_bg,bg_scroll
    pg.init()
    pg.display.set_caption("와샌즈")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()

    running=True

    while running:
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
        if bg_scroll%10==0:
            screen.blit(img_ss[3],[s.x+29, s.y+100])
        screen.blit(img_ss[s.img_num],[s.x,s.y])
        pg.transform.rotozoom(img_ss[s.img_num],0,0.1)
        clock.tick(50)
        if s.speed <= 9:
            s.speed = 10
        if s.speed>20:
            s.speed=19
        pg.display.update()
        print(s.speed)
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
