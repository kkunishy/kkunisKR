import pygame as pg
import pygame.display
import sys


#시작
pg.init()
pg.display.set_caption("그림 띄우기")
screen=pg.display.set_mode((960,720))
#이미지 링크
img_ceobe=pg.image.load("케오베.png")
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
        key=pg.key.get_pressed()
        #^^^  key[pygame.K_UP]=1 을 출력
        screen.blit(img_ceobe,[350,200])
        txt1=font1.render("Up key enabled:"+str(key[pg.K_UP]),True,(0,255,255),(0,0,0))
        screen.blit(txt1,[100,100])
        txt2=font1.render("your dad",True,(0,255,255),(0,0,0))
        screen.blit(txt2,[100,300])
        pygame.display.update()
pg.quit()
sys.exit()