import pygame as pg
import pygame.display
import sys
import random as rd


#시작
pg.init()
pg.display.set_caption("그림 띄우기")
screen=pg.display.set_mode((960,720))
#이미지 링크
img_ceobe=pg.image.load("케오베.png")
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
        screen.blit(img_ceobe,[350,200])
        pygame.display.update()
        for i in range(0,100):
            screen.fill(0,rd.randrange(0,255),rd.randrange(0,255))
pg.quit()
sys.exit()