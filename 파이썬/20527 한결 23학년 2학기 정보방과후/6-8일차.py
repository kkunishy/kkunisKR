import pygame as pg
import math
import sys
import random as rd

#전역변수 영역
class starship:
    x=480+37
    y=360+48
    img_num=0
    speed=5
class bullet():
    x=0
    y=0
    a=0
    speed=0
    def __init__(self,x,y,a,speed):
        self.x=x
        self.y=y
        self.a=a
        self.speed=speed

bg_scroll=0
b_list=[]
b_t=0
z_t=0
rdnum=0
s=starship()
#이미지 영역
img_bg=pg.image.load("galaxy.png")
img_ss=[
                pg.image.load("starship.png"),
                pg.image.load("starship_l.png"),
                pg.image.load("starship_r.png"),
                pg.image.load("starship_burner.png")
                     ]
img_bul=pg.image.load("bullet.png")

#함수 영역
def move_ship(screen,key):
    global b_t,s,z_t

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
    if key[pg.K_LSHIFT]==1:
        if z_t>=1:
            z_t=0
            for i in range(0,360,30):
                z=bullet(s.x+25,s.y+20,i,100)
                b_list.append(z)
            #b=bullet(s.x+27,s.y,0,15)
            #b_list.append(b)
        
    if key[pg.K_SPACE]==1:
        if b_t>=5:
            b_t=0
            b=bullet(s.x+27,s.y,0,100)
            b_list.append(b)
def draw_bullet(screen):
    global rdnum
    for i in b_list:
        img_temp=pg.transform.rotozoom(img_bul,i.a,1.0)
        screen.blit(img_temp,[i.x,i.y])
        i.x-=math.sin(i.a-rdnum)
        i.y+=math.sin(i.a+rdnum)

        if i.y<0:
            b_list.remove(i)
#시작영역
#진행 영역
def main():
    global b_t,z_t,bg_scroll,s
    pg.init()
    pg.display.set_caption("동방프로젝트 해적판wwwww")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()
    running=True

    while running:
        b_t+=1
        z_t+=1
        rdnum=rd.randint(0,180)
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
        #bg_scroll은 배경의 Y좌표를 계산하는 애(0~720)
        bg_scroll=(bg_scroll+5)%720
        if bg_scroll%10==0:
            screen.blit(img_ss[3],[s.x+29, s.y+100])
        screen.blit(img_ss[s.img_num],[s.x,s.y])
        draw_bullet(screen)
        clock.tick(50)
        if s.speed <= 7:
            s.speed = 8
        if s.speed>30:
            s.speed=29
            
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
