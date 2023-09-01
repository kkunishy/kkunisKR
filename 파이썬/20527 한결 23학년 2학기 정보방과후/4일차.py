import pygame as pg
import pygame.display
import random as rd
import sys

#변수
ceobe_x=0
ceobe_y=0
clock_x=0
clock_y=100
circle_x=0
circle_y=0
circle_radius=50
R=100
G=100
B=100

#시작
pg.init()
pg.display.set_caption("ceobe is a fucking idiot ")
screen=pg.display.set_mode((960,720))
clock=pg.time.Clock()
#이미지 링크
img_ceobe=pg.image.load("케오베.png")
#폰트
font1=pygame.font.SysFont("맑은 고딕 Semilight",100)
#진행
running=True

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_F1:
                screen=pg.display.set_mode((960,720))
                screen.fill((200,100,180))
            if event.key==pg.K_F2 or event.key==pg.K_SPACE:
                screen=pg.display.set_mode((960,720),pg.FULLSCREEN)
                screen.fill((180,200,100))
            if event.key==pg.K_SPACE:
                screen.fill((0,0,0))

        if event.type==pg.MOUSEMOTION:
            circle_x,circle_y=pg.mouse.get_pos()
        if event.type==pg.MOUSEBUTTONDOWN:
            if event.button==1:
                R=rd.randint(0,255)         #rd=random
            if event.button==2:
                G=rd.randint(0,255)
            if event.button==3:
                B=rd.randint(0,255)
            if event.button==4:
                circle_radius+=10
            if event.button==5:
                circle_radius-=10

    key=pg.key.get_pressed()
        #^^^  key[pygame.K_UP]=1 을 출력
    if key[pg.K_UP]==True:
        ceobe_y-=1
    if key[pg.K_DOWN]==True:
        ceobe_y+=1
    if key[pg.K_LEFT]==True:
        ceobe_x-=1
    if key[pg.K_RIGHT]==True:
        ceobe_x+=1

    screen.fill((0, 0, 0))
    txt1=font1.render("Up key enabled:"+str(key[pg.K_UP]),True,(0,255,255),(0,0,0))
    screen.blit(txt1,[100,100])
    txt2=font1.render("Down key enabled:"+str(key[pg.K_DOWN]),True,(0,255,255),(0,0,0))
    screen.blit(txt2,[100,300])
    screen.blit(img_ceobe, [ceobe_x, ceobe_y])
    screen.blit(img_ceobe,[clock_x,clock_y])
    clock_x=(clock_x+1)%960
    pg.draw.circle(screen,(R,G,B),[circle_x,circle_y],circle_radius)
    if ceobe_x<-100:
        ceobe_x=-100
    if ceobe_x>720:
        ceobe_x=720
    if ceobe_y<-100:
        ceobe_y=-100
    if ceobe_y>500:
        ceobe_y=500
    if circle_radius<0:
        circle_radius=0
    pygame.display.update()
pg.quit()
sys.exit()