import pygame as pg
import sys

#전역변수 영역
bg_scroll=0
ss_x=(960/2)-37
ss_y=(720/2)+48
ss_speed=3
ss_img_num=0
bullet_x=-100
bullet_y=-100
bullet_speed=0
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
    global ss_y,ss_x,ss_speed,ss_img_num,bullet_x,bullet_y,bullet_speed

    if key[pg.K_LEFT]==1 and ss_x>0:
        ss_x-=ss_speed
        ss_img_num=1
    if key[pg.K_RIGHT]==1 and ss_x<960-74:
        ss_x+=ss_speed
        ss_img_num=2
    if key[pg.K_UP]==1 and ss_y>0:
        ss_y-=ss_speed
    if key[pg.K_DOWN]==1 and ss_y<720-96:
        ss_y+=ss_speed
    if key[pg.K_LEFT]!=1 or key[pg.K_RIGHT]!=1:
        ss_img_num=0
    if key[pg.K_1]==1:
        ss_speed+=5
    if key[pg.K_2]==1:
        ss_speed-=5
    if key[pg.K_SPACE]==1:
        bullet_x=ss_x+27
        bullet_y=ss_y
        bullet_speed=30

#시작영역
#진행 영역
def main():
    global bg_scroll,ss_x,ss_y,ss_speed,ss_img_num,bullet_x,bullet_y,bullet_speed
    pg.init()
    pg.display.set_caption("동방프로젝트 해적판wwwww")
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
        #bg_scroll은 배경의 Y좌표를 계산하는 애(0~720)
        bg_scroll=(bg_scroll+5)%720
        if bg_scroll%10==0:
            screen.blit(img_ss[3],[ss_x+29, ss_y+100])
        screen.blit(img_ss[ss_img_num],[ss_x,ss_y])

        screen.blit(img_bul,[bullet_x,bullet_y])
        bullet_y-=bullet_speed
        clock.tick(50)
        if ss_speed <= 20:
            ss_speed = 21
        if ss_speed>50:
            ss_speed=49
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
