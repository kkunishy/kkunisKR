import pygame as pg
import sys

#전역변수 영역
bg_scroll=0
ss_x=(960/2)-37
ss_y=(720/2)+48
ss_speed=5
#이미지 영역
img_bg=pg.image.load("6일차)galaxy.png")
img_ss=[
                pg.image.load("6일차)starship.png"),
                pg.image.load("6일차)starship_l.png"),
                pg.image.load("6일차)starship_r.png"),
                pg.image.load("6일차)starship_burner.png")
                     ]
#함수 영역
#시작영역
#진행 영역
def main():
    global bg_scroll,ss_x,ss_y
    pg.init()
    pg.display.set_caption("동방프로젝트 해적판")
    screen = pg.display.set_mode((960, 720))
    clock = pg.time.Clock()
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


        screen.blit(img_bg,[0,bg_scroll-720])
        screen.blit(img_bg,[0,bg_scroll])
        #bg_scroll은 배경의 Y좌표를 계산하는 애(0~720)
        bg_scroll=(bg_scroll+5)%720
        if bg_scroll%10==0:
            screen.blit(img_ss[3],[ss_x+29, ss_y+100])
        screen.blit(img_ss[0],[ss_x,ss_y])
        clock.tick(50)
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__=="__main__":
    main()
