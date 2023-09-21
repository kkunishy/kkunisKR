import pygame as pg
import sys
import math
import random

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

class enemy :
    x = 0
    y = 0
    a =0
    img_num = 0
    speed = 0
    count = 0

    def __init__ (self, x, y, a, img_num, speed, count) :
        self.x = x
        self.y = y
        self.a = a
        self.img_num = img_num
        self.speed = speed
        self.count = count
class explosion:
    x=0
    y=0
    img_num=0

    def __init__(self,x,y,img_num):
        self.x=x
        self.y=y
        self.img_num=img_num







bg_scroll=0
b_list = []
e_list = []
explosion_list=[]

tmr = 0
b_t = 0
z_t = 0
s = starship()

sound_shot=None
sound_gameover=None
sound_gameclear=None
sound_explosion=None
sound_damage=None
sound_barrage=None


#이미지 영역
img_bg=pg.image.load("galaxy.png")
img_ss=[
                pg.image.load("starship.png"),
                pg.image.load("starship_l.png"),
                pg.image.load("starship_r.png"),
                pg.image.load("starship_burner.png")
                     ]
img_bul=pg.image.load("bullet.png")
img_enemy = [
                        pg.image.load("enemy0.png"),
                        pg.image.load("enemy1.png"),
                        pg.image.load("enemy2.png"),
                        pg.image.load("enemy3.png"),
                        pg.image.load("enemy4.png"),
                        pg.image.load("enemy_boss.png"),
                        pg.image.load("enemy_boss_f.png")
                    ]
img_explosion=[
                pg.image.load("explosion1.png"),
                pg.image.load("explosion2.png"),
                pg.image.load("explosion3.png"),
                pg.image.load("explosion4.png"),
                pg.image.load("explosion5.png")
                    ]

#함수 영역
def draw_explosion(screen):
    for ex in explosion_list:
        screen.blit(img_explosion[ex.img_num],[ex.x,ex.y])
        ex.img_num+=1
        if ex.img_num%5==0:
            explosion_list.remove(ex)


def move_ship(screen,key):
    global b_t, s, z_t, sound_shot

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
        
    if key[pg.K_SPACE]==1:
        if b_t >=10 :
            b_t = 0
            b = bullet(s.x+27, s.y, 0, 10)
            b_list.append(b)
            sound_shot.play()
            
    if key[pg.K_z]==1:
        if z_t >=5 :
            z_t = 0
            sound_barrage.play()

            for a in range ( 0, 360, 1 ) :
                z = bullet (s.x+10, s.y+10 , a , 10 )
                b_list.append(z)
            

def draw_bullet(screen):
    for i in b_list :

        img_temp = pg.transform.rotozoom(img_bul, i.a,0.1)
        screen.blit(img_temp,  [i.x, i.y])

        i.x = i.x - 10*math.sin(math.radians(i.a))
        i.y = i.y - 10*math.cos(math.radians(i.a))

        if i.y<0 or i.y > 700 or i.x < 0 or i.x>950:
            b_list.remove(i)
        else:
            for j in e_list:
                if distance(i.x,i.y,j.x,j.y,img_enemy[j.img_num].get_width(),img_enemy[j.img_num].get_height()):
                    ex=explosion(j.x,j.y,0)
                    explosion_list.append(ex)
                
                    e_list.remove(j)
                    b_list.remove(i)
                    break
def distance(x1,y1,x2,y2,w2,h2):
    #x1,y1은 ship
    #x2,y2,ww2,h2는 enemy
    #if (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)<=(math.sqrt((w1/2)**2+h1/2)**2)+math.sqrt((w2/2)**2+(h2/2)**2)**2:
    return (x1-x2)**2+(y1-y2)**2<w2**2+h2**2
            
    
def draw_enemy(screen) :
    global tmr

    if tmr % 2 == 0 :
        if 0<=tmr<1000:
            x = random.randint(0,960-img_enemy[1].get_width())
            e = enemy(x, -80, 0, 4, 20, 1)   
            e_list.append(e)
        elif 1000<=tmr<2000:
            x = random.randint(0,960-img_enemy[1].get_width())
            e = enemy(x, -80, 0, 2, 20, 1)   
            e_list.append(e)
        elif 2000<=tmr:
            x = random.randint(0,960-img_enemy[1].get_width())
            e = enemy(x, -80, 0, 3, 20, 1)   
            e_list.append(e)

    for i in e_list :
        if i.y == 20 :
            i.a = random.randint(-360, 360)
            for a in range ( 0, 360, 60) :
                e=enemy(i.x,i.y+1,a,0,3,5)
                e_list.append(e)

        img_rz = pg.transform.rotozoom(img_enemy[i.img_num],i.a, 0.5)

        i.x = i.x+i.speed*math.sin(math.radians(i.a))
        i.y = i.y+i.speed*math.cos(math.radians(i.a))

        screen.blit(img_rz, [i.x, i.y] )

        if i.y<-100 or i.y > 720 or i.x < 0 or i.x > 960 :
            e_list.remove(i)
        if distance(s.x,s.y,i.x,i.y,img_enemy[i.img_num].get_width(),img_enemy[i.img_num].get_height()):
            e_list.remove(i)

        
#시작영역
#진행 영역
def main():
    global b_t, bg_scroll, s, z_t, tmr,sound_shot,sound_gameover,sound_gameclear,sound_explosion,sound_damage,sound_barrage
    pg.init()
    pg.display.set_caption("동방프로젝트 해적판wwwww")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()
    sound_shot=pg.mixer.Sound("shot.ogg")
    sound_gameover=pg.mixer.Sound("gameover.ogg")
    sound_gameclear=pg.mixer.Sound("gameclear.ogg")
    sound_explosion=pg.mixer.Sound("explosion.ogg")
    sound_damage=pg.mixer.Sound("damage.ogg")
    sound_barrage=pg.mixer.Sound("barrage.ogg")

    
    pg.mixer.music.load("bgm.ogg")
    pg.mixer.music.play(-1)
    
    running=True

    while running:
        tmr+=1
        b_t+=1
        z_t+=1
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
        pg.transform.rotozoom(img_ss[s.img_num],0,0.1)
        

        draw_bullet(screen)
        draw_enemy(screen)
        draw_explosion(screen)
        
        clock.tick(50)
        if s.speed <= 9:
            s.speed = 10
        if s.speed>20:
            s.speed=19
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
