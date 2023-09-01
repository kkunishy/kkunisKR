import pygame as pg
import pygame.display
import random as rd
import sys

#변수

circle_x=0
circle_y=0
circle_radius=50
R=0
G=0
B=0
#시작
pg.init()
pg.display.set_caption("그림그리기")
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
            if event.key==pg.K_SPACE:
                screen.fill((0,0,0))
        if event.type==pg.MOUSEMOTION:
            circle_x,circle_y=pg.mouse.get_pos()
        if event.type==pg.MOUSEBUTTONDOWN:
            if event.button==1:
                pg.draw.circle(screen, (R, G, B), [circle_x, circle_y], circle_radius)
            if event.button==4:
                R,G,B=rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)

    key=pg.key.get_pressed()
        #^^^  key[pygame.K_UP]=1 을 출력

    if circle_radius<0:
        circle_radius=0
    pygame.display.update()
    clock.tick(50)
pg.quit()
sys.exit()