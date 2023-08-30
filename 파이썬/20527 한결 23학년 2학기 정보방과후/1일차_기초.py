import pygame as pg
import sys

#시작
pg.init()

#창띄우기
pg.display.set_caption("와 샌즈")
screen=pg.display.set_mode((760,920))
screen.fill((0,0,255))

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()

#끝
pg.quit()
