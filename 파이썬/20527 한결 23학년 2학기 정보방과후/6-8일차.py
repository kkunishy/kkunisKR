import pygame as pg
import sys
import math
import random as rd

#전역변수 영역
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
class enemy:
    x=0
    y=0
    z=0
    img_num=0
    speed=0
    count=0

    def __init__(self,x,y,a,img_num,speed,count):
        self.x=x
        self.y=y
        self.a=a
        self.img_num=img_num
        self.speed=speed
        self.count=count


bg_scroll=0
b_list = []
e_list = []
tmr = 0
b_t = 0
z_t = 0
s = starship()
rdnum=0


#이미지 영역
img_bg=pg.image.load("galaxy.png")
img_ss=[
                pg.image.load("starship.png"),
                pg.image.load("starship_l.png"),
                pg.image.load("starship_r.png"),
                pg.image.load("starship_burner.png")
                     ]
img_bul=pg.image.load("bullet.png")
img_enemy=[
        pg.image.load("enemy0.png"),
        pg.image.load("enemy1.png"),
        pg.image.load("enemy2.png"),
        pg.image.load("enemy3.png"),
        pg.image.load("enemy4.png"),
        pg.image.load("enemy_boss.png"),
        pg.image.load("enemy_boss_f.png")
]
                
                

#함수 영역
def move_ship(screen,key):
    global b_t, s, z_t

    if key[pg.K_LEFT]==1 and s.x>0:
        s.x-=s.speed
        s.img_num=1
    if key[pg.K_RIGHT]==1 and s.x<960-74:
        s.x+=s.speed
        s.mg_num=2
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
        
    if key[pg.K_SPACE]==1:
        if b_t >=5 :
            b_t = 0
            b = bullet(s.x+27, s.y, 0, 10)
            b_list.append(b)
            
    if key[pg.K_z]==1:
        if z_t >= 10:
            z_t = 0

            for a in range ( 0, 360, 1 ) :
                z = bullet (s.x+27 , s.y, a , 1 )
                b_list.append(z)
            

def draw_bullet(screen):
    global s,rdnum
    for i in b_list :
        img_temp = pg.transform.rotozoom(img_bul, i.a, 1)
        screen.blit(img_temp,  [i.x, i.y])
        i.x-=36*math.sin(math.radians(i.a))
        i.y-=36*math.cos(math.radians(i.a))

        if i.y<0 or i.y>720 or i.x<0 or i.x>960:
            b_list.remove(i)       
def draw_enemy(screen):
    global tmr,e_list
    if tmr%15==0:
        x=rd.randint(0,960-img_enemy[1].get_width())
        e=enemy(x,-80,1,1,10,1)
        e_list.append(e)

    for i in e_list:
        if 300<=i.y <=330:
            i.a=rd.randint(-360,360)
        img_rz=pg.transform.rotozoom(img_enemy[i.img_num],i.a,1.0)
        i.x=i.x+i.speed*math.cos(math.radians(i.a))
        i.y=i.y+i.speed*math.sin(math.radians(i.a))
        screen.blit(img_rz,[i.x,i.y])
        i.y+=i.speed
        if i.y>720 or i.x<0 or i.x>960:
            e_list.remove(i)
#시작영역
#진행 영역
def main():
    global b_t, bg_scroll, s, z_t, rdnum,tmr
    pg.init()
    pg.display.set_caption("동방프로젝트 해적판wwwww")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()
    running=True
       
    while running:
        tmr+=1
        b_t+=1
        z_t+=1
        rdnum=rd.randint(50,90)
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
        draw_enemy(screen)
        
        clock.tick(50)
        if s.speed <= 9:
            s.speed = 10
        if s.speed>30:
            s.speed=29
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
