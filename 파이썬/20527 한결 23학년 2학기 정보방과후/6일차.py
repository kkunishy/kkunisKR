import pygame as pg
import sys

#전역변수 영역
#이미지 영역
img_bg=pg.image.load("6일차)galaxy.png")
img_ss=[
                pg.image.load("6일차)galaxy.png")
                pg.image.load("6일차)galaxy.png")
                pg.image.load("6일차)galaxy.png")
                pg.image.load("6일차)galaxy.png")]
#함수 영역
#시작영역
pg.init()
pg.display.set_caption()
screen=pg.display.set_mode((960,720))
clock=pg.time.Clock()


#진행 영역
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
    clock.tick(50)
    pg.display.update()

pg.quit()
sys.exit()
