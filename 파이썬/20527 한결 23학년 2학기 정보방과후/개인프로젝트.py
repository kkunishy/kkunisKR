import pygame as pg
import sys
import math
import random as rd


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
    y = 200
    speed = 0
    

        
img_bg=pg.image.load("galaxy.png")
img_ss=[pg.image.load("spaceship_1.png")]
img_boss=pg.image.load("enemy_boss.png")
img_bul=pg.image.load("bullet.png")

s = starship()
e=enemy()
e_list=[]
b_list=[]
bg_scroll=0
ang=1
tmr=0
b_t=0
z_t=0
spd=3

def move_ship(screen,key):
    global s

    if key[pg.K_LEFT]==1 and s.x>0:
        s.x-=s.speed
    if key[pg.K_RIGHT]==1 and s.x<960-24:
        s.x+=s.speed
    if key[pg.K_UP]==1 and s.y>0:
        s.y-=s.speed
    if key[pg.K_DOWN]==1 and s.y<720-40:
        s.y+=s.speed
    if key[pg.K_SPACE]==1:
        s.speed=7
    else:
        s.speed=15
def draw_boss(screen):
    global tmr,ang,b_t,e,b_list,spd
    if e.x<0 or e.x>519:
        ang+=1
        
    if ang%2==1:
        e.x+=1
    elif ang%2==0:
        e.x-=1
        
    if b_t >=10:
        b_t = 0
        for a in range ( 0, 360, 60) :
            b = bullet(e.x+200, e.y+170, a, spd)
            b_list.append(b)
    screen.blit(img_boss, [e.x,e.y])
    
def draw_bullet(screen):
    global e,b_list,ang,spd,tmr
    
    for i in b_list:
        if ang%2==1:
            i.a+=0.5
            spd=5
        elif ang%2==0:
            i.a-=0.8
            spd=2
        img_temp = pg.transform.rotozoom(img_bul,i.a,0.3)
        screen.blit(img_temp,[i.x ,i.y])
        
        i.x = i.x - i.speed*math.sin(math.radians(i.a))
        i.y = i.y - i.speed*math.cos(math.radians(i.a))
        
        
        if i.y<0 or i.y > 700 or i.x < 0 or i.x>950:
            b_list.remove(i)

def main():
    global s, img_bg,bg_scroll,tmr,e_list,b_t
    pg.init()
    pg.display.set_caption("와샌즈")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()

    running=True

    while running:
        tmr+=1
        b_t+=1
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
        
        draw_boss(screen)
        draw_bullet(screen)
        clock.tick(50)

        pg.display.update()
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
