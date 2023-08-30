import pygame as pg
import sys

import pygame.display

#시작
pg.init()
pg.display.set_caption("그림 띄우기")
screen=pg.display.set_mode(960,720)
#진행
running=True

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_F1:
                screen=pg.display.set_mode((960,720))
                screen.fill(200,100,180)
            if event.key==pg.K_F2 or event.key==pg.K_SPACE:
                screen=pg.display.set_mode((960,720),pg.FULLSCREEN)
                screen.fill(180,200,100)
        pygame.display.update()
pg.quit()
sys.exit()