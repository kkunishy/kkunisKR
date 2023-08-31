import pygame as pg
import pygame.display
import sys

#변수
ceobe_x=0
ceobe_y=0

#시작
pg.init()
pg.display.set_caption("그림 띄우기")
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
    pygame.display.update()
    if ceobe_x<0:
        ceobe_x=0
    if ceobe_x>960:
        ceobe_x=960
    if ceobe_y<0:
        ceobe_y=0
    if ceobe_y>720:
        ceobe_x=720
    print(str(ceobe_x)+"+"+str(ceobe_y))
pg.quit()
sys.exit()