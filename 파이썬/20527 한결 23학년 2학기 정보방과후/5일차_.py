import pygame as pg
import pygame.display
import random as rd
import sys

#변수
circle_x=-100
circle_y=-100
circle_radius=50
draw_mode=False
R=0
G=0
B=0
#시작
pg.init()
pg.display.set_caption("그림그리기")
screen=pg.display.set_mode((960,720))
screen.fill((255,255,255))
clock=pg.time.Clock()
#폰트
font1=pygame.font.SysFont("맑은 고딕 Semilight",100)
#진행
running=True

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running = False
        if event.type==pg.MOUSEBUTTONDOWN:
            if event.button==1:
                draw_mode=not(draw_mode)
            if event.button==3:
                screen.fill((255,255,255))

        if event.type==pg.MOUSEMOTION:
            if draw_mode:
                circle_x,circle_y=pg.mouse.get_pos()
            else:
                circle_x,circle_y=-100,-100
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP:
                circle_radius+=5
            if event.key==pg.K_DOWN:
                circle_radius-=5
            if event.key==pg.K_LEFT:
                R=rd.randint(0,255)
            if event.key==pg.K_RIGHT:
                G,B=rd.randint(0,255),rd.randint(0,255)
    if circle_radius<0:
        circle_radius=0
    key = pg.key.get_pressed()
    pg.draw.circle(screen,(R,G,B),[circle_x,circle_y],circle_radius)
    pygame.display.update()
    clock.tick(50)
pg.quit()
sys.exit()