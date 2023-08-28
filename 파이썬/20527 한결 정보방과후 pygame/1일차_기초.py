import pygame as pg
import sys
BLACK=(0,0, 0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED =(255,0,0)

#시작
pg.init()

#창띄우기
pg.display.set_caption("와 샌즈")
size=[400,300]
screen=pg.display.set_mode((0,0,255),pg.FULLSCREEN)
screen.fill(BLUE)

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()

#끝
pg.quit()
